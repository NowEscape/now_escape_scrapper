from typing import Final, Dict

KEY_ESCAPE_URL: Final = "https://keyescape.co.kr/web/home.php?go=rev.make"


class NextEditionTheme:

    def __init__(self, theme_name: str, theme_id: int):
        self.theme_name = theme_name
        self.theme_id = theme_id


class NextEditionCafe:
    def __init__(self, url: str, theme_list: list[NextEditionTheme]):
        self.url = url
        self.theme_list = theme_list


NEXT_EDITION_CAFE_LIST: Final = [
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/NextEdition%20Sinchon",
        theme_list=[
            NextEditionTheme(theme_name="화이트룸 (Original)", theme_id=274),
            NextEditionTheme(theme_name="더 매직", theme_id=273),
            NextEditionTheme(theme_name="13여고괴담", theme_id=272),
            NextEditionTheme(theme_name="천사와 악마", theme_id=269),
            NextEditionTheme(theme_name="그레이 in 인셉션 (19금)", theme_id=271),
            NextEditionTheme(theme_name="인디아나존스", theme_id=270),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/NextEdition%20Gundae",
        theme_list=[
            NextEditionTheme(theme_name="SOUL CHASER - 실종", theme_id=152),
            NextEditionTheme(theme_name="썸", theme_id=154),
            NextEditionTheme(theme_name="다시봄", theme_id=155),
            NextEditionTheme(theme_name="MONSTER:10800", theme_id=157),
            NextEditionTheme(theme_name="B아파트 13동 1313호", theme_id=156),
            NextEditionTheme(theme_name="이불밖은 위험해", theme_id=153),
        ],
    ),
]
