from tkinter import *
import json


class startscherm:
    def __init__(self, parent):
        self.parent = parent
        self.scherm = Frame(self.parent)
        self.scherm.config(bg = 'black')
        self.scherm.pack(fill = 'both',expand = True )

        self.startFrame = Frame(self.scherm, bg = 'black')
        self.startFrame.pack(fill = 'both', expand = True)

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

        self.startButton = Button(self.startFrame, command = self.startKnop, bg = 'red', fg = 'yellow', text = 'Start', font = ('ariel', 18, 'bold'))
        self.startButton.place( y= 200, x = 600)

        self.rulesButton = Button(self.startFrame, command = self.rulesKnop, bg = 'green', fg = 'red', text = 'Rules', font = ('ariel', 18, 'bold'))
        self.rulesButton.place( y= 275, x = 595)

        self.settingButton = Button(self.startFrame, command = self.settingKnop, bg = 'pink', fg = 'blue', text = 'Settings', font = ('ariel', 18, 'bold'))
        self.settingButton.place( y= 350, x = 585)

    def startKnop(self):
        self.startFrame.destroy()
        self.gameFrame = Frame(self.scherm, bg = 'green')
        self.gameFrame.pack(fill = 'both', expand = True)

        self.mastermindFrame = Frame(self.gameFrame, bg = 'black')
        self.mastermindFrame.place(height = 675, width = 500, y = 20, x = 400)


    def rulesKnop(self):
        self.startFrame.destroy()
        self.rulesFrame = Frame(self.scherm, bg='red')
        self.rulesFrame.pack(fill='both', expand=True)

        self.regelsFrame = Frame(self.rulesFrame, bg='white')
        self.regelsFrame.place(height=675, width=500, y=20, x=400)


    def settingKnop(self):
        self.startFrame.destroy()
        self.settingsFrame = Frame(self.scherm, bg='blue')
        self.settingsFrame.pack(fill='both', expand=True)

        self.instellingenFrame = Frame(self.settingsFrame, bg='white')
        self.instellingenFrame.place(height=675, width=500, y=20, x=400)








root = Tk()
root.config(bg = 'black')
root.attributes('-fullscreen', True)
startscherm(root)
root.mainloop()