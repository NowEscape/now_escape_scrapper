from typing import Final

KEY_ESCAPE_URL: Final = "https://keyescape.co.kr/web/home.php?go=rev.make"


class KeyEscapeTheme:

    def __init__(self, theme_name: str, theme_id: int):
        self.theme_name = theme_name
        self.theme_id = theme_id


class KeyEscapeCafe:
    def __init__(self, location: str, theme_list: list[KeyEscapeTheme]):
        self.location = location
        self.theme_list = theme_list


KEY_ESCAPE_CAFE_LIST: Final = [
    KeyEscapeCafe(
        location="강남점",
        theme_list=[
            KeyEscapeTheme(theme_name="살랑살랑연구소", theme_id=136),
            KeyEscapeTheme(theme_name="월야애담-영문병행표기", theme_id=135),
            KeyEscapeTheme(theme_name="그카지말라캤자나", theme_id=137),
        ],
    ),
    KeyEscapeCafe(
        location="홍대점",
        theme_list=[
            KeyEscapeTheme(theme_name="고백", theme_id=457),
            KeyEscapeTheme(theme_name="삐릿-뽀", theme_id=458),
            KeyEscapeTheme(theme_name="홀리데이", theme_id=459),
        ],
    ),
    KeyEscapeCafe(
        location="우주라이크",
        theme_list=[
            KeyEscapeTheme(theme_name="US", theme_id=141),
            KeyEscapeTheme(theme_name="WANNA GO HOME", theme_id=142),
        ],
    ),
    KeyEscapeCafe(
        location="강남 더오름",
        theme_list=[
            KeyEscapeTheme(theme_name="네드", theme_id=138),
            KeyEscapeTheme(theme_name="엔제리오", theme_id=139),
        ],
    ),
    KeyEscapeCafe(
        location="부산점",
        theme_list=[
            KeyEscapeTheme(theme_name="정신병동", theme_id=1542),
            KeyEscapeTheme(theme_name="파파라치", theme_id=1541),
            KeyEscapeTheme(theme_name="난쟁이의 장난-영문병행표기", theme_id=1540),
            KeyEscapeTheme(theme_name="셜록 죽음의 전화", theme_id=1543),
            KeyEscapeTheme(theme_name="신비의숲 고대마법의 비밀", theme_id=1544),
        ],
    ),
    KeyEscapeCafe(
        location="전주점",
        theme_list=[
            KeyEscapeTheme(theme_name="난쟁이의 장난-영문병행표기", theme_id=1653),
            KeyEscapeTheme(theme_name="혜화잡화점", theme_id=1654),
            KeyEscapeTheme(theme_name="월야애담-영문병행표기", theme_id=1655),
            KeyEscapeTheme(theme_name="사라진 목격자", theme_id=1657),
            KeyEscapeTheme(theme_name="살랑살랑연구소", theme_id=1656),
        ],
    ),
]
