import urllib
from datetime import datetime, timedelta

import bs4

from src.scrapers.escapeCity.constant import ESCAPE_CITY_CAFE_LIST, ESCAPE_CITY_URL
from src.utils.database import make_theme_date, update_theme_date
from bs4 import BeautifulSoup
from urllib.request import urlopen
from src.utils.dateUtil import time_pattern

from src.utils.util import try_except_handling


def scrape_escape_city_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in ESCAPE_CITY_CAFE_LIST:
            bs_object = get_bs_object(ESCAPE_CITY_URL, date_str, cafe.R_JIJEM)

            for theme in cafe.theme_list:
                time_list = scrape_escape_city_theme_bs4(bs_object, theme.theme_num)
                print(time_list)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.location} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in ESCAPE_CITY_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


def get_bs_object(url: str, date: str, R_JIJEM: str):
    details = urllib.parse.urlencode({'R_JIJEM': R_JIJEM, 'chois_date': date})
    details = details.encode('UTF-8')
    html = urllib.request.urlopen(urllib.request.Request(url, details)).read()
    bs_object = BeautifulSoup(html, "lxml")
    return bs_object


@try_except_handling
def scrape_escape_city_theme_bs4(bs_object: bs4.BeautifulSoup, theme_num: int):
    raw_data_list = [element.get_text().strip() for element in bs_object.select(
                                f'#reser3 > ul > li:nth-child({theme_num}) > div > ul > a > li')]

    return [time_pattern.search(raw_data).group() for raw_data in raw_data_list]


if __name__ == '__main__':
    scrape_escape_city_theme()
