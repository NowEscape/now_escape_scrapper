import urllib
from datetime import datetime, timedelta
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.scrapers.earthStar.constant import EARTH_STAR_CAFE_LIST
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling


def scrape_earth_star_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in EARTH_STAR_CAFE_LIST:
            for theme in cafe.theme_list:
                time_list = scrape_earth_star_theme_bs4(date_str, cafe.url, theme.theme_num)
                print(time_list)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in EARTH_STAR_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def scrape_earth_star_theme_bs4(date: str, raw_url: str, theme_num: int):
    url_final = raw_url + date
    url = urllib.request.Request(url_final)

    html = urllib.request.urlopen(url).read()
    bs_object = BeautifulSoup(html, "lxml")
    return [element.get_text().strip() for element in bs_object.select
    (f'#wrap > div > div.container > section:nth-child({theme_num}) > div > ul > li > div > button.active1 > span')]


if __name__ == '__main__':
    scrape_earth_star_theme()
