import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# ==================== КЛАСС И ФУНКЦІЇ ДЛЯ ПІДГОТОВКИ ДЕРЕВА ====================

# Клас вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для збереження кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Функція для побудови графа (networkx) із бінарного дерева (ітеративно)
def build_graph(tree_root):
    """
    Проходить дерево і додає вузли та ребра у граф.
    """
    graph = nx.DiGraph()
    stack = [tree_root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        # Додаємо вузол з його значенням і поточним кольором
        graph.add_node(node.id, label=node.val, color=node.color)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            stack.append(node.left)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            stack.append(node.right)
    return graph

# Рекурсивна функція з попередніх завдань використовується для побудови координат
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Якщо вузол ще не доданий, додаємо його позицію
        if node.id not in pos:
            pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def get_positions(tree_root):
    """
    Побудова словника позицій для вузлів дерева.
    """
    pos = {tree_root.id: (0, 0)}
    dummy_graph = nx.DiGraph()
    add_edges(dummy_graph, tree_root, pos)
    return pos

# Функція для оновлення графічного вікна із поточним станом дерева
def update_plot(tree_root, pos, title=""):
    """
    Оновлює малюнок дерева, використовуючи поточні значення кольорів вузлів.
    """
    plt.clf()  # Очистка фігури
    graph = build_graph(tree_root)
    colors = [data['color'] for _, data in graph.nodes(data=True)]
    labels = {node: data['label'] for node, data in graph.nodes(data=True)}
    plt.title(title)
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.pause(0.5)  # Пауза для візуалізації кроку

# Функція для підрахунку кількості вузлів у дереві (ітеративно)
def count_nodes(tree_root):
    count = 0
    stack = [tree_root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        count += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return count

# Функція для обчислення кольору за порядковим номером (градієнт від темного до світлого)
def get_color(order, total):
    """
    Генерує HEX-код кольору для вузла.
    Використовуємо градієнт від темного синього до світлого синього.
    Наприклад, початковий (темний): (20, 20, 80)
               кінцевий (світлий): (200, 200, 255)
    """
    if total <= 1:
        f = 1.0
    else:
        f = order / (total - 1)
    r = int(20 + f * (200 - 20))
    g = int(20 + f * (200 - 20))
    b = int(80 + f * (255 - 80))
    return f"#{r:02X}{g:02X}{b:02X}"

# ==================== ФУНКЦІЇ ДЛЯ ОБХОДУ ДЕРЕВА ====================
# Обхід дерева в глибину (DFS) без рекурсії із використанням стеку

def visualize_dfs(tree_root):
    """
    Візуалізація обходу дерева в глибину (DFS) без рекурсії.
    Кожен крок оновлює колір відвіданого вузла.
    """
    total_nodes = count_nodes(tree_root)
    pos = get_positions(tree_root)
    order = 0
    stack = [tree_root]
    visited = set()

    plt.ion()  # Включення інтерактивного режиму
    update_plot(tree_root, pos, title="DFS: Початок обходу")
    
    while stack:
        node = stack.pop()
        if node.id in visited:
            continue
        visited.add(node.id)
        # Оновлення кольору вузла згідно порядку обходу
        node.color = get_color(order, total_nodes)
        order += 1
        update_plot(tree_root, pos, title=f"DFS: Відвідано вузол {node.val}")
        # Додаємо правого, потім лівого для відвідування лівого перш за правилами DFS
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    update_plot(tree_root, pos, title="DFS: Обхід завершено")
    plt.ioff()  # Вимикаємо інтерактивний режим
    plt.show()

# Обхід дерева в ширину (BFS) без рекурсії із використанням черги

def visualize_bfs(tree_root):
    """
    Візуалізація обходу дерева в ширину (BFS) без рекурсії.
    Кожен крок оновлює колір відвіданого вузла.
    """
    total_nodes = count_nodes(tree_root)
    pos = get_positions(tree_root)
    order = 0
    queue = deque([tree_root])
    visited = set()

    plt.ion()  # Включення інтерактивного режиму
    update_plot(tree_root, pos, title="BFS: Початок обходу")
    
    while queue:
        node = queue.popleft()
        if node.id in visited:
            continue
        visited.add(node.id)
        node.color = get_color(order, total_nodes)
        order += 1
        update_plot(tree_root, pos, title=f"BFS: Відвідано вузол {node.val}")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    update_plot(tree_root, pos, title="BFS: Обхід завершено")
    plt.ioff()  # Вимикаємо інтерактивний режим
    plt.show()

# ==================== ПРИКЛАД ВИКОРИСТАННЯ ====================
if __name__ == "__main__":
    # Побудова простого бінарного дерева
    # Створимо дерево:
    #         0
    #       /   \
    #      4     1
    #     / \   /
    #    5  10 3
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Спочатку демонструємо обхід в глибину (DFS)
    print("Запуск візуалізації DFS...")
    visualize_dfs(root)

    # Для демонстрації BFS відновимо початкові кольори (або можна побудувати нове дерево)
    # Задаємо стандартний колір всім вузлам
    stack = [root]
    while stack:
        node = stack.pop()
        node.color = "skyblue"
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Потім демонструємо обхід в ширину (BFS)
    print("Запуск візуалізації BFS...")
    visualize_bfs(root)
