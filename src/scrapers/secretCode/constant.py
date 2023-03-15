from typing import Final


class SecretCodeTheme:

    def __init__(self, theme_name: str, url: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.url = url
        self.theme_num = theme_num
        self.theme_id = theme_id


class SecretCodeCafe:
    def __init__(self, theme_list: list[SecretCodeTheme]):
        self.theme_list = theme_list


SECRET_CODE_CAFE_LIST: Final = [
    SecretCodeCafe(
        theme_list=[
            SecretCodeTheme(theme_name="백마교의 최후", url="http://www.s-code.co.kr/sub_02/sub02_1.html?JIJEM=S3&D_ROOM=A&H_DATE=", theme_num=1, theme_id=397),
            SecretCodeTheme(theme_name="제페토", url="http://www.s-code.co.kr/sub_02/sub02_1.html?JIJEM=S3&D_ROOM=B&H_DATE=", theme_num=2, theme_id=394),
            SecretCodeTheme(theme_name="독립군", url="http://www.s-code.co.kr/sub_02/sub02_1.html?JIJEM=S3&D_ROOM=C&H_DATE=", theme_num=3, theme_id=395),
            SecretCodeTheme(theme_name="조난자들", url="http://www.s-code.co.kr/sub_02/sub02_1.html?JIJEM=S3&D_ROOM=D&H_DATE=", theme_num=4, theme_id=392),
            SecretCodeTheme(theme_name="미션", url="http://www.s-code.co.kr/sub_02/sub02_1.html?JIJEM=S3&D_ROOM=E&H_DATE=", theme_num=5, theme_id=396),
        ],
    ),
]
