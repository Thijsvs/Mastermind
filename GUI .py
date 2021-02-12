# importeren
from tkinter import *
import TheGame
import random
import bot


#de class voor het startscherm wordt aangemaakt
class startscherm:
    def __init__(self, parent):
        self.parent = parent
        self.scherm = Frame(self.parent)
        self.scherm.config(bg = 'black')
        self.scherm.pack(fill = 'both',expand = True )

        self.startFrame = Frame(self.scherm, bg = 'black')
        self.startFrame.pack(fill = 'both', expand = True)

        # het woord mastermind in verschillende kleuren
        self.startLabel1 = Label(self.startFrame, bg ='Black',fg ='red',text ='M',font =('ariel', 24, 'bold'))
        self.startLabel1.place(y = 50, x = 540)
        self.startLabel2 = Label(self.startFrame, bg='Black', fg='yellow', text='A', font=('ariel', 24, 'bold'))
        self.startLabel2.place(y=50, x=570)
        self.startLabel3 = Label(self.startFrame, bg='Black', fg='blue', text='S', font=('ariel', 24, 'bold'))
        self.startLabel3.place(y=50, x=595)
        self.startLabel4 = Label(self.startFrame, bg='Black', fg='green', text='T', font=('ariel', 24, 'bold'))
        self.startLabel4.place(y=50, x=617)
        self.startLabel5 = Label(self.startFrame, bg='Black', fg='pink', text='E', font=('ariel', 24, 'bold'))
        self.startLabel5.place(y=50, x=640)
        self.startLabel6 = Label(self.startFrame, bg='Black', fg='white', text='R', font=('ariel', 24, 'bold'))
        self.startLabel6.place(y=50, x=660)
        self.startLabel7 = Label(self.startFrame, bg='Black', fg='red', text='M', font=('ariel', 24, 'bold'))
        self.startLabel7.place(y=50, x=685)
        self.startLabel8 = Label(self.startFrame, bg='Black', fg='yellow', text='I', font=('ariel', 24, 'bold'))
        self.startLabel8.place(y=50, x=712)
        self.startLabel9 = Label(self.startFrame, bg='Black', fg='green', text='N', font=('ariel', 24, 'bold'))
        self.startLabel9.place(y=50, x=722)
        self.startLabel10 = Label(self.startFrame, bg='Black', fg='blue', text='D', font=('ariel', 24, 'bold'))
        self.startLabel10.place(y=50, x=745)

        # start button
        self.startButton = Button(self.startFrame, command = lambda: [TheGame.mastermind.AIcode(self), self.startKnop()], bg = 'red', fg = 'yellow', text = 'Start', font = ('ariel', 18, 'bold'))
        self.startButton.place( y= 200, x = 600)


        # settings button
        self.settingButton = Button(self.startFrame, command = self.settingKnop, bg = 'pink', fg = 'blue', text = 'Game mode', font = ('ariel', 18, 'bold'))
        self.settingButton.place( y= 320, x = 565)


    # in deze functie wordt de game gestart
    def startKnop(self):
        try:
            self.settingsFrame.destroy()
            self.attempts = 1

            self.startFrame.destroy()
            self.gameFrame = Frame(self.scherm, bg='green')
            self.gameFrame.pack(fill='both', expand=True)

            self.mastermindFrame = Frame(self.gameFrame, bg='black')
            self.mastermindFrame.place(height=675, width=600, y=20, x=400)

            codevak = Frame(self.mastermindFrame, bg='black', highlightbackground='white', highlightthickness=1.5)
            codevak.place(x=0, y=0, height=60, width=450)

            for x in range(0, 4):
                valueX = 20 + 100 * x
                secretcode = Label(codevak, text='****', bg='black', fg='white', font=('ariel', 12, 'bold'), width=10,
                                   height=2)
                secretcode.place(x=valueX, y=10)

            for y in range(0, 8):
                valueY = 80 + 50 * y
                quesvak = Frame(self.mastermindFrame, bg='black', highlightbackground='white', highlightthickness=1.5)
                quesvak.place(x=0, y=valueY, height=50, width=450)

                for x in range(0, 4):
                    valueX = 30 + 100 * x
                    quessingLabel = Label(quesvak, text='[X]', bg='black', fg='white', font=('ariel', 12, 'bold'), width=10)
                    quessingLabel.place(x=valueX, y=10)

            for y in range(0, 8):
                valueY = 80 + 50 * y

                resultvak = Frame(self.mastermindFrame, bg='black', highlightbackground='green', highlightthickness=1.5)
                resultvak.place(x=500, y=valueY, height=50, width=50)

                result1 = Label(resultvak, text='X', bg='white', fg='black', font=('ariel', 8, 'bold'), width=2)
                result1.place(x=0, y=0)

                result2 = Label(resultvak, text='X', bg='white', fg='black', font=('ariel', 8, 'bold'), width=2)
                result2.place(x=0, y=26)

                result3 = Label(resultvak, text='X', bg='white', fg='black', font=('ariel', 8, 'bold'), width=2)
                result3.place(x=26, y=0)

                result4 = Label(resultvak, text='X', bg='white', fg='black', font=('ariel', 8, 'bold'), width=2)
                result4.place(x=26, y=26)
            # met deze button worden 2 functies in het "TheGame" bestand aangeroepen
            raadbutton = Button(self.mastermindFrame,
                                command=lambda: [TheGame.mastermind.checkAwnsers(self), TheGame.mastermind.pogingen(self)],
                                text='Raden', bg='green', fg='black', font=('ariel', 16))
            raadbutton.place(x=50, y=550)

            TheGame.mastermind.manualguess(self)
        except:

            self.attempts = 1

            self.startFrame.destroy()
            self.gameFrame = Frame(self.scherm, bg = 'green')
            self.gameFrame.pack(fill = 'both', expand = True)

            self.mastermindFrame = Frame(self.gameFrame, bg = 'black')
            self.mastermindFrame.place(height = 675, width = 600, y = 20, x = 400)

            codevak = Frame(self.mastermindFrame, bg = 'black', highlightbackground = 'white', highlightthickness = 1.5)
            codevak.place(x = 0, y = 0, height = 60, width = 450)

            for x in range(0, 4):
                valueX = 20 + 100 * x
                secretcode = Label(codevak, text = '****', bg = 'black', fg = 'white', font = ('ariel', 12, 'bold'), width = 10, height = 2)
                secretcode.place( x = valueX, y = 10)

            for y in range(0, 8):
                valueY = 80 + 50 * y
                quesvak = Frame(self.mastermindFrame, bg = 'black', highlightbackground = 'white', highlightthickness = 1.5)
                quesvak.place(x = 0, y = valueY, height = 50, width = 450)

                for x in range(0, 4):
                    valueX = 30 + 100 * x
                    quessingLabel = Label(quesvak, text = '[X]', bg = 'black', fg = 'white', font = ('ariel', 12, 'bold'), width = 10)
                    quessingLabel.place(x = valueX, y = 10)


            for y in range(0, 8):
                valueY = 80 + 50 * y

                resultvak = Frame(self.mastermindFrame, bg = 'black', highlightbackground = 'green', highlightthickness = 1.5)
                resultvak.place(x = 500, y = valueY, height = 50, width = 50)

                result1 = Label(resultvak, text = 'X', bg = 'white', fg = 'black', font = ('ariel', 8, 'bold'), width = 2)
                result1.place(x = 0, y = 0)

                result2 = Label(resultvak, text='X', bg='white', fg='black', font=('ariel', 8, 'bold'), width=2)
                result2.place(x=0, y=26)

                result3 = Label(resultvak, text='X', bg='white', fg='black', font=('ariel', 8, 'bold'), width=2)
                result3.place(x=26, y=0)

                result4 = Label(resultvak, text='X', bg='white', fg='black', font=('ariel', 8, 'bold'), width=2)
                result4.place(x=26, y=26)
            # met deze button worden 2 functies in het "TheGame" bestand aangeroepen
            raadbutton = Button(self.mastermindFrame, command = lambda: [ TheGame.mastermind.checkAwnsers(self), TheGame.mastermind.pogingen(self)], text = 'Raden', bg = 'green', fg = 'black', font = ('ariel', 16))
            raadbutton.place(x = 50, y = 550)

            TheGame.mastermind.manualguess(self)



    # In deze funtie kun je de instellingen wijzigen
    def settingKnop(self):
        self.startFrame.destroy()
        self.settingsFrame = Frame(self.scherm, bg='blue')
        self.settingsFrame.pack(fill='both', expand=True)

        self.instellingenFrame = Frame(self.settingsFrame, bg='pink')
        self.instellingenFrame.place(height=675, width=500, y=20, x=400)

        self.keuzeFrame = Frame(self.instellingenFrame, bg = 'pink')
        self.keuzeFrame.place(height=675, width=500, y=0, x=0)

        self.keuzeLabel = Label(self.keuzeFrame, text = 'Hoe wilt u spelen?', bg = 'pink', fg = 'blue', font=('ariel', 20, 'bold'))
        self.keuzeLabel.place(x = 140, y = 60)

        self.aiButton = Button(self.keuzeFrame, text = 'Tegen computer', command = self.againstAI, bg = 'blue', fg = 'pink', font=('ariel', 10, 'bold'))
        self.aiButton.place(x = 100, y = 350)

        self.manualButton = Button(self.keuzeFrame, text = 'Tegen persoon', command = self.againstPerson, bg = 'blue', fg = 'pink', font=('ariel', 10, 'bold'))
        self.manualButton.place(x = 300, y = 350)

    # optie om een code te raden of een code te raden die gemaakt is door een bot
    def againstAI(self):
        self.keuzeFrame.destroy()

        self.keuzeFrame2 = Frame(self.instellingenFrame, bg = 'pink')
        self.keuzeFrame2.place(height=675, width=500, y=0, x=0)

        self.keuzeLabel2 = Label(self.keuzeFrame2, text = 'Hoe wilt u spelen?', bg = 'pink', fg = 'blue', font=('ariel', 20, 'bold'))
        self.keuzeLabel2.place(x = 140, y = 60)

        self.aiButton = Button(self.keuzeFrame2, text='Code maken', command= lambda: [TheGame.mastermind.manualcode(self), self.bot()], bg='blue', fg='pink', font=('ariel', 10, 'bold'))
        self.aiButton.place(x=100, y=350)

        self.manualButton = Button(self.keuzeFrame2, text='Code raden', command= self.bot, bg='blue', fg='pink', font=('ariel', 10, 'bold'))
        self.manualButton.place(x=300, y=350)

    # het frame waarin het werk van de bot wordt getoond
    def bot(self):
        self.settingsFrame.destroy()
        self.botFrame = Frame(self.scherm, bg='blue')
        self.botFrame.pack(fill='both', expand=True)

        self.boardFrame = Frame(self.botFrame, bg='pink')
        self.boardFrame.place(height=675, width=500, y=20, x=400)

        self.actionFrame = Frame(self.botFrame, bg='pink')
        self.actionFrame.place(height=530, width=500, y=20, x=400)



        self.activateButton = Button(self.boardFrame, text='start', command= lambda: bot.bot(), bg='blue', fg='pink',font=('ariel', 10, 'bold'))
        self.activateButton.place(x=230, y=550)

        self.actionLabel = Label(self.botFrame, text= bot.label.labeltje(self), bg='pink', fg='blue', font=('ariel', 20, 'bold'))
        self.actionLabel.place(x=500, y=200)



    # een persoon voert de code in, en een persoon raad de code
    def againstPerson(self):
        self.keuzeFrame.destroy()

        self.keuzeFrame3 = Frame(self.instellingenFrame, bg='pink')
        self.keuzeFrame3.place(height=675, width=500, y=0, x=0)

        self.aiButton = Button(self.keuzeFrame3, text='start',command=lambda: [TheGame.mastermind.manualcode(self), self.startKnop()], bg='blue',fg='pink', font=('ariel', 10, 'bold'))
        self.aiButton.place(x=100, y=350)


    # def createAIcode(self):
    #     self.settingsFrame.destroy()
    #     self.botFrame = Frame(self.scherm, bg='blue')
    #     self.botFrame.pack(fill='both', expand=True)
    #
    #     self.boardFrame = Frame(self.botFrame, bg='pink')
    #     self.boardFrame.place(height=675, width=500, y=20, x=400)


    # def guessAIcode(self):
    #     self.settingsFrame.destroy()
    #     # self.startKnop()
    #     lambda: TheGame.mastermind.AIguess(self)











root = Tk()
root.config(bg = 'black')
root.attributes('-fullscreen', True)
startscherm(root)
root.mainloop()