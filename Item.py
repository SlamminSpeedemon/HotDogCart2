from tkinter import *
class Item:
    def __init__(self, itemCost, itemName, rootWindow):
        self.itemCost = itemCost
        self.itemCount = 0
        self.itemName = itemName
        self.root = rootWindow
        self.itemString = StringVar()
        self.itemEntry = Entry(rootWindow)

    def itemAdd(self):
        self.itemCount += 1


    def addItem(self, addItems):
        self.itemCount += addItems

    def setItemCount(self, setItemCount):
        self.itemCount = setItemCount

    def guiStart(self, xPos, yPos):
        self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")
        Label(self.root, textvariable=self.itemString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=xPos, y=yPos)

        self.itemEntry.place(x=xPos + 230, y=yPos + 5)

        Button(self.root, text=("+ " + self.itemName), bg='#8B8378', font=('arial', 18, 'normal'), command=self.itemAdd()).place(x=xPos + 370, y=yPos-10)

    def guiUpdate(self):
        self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")

