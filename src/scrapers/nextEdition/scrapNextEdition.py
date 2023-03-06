import time
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

from src.scrapers.nextEdition.constant import NEXT_EDITION_CAFE_LIST
from src.utils.chromeCustomDriver import get_chrome_driver
from src.utils.database import update_theme_date, make_theme_date
from src.utils.util import try_except_handling


def scrap_next_edition_theme():
    driver = get_chrome_driver()

    theme_date_list = []
    now = datetime.now()

    for cafe in NEXT_EDITION_CAFE_LIST:
        driver.get(cafe.url)

        driver.implicitly_wait(3)

        for dateDelta in range(7):
            date = now + timedelta(dateDelta)
            date_str = date.strftime('%Y-%m-%d')
            if click_date(driver, date) is None:
                continue

            for theme in cafe.theme_list:
                theme_time_result = get_theme_time_result(driver, theme.theme_name)
                time_list = [element.text for element in theme_time_result]

                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scarping {date_str} {cafe.url} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in NEXT_EDITION_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_date_list, theme_id_list)


@try_except_handling
def click_date(driver, date) -> bool:
    driver.find_element(by=By.ID, value="datepicker").click()

    driver.implicitly_wait(1)

    element = driver.find_element(by=By.ID, value="ui-datepicker-div") \
        .find_element(by=By.XPATH, value=f"table/tbody/tr/td/a[text()='{date.day}']")
    driver.execute_script("arguments[0].click();", element)

    time.sleep(1)
    return True


def get_theme_time_result(driver, theme_name):
    return driver.find_element(by=By.XPATH, value=f"//h2[contains(text(),'{theme_name}')]")\
        .find_elements(by=By.XPATH, value="../div[contains(@class,'res-true')]/span[1]").copy()


scrap_next_edition_theme()
