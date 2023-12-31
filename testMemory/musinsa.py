import pymysql
import csv
import time
import schedule
from bs4 import BeautifulSoup
from urllib.request import urlopen


def save_data_to_database():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="mysql",
        database="musinsa",
        charset="utf8",
    )

    cursor = con.cursor()

    html = urlopen("https://search.musinsa.com/category/001001")
    bsObject = BeautifulSoup(html, "html.parser")

    item_list = bsObject.find_all("li", {"class": "li_box"})

    brand = []
    name = []
    price = []
    number = []
    number_box = 0

    for index, item in enumerate(item_list):
        if index == 20:  # 20위까지만 처리
            break

        brand_box = item.findAll("p", {"class": "item_title"})
        if len(brand_box) == 1:
            brand.append(brand_box[0].get_text())
        elif len(brand_box) == 2:
            brand.append(brand_box[1].get_text())

        name_box = item.find("a", {"class": "img-block"}).get("title")
        name.append(name_box.strip())

        price_box = item.find("p", {"class": "price"})  # 수정된 부분
        if price_box:
            price.append(price_box.get_text().strip())
        else:
            price.append("가격 정보 없음")

        number_box += 1
        number.append(str(number_box))

    # 데이터를 CSV 파일로 저장
    filename = "musinsa.csv"
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "Brand", "Name", "Price"])  # 헤더 쓰기

        # 리스트들의 길이를 확인하고 짧은 길이에 맞춰서 반복
        min_length = min(len(number), len(brand), len(name), len(price))
        for i in range(min_length):
            writer.writerow([number[i], brand[i], name[i], price[i]])

            query = "INSERT INTO ranking (number, brand, name, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (number[i], brand[i], name[i], price[i]))

    con.commit()
    con.close()

    print("데이터가 저장되었습니다.")


schedule.every(1).minutes.do(save_data_to_database)

while True:
    schedule.run_pending()
    time.sleep(1)
