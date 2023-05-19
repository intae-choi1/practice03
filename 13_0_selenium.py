import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 드라이버 수동 설치 시
# service = Service('chromedriver.exe')
# browser = webdriver.Chrome(service=service)
 
 
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f"--user-agent={ua}")
service=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.get("http://naver.com")
# iframe으로 전환
# browser.switch_to.frame('mainFrame') 
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()
browser.back()
browser.forward()
browser.refresh()
browser.back()

elem = browser.find_element(By.ID, "query")
elem.send_keys("하이")
# elem.send_keys(Keys.ENTER) # 엔터쳐도 검색이 된다
elem = browser.find_element(By.XPATH, '//*[@id="search-btn"]') # xpath로 검색버튼을 클릭해보자
elem.click()

elem = browser.find_elements(By.TAG_NAME, "a")
print(elem)
for e in elem:
    e.get_attribute("href")
    
time.sleep(1)
