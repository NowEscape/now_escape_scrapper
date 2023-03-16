from typing import Final

MASTER_KEY_URL: Final = "http://www.master-key.co.kr/booking/booking_list_new"


class MasterKeyTheme:
    def __init__(self, name: str, theme_id: int):
        self.name = name
        self.theme_id = theme_id


class MasterKeyCafe:

    def __init__(self, name: str, store_id: int, theme_list: list[MasterKeyTheme]):
        self.name = name
        self.store_id = store_id
        self.theme_list = theme_list


MASTER_KEY_CAFE_LIST = [
    MasterKeyCafe(
        name="궁동직영점",
        store_id=1,
        theme_list=[
            MasterKeyTheme(name="MSI 미제사건 전담반", theme_id=1141),
            MasterKeyTheme(name="재심", theme_id=1140),
            MasterKeyTheme(name="MK빌딩을털어라:45C6", theme_id=1142),
            MasterKeyTheme(name="블랙룸", theme_id=1138),
            MasterKeyTheme(name="화이트룸", theme_id=1139)
        ]
    ),
    MasterKeyCafe(
        name="은행직영점",
        store_id=2,
        theme_list=[
            MasterKeyTheme(name="그레이트월", theme_id=1137),
            MasterKeyTheme(name="편지", theme_id=1135),
            # MasterKeyTheme(name="1990", theme_id=), db에 없는 테마
            MasterKeyTheme(name="대탈출2", theme_id=1134),
            MasterKeyTheme(name="REC", theme_id=1136),
        ]
    ),
]
