import csv
import requests
from bs4 import BeautifulSoup

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	상장주식수	시가총액	매출액	외국인비율	PER	ROE	토론실".split('\t')
writer.writerow(title)

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

for page in range(1, 5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: continue # 의미없는 데이터 skip
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)
    