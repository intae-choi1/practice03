import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=650305&weekday=sat"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 제목과 링크
# cartoons = soup.find_all("td", attrs={"class":"title"})
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = cartoon.a["href"]
#     print(title)
#     print("https://comic.naver.com" + link)

# 평점
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("평균점수:", total_rates/len(cartoons))