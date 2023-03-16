from typing import Final, Dict


class ZeroWorldTheme:

    def __init__(self, theme_name: str, theme_id: int):
        self.theme_name = theme_name
        self.theme_id = theme_id


class ZeroWorldCafe:
    def __init__(self, url: str, theme_list: list[ZeroWorldTheme]):
        self.url = url
        self.theme_list = theme_list


ZERO_WORLD_CAFE_LIST: Final = [
    ZeroWorldCafe(
        url="https://zerogangnam.com/reservation",
        theme_list=[
            ZeroWorldTheme(theme_name="[강남] 링", theme_id=111),
            ZeroWorldTheme(theme_name="[강남] 나비효과", theme_id=110),
            ZeroWorldTheme(theme_name="[강남] 콜러", theme_id=109),
            ZeroWorldTheme(theme_name="[강남] 어느겨울밤2", theme_id=108),
            ZeroWorldTheme(theme_name="[강남] 아이엠", theme_id=107),
            ZeroWorldTheme(theme_name="[강남] 제로호텔L", theme_id=112),
            ZeroWorldTheme(theme_name="[강남] DONE", theme_id=113),
            ZeroWorldTheme(theme_name="[강남] 포레스트 (FORREST)", theme_id=114),
            ZeroWorldTheme(theme_name="[강남] 헐!", theme_id=115),
        ],
    ),
    ZeroWorldCafe(
        url="https://zeroesc.com/reservation",
        theme_list=[
            ZeroWorldTheme(theme_name="[김포] 제로호텔", theme_id=958),
            ZeroWorldTheme(theme_name="[김포] 탈옥:특별수용소", theme_id=957),
            ZeroWorldTheme(theme_name="[김포] 어느겨울밤", theme_id=956),
            ZeroWorldTheme(theme_name="[김포] 인형괴담", theme_id=952),
            ZeroWorldTheme(theme_name="[김포] 성역전설", theme_id=953),
            ZeroWorldTheme(theme_name="[김포] 피아노", theme_id=955),
            ZeroWorldTheme(theme_name="[김포] 최면", theme_id=959),
            ZeroWorldTheme(theme_name="[김포] 복희네 사진관", theme_id=954),
            ZeroWorldTheme(theme_name="[김포] 피노키오 대탈출", theme_id=951),
            ZeroWorldTheme(theme_name="[김포] 검은사원", theme_id=950),
            ZeroWorldTheme(theme_name="[김포] 해리포터의 모험:마법모자의 위기", theme_id=949),
        ],
    ),
    ZeroWorldCafe(
        url="https://zerolotteworld.com/reservation",
        theme_list=[
            ZeroWorldTheme(theme_name="[롯데]바람_우리는 그저 바람이었소", theme_id=263),
            ZeroWorldTheme(theme_name="[롯데] 아랑_굶주린이리", theme_id=262),
        ],
    ),
]
