from typing import Final

ESCAPE_CITY_URL: Final = "http://escapecity.kr/sub/sub03_1.html"


class EscapeCityTheme:

    def __init__(self, theme_name: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.theme_num = theme_num
        self.theme_id = theme_id


class EscapeCityCafe:
    def __init__(self, location: str, R_JIJEM: str, theme_list: list[EscapeCityTheme]):
        self.location = location
        self.R_JIJEM = R_JIJEM
        self.theme_list = theme_list


ESCAPE_CITY_CAFE_LIST: Final = [
    EscapeCityCafe(
        location="영등포본점",
        R_JIJEM="S1",
        theme_list=[
            EscapeCityTheme(theme_name="좀비바이러스", theme_num=4, theme_id=606),
            EscapeCityTheme(theme_name="마법학교", theme_num=7, theme_id=607),
            EscapeCityTheme(theme_name="기억의 조각", theme_num=10, theme_id=605),
            EscapeCityTheme(theme_name="S P Y", theme_num=13, theme_id=608),
            EscapeCityTheme(theme_name="카지노의 전설", theme_num=16, theme_id=609),
            EscapeCityTheme(theme_name="다시만날수있을까?", theme_num=19, theme_id=610),
        ],
    ),
    EscapeCityCafe(
        location="성신여대점",
        R_JIJEM="S2",
        theme_list=[
            EscapeCityTheme(theme_name="비밀결사대", theme_num=4, theme_id=518),
            EscapeCityTheme(theme_name="그녀를 찾아서", theme_num=7, theme_id=521),
            EscapeCityTheme(theme_name="킬러VS", theme_num=10, theme_id=519),
            EscapeCityTheme(theme_name="VS경찰", theme_num=13, theme_id=520),
            EscapeCityTheme(theme_name="시험지 유출사건", theme_num=16, theme_id=522),
        ],
    ),
    EscapeCityCafe(
        location="부천신중동점",
        R_JIJEM="S3",
        theme_list=[
            EscapeCityTheme(theme_name="부자가 될 상인가(70분)", theme_num=4, theme_id=983),
            EscapeCityTheme(theme_name="바람 바람 바람", theme_num=7, theme_id=984),
            EscapeCityTheme(theme_name="추억의 전당포", theme_num=10, theme_id=985),
            EscapeCityTheme(theme_name="원한", theme_num=13, theme_id=986),
        ],
    ),
    EscapeCityCafe(
        location="그랜드 시티 신촌점",
        R_JIJEM="S4",
        theme_list=[
            EscapeCityTheme(theme_name="연A", theme_num=4, theme_id=308),
            EscapeCityTheme(theme_name="연B", theme_num=7, theme_id=308),
            EscapeCityTheme(theme_name="신의실수A", theme_num=10, theme_id=307),
            EscapeCityTheme(theme_name="신의실수B", theme_num=13, theme_id=307),
        ],
    ),
]
