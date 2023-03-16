from typing import Final

AMAZED_URL: Final = "http://www.amazed.co.kr/wp-admin/admin-ajax.php"


class AmazedTheme:

    def __init__(self, theme_name: str, calendar_id: int, theme_id: int):
        self.theme_name = theme_name
        self.calendar_id = calendar_id
        self.theme_id = theme_id


class AmazedCafe:
    def __init__(self, theme_list: list[AmazedTheme]):
        self.theme_list = theme_list


AMAZED_CAFE_LIST: Final = [
    AmazedCafe(
        theme_list=[
            AmazedTheme(theme_name="이탈리안잡", calendar_id=8, theme_id=1036),
            AmazedTheme(theme_name="하시마", calendar_id=13, theme_id=1038),
            AmazedTheme(theme_name="REC", calendar_id=12, theme_id=1037),
        ],
    ),
]
