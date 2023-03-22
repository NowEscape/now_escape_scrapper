from typing import Final


class EscapersTheme:
    def __init__(self, theme_name: str, theme_pk: int, theme_id: int):
        self.theme_name = theme_name
        self.theme_pk = theme_pk
        self.theme_id = theme_id


class EscapersCafe:
    def __init__(self, name: str, url: str, theme_list: list[EscapersTheme]):
        self.name = name
        self.url = url
        self.theme_list = theme_list


ESCAPERS_CAFE_LIST: Final = [
    EscapersCafe(
        name="1호점",
        url="http://www.escapers.co.kr/reservation",
        theme_list=[
            EscapersTheme(theme_name="서커스:공중그네", theme_pk=1, theme_id=432),
            EscapersTheme(theme_name="싸이코메트리", theme_pk=3, theme_id=429),
            EscapersTheme(theme_name="RS의 밀실", theme_pk=5, theme_id=430),
            EscapersTheme(theme_name="붉은머리연맹", theme_pk=7, theme_id=428),
            EscapersTheme(theme_name="라이브", theme_pk=13, theme_id=433),
        ]
    ),
    EscapersCafe(
        name="2호점",
        url="http://www.escapers.co.kr/reservation/2",
        theme_list=[
            EscapersTheme(theme_name="네모네모 마믈메는 무슨밀미 밋멋믈까?", theme_pk=10, theme_id=434),
            EscapersTheme(theme_name="멍스타그램", theme_pk=14, theme_id=435),
            EscapersTheme(theme_name="인생낚시", theme_pk=16, theme_id=436),
            EscapersTheme(theme_name="만약, 당신이 길을 잃었다면", theme_pk=20, theme_id=437),
        ]
    ),
    EscapersCafe(
        name="대구점",
        url="https://escapersd.com/reservation",
        theme_list=[
            EscapersTheme(theme_name="멍스타그램", theme_pk=1, theme_id=1299),
            EscapersTheme(theme_name="웰컴 투 캔디샵", theme_pk=4, theme_id=1301),
            EscapersTheme(theme_name="폰부스", theme_pk=7, theme_id=1300),
            EscapersTheme(theme_name="돈싱크", theme_pk=8, theme_id=1302),
            EscapersTheme(theme_name="서커스 : 동성극단의 사정", theme_pk=10, theme_id=1303),
            EscapersTheme(theme_name="끝까지 간다", theme_pk=12, theme_id=1304),
        ]
    )
]
