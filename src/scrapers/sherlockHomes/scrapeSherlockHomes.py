import time
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

from src.scrapers.sherlockHomes.constant import SHERLOCK_HOMES_CAFE_LIST, SHERLOCK_URL
from src.utils.chromeCustomDriver import get_chrome_driver
from src.utils.database import update_theme_date, make_theme_date
from src.utils.util import try_except_handling


def scrap_sherlock_homes_theme():
    driver = get_chrome_driver()
    driver.get(SHERLOCK_URL)
    driver.implicitly_wait(3)

    theme_date_list = []
    now = datetime.now()

    for cafe in SHERLOCK_HOMES_CAFE_LIST:
        if click_cafe(driver, cafe) is None:
            continue

        for dateDelta in range(7):
            date = now + timedelta(dateDelta)
            date_str = date.strftime('%Y-%m-%d')
            if click_date(driver, date) is None:
                continue

            for theme in cafe.theme_list:
                theme_time_result = get_theme_time_result(driver, theme.theme_name)
                time_list = [element.text for element in theme_time_result]

                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scarping {date_str} {cafe.region1} {cafe.region2} {theme.theme_name}')


    theme_id_list = [theme.theme_id for cafe in SHERLOCK_HOMES_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_date_list, theme_id_list)


@try_except_handling
def click_cafe(driver, cafe) -> bool:
    driver.find_element(by=By.ID, value="selectArea").find_element(by=By.XPATH,
                                                                   value=f"//option[text()='{cafe.region1}']").click()
    driver.implicitly_wait(2)

    driver.find_element(by=By.ID, value="selectBranch").find_element(by=By.XPATH,
                                                                     value=f"option[text()='{cafe.region2}']").click()

    driver.implicitly_wait(2)
    return True


@try_except_handling
def click_date(driver, date) -> bool:
    driver.find_element(by=By.ID, value="res_date").click()

    driver.implicitly_wait(1)
    element = driver.find_element(by=By.ID, value="ui-datepicker-div") \
        .find_element(by=By.XPATH, value=f"table/tbody/tr/td/a[text()='{date.day}']")
    driver.execute_script("arguments[0].click();", element)

    time.sleep(1)
    return True


def get_theme_time_result(driver, theme_name):
    return driver.find_element(by=By.XPATH, value=f"//h2[contains(text(),'{theme_name}')]") \
        .find_elements(by=By.XPATH, value="../div[2]/div/a/p[1]").copy()


scrap_sherlock_homes_theme()
