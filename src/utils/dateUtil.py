import re


def get_date_time_str(date, time_str):
    return date + " " + time_str


time_pattern = re.compile('[0-9]{2}:[0-9]{2}')


def get_time_str(str):
    return time_pattern.search(str).group()
