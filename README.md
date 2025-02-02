# goit-algo-fp
my final project of the basic algorithms

Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком.
Висновки:
1. Реверсування списку реалізовано зі зміною посилань вузлів. Функція reverse_list змінює посилання між вузлами, розгортаючи список у зворотному порядку.
2. Сортування (merge sort) розбиває список на частини і збирає назад у відсортованому порядку.
3. Об'єднання двох списків зберігає порядок сортування. Функція merge_sorted_lists коректно об'єднує два впорядковані однозв’язні списки в один відсортований список.
Виконання коду дивіться у файлі: task_1.py

Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

 - Використовуємо модуль turtle, який ефективніший для фракталів.
 - Малюємо дерево рекурсивно, кожна нова гілка повертається на 45°.
 - Малювання швидке завдяки t.speed(0).
 - Рівень рекурсії налаштовується, можемо обрати 7-12.
Виконання коду дивіться у файлі: task_2.py

Завдання 3. Дерева, алгоритм Дейкстри
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

Виконання коду дивіться у файлі: task_3.py
Як працює код?
 - Зберігаємо граф у вигляді списку суміжності
 - Використовуємо heapq для роботи з бінарною купою
 - Алгоритм Дейкстри обчислює найкоротші шляхи
 - Результат — відстань до кожної вершини від стартової

Завдання 4. Візуалізація піраміди
Виконання коду дивіться у файлі: task_4.py
Пояснення коду
4.1. Клас Node
Цей клас представляє вузол дерева. Крім зберігання значення (key), кожен вузол має посилання на лівого і правого нащадка. Додатково кожному вузлу присвоюється унікальний ідентифікатор (id), що допомагає однозначно ідентифікувати його під час побудови графа.

4.2. Функція add_edges
Рекурсивно обходить дерево, додаючи в граф (використовуючи бібліотеку networkx) вузли і ребра між ними. При цьому для кожного вузла обчислюються координати (параметри x і y), що забезпечує коректне розташування вузлів на зображенні.

4.3. Функція draw_tree
Створює спрямований граф, заповнює його за допомогою функції add_edges, а потім за допомогою matplotlib відмальовує дерево. Колір вузлів і підписи беруться з атрибутів кожного вузла.

4.4.Функція build_heap_tree
Основна функція для перетворення масиву, що представляє бінарну купу, на бінарне дерево.

 - Приймає список heap і поточний індекс (за замовчуванням 0 - корінь купи).
 - Для поточного індексу створюється вузол із відповідним значенням.
 - Обчислюються індекси лівого (2 * index + 1) і правого (2 * index + 2) нащадків, після чого функція рекурсивно будує відповідні піддерева.
Таким чином, виходить бінарне дерево, що відповідає логіці подання бінарної купи у вигляді масиву.
4.5. Приклад використання
У прикладі створюється масив heap, який потім перетворюється на бінарне дерево за допомогою build_heap_tree. Функція draw_tree відповідає за візуалізацію отриманого дерева.

Завдання 5. Візуалізація обходу бінарного дерева
Виконання коду дивіться у файлі: task_5.py
Пояснення коду
1. Підготовка дерева і побудова графа
- Клас Node задає структуру вузла дерева з унікальним ідентифікатором.
- Функція get_positions (через допоміжну функцію add_edges) обходить дерево і формує словник координат для вузлів, який використовується для розташування під час візуалізації.
- Функція build_graph ітеративно обходить дерево і створює граф для побудови візуалізації через бібліотеку networkx.

2. Генерація градієнтного кольору
- Функція get_color обчислює HEX-код кольору для вузла залежно від його порядку відвідування. Для прикладу використовується градієнт від темного синього (RGB: 20,20,80) до світлого (RGB: 200,200,255).

3. Візуалізація обходу DFS (у глибину)
- Функція visualize_dfs використовує стек для ітеративного обходу дерева.
- Під час кожного відвідування вузла оновлюється його колір відповідно до порядку обходу, після чого викликається update_plot для перемальовування дерева.

4. Візуалізація обходу BFS (у ширину)
- Функція visualize_bfs використовує чергу (deque) для обходу дерева в ширину.
- Аналогічно DFS, після відвідування вузла оновлюється його колір і відбувається оновлення візуалізації.

5. Запуск програми
- У блоці if __name__ == «__main__»: створюється просте дерево. Спочатку демонструється візуалізація обходу в глибину (DFS), потім скидаються кольори і демонструється обхід у ширину (BFS).

Програма візуалізує процес обходу дерева крок за кроком, даючи змогу спостерігати, як змінюється колір кожного вузла залежно від його порядку відвідування.

Завдання 6. Жадібні алгоритми та динамічне програмування
Виконання коду дивіться у файлі: task_6.py
Пояснення:

1. Жадібний алгоритм (greedy_algorithm)
 - Для кожної страви обчислюється співвідношення калорій до вартості.
 - Страви сортуються за спаданням цього співвідношення.
 - Проходиться список страв, і якщо додавання страви не перевищує бюджет, вона включається до результату.
 - В кінці виводиться список обраних страв разом із загальною вартістю та калорійністю.

2. Динамічне програмування (dynamic_programming)
 - Задачу можна трактувати як задачу про рюкзак (0/1 knapsack), де «вага» – вартість, а «цінність» – калорійність страви.
 - Створюється DP-таблиця dp, де dp[i][j] містить максимальну калорійність, досяжну з перших i страв при бюджеті j.
 - Таблиця keep використовується для відновлення оптимального набору страв.
 - Після заповнення таблиці відновлюється набір обраних страв, який і виводиться.
 - Таким чином, даний код демонструє два підходи до розв’язання задачі з вибору їжі, дозволяючи порівняти результати жадібного алгоритму та алгоритму динамічного програмування.

Завдання 7. Використання методу Монте-Карло.
Виконання коду дивіться у файлі: task_7.py
Симуляція методом Монте-Карло виконана, результати показані у вигляді таблиці ймовірностей, яка порівнює отримані дані з аналітичними розрахунками. 
Також побудовано графік, який відображає ймовірності кожної суми для обох підходів. Ви можете переглянути таблицю для аналізу відповідностей між методами за результатами виконання коду у файлі.
