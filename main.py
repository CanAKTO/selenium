from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver=  webdriver.Chrome()
driver.maximize_window()

driver.get("https://google.com")
# time.sleep(2)
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.NAME,"q")))
# maksımum 4 saniye beklıcek bu sefer boşu boşuna beklemicek yukardaki kod
inpuelement = driver.find_element(By.NAME,"q")
time.sleep(2)
inpuelement.send_keys("can akto")
time.sleep(2)
button = driver.find_element(By.NAME,"btnK")
time.sleep(2)
button.click()

time.sleep(50)
