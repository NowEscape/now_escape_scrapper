import urllib.request
from datetime import datetime, timedelta

import bs4
from bs4 import BeautifulSoup

from src.scrapers.codeK.constant import CODE_K_CAFE_LIST, CODE_K_URL
from src.utils.database import update_theme_date, make_theme_date
from src.utils.dateUtil import time_pattern


def scrape_code_k():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in CODE_K_CAFE_LIST:
            bs_object = get_bs_object(CODE_K_URL.format(R_JIJEM=cafe.r_jijem, DATE=date_str))

            for theme in cafe.theme_list:
                time_list = scrape_code_k_theme_bs4(bs_object, theme.theme_name)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.name} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in CODE_K_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


def get_bs_object(url: str):
    html = urllib.request.urlopen(urllib.request.Request(url)).read()
    bs_object = BeautifulSoup(html, "lxml")
    return bs_object


def scrape_code_k_theme_bs4(bs_object: bs4.BeautifulSoup, theme_name: str):
    return [time_pattern.search(element.get_text()).group() for element in bs_object.select(
        f'#reser3 ul a:has(li:-soup-contains("{theme_name}")) +li div ul > a > li.timeOn')]


if __name__ == '__main__':
    scrape_code_k()
