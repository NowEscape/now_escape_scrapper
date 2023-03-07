from typing import Final, Dict

DPS_URL: Final = "https://www.dpsnnn.com/reserve"


class DPSTheme:

    def __init__(self, theme_name: str, theme_id: int):
        self.theme_name = theme_name
        self.theme_id = theme_id


class DPSCafe:
    def __init__(self, theme_list: list[DPSTheme]):
        self.theme_list = theme_list


DPS_THEME_LIST: Final = [
    DPSTheme(theme_name="상자", theme_id=57),
    DPSTheme(theme_name="행복", theme_id=58),
]

# DPS_CAFE_LIST: Final = [
#     DPSCafe(
#         theme_list=[
#             DPSTheme(theme_name="상자", theme_id=57),
#             DPSTheme(theme_name="행복", theme_id=58),
#         ],
#     ),
# ]
