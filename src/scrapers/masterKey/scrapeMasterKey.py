import urllib.request
from datetime import datetime, timedelta

from bs4 import BeautifulSoup

from src.scrapers.masterKey.constant import MASTER_KEY_CAFE_LIST, MASTER_KEY_URL
from src.utils.database import make_theme_date, update_theme_date
from src.utils.dateUtil import get_time_str


def scrape_master_key():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in MASTER_KEY_CAFE_LIST:
            bs_object = get_bs_object(MASTER_KEY_URL, cafe.store_id, date_str)

            for theme in cafe.theme_list:
                time_list = scrape_master_key_bs4(bs_object, theme)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.name} {theme.name}')

    theme_id_list = [theme.theme_id for cafe in MASTER_KEY_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


def get_bs_object(url, store_id, date):
    details = urllib.parse.urlencode({'date': date, 'store': store_id})
    details = details.encode('UTF-8')
    html = urllib.request.urlopen(url, details).read()
    return BeautifulSoup(html, "lxml")


def scrape_master_key_bs4(bs_object, theme):
    return [get_time_str(time_element.get_text())
            for time_element in
            bs_object.select(f'div.box2-inner:has(div.title:-soup-contains("{theme.name}")) p.true a')]


if __name__ == '__main__':
    scrape_master_key()
