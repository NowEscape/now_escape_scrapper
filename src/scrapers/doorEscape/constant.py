DOOR_ESCAPE_URL = "http://{CAFE_SUB_DOMAIN}doorescape.co.kr/reserve/"


class DoorEscapeTheme:
    def __init__(self, theme_id: int, theme_name: str):
        self.theme_id = theme_id
        self.theme_name = theme_name


class DoorEscapeCafe:
    def __init__(self, name: str, cafe_sub_domain: str, theme_list: list[DoorEscapeTheme]):
        self.name = name
        self.cafe_sub_domain = cafe_sub_domain
        self.theme_list = theme_list


DOOR_ESCAPE_CAFE_LIST = [
    DoorEscapeCafe(
        name="안산점",
        cafe_sub_domain="",
        theme_list=[
            DoorEscapeTheme(theme_name="파라오의 석실", theme_id=679),
            DoorEscapeTheme(theme_name="마녀의 저주", theme_id=676),
            DoorEscapeTheme(theme_name="빠삐용", theme_id=682),
            DoorEscapeTheme(theme_name="귀곡성", theme_id=681),
            DoorEscapeTheme(theme_name="검은조직", theme_id=680),
            DoorEscapeTheme(theme_name="미친 의사", theme_id=677),
            DoorEscapeTheme(theme_name="빅뱅", theme_id=678),
        ]
    ),
    DoorEscapeCafe(

        name="이수역점",
        cafe_sub_domain="isu.",
        theme_list=[
            DoorEscapeTheme(theme_name="파라오의 석실", theme_id=624),
            DoorEscapeTheme(theme_name="빠삐용", theme_id=625),
            DoorEscapeTheme(theme_name="검은조직", theme_id=626),
            DoorEscapeTheme(theme_name="S.O.S 정글", theme_id=627),
        ]
    ),
    DoorEscapeCafe(
        name="레드점",
        cafe_sub_domain="red.",
        theme_list=[
            DoorEscapeTheme(theme_name="LUCKY", theme_id=29),
            DoorEscapeTheme(theme_name="비", theme_id=30),
            DoorEscapeTheme(theme_name="유전", theme_id=31),
        ]
    ),
    DoorEscapeCafe(
        name="블루점",
        cafe_sub_domain="blue.",
        theme_list=[
            DoorEscapeTheme(theme_name="TRUTH", theme_id=32),
            DoorEscapeTheme(theme_name="이방인", theme_id=33),
        ]
    ),
    DoorEscapeCafe(
        name="홍대점",
        cafe_sub_domain="hongdae.",
        theme_list=[
            DoorEscapeTheme(theme_name="신기루", theme_id=329),
            DoorEscapeTheme(theme_name="DISCOVERY", theme_id=330),
        ]
    ),
    DoorEscapeCafe(
        name="가든점",
        cafe_sub_domain="garden.",
        theme_list=[
            DoorEscapeTheme(theme_name="출동", theme_id=26),
            DoorEscapeTheme(theme_name="INSERT COIN", theme_id=27),
            DoorEscapeTheme(theme_name="둘이라면", theme_id=28),
            # DoorEscapeTheme(theme_name="IMAGINE", theme_id=),
        ]
    ),
    DoorEscapeCafe(
        name="대전유성 NC백화점",
        cafe_sub_domain="dj.",
        theme_list=[
            DoorEscapeTheme(theme_name="나는 아직도 배고프G", theme_id=1119),
            DoorEscapeTheme(theme_name="도어항공 41C", theme_id=1122),
            DoorEscapeTheme(theme_name="서커스 : THE CLEANING MAN (공포)", theme_id=1120),
            DoorEscapeTheme(theme_name="산타의 민족", theme_id=1121),
            DoorEscapeTheme(theme_name="GOOD NIGHT", theme_id=1123),
            DoorEscapeTheme(theme_name="WOULD YOU FIND ME?", theme_id=1124),
        ]
    ),
]
