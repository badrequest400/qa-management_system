"""
Class describing subscribers to the library system
Subscribers are the observers in the Observer patter
Subscribers can borrow/return books and get notified when borrowed items are overdue
"""

class Subscriber():

    def __init__(self, name, email, address, manager):
        """
        Constructs a new Subscriber object
        As part of the construction, it registers itself as a subscriber on the manager

        :param name String: The name of the subscriber
        :param email String: The email address of the subscriber
        :param address String: The address of the subscriber
        :param manager Manager: A reference to the main library management system of type Manager
        """
        self.name = name
        self.email = email
        self.address = address
        self.manager = manager
        self.borrowed = []
        self.overdue_warnings = 0
        self.manager.addSubscriber(self)

    def message(self):
        """
        Gets notified by the main management system for overdue books to be returned
        """
        self.overdue_warnings += 1
        return 'Got message'

    def getName(self):
        return self.name
