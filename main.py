import tkinter as tk
from tkinter import ttk
from tkinter import *

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = dogInput.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = bratInput.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = hamburgerInput.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = friesInput.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = sodaInput.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = waterInput.get()
	return userInput


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def dogAdd():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def discount():
	print('clicked')


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = discount.get()
	return userInput


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def register():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')



root = Tk()

# This is the section of code which creates the main window
root.geometry('840x510')
root.configure(background='#FFEFDB')
root.title('Food Cart')


# This is the section of code which creates the a label
Label(root, text='dogs', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=57, y=43)


# This is the section of code which creates the a label
Label(root, text='brats', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=57, y=113)


# This is the section of code which creates the a label
Label(root, text='hamburg', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=57, y=183)


# This is the section of code which creates the a label
Label(root, text='fries', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=57, y=253)


# This is the section of code which creates the a label
Label(root, text='soda', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=57, y=323)


# This is the section of code which creates the a label
Label(root, text='water', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=57, y=403)


# This is the section of code which creates a text input box
dogInput=Entry(root)
dogInput.place(x=217, y=43)


# This is the section of code which creates a text input box
bratInput=Entry(root)
bratInput.place(x=217, y=113)


# This is the section of code which creates a text input box
hamburgerInput=Entry(root)
hamburgerInput.place(x=217, y=183)


# This is the section of code which creates a text input box
friesInput=Entry(root)
friesInput.place(x=217, y=253)


# This is the section of code which creates a text input box
sodaInput=Entry(root)
sodaInput.place(x=217, y=323)


# This is the section of code which creates a text input box
waterInput=Entry(root)
waterInput.place(x=217, y=403)


# This is the section of code which creates a button
Button(root, text='Update', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=227, y=443)


# This is the section of code which creates a button
Button(root, text='+ hotdog', bg='#8B8378', font=('arial', 18, 'normal'), command=dogAdd).place(x=377, y=23)


# This is the section of code which creates a button
Button(root, text='+ brat', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=377, y=93)


# This is the section of code which creates a button
Button(root, text='+ hamburger', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=377, y=163)


# This is the section of code which creates a button
Button(root, text='+ fries', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=377, y=233)


# This is the section of code which creates a button
Button(root, text='+ soda', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=377, y=303)


# This is the section of code which creates a button
Button(root, text='+ water', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=377, y=373)


# This is the section of code which creates the a label
Label(root, text='Total: ', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=33)


# This is the section of code which creates a button
Button(root, text='Apply Discount', bg='#8B8378', font=('arial', 18, 'normal'), command=discount).place(x=597, y=73)


# This is the section of code which creates the a label
Label(root, text='Final Total: ', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=183)


# This is the section of code which creates the a label
Label(root, text='Discount: ', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=577, y=143)


# This is the section of code which creates a text input box
discount=Entry(root)
discount.place(x=687, y=143)


# This is the section of code which creates a button
Button(root, text='Calculate', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=657, y=223)


# This is the section of code which creates a button
Button(root, text='Receipt', bg='#8B8378', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=707, y=283)


# This is the section of code which creates a button
Button(root, text='View Register', bg='#98F5FF', font=('arial', 18, 'normal'), command=register).place(x=637, y=443)


# This is the section of code which creates a button
Button(root, text='Exit', bg='#CD5B45', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=547, y=443)


# This is the section of code which creates a button
Button(root, text='Clear', bg='#98F5FF', font=('arial', 18, 'normal'), command=btnClickFunction).place(x=727, y=383)


# This is the section of code which creates the a label
Label(root, text='Day Total: ', bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=557, y=353)


root.mainloop()
