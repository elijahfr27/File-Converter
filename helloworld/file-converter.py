from tkinter import *
import sys
# from cloud_tools import CloudInstance

#Base Window
root = Tk(screenName = 'File Converter')

#Labels
windowLabel = Label(root, text='File Converter')

#Fields
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, 'Enter File Name')

#Methods
def myCLick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

#Buttons
buttonOne = Button(root, fg = 'red', bg = 'blue', text="Press this idk", command=myCLick)


#windowLabel.pack()

root.mainloop()