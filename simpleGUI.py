from tkinter import *

'''window = Tk()
label = Label(window,text = "Welcome to python")
button = Button(window,text="Click me")
label.pack()
button.pack()

window.mainloop()'''

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel button is clicked")

window = Tk()
btOK = Button(window,text="OK",fg="red",command = processOK)
btCancel = Button(window,text = "Cancel",bg="yellow",command = processCancel)
btOK.pack()
btCancel.pack()

window.mainloop()


