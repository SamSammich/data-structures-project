import pytest

from src.stack import Node, Stack


@pytest.fixture()
def expl1():
    return Node(5, None)

stack = Stack()

def test_node_init(expl1):
    assert expl1.data == 5
    assert expl1.next_node == None


def test_stack_init():
    assert stack.top == None

def test_stack_push():

    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    assert stack.top.data == 'data3'
    assert stack.top.next_node.data == 'data2'
    assert stack.top.next_node.next_node.data == 'data1'
    assert stack.top.next_node.next_node.next_node == None
def test_stack_pop():

    assert stack.pop() ==None