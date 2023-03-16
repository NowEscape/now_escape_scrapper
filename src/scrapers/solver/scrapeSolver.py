import urllib
from datetime import datetime, timedelta
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.scrapers.solver.constant import SOLVER_CAFE_LIST
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling


def scrape_solver_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in SOLVER_CAFE_LIST:
            for theme in cafe.theme_list:
                time_list = scrape_solver_theme_bs4(date_str, cafe.url, theme.JIJEM, theme.theme_num)
                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in SOLVER_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def scrape_solver_theme_bs4(date: str, raw_url: str, jijem: str, theme_num: int):
    details = urllib.parse.urlencode({'JIJEM': jijem, 'D_ROOM': "", 'H_Date': date})
    details = details.encode('UTF-8')
    url = urllib.request.Request(raw_url, details)

    html = urllib.request.urlopen(url).read()
    bs_object = BeautifulSoup(html, "lxml")
    return [element.get_text().strip() for element in bs_object.select
    (f'#sub_content3 > div:nth-child({theme_num}) > ul > li > span.time[style="color: #05AF84"]')]


if __name__ == '__main__':
    scrape_solver_theme()
