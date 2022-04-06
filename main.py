import tkinter as tk
from tkinter import ttk
from tkinter import *
from Item import *


# this is the function called when the update button is clicked
def update(): #update the guis for items
	hotdogObject.guiUpdate()
	bratObject.guiUpdate()
	hamburgerObject.guiUpdate()
	friesObject.guiUpdate()
	sodasObject.guiUpdate()
	watersObject.guiUpdate()

def totalsFormatter(number):
	return "Total: \t\t" + str(number) + "0"

def finalTotal():
	return "Final Total: \t" + "0"

def dayTotal():
	return "Day Total: \t" + "0"

def discount():


root = Tk()

# This is the section of code which creates the main window
root.geometry('850x510')
root.configure(background='#FFEFDB')
root.title('Food Cart')

# declare initial variables
value = 0  # value of all products in current order
total = 0  # value of all products in all orders

hotdogCost = 2.50
bratCost = 3.50
hamburgerCost = 5.00
friesCost = 2.00
sodaCost = 2.00

register = []  # 2 dimensional list that stores all previous orders


# GUI variables
itemXpos = 20
itemYpos = 40
itemYposChanger = 70

totalString = StringVar()
totalString.set(totalsFormatter(0))

finalTotalString = StringVar()
finalTotalString.set(finalTotal())

dayTotalString = StringVar()
dayTotalString.set(dayTotal())


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

watersObject = Item(0, "waters", root)
watersObject.guiStart(itemXpos, itemYpos + 5 * itemYposChanger)

#set up labels to display info
Label(root, textvariable = totalString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=33)
Label(root, textvariable = dayTotalString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=353)
Label(root, textvariable = finalTotalString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=183)

Label(root, text='Discount: ', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=143)


# This is the section of code which creates a button
Button(root, text='Update', bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: update()).place(x=227, y=443)
Button(root, text='Apply Discount', bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: discount).place(x=597, y=73)



# This is the section of code which creates a text input box
discount = Entry(root)
discount.place(x=687, y=143)

# This is the section of code which creates a button
#Button(root, text='Calculate', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=657, y=223)

# This is the section of code which creates a button
#Button(root, text='Receipt', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=707, y=283)

# This is the section of code which creates a button
#Button(root, text='View Register', bg='#98F5FF', font=('arial', 18, 'normal'), command=register).place(x=637, y=443)

# This is the section of code which creates a button
#Button(root, text='Exit', bg='#CD5B45', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=547, y=443)

# This is the section of code which creates a button
#Button(root, text='Clear', bg='#98F5FF', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=727, y=383)

# This is the section of code which creates the a label


root.mainloop()
