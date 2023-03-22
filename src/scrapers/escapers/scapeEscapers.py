from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

from src.scrapers.escapers.constant import ESCAPERS_CAFE_LIST
from src.utils.chromeCustomDriver import get_chrome_driver
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling


def scrape_escapers_theme():
    theme_date_list = []
    now = datetime.now()
    driver = get_chrome_driver()

    for cafe in ESCAPERS_CAFE_LIST:
        driver.get(cafe.url)

        driver.implicitly_wait(0.5)

        for dateDelta in range(7):
            date = now + timedelta(dateDelta)
            date_str = date.strftime('%Y-%m-%d')
            if click_date(driver, date) is None:
                continue

            for theme in cafe.theme_list:
                if click_theme(driver, theme.theme_pk) is None:
                    continue
                theme_time_result = get_theme_time_result(driver)
                time_list = [element.get_attribute('value') for element in theme_time_result]
                print(time_list)


                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in ESCAPERS_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def click_date(driver, date):
    element = driver \
        .find_element(by=By.CSS_SELECTOR,
                      value=f"div[class*='datepicker--cell'][data-date='{date.day}']")
    print(element)
    driver.execute_script("arguments[0].click();", element)

    driver.implicitly_wait(0.5)
    return True


@try_except_handling
def click_theme(driver, theme_pk):
    element = driver \
        .find_element(by=By.CSS_SELECTOR,
                      value=f"#themeChoice > label > input[value='{theme_pk}']")
    driver.execute_script("arguments[0].click();", element)

    driver.implicitly_wait(0.5)
    return True

def get_theme_time_result(driver):
    return driver \
        .find_elements(by=By.CSS_SELECTOR, value="#themeTimeWrap > label:not(.active) > input").copy()

if __name__ == "__main__":
    scrape_escapers_theme()
