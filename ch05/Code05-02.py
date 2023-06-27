from tkinter import *
from tkinter import messagebox


# 함수정의
# def myFunc():
#     messagebox.showinfo("다이얼 로그 테스트 창입니다.", "다이얼로그 내용창입니다.")


def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("다이얼 로그 테스트 창입니다.", "체크버튼해제.")
    else:
        messagebox.showinfo("다이얼 로그 테스트 창입니다.", "체크버튼선택.")


window = Tk()
window.title("윈도우 창 연습")
window.geometry("500x400")
window.resizable(width=True, height=True)

label1 = Label(window, text="문자열1")
label2 = Label(window, text="문자열2", font=("궁서체", 30), fg="red")
label3 = Label(window, text="문자열3", bg="magenta", width=100, height=100, anchor=SE)

photo = PhotoImage(file="gif/dog.gif")
photo2 = PhotoImage(file="gif/cat.gif")
photo3 = PhotoImage(file="gif/cat2.gif")

labelImg = Label(window, image=photo)
labelImg2 = Label(window, image=photo2)
labelImg3 = Label(window, image=photo3)

button1 = Button(window, text="종료버튼", fg="red", command=quit)
button1.pack()
button2 = Button(window, image=photo3, command=myFunc)
button2.pack()

chk = IntVar()
cb1 = Checkbutton(window, text="체크해주세요.", variable=chk, command=myFunc)
cb1.pack()

# 정수 값을 생성해주는 함수
var = IntVar()
rb1 = Radiobutton(window, text="라디오1", variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text="라디오2", variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text="라디오3", variable=var, value=3, command=myFunc)

resultLabel = Label(window, text="선택한 라디오 버튼 : ", fg="red")
rb1.pack()
rb2.pack()
rb3.pack()
resultLabel.pack()

# labelImg.pack(side=LEFT)
# labelImg2.pack(side=RIGHT)
# labelImg3.pack()

# label1.pack()
# label2.pack()
# label3.pack()

window.mainloop()
