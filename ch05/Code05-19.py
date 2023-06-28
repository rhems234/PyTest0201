inFp = None
inList = ""

inFp = open("C:/Temp/test.txt", "r", encoding="utf-8")
# inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
print(inList)

inFp.close()
