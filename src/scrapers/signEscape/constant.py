from typing import Final

SIGN_ESCAPE_URL: Final = "http://signescape.com/sub/sub03_1.html?chois_date={DATE}&R_JIJEM={R_JIJEM}&R_THEMA={R_THEMA}"


class SignEscapeTheme:

    def __init__(self, r_theme: str, theme_name: str, theme_id: int):
        self.r_theme = r_theme
        self.theme_name = theme_name
        self.theme_id = theme_id


class SignEscapeCafe:

    def __init__(self, name: str, r_jijem: str, theme_list: list[SignEscapeTheme]):
        self.name = name
        self.r_jijem = r_jijem
        self.theme_list = theme_list


SIGN_ESCAPE_CAFE_LIST = [
    SignEscapeCafe(
        name="인계시티점",
        r_jijem="S1",
        theme_list=[
            SignEscapeTheme(r_theme="A", theme_name="페이퍼컴터니", theme_id=754),
        ]
    ),
    SignEscapeCafe(
        name="성대역점",
        r_jijem="S2",
        theme_list=[
            SignEscapeTheme(r_theme="A", theme_name="우울증", theme_id=744),
            SignEscapeTheme(r_theme="B", theme_name="각성", theme_id=745),
            SignEscapeTheme(r_theme="C", theme_name="인턴", theme_id=746),
            SignEscapeTheme(r_theme="D", theme_name="자멜신부의 비밀", theme_id=747),
            SignEscapeTheme(r_theme="E", theme_name="고시텔", theme_id=748),
        ]
    ),
    SignEscapeCafe(
        name="인계점",
        r_jijem="S4",
        theme_list=[
            SignEscapeTheme(r_theme="A", theme_name="자파", theme_id=750),
            SignEscapeTheme(r_theme="B", theme_name="트라이위저드", theme_id=749),
            SignEscapeTheme(r_theme="C", theme_name="악은 어디에나 존재한다", theme_id=751),
            SignEscapeTheme(r_theme="D", theme_name="신비의 베이커리", theme_id=752),
            SignEscapeTheme(r_theme="E", theme_name="GATE : CCZ (episode 1)", theme_id=753),
        ]
    ),
    SignEscapeCafe(
        name="홍대점",
        r_jijem="S5",
        theme_list=[
            SignEscapeTheme(r_theme="A", theme_name="거상", theme_id=400),
            SignEscapeTheme(r_theme="B", theme_name="졸업", theme_id=401),
            SignEscapeTheme(r_theme="C", theme_name="하이팜", theme_id=402),
        ]
    ),
    SignEscapeCafe(
        name="강남시티점",
        r_jijem="S6",
        theme_list=[
            SignEscapeTheme(r_theme="A", theme_name="러너웨이", theme_id=95),
            SignEscapeTheme(r_theme="B", theme_name="MUST", theme_id=96),
        ]
    ),
]
