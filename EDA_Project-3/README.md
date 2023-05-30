# PROJECT-3. Обнаружение накрутки рейтинга отелей сайта Booking. EDA + Feature Engineering

## Оглавление
[1. Описание проекта](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#описание-проекта)

[2. Какой кейс решаем?](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#этапы-работы-над-проектом)

[5. Результаты](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#результаты)

[6. Выводы](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#выводы)

### Описание проекта

Дата-сайентист из компании Booking работает над решением проблемы накрутки рейтинга нечестными отелями. Для этого он работает над построением модели машинного обучения, предсказывающей рейтинг на основе имеющихся данных. Дата-сайентист должен добиться максимальной точности в предсказании модели, а для этого подготовить данные максимально тщательно.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#оглавление)

### Какой кейс решаем?

**Условия соревнования**

Работаем с готовым датасетом , содержащим данные о 515 тысячах отзывах на отели Европы. Проходим следующие шаги подготовки данных: очистка, анализ, проектирование признаков, их преобразования, а далее используем заранее заготовленный код для создания и обучения модели. 

Чтобы оценить результат, будем ориентироваться на метрику MAPE: чем она меньше, тем лучше. 

**Метрика качества**

Для оценки качества модели мы будем использовать метрику MAPE (mean absolute percentage error), или среднюю абсолютную процентную ошибку предсказанных значений в отношении фактических. 

<image src="/images/mape.gif" alt="Формула подсчета MAPE">

**Что практикуем**

При подготовке датасета необходимо будет вспомнить все шаги разведочного анализа, или EDA. Нужно будет не только 
- избавиться от пропущенных значений и нечисловых признаков, 
но и: 
- спроектировать новые признаки на основе информации, уже содержащейся в данных, или используя внешние источники данных, если это возможно,
- также будем использовать кодирование и преобразование признаков, 
- а после - отберём лучшие из них.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#оглавление)

### Краткая информация о данных

Датасет можно скачать в виде файла [hotels.csv](https://drive.google.com/file/d/1Qj0iYEbD64eVAaaBylJeIi3qvMzxf2C_/view?usp=sharing). В нём содержатся сведения о 515 000 отзывов на отели Европы.

Данные содержат 17 полей со следующей информацией:

**hotel_address** — адрес отеля;
**review_date** — дата, когда рецензент разместил соответствующий отзыв;
**average_score** — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
**hotel_name** — название отеля;
**reviewer_nationality** — страна рецензента;
**negative_review** — отрицательный отзыв, который рецензент дал отелю;
**review_total_negative_word_counts** — общее количество слов в отрицательном отзыв;
**positive_review** — положительный отзыв, который рецензент дал отелю;
**review_total_positive_word_counts** — общее количество слов в положительном отзыве.
**reviewer_score** — оценка, которую рецензент поставил отелю на основе своего опыта;
**total_number_of_reviews_reviewer_has_given** — количество отзывов, которые рецензенты дали в прошлом;
**total_number_of_reviews** — общее количество действительных отзывов об отеле;
**tags** — теги, которые рецензент дал отелю;
**days_since_review** — количество дней между датой проверки и датой очистки;
**additional_number_of_scoring** — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
**lat** — географическая широта отеля;
**lng** — географическая долгота отеля.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#оглавление)

### Этапы работы над проектом

Задачу, которая стоит перед дата-сайентистом, можно свести к пяти пунктам:

**Удаление строковых значений** 
Вам необходимо удалить из набора данных столбцы, данные в которых представлены не числами.

**Очистка от пропущенных значений** 
На предыдущем шаге мы делали это самым грубым из всех возможных способов, сейчас попробуйте подойти к процессу более гибко.

**Создание новых признаков** 
Мы попробуем создать новые столбцы с данными из существующих данных или с использованием внешних источников.

**Преобразование признаков** Применим различные преобразования над признаками вроде нормализации, стандартизации.
Отбор признаков. Используем анализ мультиколлинеарности как шаг отбора признаков для модели.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#оглавление)

### Результаты

В результате пробразования данных из датасета удалось добиться показателя качества модели MAPE в размере ~0.0924.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#оглавление)

### Выводы

Предобработка, разведочный анализ данных позволяют заметно улучшить качество работы модели машинного обучения по предсказанию рейтинга отеля.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/tree/main/EDA_Project-3/README.md#оглавление)