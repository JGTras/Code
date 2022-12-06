import tkinter
from tkinter import *



# This program is designed to count up from zero
class CountsUp(Frame):

    def another_window1(self):
        self.window_1 = Tk()
        self.window_1.title("Set timer")
        self.window_1.config(bg='orange')

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.widgets()
        self.running = False
        self.timer = [0,0,0]    # [minutes ,seconds, centiseconds]
        self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
        self.update_time()

    def widgets(self):
        self.timeFrame = LabelFrame(root, text='Counts Up',bg="#0F3460", fg ="yellow")
        self.timeFrame.grid(row=0,column=0)

        self.resetButton = Button(self.timeFrame, text='Reset', command=self.resetTime,bg="#0F3460", fg ="yellow")
        self.resetButton.grid(row=2,column=1)

        self.pauseButton = Button(self.timeFrame, text='Pause', command=self.pause,bg="#0F3460", fg ="yellow")
        self.pauseButton.grid(row=1,column=1)

        self.startButton = Button(self.timeFrame, text='Start', command=self.start,bg="#0F3460", fg ="yellow")
        self.startButton.grid(row=0,column=1)

        self.show = Label(self.timeFrame, text='00:00:00', font=('Helvetica', 30),bg="#0F3460", fg ="yellow")
        self.show.grid(row=0, column=0)

        self.quit = Button(self.timeFrame, text='QUIT', command=self.quit,bg="#0F3460", fg ="yellow")
        self.quit.grid(row=3, column=1)


    def update_time(self):

        if (self.running == True):      #counting down
            self.timer[2] += 1

            if (self.timer[2] >= 100):  #100 centiseconds --> 1 second
                self.timer[2] = 0       #reset to zero centiseconds
                self.timer[1] += 1      #add 1 second to the screen

            if (self.timer[1] >= 60):   #60 seconds --> 1 minute
                self.timer[0] += 1      #add 1 minute
                self.timer[1] = 0       #reset to 0 seconds

            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
            self.show.config(text=self.timeString)
        root.after(10, self.update_time)

    # Functin to Start the clock
    def start(self):
        self.running = True
        print ('Clock Running...')

    # function to pause the clock
    def pause(self):
        self.running = False
        print('Clock Paused')

    # function to reset the clock
    def resetTime(self):
        self.running = False
        self.timer = [0,0,0]
        print ('Clock is Reset')
        self.show.config(text='00:00:00')

    # Quit
    def quit(self):
        root.destroy()





root = tkinter.Tk()

up = CountsUp(root)
