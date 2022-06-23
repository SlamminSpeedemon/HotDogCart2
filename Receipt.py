import random
from tkinter import *

class Receipt:
    def __init__(self, itemsArray, total, discount):
        self.items = itemsArray
        self.total = total
        self.discount = discount
        self.labels = []
        self.root = Tk()
        self.root.geometry('360x640')
        self.root.configure(background='#FFEFDB')
        self.root.title('2831 - Receipt')


    def window(self):
        Label(self.root, text="You ordered: ", bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=25, y=25)

        for i in range(len(self.items)):
            self.labels.append(Label(self.root, text=(self.items[i].getItemCount(),self.items[i].getItemName() + "(s)"),bg='#FFEFDB', font=('arial', 18, 'normal')).place(x=25, y = 75 + i * 50))
            self.labels.append(
                Label(self.root, text=("$"+str(self.items[i].getPrice())+"0"), bg='#FFEFDB',
                      font=('arial', 18, 'normal')).place(x=250, y=75 + i * 50))



        Label(self.root, text=("Discount: "), bg='#FFEFDB',
                      font=('arial', 18, 'normal')).place(x=25, y=75 + len(self.items) * 50)
        Label(self.root, text=("$" + str(self.discount)), bg='#FFEFDB',
                  font=('arial', 18, 'normal')).place(x=250, y=75 + len(self.items) * 50)


        Label(self.root, text=("Total: $" + str(self.total) +"0"), bg='#FFEFDB', font=('arial', 18, 'bold')).place(x=170, y=75 + (len(self.items)+1) * 50)
        Label(self.root, text=("Your order will be ready\n\tin "+str(random.randint(1,15))+" min"), bg='#FFEFDB', font=('arial', 18, 'normal')).place(
            x=25, y=75 + (len(self.items) + 2) * 50)

        Button(self.root, text="Close", bg='#CD5B45', font=('arial', 18, 'normal'), command=lambda: self.exit()).place(x=125, y=50 + (len(self.items) + 4) * 50)

        self.root.mainloop()

    def exit(self):
        self.root.destroy()

