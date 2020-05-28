import tkinter
import subprocess

def onclick(process):
    subprocess.run(["python", process])

root = tkinter.Tk()
root.title("Mobile Phone")
root.geometry("300x500")
root.resizable(False, False)

button1 = tkinter.Button(root, width = 11, height = 4 , text = "알람", overrelief="solid", command = lambda: onclick("Alarm.py"))
button1.place(x=50, y=30)
button2 = tkinter.Button(root, width = 11, height = 4 , text = "게임", overrelief="solid", command = lambda: onclick("Game.py"))
button2.place(x=170, y=30)

root.mainloop()