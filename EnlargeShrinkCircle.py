from tkinter import *

class EnlargeShrinkCircle:
    def __init__(self):
        self.radius = 50

        window=Tk()
        window.title("Enlarge Shrink Circle")
        self.canvas = Canvas(window,bg = "white",width = 200,height = 200)
        self.canvas.pack()
        self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags="oval")
        self.canvas.bind("<Button-1>",self.increaseCircle)

        window.mainloop()

    def increaseCircle(self,event):
        self.canvas.delete("oval")
        if self.radius<100:
            self.radius += 2
        self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags="oval")


EnlargeShrinkCircle()

