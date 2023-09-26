from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
count = 0

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://atilsamancioglu.com")
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")))
blog_page=driver.find_element(By.XPATH,"/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"button")))
read_button=driver.find_element(By.CLASS_NAME,"button")
read_button.click()
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/aside[4]")))
article_list = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/aside[4]")
for a in  article_list.text.splitlines():
    # dizi oldu alt alta yazılı stringi splitlines() ile satır olarak bölebiliriz
    count=count+1
print(count-1)
# veya şöyle
b=len(article_list.text.splitlines())

print(f"bu kadar satır var {b}")



while True:
    continue
