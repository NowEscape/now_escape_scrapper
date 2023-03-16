import urllib.request
from datetime import datetime, timedelta

from bs4 import BeautifulSoup

from src.scrapers.secretGardenEscape.Constant import SECRET_GARDEN_CAFE_LIST, SECRET_GARDEN_URL
from src.utils.database import update_theme_date, make_theme_date
from src.utils.util import try_except_handling


def scrape_secret_garden_theme():
    theme_date_list = []
    now = datetime.now()

    for dateDelta in range(7):
        date = now + timedelta(dateDelta)
        date_str = date.strftime('%Y-%m-%d')

        for cafe in SECRET_GARDEN_CAFE_LIST:
            bs_object = get_bs_object(cafe.shop_no, date_str)
            if bs_object is None:
                continue

            for theme in cafe.theme_list:
                time_list = get_time_list(bs_object, theme.theme_name)

                theme_date_list = theme_date_list + (make_theme_date(theme.theme_id, date_str, time_list))
                print(f'{datetime.now()} scraping {date_str} {theme.theme_name}')

    theme_id_list = [theme.theme_id for cafe in SECRET_GARDEN_CAFE_LIST for theme in cafe.theme_list]

    update_theme_date(theme_id_list, theme_date_list)


@try_except_handling
def get_bs_object(shop_no: int, date: str):
    url = urllib.request.Request(SECRET_GARDEN_URL.format(SHOP_NO=shop_no, DATE=date))

    html = urllib.request.urlopen(url).read().decode("utf-8")
    bs_object = BeautifulSoup(html, "lxml")
    return bs_object


def get_time_list(bs_object, theme_name):
    time_element_list = [element.find('ul', {'class': 'reserve_Time'}).find_all('li')
                         for element in bs_object.body.find_all('div', {'class': 're_theme_box'})
                         if element.find('p', {'class': 'mtit'}).get_text() == theme_name][0]
    return [time_element.find('span', {'class': 'time'}).get_text()
            for time_element in time_element_list
            if time_element.find('a', {'class': 'end'}) is None]


if __name__ == '__main__':
    scrape_secret_garden_theme()
