from manager import *
from subscriber import *
from item import *
from Tkinter import *
from ui import *

def start():
    # INSTANTIATE ALL CLASSES FOR THE LIBRARY MANAGEMENT SYSTEM
    manager = Manager()
    items = [Book('Breakfast of Champions', 'Kurt Vonnegut', 'BSF123'), Book('Going Postal', 'Terry Pratchett', 'BSF124'), DVD('Nightmare Before Christmas', 'Tim Burton', 'DSF123')]
    for i in items:
        manager.addItem(i)

    # Subscribers automatically register themselves on the manager on instantiation
    s1 = Subscriber('John Smith', 'john.smith@gmail.com', '8 Crescent Rd', manager)
    s2 = Subscriber('Jane Doe', 'jane.doe@gmail.com', '23 Abbey Rd', manager)


    # INSTANTIATE UI ELEMENTS
    root = Tk()
    app = App(root, manager)


    # MAIN EVENT LOOP   START PROGRAM AND DISPLAY GUI
    root.mainloop()

start()

