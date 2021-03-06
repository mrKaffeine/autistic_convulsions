# Проект 0. Угадай число

## Оглавление
- [1. Описание проекта](https://github.com/mrKaffeine/autistic_convulsions/tree/main/project_0/README.md#Описание-проекта) 
- [2. Какой кейс решаем?](https://github.com/mrKaffeine/autistic_convulsions/tree/main/project_0/README.md#Какой-кейс-решаем?) 
- [3. Краткая информация о данных](https://github.com/mrKaffeine/autistic_convulsions/tree/main/project_0/README.md#Краткая-информация-о-данных) 
- [4. Этапы работы над проектом](https://github.com/mrKaffeine/autistic_convulsions/tree/main/project_0/README.md#Этапы-работы-над-проектом)
- [5. Результат](https://github.com/mrKaffeine/autistic_convulsions/tree/main/project_0/README.md#Результат) 
- [6. Выводы](https://github.com/mrKaffeine/autistic_convulsions/tree/main/project_0/README.md#Выводы) 

### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [к оглавлению](https://github.com/mrKaffeine/autistic_convulsions/tree/main/project_0/README.md#Оглавление)

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:** 
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под "угадать" подразумевается "написать программу, которая угадывает число".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества** 
Результаты оцениваются по среднемму количеству попыток при 1000 повторений.

**Что практикуем** 
Учимся писать хороший код на Python.

### Краткая информация о данных
**Переменные**
- top_limit: Верхняя граница рандомайзера предполагаемого числа
- bottom_limit: Нижняя граница рандомайзера предполагаемого числа
- number: число, загаданное компьютером

**Функции**
- random_predict(): угадывает загаданное число: подбирает случайным образом, сужая границы поиска благодаря изменению верхнего предела (top_limit) и нижнего предела (bottom_limit).
- score_game(): показывает за сколько попыток в среднем получается угадать число.

:arrow_up: [к оглавлению](https://github.com/mrKaffeine/autistic_convulsions/tree/main/project_0/README.md#Оглавление)