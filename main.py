from tkinter import *
import random as r


class Core:

    def __init__(self, win):
        self.game = False

        self.score = 0
        self.sec = 0
        self.time = 60

        self.x = 20
        self.y = 50

        self.win = win
        win.title('Running Button')
        win.geometry('550x350+300+200')
        win.resizable(False, False)

        self.ScoreText = Label(win, text='Score: ' + str(self.score), font=('Ubuntu', 25))
        self.ScoreText.grid(row=0, column=0)

        self.TimeText = Label(win, text='Time: ' + str(self.time), font=('Ubuntu', 15))
        self.TimeText.grid(row=1, column=0)

        self.c1 = Canvas(win, width=550, height=250, bg='white')
        self.c1.grid(row=2, column=0)

        self.oval = self.c1.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill='red', width=3, tag='ovals')

        self.c1.tag_bind(self.oval, "<Button-1>", self.rnd_position)
        self.tick()

        if self.game == True:
            self.c1.delete(self.oval)

    def tick(self):
        if not self.game:
            self.time -= 1
            self.sec += 1
            if self.sec < self.time:
                self.TimeText.configure(text='Time: ' + str(self.time))
                self.win.after(1000, self.tick)
            else:
                self.game = True
                self.TimeText.configure(text='Time: Out!')

    def rnd_position(self, event):
        if not self.game:
            self.score_plus()
            self.rndx = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400
                , 420, 440, 460, 480, 500]
            self.rndy = [50, 100, 150]
            self.x = r.choice(self.rndx)
            self.y = r.choice(self.rndy)
            self.c1.delete(self.oval)
            self.oval = self.c1.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill='red', width=3, tag='ovals')
            self.c1.tag_bind(self.oval, "<Button-1>", self.rnd_position)

    def score_plus(self):
        self.score += 1
        self.ScoreText.configure(text='Score: ' + str(self.score))


root = Tk()

c = Core(root)

root.mainloop()
