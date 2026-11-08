# -*- coding: utf-8 -*-
"""
Collection of Kazakh-language posts from public Telegram channels through the official API.

This is the script behind Section III-A of the paper. Anonymisation happens here, at
collection time and before any annotation: user names, hyperlinks, telephone numbers and
e-mail addresses are stripped from the message text, and nothing is kept but the anonymised
text, the channel name and the date. No account identifiers and no message identifiers are
retained, which is also why the corpus cannot be redistributed as platform IDs for others to
re-fetch.

Filters, in order: messages without text and forwarded messages are skipped; the text is
anonymised; length is restricted to 5-100 words; the post must be predominantly Cyrillic and
carry at least one Kazakh-specific grapheme, which keeps Kazakh-Russian code-switched posts
and excludes Kazakh written without those graphemes, Latin-script Kazakh among them;
advertising markers are rejected; exact duplicates are dropped, both within a run and against
an existing dataset.

Setup, once:
  1. pip install telethon pandas openpyxl
  2. Create an application at https://my.telegram.org (API development tools) and put its
     api_id and api_hash below.
  3. On the first run Telethon asks for a phone number and a login code, and writes a local
     session file.

Usage:  python telegram_collect.py
Output: collected_raw.xlsx, every post that passed the filters.

The channels sampled for the corpus are named in Section III-A of the paper. CHANNELS is left
empty here so that the script is run deliberately rather than by accident.
"""

import re
import asyncio
import pandas as pd
from telethon import TelegramClient

# ---------------- settings ----------------
API_ID = 12345          # <- your api_id
API_HASH = "your_hash"  # <- your api_hash

CHANNELS = [
    # channel user names, without the leading @
]

LIMIT_PER_CHANNEL = 5000                 # how many recent messages to read per channel
EXISTING_DATASET = "dataset_v20.xlsx"    # already-collected texts, to avoid collecting them twice
OUTPUT = "collected_raw.xlsx"

MIN_WORDS, MAX_WORDS = 5, 100
# ------------------------------------------

KAZAKH_CHARS = set("әғқңөұүһі")

# advertising markers, in Kazakh and Russian; a post containing any of them is rejected
AD_MARKERS = ["жарнама", "реклама", "промокод", "скидка", "подпишись",
              "подписывайтесь", "жазылыңыз", "erid", "#ad"]

RE_USERNAME = re.compile(r"@\w+")
RE_URL = re.compile(r"(https?://\S+|t\.me/\S+|www\.\S+)")
RE_PHONE = re.compile(r"(\+?\d[\d\-\s\(\)]{8,}\d)")
RE_EMAIL = re.compile(r"\S+@\S+\.\S+")


def anonymize(text: str) -> str:
    """Remove direct identifiers. Applied before the text is stored anywhere."""
    text = RE_URL.sub(" ", text)
    text = RE_USERNAME.sub(" ", text)
    text = RE_PHONE.sub(" ", text)
    text = RE_EMAIL.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def looks_kazakh(text: str) -> bool:
    """Kazakh, or Kazakh-Russian code-switching: predominantly Cyrillic and carrying at least
    one Kazakh-specific grapheme."""
    low = text.lower()
    cyr = sum(1 for c in low if "а" <= c <= "я" or c in KAZAKH_CHARS)
    if cyr < len(low) * 0.3:
        return False
    return any(c in KAZAKH_CHARS for c in low)


def passes_filters(text: str) -> bool:
    n_words = len(text.split())
    if not (MIN_WORDS <= n_words <= MAX_WORDS):
        return False
    if not looks_kazakh(text):
        return False
    low = text.lower()
    if any(m in low for m in AD_MARKERS):
        return False
    return True


async def main():
    try:
        existing = set(pd.read_excel(EXISTING_DATASET)["text"].astype(str))
        print(f"Existing dataset loaded: {len(existing)} texts")
    except FileNotFoundError:
        existing = set()
        print("No existing dataset found; collecting without cross-checking")

    rows, seen = [], set()
    async with TelegramClient("collector_session", API_ID, API_HASH) as client:
        for ch in CHANNELS:
            print(f"\nChannel: {ch}")
            count = 0
            try:
                async for msg in client.iter_messages(ch, limit=LIMIT_PER_CHANNEL):
                    if not msg.message:            # media without text
                        continue
                    if msg.forward is not None:    # forwarded messages are skipped
                        continue
                    text = anonymize(msg.message)
                    if not passes_filters(text):
                        continue
                    if text in seen or text in existing:
                        continue
                    seen.add(text)
                    rows.append({
                        "source": f"telegram_{ch}",
                        "date": msg.date.strftime("%Y-%m-%d"),
                        "text": text,
                    })
                    count += 1
            except Exception as e:
                print(f"  error on channel {ch}: {e}")
            print(f"  kept after filtering: {count}")

    df = pd.DataFrame(rows)
    df.insert(0, "raw_id", range(1, len(df) + 1))
    df.to_excel(OUTPUT, index=False)
    print(f"\nTotal: {len(df)} posts -> {OUTPUT}")


if __name__ == "__main__":
    asyncio.run(main())