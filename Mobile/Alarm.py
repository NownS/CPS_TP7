from tkinter import *


root = Tk()
root.title("Alarm")
root.geometry("200x200+100+100")
root.resizable(False, False)

label = Label(root, text='\n\nGood Morning!\n\n')
label.pack()

button = Button(root, width = 20, height = 5 , text = "알람 끄기", overrelief="solid", command = quit)
button.pack()

root.mainloop()