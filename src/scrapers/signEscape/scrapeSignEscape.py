import urllib.request
from datetime import datetime, timedelta

from bs4 import BeautifulSoup

from src.scrapers.signEscape.constant import SIGN_ESCAPE_CAFE_LIST, SIGN_ESCAPE_URL
from src.utils.database import make_theme_date, update_theme_date
from src.utils.dateUtil import time_pattern


def scrape_sign_escape_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in SIGN_ESCAPE_CAFE_LIST:
            for theme in cafe.theme_list:
                time_list = scrape_sign_escape_theme_bs4(date_str, cafe.r_jijem, theme.r_theme)
                print(time_list)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.name} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in SIGN_ESCAPE_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


def scrape_sign_escape_theme_bs4(date: str, r_jijem: str, r_theme: int):
    url = urllib.request.Request(SIGN_ESCAPE_URL.format(R_JIJEM=r_jijem, R_THEMA=r_theme, DATE=date))

    html = urllib.request.urlopen(url).read()
    bs_object = BeautifulSoup(html, "lxml")
    return [time_pattern.search(element.get_text().strip()).group()
            for element in bs_object.select(f'#reser4 li.timeOn')]


if __name__ == '__main__':
    scrape_sign_escape_theme()
