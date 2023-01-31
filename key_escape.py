from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timedelta

import mysql.connector

#데이터베이스
connection = mysql.connector.connect(user="root", password="jholnw0904", host="127.0.0.1", charset="utf8mb4", db="test")
cur = connection.cursor(prepared=True)

#현재 날짜
now = datetime.now()
now_date = (now + timedelta(days=1)).strftime('%Y-%m-%d')

#방탈출 매장 URL
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://keyescape.co.kr/web/home.php?go=rev.make"
driver.get(url)

#지점명 가져오기
zizum_list = driver.find_element(by=By.ID, value="zizum_data").find_elements(by=By.XPATH, value="//a/li")
zizum_name_list = []
for zizum in zizum_list:
    zizum_name_list.append(zizum.text)
zizum_name_list = zizum_name_list[:7] #오픈안한테마들 자르기

#스크래핑시작
for zizum in zizum_name_list:
    zizum_name = zizum
    driver.find_element(by=By.ID, value="zizum_data").find_element(by=By.XPATH, value=f"//a/li[text()='{zizum_name}']").click()

    driver.implicitly_wait(50)

    driver.find_element(by=By.ID, value="calendar_data").find_element(by=By.XPATH,value="//table/tbody/tr/td/a[text()='31']").click()

    driver.implicitly_wait(10)
    theme_list = driver.find_element(by=By.ID, value="theme_data").find_elements(by=By.XPATH, value="//a/li")
    theme_name_list = []
    for theme in theme_list:
        theme_name_list.append(theme.text)
    print(theme_name_list)


# driver.find_element(by=By.ID, value="calendar_data").find_element(by=By.XPATH, value="//table/tbody/tr/td/a[text()='31']").click()
#
# driver.implicitly_wait(3)
#
# driver.find_element(by=By.ID, value="theme_data").find_element(by=By.XPATH, value="//a/li[text()='살랑살랑연구소']").click()
#
# driver.implicitly_wait(10)
#
# result = driver.find_element(by=By.ID, value="theme_time_data").find_elements(by=By.CLASS_NAME, value="possible").copy()
#
# textList = map((lambda element: element.text), result)
# data = []
# for text in textList:
#     date_time = now_date + " " + text
#     theme = "1"
#     line = (date_time, theme)
#     data.append(line)
# print(data)
#
# cur.executemany("INSERT INTO theme_date(theme_date,theme_id) VALUES(?, ?)", data)
# connection.commit()