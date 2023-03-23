import urllib
from datetime import datetime, timedelta
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.scrapers.questionMark.constant import QUESTION_MARK_URL
from src.utils.database import make_theme_date, update_theme_date
from src.utils.util import try_except_handling


def scrape_queation_mark_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        time_list = scrape_queation_mark_theme_bs4(date_str, QUESTION_MARK_URL)
        theme_date_list = theme_date_list + (make_theme_date(448, date_str, time_list))
        print(f'{datetime.now()} scraping {date_str} 퀘스천마크')

    update_theme_date('448', theme_date_list)


@try_except_handling
def scrape_queation_mark_theme_bs4(date: str, raw_url: str):
    url_final = raw_url + date
    url = urllib.request.Request(url_final)

    html = urllib.request.urlopen(url).read().decode("utf-8")
    bs_object = BeautifulSoup(html, "lxml")
    return [element.get_text().strip() for element in bs_object.select
    ('#contents > div > div > div > div.time_Area > ul > li > a[href] > span.time')]


if __name__ == '__main__':
    scrape_queation_mark_theme()
