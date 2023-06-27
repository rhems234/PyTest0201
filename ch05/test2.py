from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *


# 함수정의
def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함.")


window = Tk()


def func_exit():
    window.quit()
    window.destroy()


mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

label1 = Label(window, text="입력된 값")
label1.pack()

value = askinteger("입력값 제목", "임의의 숫자 1 ~ 6", minvalue=1, maxvalue=6)
label1.configure(text=str(value))

window.mainloop()
