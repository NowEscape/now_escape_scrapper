from typing import Final

FANTASTRICK_URL: Final = "http://fantastrick.co.kr/wp-admin/admin-ajax.php"


class FantastrickTheme:

    def __init__(self, theme_name: str, calendar_id: int, action: str, theme_id: int):
        self.theme_name = theme_name
        self.calendar_id = calendar_id
        self.action = action
        self.theme_id = theme_id


FANTASTRICK_THEME_LIST: Final = [
        FantastrickTheme(theme_name="태초의 신부", calendar_id=17, action="booked_calendar_date", theme_id=143),
        FantastrickTheme(theme_name="사자의 서", calendar_id=23, action="booked_calendar_date", theme_id=1794),
]
