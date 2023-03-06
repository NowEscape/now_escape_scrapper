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
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/NextEdition%20Bucheon",
        theme_list=[
            NextEditionTheme(theme_name="주르륵", theme_id=963),
            NextEditionTheme(theme_name="쌩얼", theme_id=962),
            NextEditionTheme(theme_name="집으로", theme_id=961),
            NextEditionTheme(theme_name="진시황", theme_id=960),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/NextEdition%20Bupyung",
        theme_list=[
            NextEditionTheme(theme_name="로렌시아 - 잠들어버린 섬", theme_id=993),
            NextEditionTheme(theme_name="이상", theme_id=992),
            NextEditionTheme(theme_name="배틀쉽 프로젝트 B", theme_id=991),
            NextEditionTheme(theme_name="배틀쉽 프로젝트 A", theme_id=991),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/NextEdition%20Gangnam",
        theme_list=[
            NextEditionTheme(theme_name="저니(JOURNEY)", theme_id=6),
            NextEditionTheme(theme_name="MEMORY - Episode 1", theme_id=2),
            NextEditionTheme(theme_name="완전한사랑(리뉴얼)", theme_id=3),
            NextEditionTheme(theme_name="흐린날", theme_id=4),
            NextEditionTheme(theme_name="카르텔", theme_id=5),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/NextEdition%20Gundae2",
        theme_list=[
            NextEditionTheme(theme_name="어제, 그리고 오늘", theme_id=162),
            NextEditionTheme(theme_name="Make-up", theme_id=160),
            NextEditionTheme(theme_name="동화나라 수비대", theme_id=159),
            NextEditionTheme(theme_name="빛을 구해줘", theme_id=161),
            NextEditionTheme(theme_name="방탈출 아카데미", theme_id=163),
            NextEditionTheme(theme_name="커튼콜", theme_id=158),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/Nextedition%20Gangnam2",
        theme_list=[
            NextEditionTheme(theme_name="마법소녀", theme_id=11),
            NextEditionTheme(theme_name="중대장은 오늘 너희에게 무척 실망했다.", theme_id=7),
            NextEditionTheme(theme_name="커넥트 (Connect)", theme_id=10),
            NextEditionTheme(theme_name="심판", theme_id=8),
            NextEditionTheme(theme_name="퀴즈 인 더 노블 (Quiz in The Noble)", theme_id=9),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/Nextedition%20Bundangseohyun",
        theme_list=[
            NextEditionTheme(theme_name="너에게 가는 길", theme_id=820),
            NextEditionTheme(theme_name="평범한 하루", theme_id=821),
            NextEditionTheme(theme_name="짠해", theme_id=819),
            NextEditionTheme(theme_name="몽중몽", theme_id=818),
            NextEditionTheme(theme_name="테마명을 뭐로할지 못정하겠어요ㅠㅠ", theme_id=816),
            NextEditionTheme(theme_name="익명의 여자", theme_id=817),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/Nextedition%20Gangnam3",
        theme_list=[
            NextEditionTheme(theme_name="크리쳐 - 신인류의 탄생", theme_id=15),
            NextEditionTheme(theme_name="마지막 일주", theme_id=14),
            NextEditionTheme(theme_name="안녕하세요? 무엇을 도와드릴까요?", theme_id=16),
            NextEditionTheme(theme_name="야근", theme_id=12),
            NextEditionTheme(theme_name="첫만남", theme_id=13),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/Nextedition%20Sinlim",
        theme_list=[
            NextEditionTheme(theme_name="극", theme_id=577),
            NextEditionTheme(theme_name="씨프?? XX!!", theme_id=576),
            NextEditionTheme(theme_name="Tester", theme_id=575),
            NextEditionTheme(theme_name="LOVER", theme_id=574),
            NextEditionTheme(theme_name="옛날옛날에", theme_id=573),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/Nextedition%20gangnam5",
        theme_list=[
            NextEditionTheme(theme_name="SOS", theme_id=25),
            NextEditionTheme(theme_name="그래도 피망은 먹기 싫단 말이에욧", theme_id=24),
            NextEditionTheme(theme_name="BANK RUPT", theme_id=22),
            NextEditionTheme(theme_name="우리동네 김선의 金善醫", theme_id=23),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/Nextedition%20Jamsil",
        theme_list=[
            NextEditionTheme(theme_name="데.코.연.(데이트 코스 연구회)", theme_id=236),
            NextEditionTheme(theme_name="락페스티벌", theme_id=235),
            NextEditionTheme(theme_name="작은 악마들", theme_id=234),
            NextEditionTheme(theme_name="카페라떼", theme_id=233),
        ],
    ),
    NextEditionCafe(
        url="https://www.nextedition.co.kr/shops/Nextedition%20Gundae%20Bonheur",
        theme_list=[
            NextEditionTheme(theme_name="세렌디피티(SERENDIPITY)", theme_id=164),
        ],
    ),
]
