from typing import Final


class EarthStarTheme:

    def __init__(self, theme_name: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.theme_num = theme_num
        self.theme_id = theme_id


class EarthStarCafe:
    def __init__(self, url: str, theme_list: list[EarthStarTheme]):
        self.url = url
        self.theme_list = theme_list


EARTH_STAR_CAFE_LIST: Final = [
    EarthStarCafe(
        url="https://xn--2e0b040a4xj.com/reservation?branch=1&theme=&date=",
        theme_list=[
            EarthStarTheme(theme_name="우리 아빠", theme_num=3, theme_id=1308),
            EarthStarTheme(theme_name="사명 : 투쟁의 노래", theme_num=4, theme_id=1310),
            EarthStarTheme(theme_name="펭귄키우기", theme_num=5, theme_id=1309),
            EarthStarTheme(theme_name="너의 겨울은 가고, 봄은 온다", theme_num=6, theme_id=1307),
            EarthStarTheme(theme_name="만월 <<꿈을 훔치는 요괴>>", theme_num=7, theme_id=1306),
            EarthStarTheme(theme_name="단디해라", theme_num=8, theme_id=1305),
        ],
    ),
    EarthStarCafe(
        url="https://xn--2e0b040a4xj.com/reservation?branch=2&theme=&date=",
        theme_list=[
            EarthStarTheme(theme_name="지난날을 잊었다", theme_num=3, theme_id=446),
            EarthStarTheme(theme_name="미스터리", theme_num=4, theme_id=445),
            EarthStarTheme(theme_name="퀘스트 : 여정의 시작", theme_num=5, theme_id=444),
        ],
    ),
]
