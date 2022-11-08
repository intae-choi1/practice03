import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 드라이버 수동 설치 시
# service = Service('chromedriver.exe')
# browser = webdriver.Chrome(service=service)

service=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()
browser.back()
browser.forward()
browser.refresh()
browser.back()

elem = browser.find_element(By.ID, "query")
elem.send_keys("하이")
# elem.send_keys(Keys.ENTER) # 엔터쳐도 검색이 된다
elem = browser.find_element(By.XPATH, '//*[@id="search_btn"]') # xpath로 검색버튼을 클릭해보자
elem.click()

elem = browser.find_elements(By.TAG_NAME, "a")
print(elem)
for e in elem:
    e.get_attribute("href")
    
time.sleep(1)
