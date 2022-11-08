import requests
import re
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
}
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

for item in items:
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("<광고 상품 제외>")
        continue
    name = item.find("div", attrs={"class": "name"}).get_text() # 제품 명
    price = item.find("strong", attrs={"class": "price-value"}).get_text() # 가격
    rating = item.find("em", attrs={"class": "rating"}) # 평점
    rating_total_count = item.find("span", attrs={"class": "rating-total-count"})# 평점 매긴 수
    
    if rating:
        rating = rating.get_text()
    else:
        rating = "평점 없음"
        
    if rating_total_count:
        rating_total_count = rating_total_count.get_text()
    else:
        rating_total_count = "평점 없음"
        
    print(f"{name.strip():<120}\t, {price}, {rating}, {rating_total_count}")
    
    

