## 동영상 앱을 켰을 때 실행되는 파일

import tkinter

music = tkinter.Tk()
music.title("Video")
music.geometry("200x200+200+600")
music.resizable(False, False)

label = tkinter.Label(music, text='\nVideo\n')
label.pack()

button1 = tkinter.Button(music, height = 7, width = 20, text = "영상 플레이어 종료", overrelief="solid", command = quit)
button1.pack()

music.mainloop()