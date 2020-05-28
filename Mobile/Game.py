from tkinter import *


root = Tk()
root.title("Game")
root.geometry("500x200+100+100")
root.resizable(False, False)

label = Label(root, text='\nGames\n')
label.pack()

button1 = Button(root, width = 20, text = "게임 종료", overrelief="solid", command = quit)
button1.pack()

root.mainloop()