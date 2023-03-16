from typing import Final

GET_XPHOBIA_URL_GET_TIME_META: Final = "https://www.xphobia.net/reservation/ck_date2_no1.php"
GET_XPHOBIA_URL_GET_TIME: Final = "https://www.xphobia.net/reservation/ck_date_no1.php"


class XphobiaTheme:
    def __init__(self, quest: str, theme_id: int):
        self.quest = quest
        self.theme_id = theme_id


class XphobiaCafe:
    def __init__(self, shop: str, theme_list: list[XphobiaTheme]):
        self.shop = shop
        self.theme_list = theme_list


XPHOBIA_CAFE_LIST = [
    XphobiaCafe(
        shop="던전101",
        theme_list=[
            XphobiaTheme(quest="MST 엔터테인먼트", theme_id=372),
            XphobiaTheme(quest="렛츠 플레이", theme_id=373),
            XphobiaTheme(quest="전래동 : 자살사건", theme_id=371),
            XphobiaTheme(quest="화생설화 : Blooming", theme_id=370),
        ]
    ),
    XphobiaCafe(
        shop="강남 던전",
        theme_list=[
            XphobiaTheme(quest="LOST KINGDOM : 잊혀진 전설", theme_id=66),
            XphobiaTheme(quest="강남목욕탕", theme_id=69),
            XphobiaTheme(quest="대호시장 살인사건", theme_id=68),
            XphobiaTheme(quest="마음을 그려드립니다", theme_id=67),
        ]
    ),
    XphobiaCafe(
        shop="강남 던전Ⅱ",
        theme_list=[
            XphobiaTheme(quest="LOST KINGDOM2 : 대탐험의 시작", theme_id=70),
            XphobiaTheme(quest="MAYDAY", theme_id=71),
        ]
    ),
    XphobiaCafe(
        shop="서면 던전",
        theme_list=[
            XphobiaTheme(quest="꿈의 공장", theme_id=1485),
            XphobiaTheme(quest="날씨의 신", theme_id=1486),
            XphobiaTheme(quest="오늘 나는", theme_id=1484),
        ]
    ),
    XphobiaCafe(
        shop="홍대 던전",
        theme_list=[
            XphobiaTheme(quest="꿈의 공장", theme_id=376),
            XphobiaTheme(quest="날씨의 신", theme_id=375),
            XphobiaTheme(quest="사라진 보물 : 대저택의 비밀", theme_id=377),
            XphobiaTheme(quest="오늘 나는", theme_id=374),
        ]
    ),
    XphobiaCafe(
        shop="Phobia 서면",
        theme_list=[
            XphobiaTheme(quest="Bar Solvay", theme_id=1483),
            XphobiaTheme(quest="고시원 살인사건", theme_id=1481),
            XphobiaTheme(quest="당감동 정육점", theme_id=1480),
            XphobiaTheme(quest="부활", theme_id=1478),
            XphobiaTheme(quest="산장으로의 초대", theme_id=1477),
            XphobiaTheme(quest="엘도라도", theme_id=1479),
            XphobiaTheme(quest="지하터널-2H", theme_id=1482),
        ]
    ),
    XphobiaCafe(
        shop="Phobia 동성로",
        theme_list=[
            XphobiaTheme(quest="Trade 동성로", theme_id=1279),
            XphobiaTheme(quest="모자가게의 비밀", theme_id=1281),
            XphobiaTheme(quest="심야식당", theme_id=1283),
            XphobiaTheme(quest="쏘우", theme_id=1276),
            XphobiaTheme(quest="용의선상", theme_id=1280),
            XphobiaTheme(quest="웃는 남자", theme_id=1277),
            XphobiaTheme(quest="잭 더 리퍼 동성로 1", theme_id=1282),
            XphobiaTheme(quest="잭 더 리퍼 동성로 2", theme_id=1282),
            XphobiaTheme(quest="테러 라이브 동성로", theme_id=1278),
        ]
    ),
    XphobiaCafe(
        shop="Phobia 신림",
        theme_list=[
            XphobiaTheme(quest="Neverland를 찾아서", theme_id=590),
            XphobiaTheme(quest="Sex appeal", theme_id=587),
            XphobiaTheme(quest="SPLIT", theme_id=589),
            XphobiaTheme(quest="Swing gate", theme_id=588),
        ]
    ),
    XphobiaCafe(
        shop="Phobia 명동",
        theme_list=[
            XphobiaTheme(quest="Time Slip", theme_id=528),  # 실제로는 오늘밤 주인공은 나야 나 를 지칭!!!!!!!!
            XphobiaTheme(quest="그 남자 그 여자", theme_id=529),
            XphobiaTheme(quest="도깨비", theme_id=527),
        ]
    ),
    XphobiaCafe(
        shop="Phobia 대학로",
        theme_list=[
            XphobiaTheme(quest="구룡 잠들지 않는 도시", theme_id=502),
            XphobiaTheme(quest="이런 변이 있나", theme_id=500),
            XphobiaTheme(quest="이일호씨", theme_id=499),
            XphobiaTheme(quest="잭 더 리퍼", theme_id=498),
            XphobiaTheme(quest="지금 만나러 갑니다", theme_id=501),
        ]
    )
]
