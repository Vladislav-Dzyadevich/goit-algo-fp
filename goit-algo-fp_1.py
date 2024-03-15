class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted(self, other_list):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other_list.head

        while current_self is not None and current_other is not None:
            if current_self.data < current_other.data:
                merged_list.append(current_self.data)
                current_self = current_self.next
            else:
                merged_list.append(current_other.data)
                current_other = current_other.next

        while current_self is not None:
            merged_list.append(current_self.data)
            current_self = current_self.next

        while current_other is not None:
            merged_list.append(current_other.data)
            current_other = current_other.next

        return merged_list

    def sort(self):
        if not self.head or not self.head.next:
            return

        current = self.head
        while current.next:
            if current.data > current.next.data:
                self._swap(current)
                current = self.head
            else:
                current = current.next

    def _swap(self, node):
        temp = node.data
        node.data = node.next.data
        node.next.data = temp


# Приклад використання
if __name__ == "__main__":
    # Створення списків
    list1 = LinkedList()
    list1.append(3)
    list1.append(7)
    list1.append(10)

    list2 = LinkedList()
    list2.append(1)
    list2.append(5)
    list2.append(8)

    # Виведення вихідних списків
    print("Список 1:")
    list1.display()
    print("Список 2:")
    list2.display()

    # Реверсування списку
    list1.reverse()
    print("Реверсований список 1:")
    list1.display()

    # Сортування списку
    list2.sort()
    print("Відсортований список 2:")
    list2.display()

    # Об'єднання та сортування об'єднаного списку
    merged_list = list1.merge_sorted(list2)
    print("Об'єднаний та відсортований список:")
    merged_list.display()
