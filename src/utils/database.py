from datetime import datetime

import MySQLdb
from config.credentials import DB_HOST, DB_USER, DB_PASSWORD, DB_CHARSET, DB_NAME
from src.utils.dateUtil import get_date_time_str


def get_connection():
    return MySQLdb.connect(user=DB_USER, password=DB_PASSWORD,
                           host=DB_HOST,
                           charset=DB_CHARSET,
                           db=DB_NAME)


class ThemeDate:
    def __init__(self, theme_id: int, date_time: str):
        self.theme_id = theme_id
        self.date_time = date_time

    def __str__(self):
        return f'str : {self.theme_id} - {self.date_time}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.theme_id == other.theme_id and self.date_time == other.date_time

    def __hash__(self):
        return hash((self.theme_id, self.date_time))

    def __ne__(self, other):
        return not self.__eq__(other)


def make_theme_date(theme_id: int, date: str, time_list: list) -> list:
    theme_date_list = []
    for time in time_list:
        theme_date_list.append(ThemeDate(theme_id, get_date_time_str(date, time)))
    return theme_date_list


def update_theme_date(theme_id_list, theme_date_list):
    connection = get_connection()
    cursor = connection.cursor()
    print("SELECT... ", datetime.now(), len(theme_id_list))
    select_sql = (f"SELECT t.theme_id, DATE_FORMAT(td.theme_time,'%Y-%m-%d %H:%i') "
                  f"FROM theme t "
                  f"JOIN theme_date td ON t.theme_id = td.theme_id "
                  f"WHERE t.theme_id IN ({','.join(str(e) for e in theme_id_list)})")
    cursor.execute(select_sql)

    result = cursor.fetchall()
    exist_theme_date_list = [ThemeDate(theme_id, date_time) for theme_id, date_time in result]


    print("SELECT COMPLETE... ", datetime.now(), len(exist_theme_date_list))
    #print if exist item in theme_date_list and exist_theme_date_list
    for item in set(exist_theme_date_list) & set(theme_date_list):
        print(item)

    theme_date_list_for_delete = set(exist_theme_date_list) - set(theme_date_list)

    print("DELETE... ", datetime.now(), len(theme_date_list_for_delete))
    delete_query = "DELETE FROM theme_date WHERE theme_id = %s AND theme_time = %s"
    cursor.executemany(delete_query, [(item.theme_id, item.date_time) for item in theme_date_list_for_delete])
    print("DELETE COMPLETE... ", datetime.now(), len(theme_date_list_for_delete))

    theme_date_list_for_insert = set(theme_date_list) - set(exist_theme_date_list)

    print("INSERT... ", datetime.now(), len(theme_date_list_for_insert))

    insert_query = "INSERT INTO theme_date (theme_id, theme_time, is_open) VALUES (%s, %s,1)"
    cursor.executemany(insert_query, [(item.theme_id, item.date_time) for item in theme_date_list_for_insert])
    print("INSERT COMPLETE... ", datetime.now(), len(theme_date_list_for_insert))
    connection.commit()
    print("COMMIT COMPLETE... ", datetime.now())
    cursor.close()
    connection.close()
