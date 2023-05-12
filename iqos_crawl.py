import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv


def wait_elem(browser, x_path, delay=10):
    wait_for = EC.presence_of_element_located((By.XPATH, x_path))
    ret = WebDriverWait(browser, delay).until(wait_for)
    return ret


def get_elem(browser, x_path):
    # x_path로 find
    return browser.find_element(By.XPATH, x_path)
    
# # 드라이버 수동 설치 시
# # service = Service('chromedriver.exe')
# # browser = webdriver.Chrome(service=service)

service=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# 아이코스 일루마 상품 페이지
browser.get("https://kr.iqos.com/products/iqos-device/iluma-kit")
# 나이 선택창 대기, 클릭 (성인 확인)
wait_elem(browser, '//*[@id="age"]/option[55]').click()
# 확인 클릭
get_elem(browser, '//*[@id="sav-validation-form"]/div[2]/div/button').click()
# 제품 리뷰 창 클릭 
element = get_elem(browser, '//*[@id="tab-label-reviews"]')
browser.execute_script("arguments[0].click();", element)

# 리뷰가 1000건이 나올때 까지 더보기 클릭
while len(browser.find_elements(By.CSS_SELECTOR, 'div .single-review')) < 1000:
    element = get_elem(browser, '//*[@id="product-review-main"]/div[2]/div[6]/div/div')
    browser.execute_script("arguments[0].click();", element)
    time.sleep(0.3)

# html 파일을 직접 보면서 작업하기 위해 저장
with open("iqos_crawl.html", "w", encoding="utf-8") as f:
    f.write(browser.page_source)

# HTML 파일 읽고 문자열 리턴
with open('iqos_crawl.html', 'r', encoding='utf-8') as f:
    page = f.read()

soup = BeautifulSoup(page, 'html.parser')  # Soup 객체 생성
reviews = soup.select('div .single-review')

style_pattern = re.compile('(?<=width: )\d+') # style attr에서 width 파싱
sub_pattern = re.compile('\n\s*') # 리뷰 텍스트 줄바꿈

# 스크래핑 데이터 저장 파일
filename = "iqos_crawl_data.csv"
with open(filename, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f) 
    # 컬럼 명
    columns = "site, reviewer, date created, category, product name, rating, title, review_content, lang".split(', ')
    writer.writerow(columns)

    for i, review in enumerate(reviews):
        tmp = review.select('div .produce-score-date > span')
        reviewer = tmp[0].string                                                # 작성자
        date_created = tmp[2].string                                            # 작성일자
        title = review.select_one('div .product-name').string.strip()           # 제목
        rating_str = review.select_one('div .fill-ratings').attrs.get('style')  
        m = style_pattern.search(rating_str)
        rating = int(m.group())//20                                             # 별점
        review_content = review.select_one('div .review-content').get_text().strip()
        review_content = sub_pattern.sub(' ', review_content)                           # 리뷰 본문
        
        # [site, reviewer, date created, category, product name, rating, title, review_content, lang]
        item = ['IQOS홈페이지', reviewer, date_created, '기기', '아이코스 일루마', rating, title, review_content, 'ko']
        writer.writerow(item)

