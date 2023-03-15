import urllib
from datetime import datetime, timedelta

import bs4

from src.scrapers.dumbNdumber.constant import DUMB_N_DUMBER_CAFE_LIST
from src.utils.database import make_theme_date, update_theme_date
from bs4 import BeautifulSoup
from urllib.request import urlopen

from src.utils.util import try_except_handling


def scrape_dumb_n_dumber_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in DUMB_N_DUMBER_CAFE_LIST:
            url = urllib.request.Request(cafe.url + date_str)

            html = urllib.request.urlopen(url).read().decode("utf-8")
            bs_object = BeautifulSoup(html, "lxml")
            for theme in cafe.theme_list:
                time_list = scrape_dumb_n_dumber_theme_bs4(bs_object, theme.theme_num)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.location} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in DUMB_N_DUMBER_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def scrape_dumb_n_dumber_theme_bs4(bs_object: bs4.BeautifulSoup, theme_num: int):
    return [element.get_text().strip() for element in bs_object.select(
        f'#container > div > div > div:nth-child({theme_num}) > div.time_Area > ul > li > a:not(.end) > span.time')]


if __name__ == '__main__':
    scrape_dumb_n_dumber_theme()
