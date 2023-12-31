import csv
import time
import datetime
import bs4
import urllib.request
import ssl

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

csvName = "CSV/sokcho_weather.csv_0629"
with open(csvName, "w", newline="") as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(["연월일", "시분초", "온도", "습도", "강수량", "풍향"])

nateUrl = "https://news.nate.com/weather?areaCode=11D20401"
while True:
    htmlObject = urllib.request.urlopen(nateUrl, context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, "html.parser")

    # tag 오늘의 날씨 정보, 부모 태그
    tag = bsObject.find("div", {"class": "right_today"})
    # tag의 하위에 클래스들 중에서 celsius()
    temper = tag.find("p", {"class": "celsius"}).text
    humi = tag.find("p", {"class": "humidity"}).text
    rain = tag.find("p", {"class": "rainfall"}).text
    wind = tag.find("p", {"class": "wind"}).text

    now = datetime.datetime.now()
    yymmdd = now.strftime("%Y-%m-%d")
    hhmmss = now.strftime("%H:%M:%S")

    weather_list = [yymmdd, hhmmss, temper, humi, rain, wind]
    with open(csvName, "a", newline="") as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(weather_list)
        print(weather_list)

    time.sleep(60)
