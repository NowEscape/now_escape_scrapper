from typing import Final

PLAY_THE_WORLD_URL: Final = "https://api.plit.me/v1/themes/{THEME_ID}/time_units?date={DATE}"


class PlayTheWorldTheme:

    def __init__(self, theme_name: str, theme_id_scraping: int, theme_id: int):
        self.theme_name = theme_name
        self.theme_id_scraping = theme_id_scraping
        self.theme_id = theme_id


class PlayTheWorldCafe:
    def __init__(self, name: str, theme_list: list[PlayTheWorldTheme]):
        self.name = name
        self.theme_list = theme_list


PLAY_THE_WORLD_THEME_LIST: Final = [
    PlayTheWorldCafe(
        name="플레이더월드 강남점",
        theme_list=[
            PlayTheWorldTheme(theme_name="이상한 나라로 출두요", theme_id_scraping=1, theme_id=19),
            PlayTheWorldTheme(theme_name="이웃집 또털어", theme_id_scraping=2, theme_id=17),
            PlayTheWorldTheme(theme_name="어시스턴트", theme_id_scraping=3, theme_id=21),
            PlayTheWorldTheme(theme_name="조선피자몰", theme_id_scraping=4, theme_id=20),
            PlayTheWorldTheme(theme_name="이웃집 또도와", theme_id_scraping=5, theme_id=18)
        ]
    ),
]
