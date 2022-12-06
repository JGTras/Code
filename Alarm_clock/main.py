
#use tkinter for ui
from tkinter import *
#import time will be the databse of the codes
import time
#
from tkinter import ttk, messagebox
#To play sound for the alarm
from playsound import playsound
#multiprocessing is a package that supports spawning processes using an API similar to the threading module. To do multistask
import multiprocessing
#for the dates and time
from datetime import datetime
#WHAT
from threading import *



# This is for the hours List.
hours_list = ['00', '01', '02', '03', '04', '05', '06', '07',
              '08', '09', '10', '11', '12', '13', '14', '15',
              '16', '17', '18', '19', '20', '21', '22', '23', '24']

# This is for the Minutes List.
minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23',
                '24', '25', '26', '27', '28', '29', '30', '31',
                '32', '33', '34', '35', '36', '37', '38', '39',
                '40', '41', '42', '43', '44', '45', '46', '47',
                '48', '49', '50', '51', '52', '53', '54', '55',
                '56', '57', '58', '59']

# Ringtones list to use for the selection box.
ringtones_list = ['Samsung', 'super_idol', 'bing_chilling','Giorno','Pillar_men']

# Ringtone's location.
ringtones_path = {
    'Samsung': 'C:/Users/USER/PycharmProjects/Clock/Alarm_clock/Ringtones/Samsung.mp3',
    'super_idol': 'C:/Users/USER/PycharmProjects/Clock/Alarm_clock/Ringtones/super_idol.mp3',
    'bing_chilling': 'Ringtones/bing_chilling.mp3',
    'Giorno': 'C:/Users/USER/PycharmProjects/Clock/Alarm_clock/Ringtones/Giorno.mp3',
    'Pillar_men':'C:/Users/USER/PycharmProjects/Clock/Alarm_clock/Ringtones/Pillar_men.mp3',
}


# The Class: Alarm Clock._____________________________________

class Alarm_Clock:
    def __init__(self, root):
        #dimensions of the menu
        self.window = root
        self.window.geometry("680x420+0+0")
        self.window.title("Clock application")


        # C: / Users / USER / PycharmProjects / Clock / download(1).jpg
        root.configure(bg='#16213E')
        # Display Label that shows the current time in the
        # first window
        self.display = Label(self.window, font=('Cascadia Mono SemiBold', 34),
                             bg='#16213E', fg='yellow')
        self.display.place(x=100, y=150)

        # Calling the the function.
        self.show_time()

        # Placing the set alarm button.
        # Font Type: relief solid font helevetica.
        set_button = Button(self.window,width=9, text="Set Alarm",
                            font=('Cascadia Mono SemiBold', 15), bg="#0F3460", fg="yellow",
                            command=self.another_window)
        set_button.place(x=270, y=250)

#timer button to direct to another window taht contains the class Stopwatch code
        set_button2 = Button(text="Stopwatch",width=9, font=('Cascadia Mono SemiBold',15),bg="#0F3460", fg ="yellow",command=self.another_window1)
        set_button2.place(x=270,y=310)

        set_button3 = Button(text="Timer", width=9, font=('Cascadia Mono SemiBold', 15), bg="#0F3460", fg="yellow",
                             command=self.another_window3)
        set_button3.place(x=270, y=370)

    # This function shows the current time in the first window.
    def show_time(self):
        current_time = time.strftime('%H:%M:%S %p, %A')
        # Placing the time format level.
        self.display.config(text=current_time)
        self.display.after(100, self.show_time)

    # Another Window: This window will show, when the "Set Alarm"
    # Button will pressed.

#window for timer
    def another_window3(self):
        import Testt
        Testt.countdowntimer()

        self.another_window3().mainloop()

    def another_window1(self):
        import Test
        Test.mainloop()

        self.another_window1().mainloop()
#window for alarm
    def another_window(self):
        self.window_2 = Tk()
        self.window_2.title("Set Alarm")
        self.window_2.geometry("680x420+200+200")

        self.window_2.config(bg="#16213E")

        # Hour Text.
        hours_label = Label(self.window_2, text="Hours",bg="#16213E",fg='yellow',
                            font=("times new roman", 20))
        hours_label.place(x=150, y=50)
        #  Minute text.
        minute_label = Label(self.window_2, text="Minutes",bg="#16213E",fg='yellow',
                             font=("times new roman", 20))
        minute_label.place(x=275, y=50)
        # Hour box design.
        self.hours = StringVar()
        self.hours_combobox = ttk.Combobox(self.window_2,
                                           width=10, height=10, textvariable=self.hours,
                                           font=("times new roman", 15))
        self.hours_combobox['values'] = hours_list
        self.hours_combobox.current(0)
        self.hours_combobox.place(x=150, y=90)

        # Minute Box design.
        self.minutes = StringVar()
        self.minutes_combobox = ttk.Combobox(self.window_2,
                                             width=10, height=10, textvariable=self.minutes,
                                             font=("times new roman", 15))
        self.minutes_combobox['values'] = minutes_list
        self.minutes_combobox.current(0)
        self.minutes_combobox.place(x=275, y=90)

        # Ringtone Text.
        ringtone_label = Label(self.window_2, text="Ringtones",bg="#16213E",fg='yellow',
                               font=("times new roman", 20))
        ringtone_label.place(x=150, y=130)

        # Ringtone Combobox(Choose the ringtone).
        self.ringtones = StringVar()
        self.ringtones_combobox = ttk.Combobox(self.window_2,
        width=15, height=10, textvariable=self.ringtones,
        font=("times new roman", 15))
        self.ringtones_combobox['values'] = ringtones_list
        self.ringtones_combobox.current(0)
        self.ringtones_combobox.place(x=150, y=170)

        # Title or Message Label.
        message_label = Label(self.window_2, text="Message",bg="#16213E",fg='yellow',
                              font=("times new roman", 20))
        message_label.place(x=150, y=210)

        # Message Entrybox: This Message will show, when
        # the alarm will ringing.
        self.message = StringVar()
        self.message_entry = Entry(self.window_2,
        textvariable=self.message, font=("times new roman", 14), width=30)
        self.message_entry.insert(0, 'Wake Up')
        self.message_entry.place(x=150, y=250)


        # The Cancel Button: For cancel the alarm.
        cancel_button = Button(self.window_2,
                               text='Cancel', font=('Helvetica', 15), bg="red",
                               fg="black", command=self.window_2.destroy)
        cancel_button.place(x=390, y=300)

        # The Start Button: For set the alarm time
        start_button = Button(self.window_2, text='Start', \
                              font=('Helvetica', 15), bg="green", fg="white", command=self.Threading_1)
        start_button.place(x=490, y=300)

        self.window_2.mainloop()

    # In this function, I have used python multiprocessing module
    # to play the ringtones while the alarm gets notified.

    # Creating a thread
    def Threading_1(self):
        x = Thread(target=self.set_alarm_time)
        x.start()

    # This function gets called when the start button pressed
    # in the another window for setting alarm time.
    def set_alarm_time(self):
        alarm_time = f"{self.hours_combobox.get()}:{self.minutes_combobox.get()}"
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        while True:
            # The current time is in 24 hour format6
            current_time = datetime.now()
            # Converting the current time into hour and minute
            current_time_format = current_time.strftime("%H:%M")
            if current_time_format == alarm_time:
                process = multiprocessing.Process(target=playsound,
                args=(ringtones_path[self.ringtones_combobox.get()],))
                process.start()
                # Messagebox: This messagebox will show, when the
                # alarm will ringing.
                messagebox.showinfo("Alarm", f"{self.message_entry.get()},It's {alarm_time}")
                process.terminate()
                break

if __name__ == "__main__":
    root = Tk()
    # Object of Alarm_Clock class.
    obj = Alarm_Clock(root),
    root.mainloop()