from typing import Final


class GoldKeyTheme:

    def __init__(self, theme_name: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.theme_num = theme_num
        self.theme_id = theme_id


class GoldKeyCafe:
    def __init__(self, location: str, url: str, theme_list: list[GoldKeyTheme]):
        self.location = location
        self.url = url
        self.theme_list = theme_list


GOLD_KEY_CAFE_LIST: Final = [
    GoldKeyCafe(
        location="대구동성로점",
        url="http://xn--jj0b998aq3cptw.com/layout/res/home.php?go=rev.make&s_zizum=1&rev_days=",
        theme_list=[
            GoldKeyTheme(theme_name="가이아 기적의땅 (판타지)", theme_num=4, theme_id=145),
            GoldKeyTheme(theme_name="X됐다 (코믹)", theme_num=5, theme_id=144),
            GoldKeyTheme(theme_name="JAIL.O (미션)", theme_num=6, theme_id=146),
            GoldKeyTheme(theme_name="타임스틸러 (어드벤쳐)", theme_num=7, theme_id=146),
        ],
    ),
    GoldKeyCafe(
        location="대구동성로2호점",
        url="http://xn--jj0b998aq3cptw.com/layout/res/home.php?go=rev.make&s_zizum=11&rev_days=",
        theme_list=[
            GoldKeyTheme(theme_name="BAD ROB BAD (미션,잠입)", theme_num=4, theme_id=1796),
            GoldKeyTheme(theme_name="PILGRIM (모험)", theme_num=5, theme_id=1336),
            GoldKeyTheme(theme_name="지옥 (미스터리)", theme_num=6, theme_id=1335),
            GoldKeyTheme(theme_name="다시, 너에게 (드라마)", theme_num=7, theme_id=1334),
            GoldKeyTheme(theme_name="HEAVEN (스릴러,드라마)", theme_num=8, theme_id=1332),
            GoldKeyTheme(theme_name="냥탐정 셜록캣 (추리)", theme_num=9, theme_id=1333),
        ],
    ),
    GoldKeyCafe(
        location="강남점(타임스퀘어)",
        url="http://xn--jj0b998aq3cptw.com/layout/res/home.php?go=rev.make&s_zizum=5&rev_days=",
        theme_list=[
            GoldKeyTheme(theme_name="NOMON : THE ORDEAL (판타지)", theme_num=4, theme_id=149),
            GoldKeyTheme(theme_name="섬 (미스터리)", theme_num=5, theme_id=1795),
        ],
    ),
    GoldKeyCafe(
        location="강남점(플라워로드)",
        url="http://xn--jj0b998aq3cptw.com/layout/res/home.php?go=rev.make&s_zizum=6&rev_days=",
        theme_list=[
            GoldKeyTheme(theme_name="BACK화점 (범죄)", theme_num=4, theme_id=150),
            GoldKeyTheme(theme_name="ANOTHER (스릴러)", theme_num=5, theme_id=151),
        ],
    ),
    GoldKeyCafe(
        location="건대점(유토피아호)",
        url="http://xn--jj0b998aq3cptw.com/layout/res/home.php?go=rev.make&s_zizum=7&rev_days=",
        theme_list=[
            GoldKeyTheme(theme_name="fl[ae]sh (공포,스릴러)", theme_num=4, theme_id=230),
            GoldKeyTheme(theme_name="NOW HERE (잠입)", theme_num=5, theme_id=231),
        ],
    ),
]
