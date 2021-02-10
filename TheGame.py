from tkinter import *
import random

class mastermind:
    def __init__(self):
      return




    # basic setting for the game

    def manualcode(self):
    #geef code op
    # code wordt ingesteld als code
        return





    def AIcode(self):
        colours = ['red', 'pink', 'yellow', 'green', 'orange','blue']
        self.colourcode = []

        for value in range(0, 4):
            self.colourcode.append(random.choice(colours))





    def pogingen(self):
        self.attempts += 1
        if self.attempts > 9:
            self.helaasFrame = Frame(self.gameFrame, bg='green')
            self.helaasFrame.place(y=70, x=100, height=450, width=200)

            self.helaasLabel = Label(self.helaasFrame, bg='green', fg='red', text='Helaas!\n U heeft verloren', font=('ariel', 16, 'bold'))
            self.helaasLabel.place(y=0, x=0)

            self.returnButton = Button(self.helaasFrame, command=lambda: mastermind.Afsluiten(self), text='Afsluiten', bg='pink', fg='blue', font=('ariel', 8, 'bold'))
            self.returnButton.place(y=150, x=60)
        else:
            mastermind.manualguess(self)


    def manualguess(self):
        self.correct = 0
        self.wrongplace = 0
        self.colours1 = ['red', 'pink', 'yellow', 'green', 'orange', 'blue']
        self.colours2 = ['red', 'pink', 'yellow', 'green', 'orange', 'blue']
        self.colours3 = ['red', 'pink', 'yellow', 'green', 'orange', 'blue']
        self.colours4 = ['red', 'pink', 'yellow', 'green', 'orange', 'blue']


        valueY = 480 - (self.attempts - 1) * 50

        self.raadFrame = Frame(self.mastermindFrame, bg='black', highlightbackground='white', highlightthickness=3)
        self.raadFrame.place(x=0, y=valueY, height=50, width=450)

        self.guessingButton1 = Button(self.raadFrame, text='[X]', command = lambda: mastermind.colourguess(self, 1), bg='black', fg='white', font=('ariel', 12, 'bold'), width=10, borderwidth = 0)
        self.guessingButton1.place(x=30, y=10)

        self.guessingButton2 = Button(self.raadFrame, text='[X]', command=lambda: mastermind.colourguess(self, 2), bg='black', fg='white', font=('ariel', 12, 'bold'), width=10, borderwidth = 0)
        self.guessingButton2.place(x=130, y=10)

        self.guessingButton3 = Button(self.raadFrame, text='[X]', command=lambda: mastermind.colourguess(self, 3), bg='black', fg='white', font=('ariel', 12, 'bold'), width=10, borderwidth = 0)
        self.guessingButton3.place(x=230, y=10)

        self.guessingButton4 = Button(self.raadFrame, text='[X]', command=lambda: mastermind.colourguess(self, 4), bg='black', fg='white', font=('ariel', 12, 'bold'), width=10, borderwidth = 0)
        self.guessingButton4.place(x=330, y=10)




    def colourguess(self, guess):

        if guess == 1:
            self.guessingButton1.config(text = self.colours1[0], fg = self.colours1[0])
            self.selectedcolour1 = self.colours1[0]
            self.colours1.append(self.colours1[0])
            self.colours1.pop(0)
        elif guess == 2:
            self.guessingButton2.config(text=self.colours2[0], fg=self.colours2[0])
            self.selectedcolour2 = self.colours2[0]
            self.colours2.append(self.colours2[0])
            self.colours2.pop(0)
        elif guess == 3:
            self.guessingButton3.config(text=self.colours3[0], fg=self.colours3[0])
            self.selectedcolour3 = self.colours3[0]
            self.colours3.append(self.colours3[0])
            self.colours3.pop(0)
        elif guess == 4:
            self.guessingButton4.config(text = self.colours4[0], fg = self.colours4[0])
            self.selectedcolour4 = self.colours4[0]
            self.colours4.append(self.colours4[0])
            self.colours4.pop(0)


    def AIguess(self):
        return


    def checkAwnsers(self):
        colours = ['red', 'pink', 'yellow', 'green', 'orange', 'blue']
        self.wrongplacecolours = []
        self.almost = 0
        self.rightplace = 0
        print(self.colourcode)
        valueY = 480 - (self.attempts - 1) * 50
        scorevak = Frame(self.mastermindFrame, bg='black', highlightbackground='green', highlightthickness=1.5)
        scorevak.place(x=500, y=valueY, height=50, width=50)


        try:
            self.selectedcolour1
            if self.selectedcolour1 in self.colourcode:
                if self.selectedcolour1 == self.colourcode[0]:
                    if self.colourcode.count(self.selectedcolour1) == 1:
                        self.wrongplacecolours.append(self.selectedcolour1)
                        self.correct += 1
                        self.rightplace += 1
                        self.score1 = Label(scorevak, text='X', bg='red', fg='red', font=('ariel', 8, 'bold'), width=2)
                        self.score1.place(x=26, y=26)
                    elif self.colourcode.count(self.selectedcolour1) > 1:
                        self.correct += 1
                        self.rightplace += 1
                        self.score1 = Label(scorevak, text='X', bg='red', fg='red', font=('ariel', 8, 'bold'), width=2)
                        self.score1.place(x=26, y=26)
                else:
                    if self.selectedcolour1 not in self.wrongplacecolours:
                        self.wrongplacecolours.append(self.selectedcolour1)
                        self.wrongplace += 1
                        self.almost += 1
                        self.wrongscore1 = Label(scorevak, text='X', bg='white', fg='white', font=('ariel', 8, 'bold'), width=2)
                        self.wrongscore1.place(x=26, y=26)

        except:
            print('hi')

        try:
            if self.selectedcolour2 in self.colourcode:
                if self.selectedcolour2 == self.colourcode[1]:
                    if self.colourcode.count(self.selectedcolour2) == 1:
                        self.wrongplacecolours.append(self.selectedcolour2)
                        self.correct += 1
                        self.rightplace +=1
                        self.score2 = Label(scorevak, text='X', bg='red', fg='red', font=('ariel', 8, 'bold'), width=2)
                        self.score2.place(x=0, y=0)
                    elif self.colourcode.count(self.selectedcolour2) > 1:
                        self.correct += 1
                        self.rightplace += 1
                        self.score2 = Label(scorevak, text='X', bg='red', fg='red', font=('ariel', 8, 'bold'), width=2)
                        self.score2.place(x=0, y=0)
                else:
                    if self.selectedcolour2 not in self.wrongplacecolours:
                        self.wrongplacecolours.append(self.selectedcolour2)
                        self.wrongplace += 1
                        self.almost += 1
                        self.wrongscore2 = Label(scorevak, text='X', bg='white', fg='white', font=('ariel', 8, 'bold'), width=2)
                        self.wrongscore2.place(x=0, y=0)

        except:
            print('hi')

        try:
            if self.selectedcolour3 in self.colourcode:
                if self.selectedcolour3 == self.colourcode[2]:
                    if self.colourcode.count(self.selectedcolour3) == 1:
                        self.wrongplacecolours.append(self.selectedcolour3)
                        self.correct += 1
                        self.rightplace += 1
                        self.score3 = Label(scorevak, text='X', bg='red', fg='red', font=('ariel', 8, 'bold'), width=2)
                        self.score3.place(x=0, y=26)
                    elif self.colourcode.count(self.selectedcolour3) > 1:
                        self.correct += 1
                        self.rightplace += 1
                        self.score3 = Label(scorevak, text='X', bg='red', fg='red', font=('ariel', 8, 'bold'), width=2)
                        self.score3.place(x=0, y=26)
                else:
                    if self.selectedcolour3 not in self.wrongplacecolours:
                        self.wrongplacecolours.append(self.selectedcolour3)
                        self.wrongplace += 1
                        self.almost += 1
                        self.wrongscore3 = Label(scorevak, text='X', bg='white', fg='white', font=('ariel', 8, 'bold'), width=2)
                        self.wrongscore3.place(x=0, y=26)
        except:
            print('hi')

        try:
            if self.selectedcolour4 in self.colourcode:
                if self.selectedcolour4 == self.colourcode[3]:
                    if self.colourcode.count(self.selectedcolour4) == 1:
                        self.wrongplacecolours.append(self.selectedcolour4)
                        self.correct += 1
                        self.rightplace += 1
                        self.score4 = Label(scorevak, text='X', bg='red', fg='red', font=('ariel', 8, 'bold'), width=2)
                        self.score4.place(x=26, y=0)
                    elif self.colourcode.count(self.selectedcolour4) > 1:
                        self.correct += 1
                        self.rightplace += 1
                        self.score4 = Label(scorevak, text='X', bg='red', fg='red', font=('ariel', 8, 'bold'), width=2)
                        self.score4.place(x=26, y=0)
                else:
                    if self.selectedcolour4 not in self.wrongplacecolours:
                        self.wrongplacecolours.append(self.selectedcolour4)
                        self.wrongplace += 1
                        self.almost += 1
                        self.wrongscore4 = Label(scorevak, text='X', bg='white', fg='white', font=('ariel', 8, 'bold'), width=2)
                        self.wrongscore4.place(x=26, y=0)

        except:
            print('hi')

        if self.correct == 4:
           mastermind.Finish(self)


    def Finish(self):
        self.gefeliciteerdFrame = Frame(self.gameFrame, bg = 'green')
        self.gefeliciteerdFrame.place(y = 70, x = 100, height = 450, width= 200)

        self.gefeliciteerdLabel = Label(self.gefeliciteerdFrame, bg = 'green', fg = 'red', text = 'Gefeliciteerd!\n U heeft gewonnen', font=('ariel', 16, 'bold'))
        self.gefeliciteerdLabel.place(y = 0, x = 0)

        self.afsluitButton = Button(self.gefeliciteerdFrame, command = lambda: mastermind.Afsluiten(self) ,text = 'Afsluiten', bg = 'pink', fg = 'blue', font=('ariel', 8, 'bold'))
        self.afsluitButton.place(y = 150, x = 60)

    def Afsluiten(self):
        self.parent.destroy()