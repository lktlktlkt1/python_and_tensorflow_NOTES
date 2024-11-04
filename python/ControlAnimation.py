from tkinter import *

class ControlAnimation:
    def __init__(self):
        window = Tk()
        window.title("Control Animation")
        self.width = 250
        self.canvas = Canvas(window,bg = "white",width=self.width,height = 50)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btStop = Button(frame,text = "Stop",command = self.displayStop)
        btStop.pack(side = LEFT)
        btResume = Button(frame,text = "Resume",command = self.displayResume)
        btResume.pack(side = LEFT)
        btFaster = Button(frame,text = "Faster",command = self.displayFaster)
        btFaster.pack(side = LEFT)
        btSlower = Button(frame,text = "Slower",command = self.displaySlower)
        btSlower.pack(side = LEFT)

        self.x = 0
        self.sleepTime = 100
        self.canvas.create_text(self.x,30,text="Message moving?",tags = "text")

        self.dx = 3
        self.isStopped = False
        self.animate()

        window.mainloop()

    def displayStop(self):
        self.isStopped = True

    def displayResume(self):
        self.isStopped = False
        self.animate()

    def displayFaster(self):
        if self.sleepTime>5:
            self.sleepTime -= 20

    def displaySlower(self):
        self.sleepTime += 20

    def animate(self):
        while not self.isStopped:
            self.canvas.move("text",self.dx,0)
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            if self.x < self.width:
                self.x += self.dx
            else :
                self.x = 0
                self.canvas.delete("text")
                self.canvas.create_text(self.x,30,text = "Message moving?",tags="text")

ControlAnimation()
