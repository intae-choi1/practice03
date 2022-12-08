import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.headless = True
# headless chrome하면 user-agent가 바뀌니까 다시 정상으로 돌리기
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()
url = "https://flight.naver.com/"
browser.get(url) 

def wait_elem(browser, x_path, delay=10):
    wait_for = EC.presence_of_element_located((By.XPATH, x_path))
    ret = WebDriverWait(browser, delay).until(wait_for)
    return ret


wait_elem(browser, '//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[1]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//button[text()="가는 날"]').click()
time.sleep(1)
browser.find_elements(By.XPATH, '//b[text()="27"]')[0].click()
time.sleep(0.5)
browser.find_elements(By.XPATH, '//b[text()="28"]')[1].click()
browser.find_element(By.XPATH, '//b[text()="도착"]').click()

input_box = browser.find_element(By.CLASS_NAME, 'autocomplete_input__1vVkF')
input_box.send_keys("제주도")
input_box.send_keys(Keys.ENTER)
wait_elem(browser, '//i[text()="CJU"]', 5).click()

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# presence_of_element_located(찾을거, 엘레먼트)가 찾을 엘레먼트가
# 나올 때 까지 기다려달라
# 10초가 넘으면 에러가 남
elem = WebDriverWait(browser, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div/button')))
elem.click()
while True:
    a = input()
    if a == "b": break