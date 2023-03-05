import time
from datetime import datetime, timedelta
from typing import Final, Dict

from selenium.webdriver.common.by import By

from src.utils.chromeCustomDriver import get_chrome_driver
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling

KEY_ESCAPE_MAP: Final[Dict] = {
    "url": "https://keyescape.co.kr/web/home.php?go=rev.make",
    "cafeList": [
        {
            "locationForScrap": "강남점",
            "themeList": [
                {
                    "themeNameForScrap": "살랑살랑연구소",
                    "theme_id": "136"
                },

                {
                    "themeNameForScrap": "월야애담-영문병행표기",
                    "theme_id": "135"
                },

                {
                    "themeNameForScrap": "그카지말라캤자나",
                    "theme_id": "137"
                }
            ]
        },
        {
            "locationForScrap": "홍대점",
            "themeList": [
                {
                    "themeNameForScrap": "고백",
                    "theme_id": "457"
                },

                {
                    "themeNameForScrap": "삐릿-뽀",
                    "theme_id": "458"
                },

                {
                    "themeNameForScrap": "홀리데이",
                    "theme_id": "459"
                }
            ]
        },
        {
            "locationForScrap": "우주라이크",
            "themeList": [
                {
                    "themeNameForScrap": "US",
                    "theme_id": "141"
                },

                {
                    "themeNameForScrap": "WANNA GO HOME",
                    "theme_id": "142"
                }
            ]
        },
        {
            "locationForScrap": "강남 더오름",
            "themeList": [
                {
                    "themeNameForScrap": "네드",
                    "theme_id": "138"
                },

                {
                    "themeNameForScrap": "엔제리오",
                    "theme_id": "139"
                }
            ]
        },
        {
            "locationForScrap": "부산점",
            "themeList": [
                {
                    "themeNameForScrap": "정신병동",
                    "theme_id": "1542"
                },

                {
                    "themeNameForScrap": "파파라치",
                    "theme_id": "1541"
                },

                {
                    "themeNameForScrap": "난쟁이의 장난-영문병행표기",
                    "theme_id": "1540"
                },
                {
                    "themeNameForScrap": "셜록 죽음의 전화",
                    "theme_id": "1543"
                },
                {
                    "themeNameForScrap": "신비의숲 고대마법의 비밀",
                    "theme_id": "1544"
                }
            ]
        },
        {
            "locationForScrap": "전주점",
            "themeList": [
                {
                    "themeNameForScrap": "난쟁이의 장난-영문병행표기",
                    "theme_id": "1653"
                },
                {
                    "themeNameForScrap": "혜화잡화점",
                    "theme_id": "1654"
                },
                {
                    "themeNameForScrap": "월야애담-영문병행표기",
                    "theme_id": "1655"
                },
                {
                    "themeNameForScrap": "사라진 목격자",
                    "theme_id": "1657"
                },
                {
                    "themeNameForScrap": "살랑살랑연구소",
                    "theme_id": "1656"
                }
            ]
        }
    ]
}


@try_except_handling
def click_date_element(driver, day, is_today):
    date_element = get_date_element(driver, day, is_today)
    driver.execute_script("arguments[0].click();", date_element)
    driver.implicitly_wait(10)
    return True


def get_date_element(driver, day, is_today):
    return driver.find_element(by=By.ID, value="calendar_data") \
        .find_element(by=By.XPATH,
                      value=f".//table/tbody/tr/td/a{'/u' if is_today else ''}[text()='{day}']//..")


@try_except_handling
def click_cafe_element(driver, cafe):
    cafe_element = get_cafe_element(driver, cafe)
    driver.execute_script("arguments[0].click();", cafe_element)
    driver.implicitly_wait(10)
    return True


def get_cafe_element(driver, cafe):
    return driver.find_element(by=By.ID, value="zizum_data") \
        .find_element(by=By.XPATH, value=f".//a/li[text()='{cafe['locationForScrap']}']//..")


@try_except_handling
def click_theme_element(driver, theme) -> bool:
    theme_element = get_theme_element(driver, theme)
    driver.execute_script("arguments[0].click();", theme_element)
    time.sleep(0.5)
    driver.implicitly_wait(10)
    return True


def get_theme_element(driver, theme):
    return driver.find_element(by=By.ID, value="theme_data") \
        .find_element(by=By.XPATH, value=f".//a/li[text()='{theme['themeNameForScrap']}']//..")


def get_theme_time_result(driver):
    return driver.find_element(by=By.ID, value="theme_time_data") \
        .find_elements(by=By.CLASS_NAME, value="possible").copy()


def scrap_key_escape_theme():
    driver = get_chrome_driver()

    driver.get(KEY_ESCAPE_MAP["url"])

    driver.implicitly_wait(3)

    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        if click_date_element(driver, date.day, dateDelta == 0) is None:
            continue

        for cafe in KEY_ESCAPE_MAP.get("cafeList"):
            if click_cafe_element(driver, cafe) is None:
                continue

            for theme in cafe.get("themeList"):
                if click_theme_element(driver, theme) is None:
                    continue

                theme_time_result = get_theme_time_result(driver)
                time_list = [element.text for element in theme_time_result]

                theme_date_list = theme_date_list + (make_theme_date(theme["theme_id"], date_str, time_list))
                print(f'scarping {date_str} {cafe["locationForScrap"]} {theme["themeNameForScrap"]}')

    print(theme_date_list)

    theme_id_list = [theme["theme_id"] for cafe in KEY_ESCAPE_MAP["cafeList"] for theme in cafe["themeList"]]

    update_theme_date(theme_date_list, theme_id_list)


scrap_key_escape_theme()
