import unittest
from item import *
from datetime import datetime


class ItemTest(unittest.TestCase):

    def setUp(self):
        self.item = Item('Hundred Years of Solitude', 'Gabriel Marquez', 'BF123')

    def test_get_name(self):
        self.assertEqual(self.item.getName(), 'Hundred Years of Solitude')

    def test_get_author(self):
        self.assertEqual(self.item.getAuthor(), 'Gabriel Marquez')

    def test_get_id(self):
        self.assertEqual(self.item.getId(), 'BF123')

    def test_set_get_borrowed_date(self):
        self.item.setBorrowedDate(datetime(2015, 8, 8, 0, 0, 0, 0))
        self.assertEqual(self.item.getBorrowedDate(), datetime(2015, 8, 8, 0, 0, 0, 0))

    def test_set_get_borrowed_by(self):
        self.item.setBorrowedBy('John Smith')
        self.assertEqual(self.item.getBorrowedBy(), 'John Smith')

class BookTest(unittest.TestCase):

    def setUp(self):
        self.book = Book('Hundred Years of Solitude', 'Gabriel Marquez', 'BF123')

    def test_get_info(self):
        self.assertEqual(self.book.getInfo(), {'id': 'BF123', 'name': 'Hundred Years of Solitude', 'author': 'Gabriel Marquez'})

class DVDTest(unittest.TestCase):

    def setUp(self):
        self.dvd = DVD('Nightmare before Christmas', 'Tim Burton', 'BF126')

    def test_get_info(self):
        self.assertEqual(self.dvd.getInfo(), {'id': 'BF126', 'name': 'Nightmare before Christmas', 'director': 'Tim Burton'})


if __name__ == '__main__':
    unittest.main()
