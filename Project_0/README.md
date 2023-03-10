# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#этапы-работы-над-проектом)

[5. Результаты](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#результаты)

[6. Выводы](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#выводы)

### Описание проекта
Реализация игры с угадыванием числа, при этом компьютер самостоятельно загадывает и отгадывает число. Существуют условия реализации проекта, которые раскрываются ниже.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#оглавление)

### Какой кейс решаем?

**Условия соревнования**

- Загаданное компьютером число лежит в диапазоне от 1 до 100.
- Алгоритм сравнивает новое число с загаданным - больше оно или меньше.
- Число попыток на отгадку числа в среднем не должно превышать 20. 

**Метрика качества**

Оценка работы алгоритма производится на основе среднего значениея для тысячи вариантов загаданных чисел.

**Что практикуем**

- Учимся писать хороший код на Python.
- Учимся работать с IDE.
- Учимся работать с GitHub.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#оглавление)

### Краткая информация о данных

Работа алгоритма основывается на псевдослучайных целых числах. Используется библиотека numpy, метод random. 

**Функции:**

1. ***take_number*** - компьютер "загадывает" псевдочлучайное целое число

>Переменная ***number*** - число, которое "загадывает" компьютер.

2. ***guess_number*** - генерирует варианты чисел, чтобы угадать загаданное число, возвращает количество попыток, необходимых для отгадки. Используется рекурсия.

>**Переменные:**

>>***guess_try*** - псевдослучайное целое число, которое генерирует компьютер с целью "угадать" number;

3. ***start_guess_counter*** - возвращает рекурсивную функцию guess_number, обнуляя счетчик попыток угадать число.

> Переменная ***count*** - число попыток.

4. ***average_result*** - определяет среднее число попыток, которое требуется указанной функции для отгадки числа. Расчеты производятся на основе массива из 1000 "загаданных" псевдослучайных чисел.

>***Переменные:***

>>***guess_array*** - массив из из 1000 "загаданных" псевдослучайных чисел для расчета среднего количества попыток;

>>***results*** - каждый элемент этого массива показывает количество попыток угадать соответствующий элемент массива guess_array.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#оглавление)

### Этапы работы над проектом

1. Работа над кодом поделена на три части: 
- написание кода, в результате которого компьютер загадывает число;
- создание функции с алгоритмом отгадывания числа, который бы использовал операцию сравнения с загаданным числом;
- написание функции, которая будет подсчитывать, за какое в среднем число попыток алгоритм заканчивает работу.

2. Доработка алгоритма поиска загаданного числа до тех пор, пока он не будет соответствовать нужному по условию качеству.

3. Написание необходимой документации.

4. Фиксация версий библиотек через команду pip freeze.

5. Публикация проекта на GitHub.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#оглавление)

### Результаты

В результате серии запусков алгоритм поиска загаданного числа в среднем добивается успеха менее, чем за 20 попыток.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#оглавление)

### Выводы

Представленный алгоритм соответствует поставленной задаче.

:arrow_up: [к оглавлению](https://github.com/irkovsky/sf_data_science/blob/main/project_0/README.md#оглавление)
