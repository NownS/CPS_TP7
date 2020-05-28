##모바일 컨트롤러(휴대폰) 추상화 모델

import tkinter
import subprocess
import time
import threading
from datetime import datetime

hour = 0
minute = 0
sec = 0

def alarm_timeset(event):
        arr = str(entry.get())
        label.config(text="알람 시간:" + arr)
        global hour
        global minute
        global sec
        hour, minute, sec = arr.split(":")
        hour = int(hour)
        minute = int(minute)
        sec = int(sec)

#------------------------알람 기록 프로세스------------------------------#

def clockcount():
    while (1):
        today = datetime.today()
        if(hour == today.hour and minute == today.minute and sec == today.second):
            subprocess.run(["python", "Alarm.py"])
        time.sleep(1)



def onclick(process):
    subprocess.run(["python", process])

root = tkinter.Tk()
root.title("Mobile Phone")
root.geometry("300x400")
root.resizable(False, False)

button1 = tkinter.Button(root, width = 11, height = 4 , text = "Alarm", overrelief="solid", command = lambda: onclick("Alarm.py"))
button1.place(x=50, y=30)
button2 = tkinter.Button(root, width = 11, height = 4 , text = "Game", overrelief="solid", command = lambda: onclick("Game.py"))
button2.place(x=170, y=30)
button3 = tkinter.Button(root, width = 11, height = 4 , text = "Messenger", overrelief="solid", command = lambda: onclick("Game.py"))
button3.place(x=50, y=150)
button4 = tkinter.Button(root, width = 11, height = 4 , text = "Music", overrelief="solid", command = lambda: onclick("Game.py"))
button4.place(x=170, y=150)
button5 = tkinter.Button(root, width = 11, height = 4 , text = "Training", overrelief="solid", command = lambda: onclick("Game.py"))
button5.place(x=50, y=270)
button6 = tkinter.Button(root, width = 11, height = 4 , text = "Video", overrelief="solid", command = lambda: onclick("Game.py"))
button6.place(x=170, y=270)

entry = tkinter.Entry(root, width = 7)
entry.bind("<Return>", alarm_timeset)
entry.place(x=65,y=110)

label = tkinter.Label(root, text="")
label.place(x=40,y=130)

t = threading.Thread(target = clockcount, args=())
t.start()                                        #알람 백그라운드 실행

root.mainloop()