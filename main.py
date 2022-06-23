import tkinter as tk
from tkinter import ttk
from tkinter import *
from Item import*
from Receipt import*

# declare and set final variables

hotdogCost = 2.50
bratCost = 3.50
hamburgerCost = 5.00
friesCost = 2.00
sodaCost = 2.00
waterCost = 1.00

# define functions

# this is the function called when the update button is clicked
def update():  # update the guis for items
    for i in range(len(ObjectsArray)):
        ObjectsArray[i].guiUpdate()

def totalsFormatter(number):
    return "Total: \t\t" + str(number) + "0"

def getFormatted():
    return "Total: \t\t" + str(getTotal()) + "0"

def getTotal():
    sum = 0
    for i in range(len(ObjectsArray)):
        sum += ObjectsArray[i].getPrice()
    return sum

def getDiscount():
    try:
        if (getTotal() - float(discountBox.get()) > 0 and float(discountBox.get()) > 0):
            return float(discountBox.get())
        else:
            return 0
    except:
        return 0

def discountSet():
    try:
        if (getTotal() - float(discountBox.get()) > 0 and float(discountBox.get()) > 0):
            print("discount is not 0")
            finalTotalString.set("Final Total: \t" + str(getTotal() - float(discountBox.get())) + "0")
        else:
            print("discount is 0")
            finalTotalString.set("Final Total: \t" + str(getTotal()))
    except:
        finalTotalString.set("Final Total: \t" + str(getTotal()) + "0")

def calculate():
    update()
    totalString.set(getFormatted())
    discountSet()

def exit():
    root.destroy()

def clear():
    for i in range(len(ObjectsArray)):
        ObjectsArray[i].clearEntry()
    calculate()

def save():
    calculate()
    itemsArray = []
    for i in range(len(ObjectsArray)):
        itemsArray.append(ObjectsArray[i].getItemCount())

    receipt = Receipt(ObjectsArray, getTotal() - getDiscount(), getDiscount())

    receipt.window()

#main program

root = Tk()

# This is the section of code which creates the main window
root.geometry('870x610')
root.configure(background='#FFEFDB')
root.title('2831 - Food Truck')

# GUI variables
itemXpos = 120
itemYpos = 140
itemYposChanger = 70

totalString = StringVar()

finalTotalString = StringVar()

# set up objects to handle GUI
hotdogObject = Item(hotdogCost, "hotdogs", root)
hotdogObject.guiStart(itemXpos, itemYpos)

bratObject = Item(bratCost, "brats", root)
bratObject.guiStart(itemXpos, itemYpos + itemYposChanger)

hamburgerObject = Item(hamburgerCost, "hamburgers", root)
hamburgerObject.guiStart(itemXpos, itemYpos + 2 * itemYposChanger)

friesObject = Item(sodaCost, "fries", root)
friesObject.guiStart(itemXpos, itemYpos + 3 * itemYposChanger)

sodasObject = Item(sodaCost, "sodas", root)
sodasObject.guiStart(itemXpos, itemYpos + 4 * itemYposChanger)

watersObject = Item(waterCost, "waters", root)
watersObject.guiStart(itemXpos, itemYpos + 5 * itemYposChanger)

#making lists for objects and add buttons
ObjectsArray = [hotdogObject, bratObject, hamburgerObject, friesObject, sodasObject, watersObject]

totalString.set(totalsFormatter(hotdogObject.getPrice() + bratObject.getPrice() + hamburgerObject.getPrice() + friesObject.getPrice() + sodasObject.getPrice()))

# set up labels to display info
Label(root, text="WELCOME TO                   FOOD TRUCK!", bg='#FFEFDB', font=('arial', 30, 'bold')).place(x=50, y=15)
Button(root, text="HARSH'S", bg='#98F5FF', font=('calibri', 31, 'bold')).place(x=345, y=-5) #is a button for aesthetics sake
Label(root, text="Use buttons or enter numbers in the boxes. Press Calculate to see the price. \nWhen you are ready press order for your mobile pick up.", bg='#FFEFDB', font=('arial', 16, 'normal')).place(x=65, y=80)
Label(root, textvariable=totalString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=133)
Label(root, textvariable=finalTotalString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=243)
Label(root, text='Coupon: ', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=187)

#Buttons
Button(root, text="Enter Inputs", bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: update()).place(x=375, y=533)
Button(root, text='Calculate', bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: calculate()).place(x=708, y=483)
Button(root, text='Exit', bg='#CD5B45', font=('arial', 18, 'normal'), command=lambda: exit()).place(x=577, y=483)
Button(root, text='Clear', bg='#CD5B45', font=('arial', 18, 'normal'), command=lambda: clear()).place(x=577, y=423)
Button(root, text='Order', bg = '#98F5FF', font=('arial', 18, 'normal'), command=lambda: save()).place(x=747, y=423)

# This is the section of code which creates an additional feature: coupon entry option
discountBox = Entry(root)
discountBox.place(x=697, y=193)

#MAIN WINDOW STARTS
root.mainloop()