from typing import Final


class PointNineTheme:

    def __init__(self, theme_name: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.theme_num = theme_num
        self.theme_id = theme_id


class PointNineCafe:
    def __init__(self, location: str, url: str, theme_list: list[PointNineTheme]):
        self.location = location
        self.url = url
        self.theme_list = theme_list


POINT_NINE_CAFE_LIST: Final = [
    PointNineCafe(
        location="강남점",
        url="https://point-nine.com/layout/res/home.php?go=rev.make&s_zizum=1&rev_days=",
        theme_list=[
            PointNineTheme(theme_name="EP1 : 시간이 멈춘 마을  ()", theme_num=4, theme_id=145),
            PointNineTheme(theme_name="EP2 : 열쇠공의 이중생활  ()", theme_num=5, theme_id=144),
            PointNineTheme(theme_name="EP4 : 주인 없는 낡은 서점  ()", theme_num=6, theme_id=146),
        ],
    ),
    PointNineCafe(
        location="강남2호점",
        url="https://point-nine.com/layout/res/home.php?go=rev.make&s_zizum=4&rev_days=",
        theme_list=[
            PointNineTheme(theme_name="HOMECOMING  ()", theme_num=4, theme_id=147),
            PointNineTheme(theme_name="HOMETOWN  ()", theme_num=5, theme_id=148),
        ],
    ),
    PointNineCafe(
        location="건대점",
        url="https://point-nine.com/layout/res/home.php?go=rev.make&s_zizum=5&rev_days=",
        theme_list=[
            PointNineTheme(theme_name="RETURN  (드라마)", theme_num=4, theme_id=228),
            PointNineTheme(theme_name="ALBA  (잠입)", theme_num=5, theme_id=229),
        ],
    ),
    PointNineCafe(
        location="홍대점",
        url="https://point-nine.com/layout/res/home.php?go=rev.make&s_zizum=6&rev_days=",
        theme_list=[
            PointNineTheme(theme_name="SILENT  (스릴, 수사)", theme_num=4, theme_id=460),
            PointNineTheme(theme_name="LISTEN  (액션,스릴)", theme_num=5, theme_id=461),
        ],
    ),
]
