import time
from datetime import datetime, timedelta
from typing import Final, Dict

import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

KEY_ESCAPE_MAP: Final[Dict] = {
    "url": "https://keyescape.co.kr/web/home.php?go=rev.make",
    "cafeList": [
        {
            "locationForScrap": "강남점",
            "themeList": [
                {
                    "themeNameForScrap": "살랑살랑연구소",
                    "themeId": "136"
                },

                {
                    "themeNameForScrap": "월야애담-영문병행표기",
                    "themeId": "135"
                },

                {
                    "themeNameForScrap": "그카지말라캤자나",
                    "themeId": "137"
                }
            ]
        },
        {
            "locationForScrap": "홍대점",
            "themeList": [
                {
                    "themeNameForScrap": "고백",
                    "themeId": "457"
                },

                {
                    "themeNameForScrap": "삐릿-뽀",
                    "themeId": "458"
                },

                {
                    "themeNameForScrap": "홀리데이",
                    "themeId": "459"
                }
            ]
        },
        {
            "locationForScrap": "우주라이크",
            "themeList": [
                {
                    "themeNameForScrap": "US",
                    "themeId": "141"
                },

                {
                    "themeNameForScrap": "WANNA GO HOME",
                    "themeId": "142"
                }
            ]
        },
        {
            "locationForScrap": "강남 더오름",
            "themeList": [
                {
                    "themeNameForScrap": "네드",
                    "themeId": "138"
                },

                {
                    "themeNameForScrap": "엔제리오",
                    "themeId": "139"
                }
            ]
        },
        {
            "locationForScrap": "부산점",
            "themeList": [
                {
                    "themeNameForScrap": "정신병동",
                    "themeId": "1542"
                },

                {
                    "themeNameForScrap": "파파라치",
                    "themeId": "1541"
                },

                {
                    "themeNameForScrap": "난쟁이의 장난-영문병행표기",
                    "themeId": "1540"
                },
                {
                    "themeNameForScrap": "셜록 죽음의 전화",
                    "themeId": "1543"
                },
                {
                    "themeNameForScrap": "신비의숲 고대마법의 비밀",
                    "themeId": "1544"
                }
            ]
        },
        {
            "locationForScrap": "전주점",
            "themeList": [
                {
                    "themeNameForScrap": "난쟁이의 장난-영문병행표기",
                    "themeId": "1653"
                },
                {
                    "themeNameForScrap": "혜화잡화점",
                    "themeId": "1654"
                },
                {
                    "themeNameForScrap": "월야애담-영문병행표기",
                    "themeId": "1655"
                },
                {
                    "themeNameForScrap": "사라진 목격자",
                    "themeId": "1657"
                },
                {
                    "themeNameForScrap": "살랑살랑연구소",
                    "themeId": "1656"
                }
            ]
        }
    ]
}


def scrap_key_escape_theme():
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
    # 방탈출 매장 URL
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(KEY_ESCAPE_MAP["url"])

    driver.implicitly_wait(3)

    data_for_insert_db = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        try:
            driver.find_element(by=By.ID, value="calendar_data") \
                .find_element(by=By.XPATH,
                              value=f"//table/tbody/tr/td/a{'/u' if dateDelta == 0 else ''}[text()='{date.day}']") \
                .click()
            driver.implicitly_wait(10)
        except:
            continue

        for cafe in KEY_ESCAPE_MAP.get("cafeList"):
            try:
                driver.find_element(by=By.ID, value="zizum_data") \
                    .find_element(by=By.XPATH, value=f"//a/li[text()='{cafe['locationForScrap']}']") \
                    .click()
                driver.implicitly_wait(10)
            except:
                continue

            for theme in cafe.get("themeList"):
                try:
                    driver.find_element(by=By.ID, value="theme_data") \
                        .find_element(by=By.XPATH, value=f"//a/li[text()='{theme['themeNameForScrap']}']") \
                        .click()

                    time.sleep(0.5)
                    driver.implicitly_wait(5)

                    result = driver.find_element(by=By.ID, value="theme_time_data").find_elements(by=By.CLASS_NAME,
                                                                                                  value="possible").copy()

                    textList = map((lambda element: element.text), result)

                    for text in textList:
                        date_time = date_str + " " + text
                        line = (date_time, theme["themeId"])
                        data_for_insert_db.append(line)
                except:
                    print("error", theme)

    print(data_for_insert_db)

    theme_id_list = []

    for cafe in KEY_ESCAPE_MAP["cafeList"]:
        for theme in cafe["themeList"]:
            theme_id_list.append(theme["themeId"])

    cur.execute("DELETE FROM theme_date WHERE theme_id IN (" + ','.join(str(e) for e in theme_id_list) + ")")
    cur.executemany("INSERT IGNORE INTO theme_date(theme_time,theme_id, is_open) VALUES(?, ?, 1)", data_for_insert_db)
    connection.commit()
