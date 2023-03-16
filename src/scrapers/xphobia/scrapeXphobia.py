import urllib
from datetime import datetime, timedelta
import json
from urllib.request import urlopen

from src.scrapers.xphobia.constant import XPHOBIA_CAFE_LIST, GET_XPHOBIA_URL_GET_TIME_META, GET_XPHOBIA_URL_GET_TIME
from src.utils.database import update_theme_date, make_theme_date
from src.utils.dateUtil import get_time_str
from src.utils.util import merge_dicts


def scrape_xphobia_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in XPHOBIA_CAFE_LIST:

            for theme in cafe.theme_list:
                time_list = scrape_xphobia_theme_json(cafe.shop, theme.quest, date.strftime('%Y%m%d'))
                print(time_list)

                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {theme.quest}')

    theme_id_list = [theme.theme_id for cafe in XPHOBIA_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


def scrape_xphobia_theme_json(shop: str, quest: str, date: str):
    params = urllib.parse.urlencode({'shop': shop, 'quest': quest, 'quest2': quest, 'date': date}).encode('UTF-8')
    url = urllib.request.Request(GET_XPHOBIA_URL_GET_TIME_META, params)

    json_data = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))[0]
    available_time_list = []
    for index in range(1, 51):
        if json_data[f'ro_day{index}'] == "":
            break
        available_time_list.append(get_time_str(json_data[f'ro_day{index}']))

    params = \
        urllib.parse.urlencode(
            merge_dicts({'qr_id': "", 'shop': shop, 'quest': quest, 'date': date},
                        {f'time[{index}]': time for index, time in enumerate(available_time_list)})
        ).encode('UTF-8')
    url = urllib.request.Request(GET_XPHOBIA_URL_GET_TIME, params)
    json_data = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
    _ = [available_time_list.remove(time['rel_order_time']) for time in json_data]
    return available_time_list


if __name__ == '__main__':
    scrape_xphobia_theme()
