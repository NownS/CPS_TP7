import tkinter


alarm = tkinter.Tk()
alarm.title("Alarm")
alarm.geometry("200x200+100+100")
alarm.resizable(False, False)

label = tkinter.Label(alarm, text='\n\nGood Morning!\n\n')
label.pack()

button = tkinter.Button(alarm, width = 20, height = 5 , text = "알람 끄기", overrelief="solid", command = alarm.quit)
button.pack()

alarm.mainloop()