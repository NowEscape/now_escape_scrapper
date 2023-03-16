import urllib
from datetime import datetime, timedelta
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.scrapers.amazed.constant import AMAZED_CAFE_LIST, AMAZED_URL
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling


def scrape_amazed_theme():
    theme_date_list = []
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d')

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in AMAZED_CAFE_LIST:
            for theme in cafe.theme_list:
                time_list = scrape_amazed_theme_bs4(date_str, AMAZED_URL, theme.calendar_id, now_str)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in AMAZED_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def scrape_amazed_theme_bs4(date: str, url: str, calendar_id: int, now: str):
    details = urllib.parse.urlencode({'action': 'booked_appointment_list_date', 'date': date,
                                      'calendar_id': calendar_id, 'force_default': now})
    details = details.encode('UTF-8')
    url = urllib.request.Request(url, details)

    html = urllib.request.urlopen(url).read()
    bs_object = BeautifulSoup(html, "lxml")
    return [element.find('span', {'class': 'button-timeslot'}).text
            for element in bs_object.body.find_all('span', {'class': 'timeslot-people'})
            if not element.find('button').has_attr('disabled')]


if __name__ == '__main__':
    scrape_amazed_theme()
