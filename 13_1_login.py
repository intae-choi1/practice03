import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

browser.find_element(By.ID, "id").send_keys("my_id")
browser.find_element(By.ID, "pw").send_keys("my_pass")
browser.find_element(By.ID, "log.login").click()


browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("z")

time.sleep(1)