CODE_K_URL = "http://www.code-k.co.kr/sub/code_sub04_1.html?R_JIJEM={R_JIJEM}&CHOIS_DATE={DATE}&DIS_T=S"


class CodeKTheme:
    def __init__(self, theme_name: str, theme_id: int):
        self.theme_name = theme_name
        self.theme_id = theme_id


class CodeKCafe:
    def __init__(self, name: str, r_jijem: str, theme_list: list[CodeKTheme]):
        self.name = name
        self.r_jijem = r_jijem
        self.theme_list = theme_list


CODE_K_CAFE_LIST = [
    CodeKCafe(
        name="강남점",
        r_jijem="S1",
        theme_list=[
            CodeKTheme(theme_name="도둑들", theme_id=132),
            # CodeKTheme(theme_name="마법사 케라스의 방", theme_id=),
            CodeKTheme(theme_name="얼어붙은 물의 신전", theme_id=134),
            CodeKTheme(theme_name="살인사건 현장", theme_id=126),
            CodeKTheme(theme_name="기억상실", theme_id=125),
            CodeKTheme(theme_name="미치광이 연쇄살인범", theme_id=133),
            CodeKTheme(theme_name="셜록홈즈: 살인누명", theme_id=127),
            CodeKTheme(theme_name="충무공 이순신", theme_id=121),
            CodeKTheme(theme_name="감옥탈출", theme_id=129),
            CodeKTheme(theme_name="저주받은 산장", theme_id=123),
            CodeKTheme(theme_name="좀비 90일후", theme_id=130),
            CodeKTheme(theme_name="납치 (2인전용)", theme_id=124),
            CodeKTheme(theme_name="테러리스트", theme_id=128),
            CodeKTheme(theme_name="기술자들", theme_id=131),
            CodeKTheme(theme_name="미스터리 거울의 방 (3인이상) -15세 이상-", theme_id=122),
        ]
    ),
    CodeKCafe(
        name="구월점",
        r_jijem="S2",
        theme_list=[
            CodeKTheme(theme_name="감옥탈출", theme_id=1046),
            CodeKTheme(theme_name="좀비 90일후", theme_id=1047),
            CodeKTheme(theme_name="납치 (2인전용)", theme_id=1045),
            CodeKTheme(theme_name="충무공 이순신", theme_id=1049),
            CodeKTheme(theme_name="미스터리 거울의 방 (3인이상) -15세 이상-", theme_id=1048),
        ]
    ),
    CodeKCafe(
        name="홍대점",
        r_jijem="S3",
        theme_list=[
            CodeKTheme(theme_name="꼬레아 우라", theme_id=447),
        ]
    ),
]
