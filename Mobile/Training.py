## 운동 앱을 켰을 때 실행되는 파일

import tkinter

music = tkinter.Tk()
music.title("Training")
music.geometry("500x200+100+100")
music.resizable(False, False)

label = tkinter.Label(music, text='\nTraining\n')
label.pack()

button1 = tkinter.Button(music, width = 20, text = "운동 플레이어 종료", overrelief="solid", command = quit)
button1.pack()

music.mainloop()