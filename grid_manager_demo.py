from tkinter import *

class GridManagerDemo:
    def __init__(self):
        window=Tk()
        window.title("Grid Manager Demo")

        message = Message(window,text="This message widget occupies three rows and two columns")
        message.grid(row = 1,column = 1,rowspan = 3,columnspan = 2)
        Label(window,text="First name:").grid(row = 1,column = 3)
        Entry(window).grid(row = 1,column = 4,padx = 5,pady = 5)
        Label(window,text ="Last Name:").grid(row = 2,column = 3)
        Entry(window).grid(row = 2, column = 4)
        Button(window,text = "Get Name").grid(row = 3,padx = 5,pady = 5,column = 4,sticky = E)
        #将pady调整为500，也会影响message的位置？
        window.mainloop()


GridManagerDemo()


