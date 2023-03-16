from typing import Final

ESCAPERS_URL: Final = "https://escapersd.com/reservation/theme"


class EscapersTheme:
    def __init__(self, themePK: int, theme_id: int):
        self.themePK = themePK
        self.theme_id = theme_id


class EscapersCafe:
    def __init__(self, name: str, theme_list: list[EscapersTheme]):
        self.name = name
        self.theme_list = theme_list
