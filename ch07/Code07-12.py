from tkinter import *
import xlsxwriter

window = Tk()
photo = PhotoImage(file="C:/CookAnalysis/GIF/pic7.gif")
h = photo.height()
w = photo.width()

photoR = [[0 for _ in range(h)] for _ in range(w)]
photoG = [[0 for _ in range(h)] for _ in range(w)]
photoB = [[0 for _ in range(h)] for _ in range(w)]

for i in range(w):
    for k in range(h):
        r, g, b = photo.get(i, k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

workbook = xlsxwriter.Workbook("C:/CookAnalysis/Excel/pic7.xlsx")
# 워크 시트 3개
worksheetR = workbook.add_worksheet("photoR")
worksheetG = workbook.add_worksheet("photoG")
worksheetB = workbook.add_worksheet("photoB")

# 10진수 -> 16진수로 변환 하는 작업, 해당 HEX 결과의 값이 0xFF 형식인데.
# 만약, 2자리가 아니라, 1자리 이면, 앞에 0을 붙여서 출력함.
for i in range(w):
    for k in range(h):
        worksheetR.write(i, k, photoR[i][k])
        worksheetG.write(i, k, photoG[i][k])
        worksheetB.write(i, k, photoB[i][k])

workbook.close()
print("Save. OK~")
