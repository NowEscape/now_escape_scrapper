from datetime import datetime, timedelta

import requests
import json
from src.scrapers.playTheWorld.constant import PLAY_THE_WORLD_THEME_LIST, PLAY_THE_WORLD_URL
from src.utils.database import update_theme_date, make_theme_date
from src.utils.dateUtil import time_pattern


def scrape_play_the_world_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in PLAY_THE_WORLD_THEME_LIST:

            for theme in cafe.theme_list:
                time_list = scrape_play_the_world_theme_json(date_str, theme.theme_id_scraping)

                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for theme in PLAY_THE_WORLD_THEME_LIST]

    update_theme_date(theme_id_list, theme_date_list)


def scrape_play_the_world_theme_json(date: str, theme_id_scraping: int):
    url = PLAY_THE_WORLD_URL.format(THEME_ID=theme_id_scraping, DATE=date)
    response = requests.get(url)
    json_data = json.loads(response.text)

    return [time_pattern.search(time_unit['start_time']).group()
            for time_unit in json_data['data']['time_units'] if
            time_unit['reserve_status'] == 'default']


if __name__ == '__main__':
    scrape_play_the_world_theme()
