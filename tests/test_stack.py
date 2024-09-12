import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()  # Create a new Stack instance for each test

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty_stack(self):
        self.assertIsNone(self.stack.pop())

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.size(), 2)  # Peek shouldn't affect the size

    def test_peek_empty_stack(self):
        self.assertIsNone(self.stack.peek())

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)


if __name__ == '__main__':
    unittest.main()

