from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

path = "C:\\Users\\user\\Desktop\eset_bot\\chromedriver.exe"
googleUrl = "https://uzsoft.uz/baza-obnovlenie-eset-nod32-tas-ix/"

driver = webdriver.Chrome(executable_path=path)
driver.get(googleUrl)




DownloadButton = driver.find_element(By.XPATH, '//*[@id="post-40729"]/div[2]/div/section[1]/div/div[1]/div/div/div/div/div/div[2]/a').click()
time.sleep(3600)
driver.quit()
