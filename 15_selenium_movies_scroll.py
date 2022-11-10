import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
service=Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")
# 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height: break # 스크롤 내리기 전이랑 후랑 높이가 같으면 끝까지 온 거다
    prev_height = curr_height
print("스크롤 완료")

# 셀레니움으로 동작시킨 browser(html)을 가지고 파싱해보자
import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"title": re.compile(".*")})
    # print(title.attrs['title'])
    # print(title['title']) # 둘다 됨
    print(title)