|№|Питання користувача|Іменовані сутності|Інтенти|Відповідь системи|Характеристика відповіді|
| :- | :- | :- | :- | :- | :- |
|1\.|Що таке реабілітація?|` `[{"words": ["реабілітація"],"type": "noun","main word": "реабілітація"}]|` `[ { "intent": "subject", "type": "interrogation", "probability": 0.8, "subject": "реабілітація", "object": null }, { "intent": "object", "type": "interrogation", "probability": 0.6, "subject": null, "object": "реабілітація" }, { "intent": "definition", "type": "narration", "probability": 0.5, "subject": "реабілітація", "object": null } ]|{ "intent": "subject", "results": [ "Реабілітація вважається однією з п'яти стратегій охорони здоров'я і є основною стратегією охорони здоров'я у первинній медичній допомозі.", "Реабілітація є ключовою стратегією охорони здоров'я в ХХІ столітті.", "Реабілітація є однією з головних стратегій охорони здоров'я і має показники результативності, які показані в Таблиці II27." ] }  { "intent": "object", "results": [ "Реабілітація є темою, про яку йдеться в тексті." ] }  { "intent": "definition", "results": [ "Реабілітація - це стратегія в галузі охорони здоров'я, яка спрямована на вирішення основних проблем в сфері здоров'я в суспільстві шляхом надання промоційних, превентивних, лікувальних та реабілітаційних послуг." ] }|TP, TP, TP, FP, TP|
|2|Розкажи про основні задачі реабілітації.|[ { "words": ["основні", "задачі", "реабілітації"], "type": "noun", "main word": "задачі" }, { "words": ["розкажи", "про"], "type": "verb", "main word": "розкажи" }, { "words": ["реабілітації"], "type": "noun", "main word": "реабілітації" } ]|[ { "intent": "find subjects", "type": "narration", "probability": 0.8, "subject": "основні задачі реабілітації", "object": null }, { ["intent": "define intents", "type": "interrogation", "probability": 0.7, "subject": null, "object": null }, { "intent": "find objects", "type": "interrogation", "probability": 0.6, "subject": null, "object": "реабілітації" }, { "intent": "quantity", "type": "imperative", "probability": 0.4, "subject": null, "object": null } ]|{ "intent": "find subjects", "results": [ "Основні задачі реабілітації включають оптимізацію функціонування особи та підвищення її якості життя, а також зосередження на взаємодії особи та середовища для досягнення оптимального результату функціонування." ] }, { "intent": "define intents", "results": [ "Запитання про визначення намірів (intents) можна розуміти як запит на пояснення того, що саме означає термін 'intents'. В контексті даної задачі, intentions (або наміри) – це конкретні запити користувачів, які вони висловлюють через систему взаємодії з іншими користувачами або з комп'ютером за допомогою мови або інших засобів комунікації." ] }, { "intent": "find objects", "results": [ "У тексті згадується об'єкт 'реабілітації', який є основним предметом дослідження та практики у Фізичній та Реабілітаційній Медицині, та який є об'єктом оптимізації функціонування людини." ] }, { "intent": "quantity", "results": null }|TP, FP, FP, TN|
|3|Сфера відповідальності фізичної та реабілітаційної медицини|[ { "words": ["сфера", "відповідальність"], "type": "noun", "main word": "сфера" }, { "words": ["фізична", "медицина"], "type": "noun", "main word": "медицина" }, { "words": ["реабілітаційна", "медицина"], "type": "noun", "main word": "медицина" }, { "words": ["відповідальність"], "type": "noun", "main word": "відповідальність" }, { "words": ["фізична"], "type": "adjective", "main word": "фізичний" }, { "words": ["реабілітаційна"], "type": "adjective", "main word": "реабілітаційний" }]|[ { "intent": "subject", "type": "narration", "probability": 0.8, "subject": "фізична та реабілітаційна медицина", "object": "" }, { "intent": "location", "type": "interrogation", "probability": 0.2, "subject": "", "object": "Сфера відповідальності" } ]|{ "intent": "subject", "results": "Контекст визначення обмеження життєдіяльності та епідеміології функціонування був описаний в тексті, який стосується фізичної та реабілітаційної медицини. Зокрема, реабілітація в цілому і ФРМ спрямовані на оптимізацію функціонування в усіх доменах, що можна вважати частиною фізичної та реабілітаційної медицини." }  { "intent": "location", "results": "В тексті не було згадано конкретну сферу відповідальності, пов'язану з обмеженнями життєдіяльності та епідеміологією функціонування." }|FP, TN|
|4|Міжнародна класифікація функціонування|[ { "words": ["міжнародна класифікація", "функціонування"], "type": "noun", "main word": "класифікація" }, { "words": ["функціонування"], "type": "verb", "main word": "функціонування" } ]|[ { "intent": "subject", "type": "narration", "probability": 0.8, "subject": "Міжнародна класифікація функціонування", "object": null }, { "intent": "object", "type": "interrogation", "probability": 0.6, "subject": null, "object": "Міжнародна класифікація функціонування" }, { "intent": "definition", "type": "imperative", "probability": 0.4, "subject": null, "object": null } ]|{ "intent": "subject", "results": "Міжнародна класифікація функціонування захоплює наше інтуїтивне поняття про обмеження життєдіяльності, як проблеми особи, що виконує дії, які він чи вона має або бажає виконати, внаслідок основного стану здоров'я." }  { "intent": "object", "results": "Міжнародна класифікація функціонування описує досвід концептуалізації обмеження життєдіяльності з точки зору базового поняття функціонування." }  { "intent": "definition", "results": "Будь ласка, надайте більше інформації для визначення, що саме ви хочете дізнатися про Міжнародну класифікацію функціонування." }|TP, TP, FN|
|5|На що повинна спиратися ФРМ?|[ { "words": ["що", "ФРМ"], "type": "noun", "main word": "ФРМ" }, { "words": ["повинна", "спиратися"], "type": "verb", "main word": "спиратися" } ]|[ { "intent": "subject", "type": "interrogation", "probability": 0.8, "subject": "ФРМ", "object": null }, { "intent": "cause", "type": "narration", "probability": 0.6, "subject": "ФРМ", "object": "спиратися" }, { "intent": "way of doing", "type": "interrogation", "probability": 0.4, "subject": null, "object": "спиратися" } ]|{ "intent": "subject", "results": "ФРМ є первинною медичною спеціальністю, зазначена в Білій книзі з Фізичної та Реабілітаційної Медицини у Європі. БК містить інформацію про визначення та поняття ФРМ, основи ФРМ, історію спеціальності ФРМ, знання та навички лікарів ФРМ, сферу клінічних компетентностей ФРМ, місце спеціальності ФРМ в системі охорони здоров'я та суспільстві, освіту та безперервний професійний розвиток лікарів ФРМ, особливості та проблеми науки та досліджень в ФРМ та проблеми та перспективи майбутнього ФРМ." }  { "intent": "cause", "results": "Для опису, розуміння та впливу на функціонування ФРМ повинна спиратися на МКФ, як з точки зору її основної концептуальної моделі функціонування, так і більш практично, на її класифікації, які можуть бути використані для забезпечення порівнянності зібраних та представлених даних. МКФ можливо застосувати в описі окремих пацієнтів ( Таблиця І ), а також популяцій ( Малюнок 2 ). За допомогою МКФ завдання та цілі втручань можна визначити в термінах рівня функціонування особи ( через відповідні домени ), основного стану здоров'я та супутніх захворювань, а також відповідних особистих факторів та факторів середовища, які формують життєвий досвід здоров'я особи." }  { "intent": "way of doing", "results": "Методика функціональної класифікації МКФ може бути використана для опису окремих пацієнтів ( Таблиця І ), а також популяцій ( Малюнок 2 ). За допомогою МКФ завдання та цілі втручань можна визначити в термінах рівня функціонування особи ( через відповідні домени ), основного стану здоров'я та супутніх захворювань, а також відповідних особистих факторів та факторів середовища, які формують життєвий досвід здоров'я особи." }|FP, TP, FP|
|6|Розкажи про взаємодію особи і середовища.|[ { "words": ["взаємодія", "особа", "середовище"], "type": "noun", "main word": "взаємодія" }, { "words": ["розкажи"], "type": "verb", "main word": "розкажи" } ]|[ { "intent": "find subjects", "type": "narration", "probability": 0.7, "subject": "особа", "object": "середовище" }, { "intent": "find objects", "type": "narration", "probability": 0.5, "subject": "особа", "object": "взаємодію" }, { "intent": "define intents", "type": "interrogation", "probability": 0.4, "subject": "", "object": "взаємодію особи і середовища" }]|{ “intent”: “find subjects”, “results”: “В контексті практики реабілітації особа є одним з головних суб'єктів. Втручання повинні зосереджуватися на взаємодії особи та середовища для досягнення ефективності та якості реабілітаційних заходів.” }  { “intent”: “find objects”, “results”: “В контексті практики реабілітації взаємодія між особою та середовищем є важливим об'єктом, на якому повинні зосереджуватися реабілітаційні заходи.” }  { “intent”: “define intents”, “results”: “Один з головних інтентів в контексті практики реабілітації - це сприяння взаємодії між особою та середовищем для досягнення ефективності та якості реабілітаційних заходів.” }|TP, TP, TP|
|7|Інструменти класифікації обмежень життєдіяльності.|[ { "words": ["інструменти", "класифікації", "обмежень", "життєдіяльності"], "type": "noun", "main word": "інструмент" }, { "words": ["класифікації"], "type": "noun", "main word": "класифікація" }, { "words": ["обмежень", "життєдіяльності"], "type": "noun", "main word": "обмеження" }, { "words": ["класифікації"], "type": "verb", "main word": "класифікувати" } ]|[ { "intent": "instrument", "type": "narration", "probability": 0.9, "subject": "Інструменти", "object": "класифікації обмежень життєдіяльності" }, { "intent": "find objects", "type": "interrogation", "probability": 0.7, "subject": "", "object": "обмежень життєдіяльності" }, { "intent": "find subjects", "type": "interrogation", "probability": 0.6, "subject": "", "object": "" }, { "intent": "quantity", "type": "interrogation", "probability": 0.4, "subject": "", "object": ""}]|{ "intent": "instrument", "results": "Інструменти класифікації обмежень життєдіяльності дозволяють визначити домени функціонування, збирати дані про функціонування, звітувати про дані та проводити достовірне порівняння даних про функціонування з різних джерел. Існують також практичні інструменти для імплементації МКФ в клінічну практику, надання та оплату послуг, політику і дослідження." } { "intent": "find objects", "results": "Об'єктом дослідження є обмеження життєдіяльності." } { "intent": "find subjects", "results": "В даному тексті немає конкретного суб'єкта, але йдеться про клініцистів, дослідників та користувачів МКФ." } { "intent": "quantity", "results": null }|TP, FP, TN, TN|
|8|Як враховується життєвий досвід здоров’я?|[ { "words": ["враховується", "досвід", "здоров'я"], "type": "verb", "main word": "враховується" }, { "words": ["життєвий", "досвід", "здоров'я"], "type": "noun", "main word": "життєвий досвід здоров'я" } ]|[ { "intent": "subject", "type": "interrogation", "probability": 0.8, "subject": "життєвий досвід здоров’я", "object": null }, { "intent": "conditions", "type": "narration", "probability": 0.6, "subject": "здоров’я", "object": "життєвий досвід" }, { "intent": "relation", "type": "interrogation", "probability": 0.4, "subject": "життєвий досвід", "object": "здоров’я" } ]|{ "intent": "subject", "results": "МКФ забезпечує класифікацію та стандартну міжнародну загальну мову, в термінах якої життєвий досвід здоров'я може бути операціоналізованим на індивідуальному та популяційному рівнях. МКФ є міжнародною класифікацією здоров'я та функціонування; це також інформаційна довідкова система для стандартизованого опису здоров'я, функціонування та обмежень життєдіяльності на всіх рівнях охорони здоров'я та пов'язаних систем, включаючи соціальні, освітні та трудові." }  { "intent": "conditions", "results": "МКФ є міжнародною класифікацією здоров'я та функціонування; це також інформаційна довідкова система для стандартизованого опису здоров'я, функціонування та обмежень життєдіяльності на всіх рівнях охорони здоров'я та пов'язаних систем, включаючи соціальні, освітні та трудові. У МКФ біомедична природа та загальний вплив станів здоров'я в контексті життя людей, беручи до уваги середовище, в якому вони живуть, та їх особисті фактори, і називається функціонуванням. МКФ є значущою та корисною для практикуючих фахівців, які прагнуть оптимізувати функціонування окремих пацієнтів, політиків, які прагнуть формувати систему охорони здоров'я відповідно до вимог і потреб функціонування людей, та для дослідників, які прагнуть пояснити та впливати на функціонування, а також наук та професій з функціонування." }  { "intent": "relation", "results": "МКФ концептуалізує життєвий досвід здоров'я з точки зору базового поняття функціонування МКФ в різних доменах функцій та структур організму, активності та - напр. всього, що робить організм, і дій, простих та складних, що виконують у взаємодії з факторами середовища, які можуть діяти як бар'єри (обмежують виконання) або сприятливі чинники (підвищують виконання). У МКФ зазначено, що порогові значення обмежень життєдіяльності будуть визначатися по-різному для різних цілей, включаючи юридичні визначення обмежень життєдіяльності з метою надання підтримки та послуг, які є різними між країнами та, навіть, між різними міністерствами всередині країн." }|TP, TP, TP|
|9|Особливості реабілітації онкохворих.|[ { "words": ["особливості", "реабілітація", "онкохворі"], "type": "noun", "main word": "реабілітація" }, { "words": ["онкохворих"], "type": "noun", "main word": "онкохворих" }, { "words": ["надати", "реабілітація"], "type": "verb", "main word": "реабілітація" }, { "words": ["онкохворих"], "type": "noun", "main word": "онкохворих" } ]|[ { "intent": "find subjects", "type": "narration", "probability": 0.8, "subject": "онкохворі", "object": null }, { "intent": "find objects", "type": "narration", "probability": 0.7, "subject": null, "object": "реабілітація" }, { "intent": "define intents", "type": "imperative", "probability": 0.6, "subject": null, "object": null } ]|{ "intent": "find subjects", "results": "У тексті немає конкретної інформації про реабілітацію онкохворих." }  { "intent": "find objects", "results": { "Введення Біла книга ( БК ) з Фізичної та Реабілітаційної Медицини ( ФРМ ) у Європі розроблена чотирма Європейськими Органами ФРМ і є довідником для лікарів ФРМ у Європі.": "реабілітація", "Реабілітація, основна стратегія охорони здоров'я в системі охорони здоров'я": "реабілітація", "Визначення реабілітації на основі МКФ": "реабілітація" } }  { "intent": "define intents", "results": "Мета цього запиту - отримати перелік можливих намірів, які можуть бути задані відносно тексту. У цьому випадку можливі наміри: 'find subjects' - знайти предмети, про які йдеться в тексті; 'find objects' - знайти об'єкти, які згадуються в тексті; 'define intents' - визначити можливі наміри, які можна задати відносно тексту." }|TN, FP, FP|
|10|Основне джерело смертності у розвинених країнах.|[ { "words": ["основне", "джерело", "смертності"], "type": "noun", "main word": "джерело" }, { "words": ["розвинених", "країн"], "type": "noun", "main word": "країн" }, { "words": ["умирання"], "type": "verb", "main word": "умирання" } ]|[ { "intent": "subject", "type": "narration", "probability": 0.6, "subject": "основне джерело смертності", "object": "" }, { "intent": "place", "type": "narration", "probability": 0.3, "subject": "", "object": "розвинені країни" }, { "intent": "object", "type": "interrogation", "probability": 0.08, "subject": "", "object": "смертність" }, { "intent": "quantity", "type": "imperative", "probability": 0.02, "subject": "", "object": "кількість смертей" } ]|{ "intent": "subject", "results": "Головним джерелом смертності стали хронічні неінфекційні захворювання, які є основним джерелом смертності в високорозвинених країнах." }  { "intent": "place", "results": "Високорозвинені країни є місцем, де хронічні неінфекційні захворювання стали основним джерелом смертності." }  { "intent": "object", "results": "Запит на кількість смертей не був знайдений у вхідних даних." }  { "intent": "quantity", "results": "Запит на кількість смертей не був знайдений у вхідних даних." }|TP, TP, TN, TN|

TP – 17 TN – 7 FP – 9 FN – 1  Accuracy = 0,7059 Precision = 0,6534 Recall = 0,9444 F1 = 0,7724   Проводил тестирование нашей методики. Не могу сказать, на сколько всё это корректно, да и количество вопросов было не таким уж и большим. Несколько слов о методике. Метод предполагает возможность выдачи нескольких ответов на один вопрос в соответствии с интентами. Сразу оговорюсь, что вопросов совсем-совсем из другой предметной области, чтобы даже нельзя было выбрать ни одного релевантного контекста не задавалось, тут TN гарантирован. Соответственно, некоторые из ответов могут быть правильными, другие - не совсем. В зачёт шли все ответы. Таким образом, у нас при подсчёте результатов – ответов больше, чем вопросов. Истинно позитивным (TP) считалось если ответ дан и он верен. Истинно негативным считался случай, если ответ не дан (или система в том или ином виде ответила «не знаю») и такой информации в тексте действительно не содержится. Ложно позитивным считалась попытка системы дать информативный ответ, но он не соответствовал или плохо соответствовал вопросу. Ложно негативным считалось, если ответ не дан, но такая информация на самом деле в тексте была. Результат вышел следующий: TP – 17 TN – 7 FP – 9 FN – 1 Таким образом, метрики: Accuracy = 0,7059 Precision = 0,6534 Recall = 0,9444 F1 = 0,7724 Мы видим, что в рамках данного метода GPT склонен к ложно положительным ответам. То есть, он всячески пытается что-то выдать, хоть как-то связанное, даже если оно не совсем в тему. Но всё-таки бывает, что честно говорит «не знаю» или «информации в предоставленном тексте не содержится». Но, на самом деле, не всё так ужасно с таким низким Precision. Дело в том, что при подсчёте учитывались все ответы, в том числе и данные на один вопрос. Так, часто эти FP соседствовали с TP. То есть, это получается, как дополнительная информация, которую напрямую не спрашивали. Но всё же – это своего рода поисковый мусор.     TP – 8 TN – 2 FP – 0 FN – 0   Accuracy = 1 Precision = 1 Recall = 1 F1 = 1    