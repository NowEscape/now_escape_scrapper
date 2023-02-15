import time
from datetime import datetime, timedelta
from typing import Final, Dict

import mysql.connector
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
                    "themeName": "황금 감옥 : 와캄",
                    "themeId": "548"
                },
                {
                    "themeName": "지프리트의 심장",
                    "themeId": "549"
                },
                {
                    "themeName": "스토커",
                    "themeId": "545"
                },
                {
                    "themeName": "파라오의 심판",
                    "themeId": "547"
                },
                {
                    "themeName": "도둑들",
                    "themeId": "544"
                },
                {
                    "themeName": "미녀와야수2",
                    "themeId": "546"
                }
            ]
        },
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "노량진점",
            "themeList": [
                {
                    "themeName": "어린왕자",
                    "themeId": "636"
                },
                {
                    "themeName": "빛과 그림자:화이트의죽음2",
                    "themeId": "637"
                },
                {
                    "themeName": "반하셨군요?",
                    "themeId": "638"
                },
                {
                    "themeName": "중고로운 평화나라",
                    "themeId": "639"
                }
            ]
        }
    ]
}

def get_theme_name(theme_name):
    return theme_name + " &nbsp;"

def scrap_sherlock_homes_theme():
    connection = mysql.connector.connect(user="nowadmin", password="Nowescape1!",
                                         host="nowescape-db.cvafksmpbb8z.ap-northeast-2.rds.amazonaws.com",
                                         charset="utf8mb4",
                                         db="now_escape")
    cur = connection.cursor(prepared=True)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    # linux 환경에서 필요한 option
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # 방탈출 매장 URL
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    driver.get(SHERLOCK_HOMES_MAP["url"])

    driver.implicitly_wait(3)

    data_for_insert_db = []
    now = datetime.now()

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

            time.sleep(1)

            for theme in cafe["themeList"]:
                result = driver\
                    .find_element(by=By.XPATH, value=f"//h2[contains(text(),'{theme['themeName']}')]")\
                    .find_elements(by=By.XPATH, value="../div[2]/div/a/p[1]").copy()
                textList = map((lambda element: element.text), result)
                for text in textList:
                    date_time = date_str + " " + text
                    line = (date_time, theme["themeId"])
                    data_for_insert_db.append(line)

    print(data_for_insert_db)


    theme_id_list = []

    for cafe in SHERLOCK_HOMES_MAP["cafeList"]:
        for theme in cafe["themeList"]:
            theme_id_list.append(theme["themeId"])

    cur.execute("DELETE FROM theme_date WHERE theme_id IN (" + ','.join(str(e) for e in theme_id_list) + ")")
    cur.executemany("INSERT IGNORE INTO theme_date(theme_time,theme_id, is_open) VALUES(?, ?, 1)", data_for_insert_db)
    connection.commit()

scrap_sherlock_homes_theme()
