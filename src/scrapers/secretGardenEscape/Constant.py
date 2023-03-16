# 비밀의 화원 url 상수
SECRET_GARDEN_URL = 'http://m.secretgardenescape.com/reservation.html?k_shopno={SHOP_NO}&rdate={DATE}'


class SecretGardenTheme:

    def __init__(self, theme_name: str, theme_id: int):
        self.theme_name = theme_name
        self.theme_id = theme_id


class SecretGardenCafe:
    def __init__(self, name: str, shop_no: int, theme_list: list[SecretGardenTheme]):
        self.name = name
        self.shop_no = shop_no
        self.theme_list = theme_list


SECRET_GARDEN_CAFE_LIST = [
    SecretGardenCafe(
        name="다운타운 홍대",
        shop_no=2,
        theme_list=[
            SecretGardenTheme(theme_name="Promesa", theme_id=386),
            SecretGardenTheme(theme_name="BOSS : COMPANY_LU", theme_id=387),
        ]
    ),

    SecretGardenCafe(
        name="서면점",
        shop_no=3,
        theme_list=[
            SecretGardenTheme(theme_name="아뜰리에", theme_id=1470),
            SecretGardenTheme(theme_name="비밀의 화원", theme_id=1471),
            SecretGardenTheme(theme_name="연애학개론", theme_id=1473),
            SecretGardenTheme(theme_name="컬러즈", theme_id=1476),
            SecretGardenTheme(theme_name="블라인드", theme_id=1474),
            SecretGardenTheme(theme_name="베이비 레이스", theme_id=1472),
            SecretGardenTheme(theme_name="슈퍼 엔지니어", theme_id=1475),
        ]
    ),

    SecretGardenCafe(
        name="대학로점",
        shop_no=4,
        theme_list=[
            SecretGardenTheme(theme_name="비밀의 모험", theme_id=494),
            SecretGardenTheme(theme_name="슈퍼플레이어:PLAYER1", theme_id=493),
            SecretGardenTheme(theme_name="엑스튜브", theme_id=495),
            SecretGardenTheme(theme_name="대감댁변씨", theme_id=492),
            SecretGardenTheme(theme_name="나이스", theme_id=496),
            SecretGardenTheme(theme_name="혜화애(야외테마)", theme_id=497),
        ]
    ),
    SecretGardenCafe(
        name="건대점",
        shop_no=5,
        theme_list=[
            SecretGardenTheme(theme_name="비밀의 선물", theme_id=192),
            SecretGardenTheme(theme_name="우리의 전 사랑", theme_id=193),
            SecretGardenTheme(theme_name="레드림 컴퍼니", theme_id=194),
            SecretGardenTheme(theme_name="안녕", theme_id=195),
            SecretGardenTheme(theme_name="우끼끼", theme_id=196),
            SecretGardenTheme(theme_name="핑크슈즈", theme_id=197),
        ]
    ),
    SecretGardenCafe(
        name="동성로점",
        shop_no=6,
        theme_list=[
            SecretGardenTheme(theme_name="리비도", theme_id=1272),
            SecretGardenTheme(theme_name="대×9탈출", theme_id=1273),
            SecretGardenTheme(theme_name="안녕", theme_id=1269),
            SecretGardenTheme(theme_name="비밀의 선물", theme_id=1270),
            SecretGardenTheme(theme_name="대감댁 변씨", theme_id=1271),
            SecretGardenTheme(theme_name="영웅을 찾아서", theme_id=1274),
            SecretGardenTheme(theme_name="향수 2019", theme_id=1275),
        ]
    ),
    SecretGardenCafe(
        name="미드나잇 합정",
        shop_no=7,
        theme_list=[
            SecretGardenTheme(theme_name="비밀의 가족", theme_id=383),
            SecretGardenTheme(theme_name="파리82", theme_id=384),
            SecretGardenTheme(theme_name="팩토리 엠", theme_id=385),
            SecretGardenTheme(theme_name="기다려, 금방 갈게[야외]", theme_id=382),
        ]
    ),

    SecretGardenCafe(
        name="포레스트 건대",
        shop_no=8,
        theme_list=[
            SecretGardenTheme(theme_name="아인모스", theme_id=203),
            SecretGardenTheme(theme_name="미씽 스노우맨", theme_id=198),
            SecretGardenTheme(theme_name="새벽 베이커리", theme_id=199),
            SecretGardenTheme(theme_name="너의 성인식", theme_id=200),
            SecretGardenTheme(theme_name="라스트 잡", theme_id=201),
            SecretGardenTheme(theme_name="스물아홉", theme_id=202),
        ]
    ),

    SecretGardenCafe(
        name="리버타운 강남",
        shop_no=9,
        theme_list=[
            SecretGardenTheme(theme_name="무고", theme_id=59),
            SecretGardenTheme(theme_name="스토커", theme_id=60),
            SecretGardenTheme(theme_name="후레쉬망고 호스텔 (03/09~)", theme_id=64),
            SecretGardenTheme(theme_name="Z", theme_id=65),
            SecretGardenTheme(theme_name="브로커 나씨", theme_id=61),
            SecretGardenTheme(theme_name="만화 : 늦게 피어난 꽃", theme_id=63),
        ]
    ),
    SecretGardenCafe(
        name="광주점",
        shop_no=10,
        theme_list=[
            SecretGardenTheme(theme_name="무고", theme_id=1714),
            SecretGardenTheme(theme_name="리비도", theme_id=1715),
            SecretGardenTheme(theme_name="스토커", theme_id=1716),
            SecretGardenTheme(theme_name="새벽 베이커리", theme_id=1717),
            SecretGardenTheme(theme_name="비밀의 가족", theme_id=1718),
            SecretGardenTheme(theme_name="라스트 잡", theme_id=1719),
            SecretGardenTheme(theme_name="Love Blossom", theme_id=1720),
        ]
    ),
    SecretGardenCafe(
        name="시네마틱 혜화",
        shop_no=11,
        theme_list=[
            SecretGardenTheme(theme_name="H.E.L.L.P", theme_id=485),
            SecretGardenTheme(theme_name="달 : 기억의 조각", theme_id=486),
            SecretGardenTheme(theme_name="딜레마", theme_id=491),
            SecretGardenTheme(theme_name="도망자 여씨", theme_id=490),
            SecretGardenTheme(theme_name="삼남매 이씨", theme_id=487),  # TODO: 장녀, 차녀, 막내 db에서 구분 없애야 함!!!
        ]
    ),
    SecretGardenCafe(
        name="전주점",
        shop_no=12,
        theme_list=[
            SecretGardenTheme(theme_name="달 : 기억의 조각", theme_id=1623),
            SecretGardenTheme(theme_name="사춘기", theme_id=1624),
            SecretGardenTheme(theme_name="담력학원", theme_id=1625),
        ]
    )
]
