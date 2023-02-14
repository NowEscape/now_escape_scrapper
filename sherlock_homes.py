from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timedelta

import mysql.connector

# 데이터베이스
# connection = mysql.connector.connect(user="root", password="jholnw0904", host="127.0.0.1", charset="utf8mb4", db="test")
# cur = connection.cursor(prepared=True)

# 현재 날짜
now = datetime.now()
now_date = now.strftime('%Y-%m-%d')

# 방탈출 매장 URL
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://sherlock-holmes.co.kr/reservation/"
driver.get(url)

driver.find_element(by=By.ID, value="selectArea").find_element(by=By.XPATH, value="//option[text()='서울특별시']").click()

driver.implicitly_wait(2)

driver.find_element(by=By.ID, value="selectBranch").find_element(by=By.XPATH, value="//option[text()='노원점']").click()

driver.implicitly_wait(2)

driver.find_element(by=By.ID, value="res_date").click()

driver.implicitly_wait(2)

driver.find_element(by=By.ID, value="ui-datepicker-div").find_element(by=By.XPATH,
                                                                      value="//table/tbody/tr/td/a[text()='16']").click()

time.sleep(2)

result = driver.find_element(by=By.ID, value="theme_ac_279").find_elements(by=By.XPATH,
                                                                           value="div[2]/div/a/p[1]").copy()
textList = map((lambda element: element.text), result)
data = []
for text in textList:
    date_time = now_date + " " + text
    theme = "549"
    line = (date_time, theme)
    data.append(line)
print(data)

# cur.executemany("INSERT INTO theme_date(theme_time,theme_id, is_open) VALUES(?, ?, 1)", data)
# connection.commit()
