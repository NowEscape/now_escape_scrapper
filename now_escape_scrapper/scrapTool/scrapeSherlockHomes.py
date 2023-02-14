import time
from datetime import datetime, timedelta
from typing import Final, Dict

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


SHERLOCK_HOMES_MAP: Final[Dict] = {
    "url": "https://sherlock-holmes.co.kr/reservation",
    "cafeList": [
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "노원점",
            "themeList": [
                {
                    "themeIdForScrap": "theme_ac_289",
                    "themeId": "548"
                },
            ]
        }
    ]
}


def scrap_sherlock_homes_theme():
    # connection = mysql.connector.connect(user="nowadmin", password="Nowescape1!",
    #                                      host="nowescape-db.cvafksmpbb8z.ap-northeast-2.rds.amazonaws.com",
    #                                      charset="utf8mb4",
    #                                      db="now_escape")
    # cur = connection.cursor(prepared=True)
    now = datetime.now()

    # 방탈출 매장 URL
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(SHERLOCK_HOMES_MAP["url"])

    driver.implicitly_wait(3)

    data_for_insert_db = []
    for cafe in SHERLOCK_HOMES_MAP["cafeList"]:
        driver.find_element(by=By.ID, value="selectArea").find_element(by=By.XPATH,
                                                                       value=f"//option[text()='{cafe['region1ForScrap']}']").click()
        driver.implicitly_wait(2)

        driver.find_element(by=By.ID, value="selectBranch").find_element(by=By.XPATH,
                                                                         value=f"option[text()='{cafe['region2ForScrap']}']").click()

        driver.implicitly_wait(2)

        driver.find_element(by=By.ID, value="res_date").click()

        driver.implicitly_wait(2)

        for dateDelta in range(7):
            date = now + timedelta(dateDelta)
            date_str = date.strftime('%Y-%m-%d')
            element = driver.find_element(by=By.ID, value="ui-datepicker-div") \
                .find_element(by=By.XPATH, value=f"table/tbody/tr/td/a[text()='{date.day}']")
            driver.execute_script("arguments[0].click();", element)

            time.sleep(2)

            for theme in cafe["themeList"]:
                result = driver.find_element(by=By.ID, value=theme["themeIdForScrap"])\
                    .find_elements(by=By.XPATH, value="div[2]/div/a/p[1]").copy()
                textList = map((lambda element: element.text), result)
                for text in textList:
                    date_time = date_str + " " + text
                    line = (date_time, theme["themeId"])
                    data_for_insert_db.append(line)

    print(data_for_insert_db)


scrap_sherlock_homes_theme()
