from item import *
from subscriber import *
from datetime import datetime

"""
Main library management system
"""
class Manager:
    """
    Class for main manager system
    """
    def __init__(self, items=[], subscribers=[]):
        """
        Constructs a manager object, there should be only one in the program
        :param items Array:  Array of references of type Item
        :param subscribers Array:  Array of references of type Subscriber
        """
        self.__items = items
        self.__subscribers = subscribers
        self.__borrowed = []

    def addSubscriber(self, subscriber):
        """
        Adds a new subscriber to the system
        Needs to be of type Subscriber, otherwise returns error message
        :param subscriber Subscriber: reference to new subscriber object to be added
        """
        if isinstance(subscriber, Subscriber):
            self.__subscribers.append(subscriber)
        else:
            return 'Can only add type Subscriber'

    def getSubscribers(self):
        """
        Returns all references to subscribers registered with the manager
        :return Array<Subscriber>:
        """
        return self.__subscribers

    def getSubscriber(self, name):
        """
        Returns a reference to a subscriber registered with the manager
        :param name String: Name of the subscriber
        :return Array<Subscriber>:
        """
        for i in self.__subscribers:
            if i.getName() == name:
                return i

    def addItem(self, item):
        """
        Adds a new item to the system
        Needs to be of type Item, otherwise returns error message
        :param item Item: reference to new item object to be added
        """
        if isinstance(item, Item):
            self.__items.append(item)
        else:
            return 'Can only add type Item'

    def getItems(self):
        """
        Returns all references to items registered with the manager
        :return Array<Item>:
        """
        return self.__items

    def getBorrowed(self):
        """
        Returns all references to items that have been borrowed
        :return Array<Item>:
        """
        return self.__borrowed

    def borrowItem(self, id, name):
        """
        Called by subscribers, borrows an item on the system
        The item is moved from the 'items' array to the 'borrowed' array
        """
        done = False
        for i in range(len(self.__items)):
            if self.__items[i].getId() == id:
                borrowed = self.__items.pop(i)
                borrowed.setBorrowedDate(datetime.now())
                borrowed.setBorrowedBy(name)
                self.__borrowed.append(borrowed)
                done = True
        if done == False:
            return 'Item ID was not found in database'
        else:
            return 'Item borrowed'

    def returnItem(self, id):
        """
        Called by subscribers, returns an item on the system
        The item is moved from the 'borrowed' array to the 'items' array
        """
        returned = False
        for i in range(len(self.__borrowed)):
            if self.__borrowed[i].getId() == id:
                item = self.__borrowed.pop(i)
                item.setBorrowedDate = None
                item.setBorrowedBy = None
                self.__items.append(item)
                returned = True
        if returned == False:
            return 'Item ID was not found in database'
        else:
            return 'Item returned'

    def messageOverDue(self, subscriber):
        """
        Notifies a subscriber that a book is overdue on the system
        """
        res = subscriber.message()
        if res == 'Got message':
            return 'Message sent and confirmed'
        else:
            return 'Message sent, but not confirmed'

    def checkDueDates(self):
        """
        Returns a list of item references that are due for return
        :return Array<Item>: items due for return
        """
        due = []
        for i in self.__borrowed:
            if (datetime.now() - i.getBorrowedDate()).days > 7:
                due.append(i)
            else:
                continue
        return due

    def broadcast(self):
        """
        Uses class methods to message all Subscribers who have outstanding items due for return
        :return None:
        """
        for i in self.checkDueDates():
            self.messageOverDue(self.getSubscriber(i.getBorrowedBy()))
