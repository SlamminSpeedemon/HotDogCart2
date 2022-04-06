from tkinter import *
class Item:
    def __init__(self, itemCost, itemName, rootWindow):
        self.itemCost = itemCost
        self.itemCount = int(0)
        self.itemName = itemName
        self.root = rootWindow
        self.itemString = StringVar()
        self.itemEntry = Entry(rootWindow)

    def addItem(self, addItems):
        self.itemCount += addItems

    def setItemCount(self, setItemCount):
        self.itemCount = setItemCount

    def clearEntry(self):
        self.itemCount = 0
        self.itemEntry.delete(0, 5)

    def getItemCount(self):

        return self.itemCount

    def getPrice(self):
        return float(self.itemCount) * self.itemCost

    def guiStart(self, xPos, yPos):
        if (self.itemCost != 0):
            self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")
        else:
            self.itemString.set(str(self.itemCount) + " " + self.itemName + " (free)")
        Label(self.root, textvariable=self.itemString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=xPos + 20, y=yPos)

        self.itemEntry.place(x=xPos + 270, y=yPos + 5)

        #Button(self.root, text=("add 1"), bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: self.addItem(1)).place(x=xPos + 420, y=yPos-10)

    def guiUpdate(self):
        try:
            dummyVar = int(self.itemEntry.get()) + 1 #will throw error if not int
            self.setItemCount(self.itemEntry.get())
        except:
            self.setItemCount(0)

        if (int(self.itemCount) < 0):
            self.itemCount = 0
        self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")

