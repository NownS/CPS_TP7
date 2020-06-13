##홈 컨트롤러(스마트 홈) 추상화 모델

import tkinter
import subprocess
import time
import threading

def onclick(process):
    subprocess.Popen(["python", process])

root = tkinter.Tk()
root.title("Home")
root.geometry("300x400+100+100")
root.resizable(False, False)

button1 = tkinter.Button(root, width = 11, height = 4 , text = "AirConditioner", overrelief="solid", command = lambda: onclick("AirConditioner.py"))
button1.place(x=50, y=30)
button2 = tkinter.Button(root, width = 11, height = 4 , text = "DoorLock", overrelief="solid", command = lambda: onclick("DoorLock.py"))
button2.place(x=170, y=30)
button3 = tkinter.Button(root, width = 11, height = 4 , text = "Lamp", overrelief="solid", command = lambda: onclick("Lamp.py"))
button3.place(x=50, y=150)
button4 = tkinter.Button(root, width = 11, height = 4 , text = "TV", overrelief="solid", command = lambda: onclick("TV.py"))
button4.place(x=170, y=150)
button5 = tkinter.Button(root, width = 11, height = 4 , text = "Vacuum", overrelief="solid", command = lambda: onclick("Vacuum.py"))
button5.place(x=50, y=270)
button6 = tkinter.Button(root, width = 11, height = 4 , text = "Washer", overrelief="solid", command = lambda: onclick("Washer.py"))
button6.place(x=170, y=270)


root.mainloop()