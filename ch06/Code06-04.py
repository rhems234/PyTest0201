with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp:
    with open("C:/CookAnalysis/CSV/new_singer3.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        header_list = header.split(",")
        header_str = ",".join(map(str, header_list))
        outFp.write(header_str + "\n")
        # 2번째 행부터 데이터 쓰기 작업.
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(",")  # 2번째 행의 전체 데이터.
            row_list[-1] = row_list[-1].replace(".", "/")
            height_str = "{0:.2f}".format(int(row_list[-2]))
            row_list[-2] = height_str
            row_str = ",".join(map(str, row_list))
            outFp.write(row_str + "\n")

print("Save. OK~")
