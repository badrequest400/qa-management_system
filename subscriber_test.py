import unittest
from manager import *
from subscriber import *


class SubscriberTest(unittest.TestCase):

    def setUp(self):
        self.manager = Manager()
        self.subscriber = Subscriber('John Smith', 'john.smith@gmail.com', '8 Crescent Rd', self.manager)

    def test_subscriber_registered(self):
        self.assertEqual(self.manager.getSubscribers(), [self.subscriber])



if __name__ == '__main__':
    unittest.main()
