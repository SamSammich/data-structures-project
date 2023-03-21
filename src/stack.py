class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""
    stack_list = []
    def __init__(self):

        """Конструктор класса Stack"""
        self.top = None



    def push(self, data):
        node = Node(data, self.top)
        self.top = node
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        while len(self.stack_list) > 0:
            tample = self.stack_list[-1]
            self.stack_list.pop()
            return tample
