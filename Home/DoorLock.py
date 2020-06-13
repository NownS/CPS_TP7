## 도어락을 켰을 때 실행되는 파일

import tkinter

root = tkinter.Tk()
root.title("DoorLock")
root.geometry("500x200+100+100")
root.resizable(False, False)

label = tkinter.Label(root, text='\nDoorLock\n')
label.pack()

button1 = tkinter.Button(root, width = 20, text = "컨트롤러 종료", overrelief="solid", command = quit)
button1.pack()

root.mainloop()