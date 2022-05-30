# Аналитик данных — Яндекс.Практикум
[Аналитик данных — Яндекс.Практикум](https://praktikum.yandex.ru/data-analyst/)

Ссылка на курс: https://praktikum.yandex.ru/data-analyst/


## Как выглядит программа:
[Аналитик данных — программа](https://code.s3.yandex.net/consult/programs/%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_%D0%BE%D1%82_%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D1%83%D0%BC%D0%B0.pdf)

## Как выглядит сертификат ([PDF-версия](certificate/certificate.pdf)):
![Аналитик данных — сертификат](/certificate/certificate-1.png)

## Описание проектов:
| Проект    | Задачи проекта   | Описание проекта                                                   | Навыки и инструменты  |
|-----------|------------------|--------------------------------------------------------------------|-----------------------|
|1 [Исследование музыки больших городов](https://github.com/Rabosina/practicum_Y/blob/main/01%20%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20Python/YP1_music_project.ipynb)|На реальных данных Яндекс.Музыки c помощью библиотеки Pandas и её возможностей проверить данные и сравнить поведение и предпочтения пользователей двух столиц — Москвы и Санкт-Петербурга|Сравнение Москвы и Петербурга окружено мифами: - Москва — мегаполис, подчинённый жёсткому ритму рабочей недели; - Петербург — город своеобразной культуры, непохожий на Москву. Некоторые мифы отражают действительность. Другие — пустые стереотипы. Бизнес должен отличать первые от вторых, чтобы принимать рациональные решения. На реальных данных Яндекс.Музыки я проверила данные и сравнила поведение пользователей двух столиц|Pandas, Python. Обработка данных, дубликаты, пропуски, логическая индексация, группировка, сортировка|
|2 [Исследование надежности заемщиков](https://github.com/Rabosina/practicum_Y/blob/main/02%20%D0%9F%D1%80%D0%B5%D0%B4%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85/YP2_credit_scoring__project.ipynb)|На основе статистики о платёжеспособности клиентов исследовать влияет ли семейное положение и количество детей клиента на факт возврата кредита в срок|На основе данных кредитного отдела банка исследовала влияние семейного положения и количества детей на факт погашения кредита в срок. Была получена информация о данных. Определены и обработаны пропуски. Заменены типы данных на соответствующие хранящимся данным. Удалены дубликаты. Категоризованы данные. Один датафрейм декомпозирован на три.|Pandas, Python, предобработка данных. Обработка данных, дубликаты, пропуски, категоризация, декомпозиция|
|3 [Исследование объявлений о продаже квартир](https://github.com/Rabosina/practicum_Y/blob/main/03%20%D0%98%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85/YP3_real_estate_project.ipynb)|Используя данные сервиса Яндекс.Недвижимость, определить рыночную стоимость объектов недвижимости и типичные параметры квартир|На основе данных сервиса Яндекс.Недвижимость определена рыночная стоимость объектов недвижимости разного типа, типичные параметры квартир, в зависимости от удаленности от центра. Проведена предобработка данных. Добавлены новые данные. Построены гистограммы, боксплоты, диаграммы рассеивания.|Matplotlib, Pandas, Python, визуализация данных, исследовательский анализ данных, предобработка данных. Обработка данных, histogram, boxplot, scattermatrix, категоризация, scatterplot,  фрод-мониторинг|
|4 [Определение перспективного тарифа для телеком-компании](https://github.com/Rabosina/practicum_Y/blob/main/04%20%D0%A1%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85/YP4_mobile_operator_project.ipynb)|На основе данных клиентов оператора сотовой связи проанализировать поведение клиентов и поиск оптимального тарифа|Проведен предварительный анализ использования тарифов на выборке клиентов, проанализировано поведение клиентов при использовании услуг оператора и рекомендованы оптимальные наборы услуг для пользователей. Проведена предобработка данных, их анализ. Проверены гипотезы о различии выручки абонентов разных тарифов и различии выручки абонентов из Москвы и других регионов.|Matplotlib, NumPy, Pandas, Python, SciPy, описательная статистика, проверка статистических гипотез. Обработка данных, histogram, boxplot, статистический тест, критерий Стьюдента |
|5 [Сборный проект 1. Анализ игровой индустрии](https://github.com/Rabosina/practicum_Y/blob/main/05%20%D0%A1%D0%B1%D0%BE%D1%80%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%201/YP5_S1_games_project.ipynb)|Используя исторические данные о продажах компьютерных игр, оценки пользователей и экспертов, жанры и платформы, выявить закономерности, определяющие успешность игры |Выявлены параметры, определяющие успешность игры в разных регионах мира. На основании этого подготовлен отчет для магазина компьютерных игр для планирования рекламных кампаний. Проведена предобработка данных, анализ. Выбран актуальный период для анализа. Составлены портреты пользователей каждого региона. Проверены гипотезы: средние пользовательские рейтинги платформ Xbox One и PC одинаковые; средние пользовательские рейтинги жанров Action и Sports разные. При анализе использовал критерий Стьюдента для независимых выборок.|Matplotlib, NumPy, Pandas, Python, исследовательский анализ данных, описательная статистика, предобработка данных, проверка статистических гипотез. Обработка данных, histogram, boxplot, статистический тест, критерий Стьюдента, piechart|
|6 [Исследование данных об инвестиции венчурных фондов в компании-стартапы](https://github.com/Rabosina/practicum_Y/tree/main/06%20%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20SQL)|Произвести различные выгрузки данных авиакомпаний с помощью SQL|Проект автоматически проверяется в тренажёре SQL. В самостоятельном проекте этого курса работа идёт с базой данных, которая хранит информацию о венчурных фондах и инвестициях в компании-стартапы. Эта база данных основана на датасете Startup Investments, опубликованном на популярной платформе для соревнований по исследованию данных Kaggle|PostgreSQL, SQL. Обработка данных, выгрузка данных, SQL|
|7 [Анализ бизнес-показателей приложения ProcrastinatePRO+](https://github.com/Rabosina/practicum_Y/blob/main/07%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B1%D0%B8%D0%B7%D0%BD%D0%B5%D1%81-%D0%BF%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%B9/YP7_business_indicators_project.ipynb)|Задача для маркетингового аналитика развлекательного приложения Procrastinate Pro+. Несмотря на огромные вложения в рекламу, последние несколько месяцев компания терпит убытки. Ваша задача — разобраться в причинах и помочь компании выйти в плюс.|Проведен анализ данных от ProcrastinatePRO+. Рассчитаны различные метрики, использован когортный анализ: LTV, CAC, Retention rate, DAU, WAU, MAU и т.д. Использованы уже написанные ранее функции расчёта метрик. Сделаны правильные выводы по полученным данным|Matplotlib, Pandas, Python, Seaborn, когортный анализ, продуктовые метрики, юнит-экономика. Обработка данных, статистический тест, LTV, CAC, когортный анализ|
|8 [Проверка гипотез по увеличению выручки в интернет-магазине —оценить результаты A/B теста](https://github.com/Rabosina/practicum_Y/blob/main/08%20%D0%9F%D1%80%D0%B8%D0%BD%D1%8F%D1%82%D0%B8%D0%B5%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B9%20%D0%B2%20%D0%B1%D0%B8%D0%B7%D0%BD%D0%B5%D1%81%D0%B5/YP8_internet_store_project.ipynb)|Используя данные интернет-магазина приоритезировать гипотезы, произвести оценку результатов A/B-тестирования различными методами|Проведена приоритизация гипотез по фреймворкам ICE и RICE. Затем провел анализ результатов A/B-теста, построил графики кумулятивной выручки, среднего чека, конверсии по группам, а затем посчитал статистическую значимость различий конверсий и средних чеков по сырым и очищенным данным. На основании анализа мной было принято решение о нецелесообразности дальнейшего проведения теста|A/B-тестирование, Matplotlib, Pandas, Python, SciPy, проверка статистических гипотез. A/B-тест, статистический тест, фреймворк, RICE, ICE|
|9 [Исследования рынка общепита в Москве для принятия решения об открытии нового заведения](https://github.com/Rabosina/practicum_Y/blob/main/09%20%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85/YP9_MSC_cafe_project.ipynb) / [Презентация](https://github.com/Rabosina/practicum_Y/blob/main/09%20%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85/%D0%9F%D1%80%D0%B5%D0%B7%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BE%D0%B1%D1%89%D0%B5%D0%BF%D0%B8%D1%82%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B.pdf)|Исследование рынка общественного питания на основе открытых данных, подготовка презентации для инвесторов|Мною был исследован вопрос - будет ли успешным и популярным на долгое время кафе, в котором гостей обслуживают роботы-официанты. По результатам анализа подготовлена презентация для инвесторов с рекомендациями. В построении графиков я использовала библиотеки seaborn и plotly|Pandas, Plotly, Python, Seaborn, визуализация данных. Обработка данных, визуализация данных, создание презентаций|
|10 [Сборный проект 2. Анализ пользовательского поведения в мобильном приложении — воронки](https://clck.ru/nwSZp)|На основе данных использования мобильного приложения для продажи продуктов питания проанализировать воронку продаж, а также оценить результаты A/A/B-тестирования |В данном проекте мной были изучены принципы событийной аналитики. Я построила воронку продаж, исследовал путь пользователей до покупки. Проанализировала результаты A/B-теста введения новых шрифтов. Сравнила 2 контрольных группы между собой, убедилась в правильном разделении трафика, а затем сравнила с тестовой группой. Выявлено, что новый шрифт значительно не повлияет на поведение пользователей|A/B-тестирование, Matplotlib, Pandas, Plotly, Python, Seaborn, визуализация данных, проверка статистических гипотез, продуктовые метрики, событийная аналитика. A/А/B-тест, визуализация, статистический тест|
|11 [Дашборд по пользовательским событиям для Яндекс.Дзена](https://github.com/Rabosina/practicum_Y/tree/main/11%20%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F.%20%D0%94%D0%B0%D1%88%D0%B1%D0%BE%D1%80%D0%B4%20Tableau)|Используя данные Яндекс.Дзена построить дашборд с метриками взаимодействия пользователей с карточками статей|Работу над этим проектом я провела на удаленной машине в сервисе Yandex.Cloud. Мной был установлен PostgreSQL, развернута база данных. Затем я написала скрипт пайплайна, который позволил собирать данные за определенный временной период, и настроила его автономную работу через crontab. Для визуализации собранных данных я написала скрипт дашборда с несколькими фильтрами и также запустила его на удаленной машине. По результатам была подготовлена презентация с полученными графиками|Python, SQLAlchemy, PostgreSQL, dash, Tableau, продуктовые метрики, построение дашбордов. Дашборд, пайплайн, Yandex.Cloud, удаленный сервер, виртуальная машина, cron|
|12 [Прогнозирование вероятности оттока пользователей для фитнес-центров](https://clck.ru/nwQJ7)|На основе данных о посетителях сети фитнес-центров спрогнозировать вероятность оттока для каждого клиента в следующем месяце, сформировать с помощью кластеризации портреты пользователей|В данном проекте были изучены принципы событийной аналитики. Построена воронку продаж, исследован путь пользователей до покупки. Проанализированы результаты A/B-теста введения новых шрифтов. Были сопоставлены 2 контрольных группы между собой, оценена корректность проведения А/В теста и разделение трафика. Выявлено, что новый шрифт значительно не повлияет на поведение пользователей.|Python, Pandas, Scikit-learn, Matplotlib, Seaborn, машинное обучение, классификация, кластеризация. KMeans, Machine Learning, дендрограмма, RandomForestClassifier, LogisticRegression|
|13 Выпускной проект: [Исследование](https://clck.ru/nwPCb), [Презентация](https://clck.ru/iL5XQ)|Провести анализ ассортимента интернет-магазина товаров для дома и быта «Пока все ещё тут» на основе транзакций для отдела закупки и сформулировать рекомендации.| В данном проекте проведен исследовательский анализ данных EDA, проведена категоризация данных, использовано машинное обучение. Товары разделены на кластеры: охарактеризованы их основные свойства, проанализированы основные признаки, наиболее сильно влияющие на показатель выручки. Сформулированы и проверены статистические гипотезы. Даны рекомендации для повышения эффективности работы магазина  | Python, Pandas, Scikit-learn, Matplotlib, Seaborn, машинное обучение, классификация, кластеризация, KMeans, Machine Learning, дендрограмма, RandomForestClassifier, LogisticRegression, Tableau, визуализация |
|14  Выпускной проект:[SQL](https://github.com/Rabosina/practicum_Y/tree/main/15%20%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.%20SQL%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D1%8B%D0%BD%D0%BA%D0%B0%20%D0%BA%D0%BD%D0%B8%D0%B3)|Проанализировать базу данных книжного сервиса (при помощи SQL-запросов) и выявить ключевые характеристики и данные, которые помогут сервису для чтения книг сформулировать ценностное предложение для нового продукта.  | В ходе выполнения проекта произведена коннекция к базе данных, осмотр содержимого таблиц, написание 5 SQL-запросов. Сформулирован общий вывод по результатам запросов.| Python, Pandas, SQL, SQLAlchemy| 
|15  Выпускной проект: [A/B тест](https://nbviewer.org/github/Rabosina/practicum_Y/blob/main/14%20%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.%20AB%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%BE%D0%B2%20%D0%B2%D0%BD%D0%B5%D0%B4%D1%80%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F/YP_14_AB_recommender_system_test.ipynb)|На основе данных о проанализировать воронку продаж, а также оценить корректность и результаты A/B-тестирования. |В рамках проекта удалось: оценить корректность проведения теста, проанализировать результаты теста. Чтобы оценить корректность проведения теста, проверено: пересечение тестовой аудитории с конкурирующим тестом, выполнение условий Технического задания, совпадение теста и маркетинговых событий, другие проблемы временных границ теста. |A/B-тестирование, Matplotlib, Pandas, NumPy, Plotly, Python, Seaborn, визуализация данных, проверка статистических гипотез, продуктовые метрики, событийная аналитика.|
---
