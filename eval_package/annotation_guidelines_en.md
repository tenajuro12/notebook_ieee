# Annotation guidelines — emotion in Kazakh social-media posts

Twelve classes, version 4. These are the guidelines used to annotate the corpus described in
*Emotion Classification in Kazakh Social Media: What Limits Performance in a Low-Resource
Setting?* (ICTACS-2026) and to carry out the independent second annotation reported in
Section III-C.

The working document was written in Russian, which is the working language of the annotators;
it is included in this package as `annotation_guidelines_ru.md`. This is an English rendering
of the same content. Examples are left in the original Kazakh, including the
Kazakh–Russian code-switching that is characteristic of the material.

---

## The governing principle

**Annotate the emotion of the AUTHOR, not the emotional charge of the situation.**

If a writer reports a painful event without expressing their own state, the label is
**Neutral**, however dramatic the content.

> "My ex is writing, crying, asking to come back. Should I forgive cheating??"
> → **Neutral**: the author describes a situation and asks a question, and says nothing about
> their own state.

> "My ex is writing… Шаршадым осыдан, ұйықтай алмай жүрмін"
> → **Exhaustion**: the author names their state directly.

Look for state signals: қорқамын, шаршадым, ұят болды, жылап отырмын, күш жоқ, ашуланамын,
таң қалдым, жалғызбын, state emoji, evaluative words about the self. No signal, Neutral.

## The second principle: what the experience is directed at

Most boundary cases resolve with one question — **what is the author's experience directed
at?**

| Directed at | Class |
|---|---|
| the self as a person | Worthlessness |
| one's own specific act or trait | Shame |
| one's own future | Hopelessness, Fear |
| one's own reserves of strength | Exhaustion |
| the absence of people around | Loneliness |
| specific people and circumstances in one's own life | Frustration |
| society, a norm, people in general | Indignation |
| an external object of aversion | Disgust |

---

## The twelve classes

### Joy
Joy, gratitude, pride, achievement, hope, tenderness, a warm story. Any positively valenced
emotion of the author.

> «ағылшыннан C1 алдым!!! 🎓 3 жыл еңбектендім. қазақша, орысша, енді ағылшынша. кайф 😭»

> «әжем 78 жасында латынша оқуды үйренді 📖 бүгін маған өзі сообщение жазды. қателері толып тұр 😂 бірақ ӨЗІ жазды!!!»

### Hopelessness
Hopelessness, focused on **the future** and its futility: ештеңе өзгермейді, бәрі бекер,
мағынасы жоқ, соңы көрінбейді. Often a sense of a closed loop repeating year after year.

> «бір кезде жақсы күндер болады деп шын сенетінмін. қазір ондай ой жоқ»

> «Жыл сайын “келесі жыл жақсы болады” дейміз. Өткен жылы да солай айтқанбыз. Биыл да айтып отырмыз»

### Worthlessness
A negative evaluation of **the self as a person** as the central theme of the post:
түкке тұрғысызбын, менен пайда жоқ, орнымды біреу тез басады. Also persistent self-blame, and
doubt that one is worth anything to those close.

> «Ата-анам менің оқуым үшін төрт жыл ақша төледі. Қазір соған қарап отырып, сол ақшаның ақталғанын өзім де сұраймын»

> «Не айтсам да біртүрлі естіліп кетеді. Кейде үндемей отырғаным дұрыс шығар деп ойлаймын»

### Exhaustion
Depletion, burnout, apathy: шаршадым, күш жоқ, енді болмайды. A state of **resources**, not of
self-worth and not of the future.

> «2 жұмыс + бала + үй. кешкі 10-да ғана отырам. отыра сала ұйықтап қалам»

> «үйдің жұмысы бітпейді. жусаң — қайта кір, жинасаң — қайта шашылады. қолым талды уже»

### Loneliness
A deficit of **connection with people**: жалғызбын, сөйлесетін адам жоқ, isolation, being
unneeded. **Ordinary grief of loss and separation belongs here too** — the death of a person
or a pet, moving away, a break-up, missing someone. The scheme has no separate class for
plain sadness.

> «Сөйлесетін адам болмаған соң осында жазып отырмын. Тіпті бейтаныстарға болса да, біреуге айтып қалғым келді»

> «12 жыл асыраған мысығым көз алдымда өліп қалды. 1 жыл болды есімнен кетпейді»

### Frustration
Irritation, resentment, anger, grievance directed at **specific people and circumstances of
the author's own life**: relatives, a partner, friends, neighbours, work, daily life. Often
ends in a question such as не істеу керек?

> «Қарыз алатын кезде жалынып, мүләйімсіп тұратын досың қайтаратын уақытында өзінше болып кетсе не істеу керек?»

> «Әжем бар, ол всегда заттарыма тиіседі, косметикамды алып қолданады, рұқсатсыз алып кете береді»

### Indignation
Moral outrage directed at **society, a norm, a group of people or injustice in general**, not
at the author's own situation. The author passes judgement on "the way things are done here".

> «Осы неге қызбен жүріп оны пайдаланып кетсең жігіттерге “ұялмайсың ба?” дейді, ал қыздар пайдаланып кетсе ешкім үндемейді»

> «Әлі күнге мектеп қызметкерлерін өз қалауларынсыз газетке жазылдыруға мәжбірлеу бар екеніне таңғалдым»

### Shame
Shame and embarrassment over **a specific episode or one's own trait**, without devaluing
oneself as a person. Two forms: embarrassment (ұят болды, кірерге тесік таппадым), often with
humour; and shame proper, without the joking register.

> «6 сыныпта ТЖБ жазбау үшін көзім көрмей қалды деп, өкіріп жылап, сыныпты түгел шулатып алғанмын. Есіме түссе қатты ұялып кетем 🤦‍♀️»

> «Атым Гүлбану, тіпті атымды айтуға ұялам... Ұят!»

### Fear
Anxiety, fear of the future or of a concrete threat, nervousness before an event, social
timidity as a stable trait.

> «Тұрмысқа шығайын деп жатырмын, маған совет керек 🙏 Жамаааан қобалжып жүрмін 🥹»

> «Өте ұялшақпын, ата-анаммен бір жаққа шыққанда да қатты ұяламын»

### Surprise
Surprise at the unexpected, **or** bewilderment and incomprehension: таң қалдым, түсінбеймін,
қалай солай болды? Without moral judgement.

> «Астанада қыркүйекте қар жауды. Қыркүйекте!!»

> «Кеше ғана доллар 520 болды, бүгін обменникте мүлде басқа сан. Бір түнде не болып кетті?»

### Disgust
Aversion to something **external**: a person, an act, filth, physiology.

> «асханада борщтан шаш шықты. ұзын, қара. қасықты қойдым да тамақ ішпей шығып кеттім»

> «Сосед подъезге қоқыс пакетін шығарып қояды, үш күн тұрады, ағып кетеді»

### Neutral
No expressed emotion of the author: information, a mundane question, a joke, banter, an
aphorism, provocation, or an account of a situation without the author's own state.

> «Неге кухняның раковинасында қол жуу бір түрлі»

> «Туысқандар жасаған иттіктерді жазып кетші осы жерге»

---

## Boundary rules

| What the post contains | Class | Not to be confused with |
|---|---|---|
| "I myself am worth nothing", self-blame | **Worthlessness** | Shame, Hopelessness |
| ұят болды about a specific episode or trait | **Shame** | Worthlessness |
| ұяламын as a character trait, fear of future situations | **Fear** | Shame |
| ұят in a purely humorous anecdote, no distress | **Neutral** | Shame |
| "nothing will change, the same lies ahead" | **Hopelessness** | Worthlessness, Exhaustion |
| "no strength left, I can't cope" | **Exhaustion** | Hopelessness |
| loss, death of a person or pet, separation, moving away | **Loneliness** | Exhaustion, Neutral |
| "nobody needs me" — there is nobody around | **Loneliness** | Worthlessness |
| "nobody needs me" — I am useless | **Worthlessness** | Loneliness |
| a grievance against a specific person in one's life | **Frustration** | Indignation |
| outrage at a norm, at society, at "how things are done" | **Indignation** | Frustration |
| таң қалдым **with** a moral judgement | **Indignation** | Surprise |
| таң қалдым **without** a judgement | **Surprise** | Indignation |
| aversion to an external object or person | **Disgust** | Indignation |
| aversion to oneself | **Worthlessness** | Disgust |
| anger at oneself | **Worthlessness** | Frustration |
| a calm request for advice, no state of one's own | **Neutral** | Frustration, Fear |
| a question carrying anxiety about the future | **Fear** | Neutral |
| a joke, anecdote, self-irony, provocation | **Neutral** | Joy, Shame, Frustration |
| a hard story whose author does not name their own state | **Neutral** | any |

### Frustration or Indignation — a quick test

Ask: **does the post survive if the author is removed from it?**

- "My neighbour takes my things without asking" — without the author there is no post →
  **Frustration**.
- "Here a girl gets condemned and a boy does not" — the author is only a witness to the norm →
  **Indignation**.

### The most frequent error: Frustration against Neutral

Crude or blunt wording does not by itself indicate emotion. A post in the register of "this
has built up, let me say it" is Frustration; a post in the register of "let's discuss / post
your stories / here's a joke" is Neutral, however bluntly it is written.

---

## Additional rules

1. **Mixed emotions** — choose the **dominant** one, the emotion the post was written for. If
   none can be singled out and the post is mainly an account of a situation, Neutral.
2. **Past emotions.** If the author recalls what they felt earlier but is calm now, annotate
   the present state (often Neutral). Exception: Shame, where recalling the awkward episode is
   itself the experience (есіме түссе ұялып кетем).
3. **Do not fill in for the author.** "Given the situation they must be suffering" is still
   Neutral.
4. **Long posts.** Judge by what the post was written for, not by the most vivid phrase in the
   middle.
5. **A question at the end** (не істеу керек?, қалай ойлайсыңдар?) does not determine the
   class. What determines it is the state in which the author asks.
6. Exactly one class per post. In the corpus, posts that fit none of the classes, contained
   advertising, or involved minors in a sexualised context were removed rather than forced
   into a class.
