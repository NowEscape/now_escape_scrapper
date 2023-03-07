import re
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

from src.scrapers.danPyeonSeon.constant import DPS_THEME_LIST, DPS_URL
from src.utils.chromeCustomDriver import get_chrome_driver
from src.utils.database import update_theme_date, make_theme_date
from src.utils.util import try_except_handling


def scrap_dps_theme():
    driver = get_chrome_driver()

    driver.get(DPS_URL)

    driver.implicitly_wait(1)

    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%-m-%-d')

        for theme in DPS_THEME_LIST:
            theme_time_result = get_theme_time_result(driver, date_str, theme.theme_name)
            time_list = [element.text for element in theme_time_result]
            #요기서 자르면 되지 않을까
            print(time_list)
            theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
            print(f'{datetime.now()} scarping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for theme in DPS_THEME_LIST]

    update_theme_date(theme_id_list, theme_date_list)


def get_theme_time_result(driver, date_str, theme_name):
    return driver.find_elements\
     (by=By.XPATH, value=f"//td[contains(@data-date,'{date_str}')]/div/div[3]/"
        f"div[contains(@class, 'booking_list  hide_badge')]/a/div/div/span[1][contains(text(), '{theme_name}')]").copy()


scrap_dps_theme()
