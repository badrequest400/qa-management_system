from datetime import datetime

"""
Classes for items on stock in the library system
"""

class Item:
    """
    Abstract super class of Item, should be instantiated as either Book or DVD
    """
    def __init__(self, name, author, id):
        """
        Constructs an Item type
        :param name String:  The name/title of the item
        :param author String:  The author/director of the item
        :param id String:  The unique ID of the item on the system
        """
        self.name = name
        self.author = author
        self.id = id
        self.borrowedDate = None
        self.borrowedBy = None

    def getName(self):
        """
        Returns the name of the item
        :return String:
        """
        return self.name

    def getAuthor(self):
        """
        Returns the author/director of the item
        :return String:
        """
        return self.author

    def getId(self):
        """
        Returns the unique ID for this item
        :return String:
        """
        return self.id

    def getInfo(self):
        """
        Abstract method for summary information, overridden in subclasses
        :raises: NotImplementedError
        """
        raise NotImplementedError

    def setBorrowedDate(self, date):
        """
        Sets the date of when the item was borrowed, due date can eb calculated from this
        :param date datetime: The date-time when the item was borrowed
        """
        if isinstance(date, datetime):
            self.borrowedDate = date
        else:
            return 'Can only set type of datetime'

    def getBorrowedDate(self):
        """
        Returns the date-time when the item was borrowed
        :return String:
        """
        return self.borrowedDate

    def setBorrowedBy(self, name):
        """
        Sets the name of who the item was borrowed by
        :param name String: The name of the borrower
        """
        self.borrowedBy = name

    def getBorrowedBy(self):
        """
        Returns the name of the subscriber who borrowed the item
        :return String: The name of the borrower
        """
        return self.borrowedBy

class Book(Item):
    """
    Book item on the library system extends Item
    """
    def getInfo(self):
        """
        Returns summary information about the Book
        :return Dict: {id: String, name: String, author: String}
        """
        return {'id': self.id, 'name': self.name, 'author': self.author}

class DVD(Item):
    """
    DVD item on the library system extends Item
    """
    def getInfo(self):
        """
        Returns summary information about the DVD
        :return Dict: {id: String, name: String, director: String}
        """
        return {'id': self.id, 'name': self.name, 'director': self.author}
