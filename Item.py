from tkinter import *
class Item:
    def __init__(self, itemCost, itemName):
        self.itemCost = itemCost
        self.itemCount = 0
        self.itemString = StringVar()
        self.itemName = itemName

    def addDog(self, additionalDogs):
        self.itemCount += additionalDogs

    def setDog(self, setDog):
        self.itemCount = setDog

    def guiStart(self, root, xPos, yPos):
        self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")
        Label(root, textvariable=self.itemString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=xPos, y=yPos)

    def guiUpdate(self):
        self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")

