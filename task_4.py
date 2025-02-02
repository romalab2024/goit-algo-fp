import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для збереження кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Рекурсивна функція для додавання вузлів та ребер у граф
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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

# Функція для відображення дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використання значення вузла для підписів

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для побудови бінарного дерева з масиву, що представляє бінарну купу
def build_heap_tree(heap, index=0):
    """
    Побудова бінарного дерева з масиву-купу.
    :param heap: список, що представляє бінарну купу.
    :param index: поточний індекс у масиві, за замовчуванням 0 (корінь купи).
    :return: кореневий вузол бінарного дерева.
    """
    if index >= len(heap):
        return None

    # Створення вузла з поточним значенням
    node = Node(heap[index])

    # Обчислення індексів лівого та правого нащадків та рекурсивне побудова піддерев
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = build_heap_tree(heap, left_index)
    node.right = build_heap_tree(heap, right_index)

    return node

# Приклад використання:
# Масив, що представляє бінарну купу
heap = [10, 15, 20, 17, 25, 30, 35]

# Побудова бінарного дерева з масиву-купу
heap_tree_root = build_heap_tree(heap)

# Відображення дерева
draw_tree(heap_tree_root)
