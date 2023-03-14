import urllib
from datetime import datetime, timedelta
from src.scrapers.keyEscape.constant import KEY_ESCAPE_CAFE_LIST, KEY_ESCAPE_URL
from src.utils.database import make_theme_date, update_theme_date
from bs4 import BeautifulSoup
from urllib.request import urlopen

from src.utils.util import try_except_handling


def scrape_key_escape_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in KEY_ESCAPE_CAFE_LIST:
            for theme in cafe.theme_list:
                time_list = scrape_key_escape_theme_bs4(date_str, cafe.zizum_num, theme.theme_num)

                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.location} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in KEY_ESCAPE_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def scrape_key_escape_theme_bs4(date: str, zizum_num: int, theme_num: int):
    details = urllib.parse.urlencode({'zizum_num': zizum_num, 'rev_days': date, 'theme_num': theme_num})
    details = details.encode('UTF-8')
    url = urllib.request.Request(KEY_ESCAPE_URL, details)

    html = urllib.request.urlopen(url).read().decode("utf-8")
    bs_object = BeautifulSoup(html, "lxml")
    return [element.get_text().strip() for element in bs_object.body.find_all('li', {'class': 'possible'})]


if __name__ == '__main__':
    scrape_key_escape_theme()
