import json
import urllib.request
from datetime import datetime, timedelta

from bs4 import BeautifulSoup

from src.scrapers.roomExCape.constant import ROOM_EX_CAPE_CAFE_LIST, ROOM_EX_CAPE_URL
from src.utils.database import make_theme_date, update_theme_date


def scrape_room_ex_cape():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        details = urllib.parse.urlencode({'date': date})
        details = details.encode('UTF-8')
        url = urllib.request.Request(ROOM_EX_CAPE_URL, details)

        response_json = json.loads(urllib.request.urlopen(url, details).read())
        for cafe in ROOM_EX_CAPE_CAFE_LIST:
            for theme in cafe.theme_list:
                date = now + timedelta(dateDelta)
                date_str = date.strftime('%Y-%m-%d')

                time_list = scrape_room_ex_cape_bs4(response_json, theme)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.name} {theme.name}')

    theme_id_list = [theme.theme_id for cafe in ROOM_EX_CAPE_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


def scrape_room_ex_cape_bs4(response, theme):
    html = [data['html'] for data in response['data'] if int(data['code']) == theme.code][0]
    bs_object = BeautifulSoup(html, "lxml")
    return [time_element.select_one('span').get_text().strip()
            for time_element in bs_object.select('ol > li.on')]


if __name__ == '__main__':
    scrape_room_ex_cape()
