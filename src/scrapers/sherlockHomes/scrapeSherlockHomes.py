import urllib
from datetime import datetime, timedelta
from urllib.request import urlopen

import bs4
from bs4 import BeautifulSoup

from src.scrapers.sherlockHomes.constant import SHERLOCK_HOMES_CAFE_LIST, SHERLOCK_HOMES_URL
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling


def scrape_sherlock_homes_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in SHERLOCK_HOMES_CAFE_LIST:
            bs_object = get_bs_object(SHERLOCK_HOMES_URL.format(SIDO=cafe.sido, BNO=cafe.bno, DATE=date_str))

            for theme in cafe.theme_list:
                time_list = scrape_sherlock_homes_theme_bs4(bs_object, theme.theme_num)
                print(time_list)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.region2} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in SHERLOCK_HOMES_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


def get_bs_object(url):
    html = urllib.request.urlopen(urllib.request.Request(url)).read().decode("utf-8")
    bs_object = BeautifulSoup(html, "lxml")
    return bs_object


@try_except_handling
def scrape_sherlock_homes_theme_bs4(bs_object: bs4.BeautifulSoup, theme_num: int):
    return [element.get_text().strip() for element in bs_object.select
    ('div.inner container > li:nth-child(1) > div.row > div > a > p.time')]


#theme_ac_186 > div.row > div > div > p.time
#theme_ac_186 > div.row > div > a > p.time
#theme_ac_283 > div.row > div:nth-child(3) > a > p.time

if __name__ == '__main__':
    scrape_sherlock_homes_theme()
