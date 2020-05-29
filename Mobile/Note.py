## 노트를 켰을 때 실행되는 파일

import tkinter

note = tkinter.Tk()
note.title("Note")
note.geometry("500x200+100+100")
note.resizable(False, False)

label = tkinter.Label(note, text='\nNote\n')
label.pack()

button1 = tkinter.Button(note, width = 20, text = "노트 종료", overrelief="solid", command = quit)
button1.pack()

note.mainloop()