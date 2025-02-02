class Node:
    """Клас вузла однозв’язного списку"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Клас однозв’язного списку"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додає елемент у кінець списку"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Виводить список"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_list(linked_list):
    """Реверсує однозв’язний список"""
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def merge_sorted_lists(l1, l2):
    """Об’єднує два відсортовані списки в один"""
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next

def merge_sort(head):
    """Сортує однозв’язний список методом злиття"""
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    return merge_sorted_lists(left, right)

def get_middle(head):
    """Знаходить середину списку"""
    if not head:
        return head

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    # Створення та сортування списку
    ll = LinkedList()
    for value in [4, 2, 1, 3]:
        ll.append(value)

    print("Несортований список:")
    ll.print_list()

    ll.head = merge_sort(ll.head)
    print("Відсортований список:")
    ll.print_list()

    # Реверсування списку
    reverse_list(ll)
    print("Реверсований список:")
    ll.print_list()

    # Створення другого відсортованого списку
    ll2 = LinkedList()
    for value in [5, 6, 7]:
        ll2.append(value)

    print("Другий відсортований список:")
    ll2.print_list()

    # Об'єднання двох списків
    merged_list = LinkedList()
    merged_list.head = merge_sorted_lists(ll.head, ll2.head)
    print("Об'єднаний відсортований список:")
    merged_list.print_list()
