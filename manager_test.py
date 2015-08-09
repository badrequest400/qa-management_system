import unittest
from manager import *
from item import *
from subscriber import *

class ManagerTest(unittest.TestCase):

    def setUp(self):
        self.a = Item('Hundred Years of Solitude', 'Gabriel Marquez', 'BF123')
        self.b = Item('The Neuromancer', 'William Gibson', 'BF124')
        self.c = Item('Going Postal', 'Terry Pratchett', 'BF125')
        self.manager = Manager([self.a, self.b], [])
        self.d = Subscriber('John Smith', 'john.smith@gmail.com', '8 Crescent Rd', self.manager)
        self.manager.__borrowed = []

    def test_add_get_subscribers(self):
        self.assertEqual(self.manager.addSubscriber('John Smith'), 'Can only add type Subscriber')
        self.assertEqual(self.manager.getSubscribers(), [self.d])
        self.assertNotEqual(self.manager.getSubscribers(), ['a', 'b'])

    def test_add_get_item(self):
        self.assertEqual(self.manager.addItem('a String'), 'Can only add type Item')
        self.manager.addItem(self.c)
        self.assertEqual(self.manager.getItems(), [self.a, self.b, self.c])

    def test_borrow_item(self):
        self.manager.addItem(self.c)
        self.assertEqual(self.manager.getItems(), [self.a, self.b, self.c])
        self.assertEqual(self.manager.borrowItem('BF125', 'John Smith'), 'Item borrowed')
        self.assertEqual(self.manager.getItems(), [self.a, self.b])
        self.assertEqual(self.manager.getBorrowed(), [self.c])
        self.assertEqual(self.manager.borrowItem('HF987', 'Jane Smith'), 'Item ID was not found in database')

    def test_item_return(self):
        self.manager.addItem(self.c)
        self.manager.borrowItem('BF125', 'John Smith')
        self.assertEqual(self.manager.getItems(), [self.a, self.b])
        self.assertEqual(self.manager.getBorrowed(), [self.c])
        self.assertEqual(self.manager.returnItem('BF125'), 'Item returned')
        self.assertEqual(self.manager.getItems(), [self.a, self.b, self.c])
        self.assertEqual(self.manager.getBorrowed(), [])
        self.assertEqual(self.manager.returnItem('HF987'), 'Item ID was not found in database')

    def test_message_overdue(self):
        self.assertEqual(self.manager.messageOverDue(self.d), 'Message sent and confirmed')

    def test_check_duedates(self):
        self.manager.addItem(self.c)
        self.manager.borrowItem('BF125', 'John Smith')
        # SET BORROWED DATE BACK FROM CURRENT TIME SO IT WILL BE DUE FOR TEST CASE
        for i in self.manager.getBorrowed():
            if i.getId() == 'BF125':
                i.setBorrowedDate(datetime(2015, 6, 12, 0, 0, 0, 0))
        self.assertEqual(self.manager.checkDueDates()[0].getId(), 'BF125')



if __name__ == '__main__':
    unittest.main()
