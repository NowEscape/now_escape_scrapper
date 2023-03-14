from typing import Final

KEY_ESCAPE_URL: Final = "https://keyescape.co.kr/web/rev.theme_time.php"


class KeyEscapeTheme:

    def __init__(self, theme_name: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.theme_num = theme_num
        self.theme_id = theme_id


class KeyEscapeCafe:
    def __init__(self, location: str, zizum_num: int, theme_list: list[KeyEscapeTheme]):
        self.location = location
        self.zizum_num = zizum_num
        self.theme_list = theme_list


KEY_ESCAPE_CAFE_LIST: Final = [
    KeyEscapeCafe(
        location="강남점",
        zizum_num=3,
        theme_list=[
            KeyEscapeTheme(theme_name="살랑살랑연구소", theme_num=6, theme_id=136),
            KeyEscapeTheme(theme_name="월야애담-영문병행표기", theme_num=5, theme_id=135),
            KeyEscapeTheme(theme_name="그카지말라캤자나", theme_num=7, theme_id=137),
        ],
    ),
    KeyEscapeCafe(
        location="홍대점",
        zizum_num=10,
        theme_list=[
            KeyEscapeTheme(theme_name="고백", theme_num=43, theme_id=457),
            KeyEscapeTheme(theme_name="삐릿-뽀", theme_num=41, theme_id=458),
            KeyEscapeTheme(theme_name="홀리데이", theme_num=45, theme_id=459),
        ],
    ),
    KeyEscapeCafe(
        location="우주라이크",
        zizum_num=16,
        theme_list=[
            KeyEscapeTheme(theme_name="US", theme_num=55, theme_id=141),
            KeyEscapeTheme(theme_name="WANNA GO HOME", theme_num=54, theme_id=142),
        ],
    ),
    KeyEscapeCafe(
        location="강남 더오름",
        zizum_num=14,
        theme_list=[
            KeyEscapeTheme(theme_name="네드", theme_num=48, theme_id=138),
            KeyEscapeTheme(theme_name="엔제리오", theme_num=51, theme_id=139),
        ],
    ),
    KeyEscapeCafe(
        location="부산점",
        zizum_num=9,
        theme_list=[
            KeyEscapeTheme(theme_name="정신병동", theme_num=37, theme_id=1542),
            KeyEscapeTheme(theme_name="파파라치", theme_num=38, theme_id=1541),
            KeyEscapeTheme(theme_name="난쟁이의 장난-영문병행표기", theme_num=35, theme_id=1540),
            KeyEscapeTheme(theme_name="셜록 죽음의 전화", theme_num=39, theme_id=1543),
            KeyEscapeTheme(theme_name="신비의숲 고대마법의 비밀", theme_num=36, theme_id=1544),
        ],
    ),
    KeyEscapeCafe(
        location="전주점",
        zizum_num=7,
        theme_list=[
            KeyEscapeTheme(theme_name="난쟁이의 장난-영문병행표기", theme_num=32, theme_id=1653),
            KeyEscapeTheme(theme_name="혜화잡화점", theme_num=31, theme_id=1654),
            KeyEscapeTheme(theme_name="월야애담-영문병행표기", theme_num=29, theme_id=1655),
            KeyEscapeTheme(theme_name="사라진 목격자", theme_num=33, theme_id=1657),
            KeyEscapeTheme(theme_name="살랑살랑연구소", theme_num=30, theme_id=1656),
        ],
    ),
    KeyEscapeCafe(
        location="메모리얼컴퍼니",
        zizum_num=18,
        theme_list=[
            KeyEscapeTheme(theme_name="FILM BY EDDY", theme_num=57, theme_id=140),
            KeyEscapeTheme(theme_name="FILM BY STEVE", theme_num=58, theme_id=1793),
        ],
    ),
]
