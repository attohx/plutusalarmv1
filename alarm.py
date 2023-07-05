from tkinter import *
import datetime
import time
import winsound

def alarmclock(alarm_set):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S.....")
        print(now)
        
        if now == alarm_set:
            print("WAKE UP!!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

def actual_time():
    alarm_set = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarmclock(alarm_set)


clockui = Tk()

clockui.title("Alarm Clock")
clockui.geometry("400x200")

hour = StringVar()
min = StringVar()
sec = StringVar()

time_format=Label(clockui, text = "Input time in 24 hour format!", fg="red", bg="black", font="Helvetica").place(x = 100,y = 150)
addTime = Label(clockui, text="Hour  -  Min  -  Sec", font = 60 ).place(x = 110)
setTheAlarm = Label(clockui, text = "Input Time", fg="darkorchid1", relief = "solid", font=("Helvetica", 7, "bold")).place(x = 0,y = 29)

hourTime = Entry(clockui, textvariable = hour,bg = "pink",width = 15).place(x = 110,y = 30)
minTime = Entry(clockui, textvariable = min,bg = "pink", width = 15).place(x = 150, y = 30)
secTime = Entry(clockui, textvariable = sec,bg ="pink", width = 15).place(x = 200, y = 30)

submit = Button(clockui, text = "Activate Alarm", fg = "red", width = 10, command = actual_time).place(x = 150, y = 90)


clockui.mainloop()