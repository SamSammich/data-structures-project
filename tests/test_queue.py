"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src import queue


class TestQueue(unittest.TestCase):
    """Testing func. engueue"""
    def test_enqueue(self):
        test_queue = queue.Queue()
        test_queue.enqueue('data1')
        test_queue.enqueue('data2')
        self.assertEqual(test_queue.head.data, 'data1')
        self.assertEqual(test_queue.head.next_node.data, 'data2')
        """Testing func. queue"""
    def test_empty_queue(self):
        test_queue = queue.Queue()
        test_queue.enqueue('data1')
        test_queue.enqueue('data2')
        self.assertEqual(test_queue.dequeue(), 'data1')
        test_queue.dequeue()
        self.assertIsNone(test_queue.dequeue())

