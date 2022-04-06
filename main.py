import tkinter as tk
from tkinter import ttk
from tkinter import *
from Item import *

# declare initial variables
hotdogCost = 2.50
bratCost = 3.50
hamburgerCost = 5.00
friesCost = 2.00
sodaCost = 2.00

register = []  # 2 dimensional list that stores all previous orders


# define functions


# this is the function called when the update button is clicked
def update():  # update the guis for items
    hotdogObject.guiUpdate()
    bratObject.guiUpdate()
    hamburgerObject.guiUpdate()
    friesObject.guiUpdate()
    sodasObject.guiUpdate()
    watersObject.guiUpdate()


def totalsFormatter(number):
    return "Total: \t\t" + str(number) + "0"


def getFormatted():
    return "Total: \t\t" + str(getTotal()) + "0"


def getTotal():
    return hotdogObject.getPrice() + bratObject.getPrice() + hamburgerObject.getPrice() + friesObject.getPrice() + sodasObject.getPrice()


def dayTotal():
    return "Day Total: \t" + "0"


def discountGet():
    try:
        if (getTotal() - int(discountBox.get()) > 0):
            finalTotalString.set("Final Total: \t" + str(getTotal() - int(discountBox.get())))
        else:
            finalTotalString.set("Final Total: \t0.00")
    except:
        finalTotalString.set("Final Total: \t0.00")

def calculate():
    update()
    totalString.set(getFormatted())

def exit():
    root.destroy()

def clear():
    hotdogObject.clearEntry()
    bratObject.clearEntry()
    hamburgerObject.clearEntry()
    friesObject.clearEntry()
    sodasObject.clearEntry()
    watersObject.clearEntry()
    calculate()

def save():
    register.append([hotdogObject.getItemCount(), bratObject.getItemCount(), hamburgerObject.getItemCount(), friesObject.getItemCount(), sodasObject.getItemCount(), watersObject.getItemCount()])
    print(register)
#main program

root = Tk()

# This is the section of code which creates the main window
root.geometry('870x510')
root.configure(background='#FFEFDB')
root.title('Food Cart')

# GUI variables
itemXpos = 20
itemYpos = 40
itemYposChanger = 70

totalString = StringVar()


finalTotalString = StringVar()
#finalTotalString.set(getFormattedTotal())

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

totalString.set(totalsFormatter(hotdogObject.getPrice() + bratObject.getPrice() + hamburgerObject.getPrice() + friesObject.getPrice() + sodasObject.getPrice()))

# set up labels to display info
Label(root, textvariable=totalString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=33)
Label(root, textvariable=dayTotalString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=343)
Label(root, textvariable=finalTotalString, bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=183)

Label(root, text='Discount: ', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=143)

#Buttons
Button(root, text='Update', bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: update()).place(x=227, y=443)
Button(root, text='Apply Discount', bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: discountGet()).place(
    x=597, y=73)
Button(root, text='Calculate', bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: calculate()).place(x=657, y=223)
Button(root, text='Exit', bg='#CD5B45', font=('arial', 18, 'normal'), command=lambda: exit()).place(x=547, y=443)
Button(root, text='Clear', bg='#CD5B45', font=('arial', 18, 'normal'), command=lambda: clear()).place(x=547, y=383)

#save register buttons
Button(root, text='Save Order', bg = '#98F5FF', font=('arial', 18, 'normal'), command=lambda: save()).place(x=687, y=383)
Button(root, text='View Register', bg='#98F5FF', font=('arial', 18, 'normal'), command=register).place(x=663, y=443)

# This is the section of code which creates a text input box
discountBox = Entry(root)
discountBox.place(x=687, y=143)


root.mainloop()
