from typing import Final


class SecretCodeTheme:

    def __init__(self, theme_name: str, JIJEM: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.JIJEM = JIJEM
        self.theme_num = theme_num
        self.theme_id = theme_id


class SecretCodeCafe:
    def __init__(self, url: str, theme_list: list[SecretCodeTheme]):
        self.url = url
        self.theme_list = theme_list


SECRET_CODE_CAFE_LIST: Final = [
    SecretCodeCafe(
        url="http://www.s-code.co.kr/sub_02/sub02_1.html",
        theme_list=[
            SecretCodeTheme(theme_name="백마교의 최후", JIJEM="S3", theme_num=1, theme_id=397),
            SecretCodeTheme(theme_name="제페토", JIJEM="S3", theme_num=2, theme_id=394),
            SecretCodeTheme(theme_name="독립군", JIJEM="S3", theme_num=3, theme_id=395),
            SecretCodeTheme(theme_name="조난자들", JIJEM="S3", theme_num=4, theme_id=392),
            SecretCodeTheme(theme_name="미션", JIJEM="S3", theme_num=5, theme_id=396),
        ],
    ),
]
