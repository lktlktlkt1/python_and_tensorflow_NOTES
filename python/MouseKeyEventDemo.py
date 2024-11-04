from tkinter import *
class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        window.title("Mouse Key Event Demo")
        window.geometry("200x200")
        window.resizable(False,False)
        canvas = Canvas(window,bg="white",width = 200,height = 200)
        canvas.pack()

        canvas.bind("<Button-1>",self.processMouseEvent)
        canvas.bind("<Key>",self.processKeyEvent)
        canvas.focus_set()

        window.mainloop()


    def processMouseEvent(self,event):
        print("Clicked at",event.x,event.y)
        print("Position in the screen is",event.x_root,event.y_root)
        print("The number clicked at is",event.num)

    def processKeyEvent(self,event):
        print("keysym?",event.keysym)
        print("char?",event.char)
        print("keycode?",event.keycode)

MouseKeyEventDemo()


