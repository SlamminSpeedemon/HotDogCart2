from tkinter import *
import time

class Item:
    def __init__(self, itemCost, itemName, rootWindow):
        self.itemCost = itemCost
        self.itemCount = int(0)
        self.itemName = itemName
        self.root = rootWindow
        self.itemString = StringVar()
        self.itemEntry = Entry(rootWindow)


    def addItem(self, addItems):
        self.itemCount += int(addItems)

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
        if (self.itemCost != 0.0):
            self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")
        else:
            self.itemString.set(str(self.itemCount) + " " + self.itemName + " (free)")
        Label(self.root, textvariable=self.itemString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=xPos + 20, y=yPos)

        Button(self.root, text="Add 1", bg='#00FF00', font=('arial', 18, 'normal'), command = lambda: self.addAnItem()).place(x=xPos-80, y = yPos-10)

        self.itemEntry.place(x=xPos + 290, y=yPos + 5)

    def guiUpdate(self):
        try:
            dummyVar = int(self.itemEntry.get()) + 1 #will throw error if not int
            self.setItemCount(self.itemEntry.get())
        except:
            self.itemEntry.delete(0,55)
            self.itemEntry.insert(0,str(self.itemCount))

        if (int(self.itemCount) < 0):
            self.itemEntry.delete(0,1) #only delete negative sign and redo calculation

            self.guiUpdate()


        if (int(self.itemCount) > 1000):
            self.itemEntry.delete(0,55)
            self.itemEntry.insert(0,"MAX IS 1000!")
            self.itemCount = 1000

        if (self.itemCost != 0.0):
            self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")
        else:
            self.itemString.set(str(self.itemCount) + " " + self.itemName + " (free)")

    def getItemName(self):
        return self.itemName

    def addAnItem(self):
        self.itemEntry.delete(0,55)
        self.itemCount = int(self.itemCount) #required due string casting caused by concatentation during "enter" button press
        if (int(self.itemCount) < 0):
            self.itemCount = 0


        self.itemCount += 1

        self.itemEntry.insert(0,str(self.itemCount))

        if (self.itemCost != 0.0):
            self.itemString.set(str(self.itemCount) + " " + self.itemName + " (" + str(self.itemCost) + "0)")
        else:
            self.itemString.set(str(self.itemCount) + " " + self.itemName + " (free)")
