from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

from src.scrapers.zeroWorld.constant import ZERO_WORLD_CAFE_LIST
from src.utils.chromeCustomDriver import get_chrome_driver
from src.utils.database import update_theme_date, make_theme_date
from src.utils.util import try_except_handling


def scrape_zero_world_theme():
    driver = get_chrome_driver()

    theme_date_list = []
    now = datetime.now()

    for cafe in ZERO_WORLD_CAFE_LIST:
        driver.get(cafe.url)

        driver.implicitly_wait(1)
        for dateDelta in range(7):
            date = now + timedelta(dateDelta)
            date_str = date.strftime('%Y-%m-%d')

            if click_date(driver, date) is None:
                continue

            for theme in cafe.theme_list:
                if click_theme(driver, theme) is None:
                    continue

                theme_time_result = get_theme_time_result(driver)
                time_list = [element.text for element in theme_time_result]
                print(time_list)

                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in ZERO_WORLD_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def click_date(driver, date) -> bool:
    date_element = get_date_element(driver, date)
    driver.execute_script("arguments[0].click();", date_element)
    driver.implicitly_wait(0.5)
    return True


@try_except_handling
def click_theme(driver, theme) -> bool:
    theme_element = get_theme_element(driver, theme)
    driver.execute_script("arguments[0].click();", theme_element)
    return True


def get_theme_time_result(driver):
    return driver \
        .find_element(by=By.ID, value="themeTimeWrap") \
        .find_elements(by=By.XPATH, value="./label[not(contains(@class, 'active'))]/span").copy()


def get_date_element(driver, date):
    return driver.find_element(by=By.ID, value="calendar") \
        .find_element(by=By.XPATH, value=f".//div/div/div/div/div[2]/div[text()='{date.day}']")


def get_theme_element(driver, theme):
    return driver.find_element(by=By.ID, value="themeChoice") \
        .find_element(by=By.XPATH, value=f"//label/span[text()='{theme.theme_name}']//..")


if __name__ == '__main__':
    scrape_zero_world_theme()
