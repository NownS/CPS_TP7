## 게임을 켰을 때 실행되는 파일

import tkinter

root = tkinter.Tk()
root.title("Game")
root.geometry("200x200+200+100")
root.resizable(False, False)

label = tkinter.Label(root, text='\nGames\n')
label.pack()

button1 = tkinter.Button(root, height = 7, width = 20, text = "게임 종료", overrelief="solid", command = quit)
button1.pack()

root.mainloop()