## 세탁기를 켰을 때 실행되는 파일

import tkinter

root = tkinter.Tk()
root.title("Washer")
root.geometry("200x200+1200+600")
root.resizable(False, False)

label = tkinter.Label(root, text='\nWasher\n')
label.pack()

button1 = tkinter.Button(root, height = 7, width = 20, text = "컨트롤러 종료", overrelief="solid", command = quit)
button1.pack()

root.mainloop()