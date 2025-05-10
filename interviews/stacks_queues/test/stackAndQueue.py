from .. import stackWithGetMin, doubleStackQueue
import unittest


class TestStackWithGetMin(unittest.TestCase):
    def setUp(self):
        self.stack = stackWithGetMin.Stack1()
        test_data = [34, 66, 39, 35, 53, 55, 17, 42, 43, 90]
        for i in test_data:
            self.stack.push(i)

    def test_stackWithGetmin(self):
        self.assertEqual(self.stack.getMin(), 17)
        self.assertEqual(self.stack.pop(), 90)
        self.assertEqual(self.stack.pop(), 43)
        self.assertEqual(self.stack.pop(), 42)
        self.assertEqual(self.stack.pop(), 17)
        self.assertEqual(self.stack.getMin(), 34)


class TestDoubleStackQueue(unittest.TestCase):
    def setUp(self):
        self.queue = doubleStackQueue.DoubleStackQueue()

    def test_pop(self):
        self.queue.push(1)
        self.queue.push(3)
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 3)
        self.assertEqual(self.queue.pop(), 2)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStackWithGetMin('test_stackWithGetmin'))
    suite.addTest(TestDoubleStackQueue('test_doubleStackQueue'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
