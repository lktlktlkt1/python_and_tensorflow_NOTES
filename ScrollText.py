from tkinter import *

class ScrollText:
    def __init__(self):
        window = Tk()
        window.title("Scroll Text")

        frame1=Frame(window)
        frame1.pack()
        scrollBar = Scrollbar(frame1)
        scrollBar.pack(side = RIGHT,fill = Y)
        text = Text(frame1,width = 40,height = 10,wrap = WORD,yscrollcommand=scrollBar.set)
        text.pack()

        window.mainloop()

ScrollText()