class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if not self.head:
            self.head = self.tail = Node(data, next_node=None)

        else:
            node = Node(data, next_node=None)
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        node = self.head
        if node:
            self.head = node.next_node
            return node.data
        else:
            return self.head

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:  # Если очередь пуста, возвращаем пустую строку
            return ''
        node = self.head
        result = []
        while node:  # В цикле перебираем очередь
            result.append(f'{node.data}')
            node = node.next_node
        return '\n'.join(result)  # Соединяем данные из списка
