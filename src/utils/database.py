import mysql.connector
from config.credentials import DB_HOST, DB_USER, DB_PASSWORD, DB_CHARSET, DB_NAME
from src.utils.dateUtil import get_date_time_str


def get_connection():
    return mysql.connector.connect(user=DB_USER, password=DB_PASSWORD,
                                   host=DB_HOST,
                                   charset=DB_CHARSET,
                                   db=DB_NAME)


class theme_date:
    def __init__(self, theme_id, date_time):
        self.theme_id = theme_id
        self.date_time = date_time

    def __str__(self):
        return f'str : {self.theme_id} - {self.date_time}'


def make_theme_date(theme_id: int, date: str, time_list: list) -> list:
    theme_date_list = []
    for time in time_list:
        theme_date_list.append(theme_date(theme_id, get_date_time_str(date, time)))
    return theme_date_list


def update_theme_date(theme_id_list, theme_date_list):
    connection = get_connection()
    cursor = connection.cursor(prepared=True)
    cursor.execute("DELETE FROM theme_date WHERE theme_id IN (" + ','.join(str(e) for e in theme_id_list) + ")")
    insert_query = "INSERT INTO theme_date (theme_id, theme_time, is_open) VALUES (%s, %s,1)"
    cursor.executemany(insert_query, theme_date_list)
    connection.commit()
    cursor.close()
    connection.close()
