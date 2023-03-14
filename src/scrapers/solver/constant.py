from typing import Final


class SolverTheme:

    def __init__(self, theme_name: str, JIJEM: str, theme_num: int, theme_id: int):
        self.theme_name = theme_name
        self.JIJEM = JIJEM
        self.theme_num = theme_num
        self.theme_id = theme_id


class SolverCafe:
    def __init__(self, url: str, theme_list: list[SolverTheme]):
        self.url = url
        self.theme_list = theme_list


SOLVER_CAFE_LIST: Final = [
    SolverCafe(
        url="http://solver-gd.com/sub/03_1.html",
        theme_list=[
            SolverTheme(theme_name="LUCID DREAM (자각몽)", JIJEM="S1", theme_num=1, theme_id=204),
            SolverTheme(theme_name="COLD CASE (미제 사건)", JIJEM="S1", theme_num=2, theme_id=205),
            SolverTheme(theme_name="THE CAGE (케이지)", JIJEM="S1", theme_num=3, theme_id=206),
        ],
    ),
    SolverCafe(
        url="http://solver-gd.com/sub/03_1.html",
        theme_list=[
            SolverTheme(theme_name="Dear Marsy(마르시)", JIJEM="S2", theme_num=1, theme_id=207),
            SolverTheme(theme_name="이층 복도 끝 화장실", JIJEM="S2", theme_num=2, theme_id=208),
            SolverTheme(theme_name="무채색 인간", JIJEM="S2", theme_num=3, theme_id=209),
        ],
    ),
]
