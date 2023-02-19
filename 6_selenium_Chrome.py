import time
from selenium import webdriver
from selenium.webdriver.common.by import By


web = webdriver.Chrome()
web.get("https://www.lagou.com/")
time.sleep(60)
xpath = By.XPATH("/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/p[1]/a")
element = web.find_element(by=xpath)

web.quit()
