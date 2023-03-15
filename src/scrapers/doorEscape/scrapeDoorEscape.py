import urllib.request
from datetime import datetime, timedelta

from bs4 import BeautifulSoup

from src.scrapers.doorEscape.constant import DOOR_ESCAPE_CAFE_LIST, DOOR_ESCAPE_URL
from src.utils.database import make_theme_date, update_theme_date


def scrape_door_escape_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in DOOR_ESCAPE_CAFE_LIST:
            for theme in cafe.theme_list:
                time_list = scrape_door_escape_theme_bs4(date_str, cafe.cafe_sub_domain, theme.theme_name)
                print(time_list)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {cafe.name} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in DOOR_ESCAPE_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)





def scrape_door_escape_theme_bs4(date: str, cafe_sub_domain: str, theme_name: str):
    details = urllib.parse.urlencode({'rdate': date})
    details = details.encode('UTF-8')
    print(DOOR_ESCAPE_URL.format(CAFE_SUB_DOMAIN=cafe_sub_domain))
    url = urllib.request.Request(DOOR_ESCAPE_URL.format(CAFE_SUB_DOMAIN=cafe_sub_domain), details)

    html = urllib.request.urlopen(url).read().decode("utf-8")
    bs_object = BeautifulSoup(html, "lxml")
    return [time_element.select_one('span.time').get_text().strip()
            for element in bs_object.select('#contents > div > div.theme_List > div.theme_box > div.theme_Text')
            if element.select_one('div.theme_Top > span.theme_name').get_text().strip() == theme_name
            for time_element in element.select('div.time_Area > ul.reserve_Time > li')
            if time_element.select_one('a.end') is None]




if __name__ == '__main__':
    scrape_door_escape_theme()
