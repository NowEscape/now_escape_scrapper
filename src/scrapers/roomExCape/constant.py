from typing import Final

ROOM_EX_CAPE_URL: Final = "http://www.ex-cape.com/sub/questAjax.php"


class RoomExCapeTheme:
    def __init__(self, name: str, code: int, theme_id: int):
        self.name = name
        self.code = code
        self.theme_id = theme_id


class RoomExCapeCafe:

    def __init__(self, name: str, theme_list: list[RoomExCapeTheme]):
        self.name = name
        self.theme_list = theme_list


ROOM_EX_CAPE_CAFE_LIST = [
    RoomExCapeCafe(
        name="신촌2호점",
        theme_list=[
            RoomExCapeTheme(name="마카오 : 꼭두각시 광시곡", code=29, theme_id=294),
            RoomExCapeTheme(name="23번째 실험연구 : 알비노", code=27, theme_id=293),
            RoomExCapeTheme(name="대저택 레테 잠겨버린 출구", code=24, theme_id=292),
            RoomExCapeTheme(name="신비로운 호빗의 집", code=21, theme_id=291),
            RoomExCapeTheme(name="비폴로 17호-우주로의 확장", code=20, theme_id=290),
        ]
    ),
    RoomExCapeCafe(
        name="신촌지점",
        theme_list=[

            RoomExCapeTheme(name="에이전트 : 노출된 미션", code=15, theme_id=284),
            RoomExCapeTheme(name="어느 구두쇠의 전시회장", code=14, theme_id=283),
            RoomExCapeTheme(name="트레져쉽 : 신화 속의 존재", code=13, theme_id=285),
            RoomExCapeTheme(name="냥이점집", code=12, theme_id=286),
        ]
    ),
    RoomExCapeCafe(
        name="올리브점",
        theme_list=[
            RoomExCapeTheme(name="JUDGE : 정의 집행", code=35, theme_id=288),
            RoomExCapeTheme(name="오즈 : 익시드 드림", code=30, theme_id=287),
        ]
    ),
]
