from typing import Final


class DumbNdumberTheme:

    def __init__(self, theme_name: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.theme_num = theme_num
        self.theme_id = theme_id


class DumbNdumberCafe:
    def __init__(self, location: str, url: str, theme_list: list[DumbNdumberTheme]):
        self.location = location
        self.url = url
        self.theme_list = theme_list


DUMB_N_DUMBER_CAFE_LIST: Final = [
    DumbNdumberCafe(
        location="대학로점",
        url="http://www.dumbndumber.kr/reservation.html?k_shopno=1&prdno=&rdate=",
        theme_list=[
            DumbNdumberTheme(theme_name="작전명: 옵저버", theme_num=6, theme_id=476),
            DumbNdumberTheme(theme_name="크라임시티", theme_num=7, theme_id=475),
            DumbNdumberTheme(theme_name="투 앨리스", theme_num=8, theme_id=478),
            DumbNdumberTheme(theme_name="푸른수염", theme_num=9, theme_id=479),
            DumbNdumberTheme(theme_name="글램핑", theme_num=10, theme_id=474),
            DumbNdumberTheme(theme_name="러브클리닉", theme_num=11, theme_id=477),
        ],
    ),
    DumbNdumberCafe(
        location="홍대점",
        url="http://www.dumbndumber.kr/reservation.html?k_shopno=2&prdno=&rdate=",
        theme_list=[
            DumbNdumberTheme(theme_name="오므라이스", theme_num=6, theme_id=325),
            DumbNdumberTheme(theme_name="소공녀", theme_num=7, theme_id=326),
            DumbNdumberTheme(theme_name="버킷리스트", theme_num=8, theme_id=328),
            DumbNdumberTheme(theme_name="기담", theme_num=9, theme_id=323),
            DumbNdumberTheme(theme_name="Knock Knock", theme_num=10, theme_id=327),
            DumbNdumberTheme(theme_name="마리오네뜨", theme_num=11, theme_id=324),
            DumbNdumberTheme(theme_name="휴가중", theme_num=12, theme_id=322),
        ],
    ),
    DumbNdumberCafe(
        location="서면점",
        url="http://www.dumbndumber-sm.kr/reservation.html?k_shopno=3&prdno=&rdate=",
        theme_list=[
            DumbNdumberTheme(theme_name="소공녀", theme_num=6, theme_id=1418),
            DumbNdumberTheme(theme_name="러브클리닉", theme_num=7, theme_id=1419),
            DumbNdumberTheme(theme_name="투 앨리스", theme_num=8, theme_id=1420),
            DumbNdumberTheme(theme_name="글램핑A", theme_num=9, theme_id=1421),
            DumbNdumberTheme(theme_name="글램핑B", theme_num=10, theme_id=1797),
            DumbNdumberTheme(theme_name="동전노래방", theme_num=11, theme_id=1422),
            DumbNdumberTheme(theme_name="작전명: 옵저버", theme_num=12, theme_id=1423),
            DumbNdumberTheme(theme_name="휴가중", theme_num=13, theme_id=1424),
            DumbNdumberTheme(theme_name="Knock Knock", theme_num=14, theme_id=1425),
            DumbNdumberTheme(theme_name="기담", theme_num=15, theme_id=1426),
            DumbNdumberTheme(theme_name="크라임시티", theme_num=16, theme_id=1427),
            DumbNdumberTheme(theme_name="푸른수염", theme_num=17, theme_id=1428),
            DumbNdumberTheme(theme_name="X테마", theme_num=18, theme_id=1429),
        ],
    ),
]
