import time
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

from src.scrapers.keyEscape.constant import KEY_ESCAPE_CAFE_LIST, KEY_ESCAPE_URL
from src.utils.chromeCustomDriver import get_chrome_driver
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling


def scrape_theme_date():
    driver = get_chrome_driver()

    driver.get(KEY_ESCAPE_URL)

    driver.implicitly_wait(3)

    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        if click_date(driver, date.day, dateDelta == 0) is None:
            continue

        for cafe in KEY_ESCAPE_CAFE_LIST:
            if click_cafe(driver, cafe) is None:
                continue

            for theme in cafe.theme_list:
                if click_theme(driver, theme) is None:
                    continue

                theme_time_result = get_theme_time_result(driver)
                time_list = [element.text for element in theme_time_result]

                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'scarping {date_str} {cafe.location} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in KEY_ESCAPE_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_date_list, theme_id_list)


@try_except_handling
def click_date(driver, day, is_today) -> bool:
    date_element = get_date_element(driver, day, is_today)
    driver.execute_script("arguments[0].click();", date_element)
    driver.implicitly_wait(10)
    return True


@try_except_handling
def click_cafe(driver, cafe) -> bool:
    cafe_element = get_cafe_element(driver, cafe)
    driver.execute_script("arguments[0].click();", cafe_element)
    driver.implicitly_wait(10)
    return True


@try_except_handling
def click_theme(driver, theme) -> bool:
    theme_element = get_theme_element(driver, theme)
    driver.execute_script("arguments[0].click();", theme_element)
    time.sleep(0.5)
    driver.implicitly_wait(10)
    return True


def get_theme_time_result(driver):
    return driver.find_element(by=By.ID, value="theme_time_data") \
        .find_elements(by=By.CLASS_NAME, value="possible").copy()


def get_date_element(driver, day, is_today):
    return driver.find_element(by=By.ID, value="calendar_data") \
        .find_element(by=By.XPATH,
                      value=f".//table/tbody/tr/td/a{'/u' if is_today else ''}[text()='{day}']//..")


def get_cafe_element(driver, cafe) -> bool:
    return driver.find_element(by=By.ID, value="zizum_data") \
        .find_element(by=By.XPATH, value=f".//a/li[text()='{cafe.location}']//..")


def get_theme_element(driver, theme):
    return driver.find_element(by=By.ID, value="theme_data") \
        .find_element(by=By.XPATH, value=f".//a/li[text()='{theme.theme_name}']//..")


scrape_theme_date()