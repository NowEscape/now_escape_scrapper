from typing import Final


class MurderParkerTheme:

    def __init__(self, theme_name: str, JIJEM: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.JIJEM = JIJEM
        self.theme_num = theme_num
        self.theme_id = theme_id


class MurderParkerCafe:
    def __init__(self, url: str, theme_list: list[MurderParkerTheme]):
        self.url = url
        self.theme_list = theme_list


MURDER_PARKER_CAFE_LIST: Final = [
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S1",
        theme_list=[
            MurderParkerTheme(theme_name="머더파커 분노의 살인_전주 1호점", JIJEM="S1", theme_num=1, theme_id=1611),
            MurderParkerTheme(theme_name="내 이름 지배만_전주 1호점", JIJEM="S1", theme_num=2, theme_id=1612),
            MurderParkerTheme(theme_name="일주(ONE WEEK)_전주 1호점", JIJEM="S1", theme_num=3, theme_id=1613),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S2",
        theme_list=[
            MurderParkerTheme(theme_name="스모커(90분)_전주2호점", JIJEM="S2", theme_num=1, theme_id=1617),
            MurderParkerTheme(theme_name="NEW 토니파커 숨겨진 과거(75분)_전주2호점", JIJEM="S2", theme_num=2, theme_id=1616),
            MurderParkerTheme(theme_name="목격자들(70분)_전주2호점", JIJEM="S2", theme_num=3, theme_id=1615),
            MurderParkerTheme(theme_name="인턴사원의 크리스마스 생존기_전주 2호점", JIJEM="S2", theme_num=4, theme_id=1614),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S3",
        theme_list=[
            MurderParkerTheme(theme_name="머더파커 분노의 살인_양산점", JIJEM="S3", theme_num=1, theme_id=1572),
            MurderParkerTheme(theme_name="엘리스 사라진 아이_양산점", JIJEM="S3", theme_num=2, theme_id=1573),
            MurderParkerTheme(theme_name="유코사스미 치밀한 복수_양산점", JIJEM="S3", theme_num=3, theme_id=1575),
            MurderParkerTheme(theme_name="오씨네 장난감 가게_양산점", JIJEM="S3", theme_num=4, theme_id=1574),
            MurderParkerTheme(theme_name="언타이틀(Untitle)_양산점", JIJEM="S3", theme_num=5, theme_id=1576),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S4",
        theme_list=[
            MurderParkerTheme(theme_name="제임스 완벽한 도피_전주 3호점", JIJEM="S4", theme_num=1, theme_id=1618),
            MurderParkerTheme(theme_name="박엠마 엄마의 향기_전주 3호점", JIJEM="S4", theme_num=2, theme_id=1619),
            MurderParkerTheme(theme_name="김파커 끝없는 복수_전주 3호점", JIJEM="S4", theme_num=3, theme_id=1620),
            MurderParkerTheme(theme_name="박마담의 비밀 클럽_전주 3호점", JIJEM="S4", theme_num=4, theme_id=1621),
            MurderParkerTheme(theme_name="전당포 불편한 거래_전주 3호점", JIJEM="S4", theme_num=5, theme_id=1622),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S5",
        theme_list=[
            MurderParkerTheme(theme_name="PC방 가는 길(Premium)_대구점", JIJEM="S5", theme_num=1, theme_id=1248),
            MurderParkerTheme(theme_name="괴짜중딩 사차원_대구점", JIJEM="S5", theme_num=2, theme_id=1249),
            MurderParkerTheme(theme_name="백_대구점", JIJEM="S5", theme_num=3, theme_id=1250),
            MurderParkerTheme(theme_name="파커vs파커(Premium)_대구점", JIJEM="S5", theme_num=4, theme_id=1251),
            MurderParkerTheme(theme_name="8585세탁소_대구점", JIJEM="S5", theme_num=5, theme_id=1252),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S6",
        theme_list=[
            MurderParkerTheme(theme_name="음대출신 김수학_건대점", JIJEM="S6", theme_num=1, theme_id=181),
            MurderParkerTheme(theme_name="파커4(80분 Premium)_건대점", JIJEM="S6", theme_num=2, theme_id=182),
            MurderParkerTheme(theme_name="우리 꼰대 진분홍_건대점", JIJEM="S6", theme_num=3, theme_id=183),
            MurderParkerTheme(theme_name="여행(70분 Premium)_건대점", JIJEM="S6", theme_num=4, theme_id=184),
            MurderParkerTheme(theme_name="꽁노리_건대점", JIJEM="S6", theme_num=5, theme_id=186),
            MurderParkerTheme(theme_name="어은꿈이진루다_건대점", JIJEM="S6", theme_num=6, theme_id=185),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S7",
        theme_list=[
            MurderParkerTheme(theme_name="파커투_광주점", JIJEM="S7", theme_num=1, theme_id=1713),
            MurderParkerTheme(theme_name="머더파커 광주점의 비밀_광주점", JIJEM="S7", theme_num=2, theme_id=1709),
            MurderParkerTheme(theme_name="선물_광주점", JIJEM="S7", theme_num=3, theme_id=1710),
            MurderParkerTheme(theme_name="포수 장덕팔_광주점", JIJEM="S7", theme_num=4, theme_id=1712),
            MurderParkerTheme(theme_name="한림축산_광주점", JIJEM="S7", theme_num=5, theme_id=1711),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S8",
        theme_list=[
            MurderParkerTheme(theme_name="동창회(3인이상가능 Premium)_건대2호점", JIJEM="S8", theme_num=1, theme_id=187),
            MurderParkerTheme(theme_name="이상한 하루_건대2호점", JIJEM="S8", theme_num=2, theme_id=188),
            MurderParkerTheme(theme_name="R003(45분 혼방)_건대 2호점", JIJEM="S8", theme_num=3, theme_id=189),
            MurderParkerTheme(theme_name="동물병원_건대 2호점", JIJEM="S8", theme_num=4, theme_id=191),
            MurderParkerTheme(theme_name="5010(60분 혼방)_건대 2호점", JIJEM="S8", theme_num=5, theme_id=190),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S9",
        theme_list=[
            MurderParkerTheme(theme_name="구둣방손님_홍대1호점", JIJEM="S9", theme_num=1, theme_id=349),
            MurderParkerTheme(theme_name="밴드의 탄생_홍대1호점", JIJEM="S9", theme_num=2, theme_id=351),
            MurderParkerTheme(theme_name="주마등_홍대1호점", JIJEM="S9", theme_num=3, theme_id=353),
            MurderParkerTheme(theme_name="칠칠77(70분 프리미엄)_홍대1호점", JIJEM="S9", theme_num=4, theme_id=352),
            MurderParkerTheme(theme_name="엠M(70분 혼방)_홍대1호점", JIJEM="S9", theme_num=5, theme_id=350),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S10",
        theme_list=[
            MurderParkerTheme(theme_name="도레미용실_대구2호점", JIJEM="S10", theme_num=1, theme_id=1256),
            MurderParkerTheme(theme_name="전국일이삼 70분_대구2호점", JIJEM="S10", theme_num=2, theme_id=1255),
            MurderParkerTheme(theme_name="타겟(target) 70분_대구 2호점", JIJEM="S10", theme_num=3, theme_id=1253),
            MurderParkerTheme(theme_name="사건의 재구성(70분 Premium)_대구 2호점", JIJEM="S10", theme_num=4, theme_id=1254),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S11",
        theme_list=[
            MurderParkerTheme(theme_name="집으로 가자 야호!(70분)_잠실점", JIJEM="S11", theme_num=1, theme_id=243),
            MurderParkerTheme(theme_name="두목 이스케이프(70분)_잠실점", JIJEM="S11", theme_num=2, theme_id=245),
            MurderParkerTheme(theme_name="정육각형(70분)_잠실점", JIJEM="S11", theme_num=3, theme_id=244),
        ],
    ),
    MurderParkerCafe(
        url="http://murderparker.com/sub_02/sub02_1.html?JIJEM=S12",
        theme_list=[
            MurderParkerTheme(theme_name="레디(Ready) 70분_부산점", JIJEM="S12", theme_num=1, theme_id=1446),
            MurderParkerTheme(theme_name="도굴왕 70분 프리미엄_부산점", JIJEM="S12", theme_num=2, theme_id=1447),
            MurderParkerTheme(theme_name="액션(Action) 70분_부산점", JIJEM="S12", theme_num=3, theme_id=1448),
            MurderParkerTheme(theme_name="사라진 보물2056 70분_부산점", JIJEM="S12", theme_num=4, theme_id=1449),
            MurderParkerTheme(theme_name="잭(JACK) 70분 프리미엄_부산점", JIJEM="S12", theme_num=5, theme_id=1450),
        ],
    ),
]
