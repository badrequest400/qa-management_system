from Tkinter import *

class App:

    # INSTANTIATE MAIN UI WINDOW AND PLACE TITLE TEXT + IMAGE
    def __init__(self, root, manager):
        self.chosen = StringVar()
        self.subscriber = StringVar()
        self.manager = manager
        self.root = root
        self.currentFrame = Frame(root, width=200)
        logo = PhotoImage(file="./book.gif")
        # Label(root, image=logo).pack()#.grid(row=0, column=1)
        Label(root, text="Library Management System", justify=LEFT, padx=20).grid(row=0, column=0)

        Label(root, text="Available items", justify=LEFT).grid(row=1, column=0, sticky='W')
        Label(root, text="Borrowed items", justify=LEFT).grid(row=1, column=2, sticky='W')
        Label(root, text="Subscribers", justify=LEFT).grid(row=1, column=1, sticky='W')

        self.currentFrame = self.drawDynamic(self.manager, self.root, self.currentFrame)

        Button(root, text="Quit", command=root.quit).grid(row=10, column=0)
        Button(root, text="Borrow", command=self.borrow).grid(row=10, column=1)
        Button(root, text="Return", command=self.returnItems).grid(row=10, column=2)

    def borrow(self):
        if self.chosen.get() and self.subscriber.get():
            self.manager.borrowItem(self.chosen.get(), self.subscriber.get())
            self.currentFrame = self.drawDynamic(self.manager, self.root, self.currentFrame)
        else:
            return

    def returnItems(self):
        if self.subscriber.get():
            for i in self.manager.getBorrowed():
                if i.getBorrowedBy() == self.subscriber.get():
                    self.manager.returnItem(i.getId())
            self.drawDynamic(self.manager, self.root, self.currentFrame)
        else:
            return

    def drawDynamic(self, manager, root, frame):
        frame.destroy()
        frame = Frame(root)
        frame.grid(row=2, column=0)
        c = 2
        for i in manager.getItems():
            Radiobutton(frame, text=i.getName(), variable=self.chosen, value=i.getId(), width=50).grid(row=c, column=0)
            c += 1

        d = 2
        for i in manager.getBorrowed():
            Label(frame, text=i.getName(), relief=RIDGE, width=50).grid(row=d, column=4)
            d += 1

        e = 2
        for i in manager.getSubscribers():
            if manager.getBorrowed():
                for j in manager.getBorrowed():
                    if j.getBorrowedBy == i.getName():
                        Radiobutton(frame, bg="red", text=i.getName(), variable=self.subscriber, value=i.getName(), width=50).grid(row=e, column=1)
                    else:
                        Radiobutton(frame, text=i.getName(), variable=self.subscriber, value=i.getName(), width=50).grid(row=e, column=1)
            else:
                Radiobutton(frame, text=i.getName(), variable=self.subscriber, value=i.getName(), width=50).grid(row=e, column=1)
            e += 1

        return frame
