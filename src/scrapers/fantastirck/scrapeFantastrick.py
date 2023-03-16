import urllib
from datetime import datetime, timedelta
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.scrapers.fantastirck.constant import FANTASTRICK_THEME_LIST, FANTASTRICK_URL
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling


def scrape_fantastrick_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for theme in FANTASTRICK_THEME_LIST:
            time_list = scrape_fantastrick_theme_bs4(date_str, theme.calendar_id)

            theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
            print(f'{datetime.now()} scraping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for theme in FANTASTRICK_THEME_LIST]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def scrape_fantastrick_theme_bs4(date: str, calendar_id: int):
    details = urllib.parse.urlencode({'action': "booked_calendar_date", 'date': date, 'calendar_id': calendar_id})
    details = details.encode('UTF-8')
    url = urllib.request.Request(FANTASTRICK_URL, details)

    html = urllib.request.urlopen(url).read().decode("utf-8")
    bs_object = BeautifulSoup(html, "lxml")

    return [datetime.strptime(
        element.find('span', {'class': 'button-timeslot'}).text
        .replace("오후", "PM").replace("오전", "AM"), '%p %I:%M').strftime('%H:%M')
            for element in bs_object.body.find_all('span', {'class': 'timeslot-people'})
            if not element.find('button').has_attr('disabled')]


if __name__ == '__main__':
    scrape_fantastrick_theme()
