# Window_functions
## About The Project
Проект по анализу таблицы с рекламными объявлениями и таблицы с характеристиками рекламных клиентов.
### Задачи
1. Посчитать среднее количество показов и среднее количество кликов на объявления за весь период.
2. Построить график распределения показов на объявление за весь период.
3. Посчитать скользящее среднее показов с окном 2. 
4. Скользящее среднее часто используется для поиска аномалий в данных. Давайте попробуем нанести на один график значения арифметического среднего по дням и скользящего среднего количества показов. В какой день наблюдается наибольшая разница по модулю между арифметическим средним и скользящим средним? Дни, в которых скользящее среднее равно NaN, не учитываем. 
5. Подгрузить данные по рекламным клиентам и найти среднее количество дней от даты создания рекламного клиента и первым запуском рекламного объявления этим клиентом.
6. Вычислить конверсию из создания рекламного клиента в запуск первой рекламы в течение не более 365 дней.
7. Разбить клиентов по промежуткам от создания до запуска рекламного объявления, равным 30. Определить, сколько уникальных клиентов запустили свое первое объявление в первый месяц своего существования (от 0 до 30 дней). 
8. Построить график категории с количеством уникальных клиентов в них.

### Built With

* Python (библиотеки matplotlib.pyplot, seaborn, pandas, numpy, plotly.express)
