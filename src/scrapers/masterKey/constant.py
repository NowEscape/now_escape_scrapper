from typing import Final

MASTER_KEY_URL: Final = "http://www.master-key.co.kr/booking/booking_list_new"


class MasterKeyTheme:
    def __init__(self, name: str, theme_id: int):
        self.name = name
        self.theme_id = theme_id


class MasterKeyCafe:

    def __init__(self, name: str, store_id: int, theme_list: list[MasterKeyTheme]):
        self.name = name
        self.store_id = store_id
        self.theme_list = theme_list


MASTER_KEY_CAFE_LIST = [
    MasterKeyCafe(
        name="궁동직영점",
        store_id=1,
        theme_list=[
            MasterKeyTheme(name="MSI 미제사건 전담반", theme_id=1141),
            MasterKeyTheme(name="재심", theme_id=1140),
            MasterKeyTheme(name="MK빌딩을털어라:45C6", theme_id=1142),
            MasterKeyTheme(name="블랙룸", theme_id=1138),
            MasterKeyTheme(name="화이트룸", theme_id=1139)
        ]
    ),
    MasterKeyCafe(
        name="은행직영점",
        store_id=2,
        theme_list=[
            MasterKeyTheme(name="그레이트월", theme_id=1137),
            MasterKeyTheme(name="편지", theme_id=1135),
            # MasterKeyTheme(name="1990", theme_id=), db에 없는 테마
            MasterKeyTheme(name="대탈출2", theme_id=1134),
            MasterKeyTheme(name="REC", theme_id=1136),
        ]
    ),
    MasterKeyCafe(
        name="천안두정점",
        store_id=7,
        theme_list=[
            MasterKeyTheme(name="시크릿가든", theme_id=1095),
            MasterKeyTheme(name="경찰서를 털어라", theme_id=1090),
            MasterKeyTheme(name="카마수트라", theme_id=1091),
            MasterKeyTheme(name="13고스트", theme_id=1092),
            MasterKeyTheme(name="스카이넷", theme_id=1093),
            MasterKeyTheme(name="화이트룸-클래식", theme_id=1094)
        ]
    ),
    MasterKeyCafe(
        name="전주고사점",
        store_id=8,
        theme_list=[
            MasterKeyTheme(name="13여고괴담", theme_id=1603),
            MasterKeyTheme(name="곡성", theme_id=1605),
            MasterKeyTheme(name="장난감가게", theme_id=1608),
            MasterKeyTheme(name="모나리자", theme_id=1607),
            MasterKeyTheme(name="조커2", theme_id=1606),
            MasterKeyTheme(name="인디아나존스", theme_id=1604),
            MasterKeyTheme(name="아나스타샤", theme_id=1609),
            MasterKeyTheme(name="블루위시", theme_id=1610),
        ]
    ),
    MasterKeyCafe(
        name="대구동성로점",
        store_id=9,
        theme_list=[
            MasterKeyTheme(name="화이트룸", theme_id=1240),
            MasterKeyTheme(name="인디아나존스", theme_id=1242),
            MasterKeyTheme(name="13여고괴담", theme_id=1239),
            MasterKeyTheme(name="드라큘라", theme_id=1241),
            MasterKeyTheme(name="천사와악마", theme_id=1237),
            MasterKeyTheme(name="그레인in인셉션", theme_id=1238),
            MasterKeyTheme(name="해리포터와 마법사의돌", theme_id=1243)
        ]
    ),
    MasterKeyCafe(
        name="프라임건대점",
        store_id=10,
        theme_list=[
            MasterKeyTheme(name="리그오브디저트", theme_id=179),
            MasterKeyTheme(name="와트와 숨겨진 시간", theme_id=180),
            MasterKeyTheme(name="디코이", theme_id=178),
            #MasterKeyTheme(name="어느별에서왔니?", theme_id=1136),
        ]
    ),
    MasterKeyCafe(
        name="홍대점",
        store_id=11,
        theme_list=[
            MasterKeyTheme(name="온칼로", theme_id=340),
            MasterKeyTheme(name="연애조작단", theme_id=341),
            MasterKeyTheme(name="B미술학원13호실", theme_id=342)
        ]
    ),
    MasterKeyCafe(
        name="익산점",
        store_id=12,
        theme_list=[
            MasterKeyTheme(name="이불밖은위험해", theme_id=1589),
            MasterKeyTheme(name="경찰서를 털어라", theme_id=1591),
            MasterKeyTheme(name="온칼로:10만년의밤", theme_id=1590),
            MasterKeyTheme(name="카마수트라", theme_id=1592),
            MasterKeyTheme(name="호스텔", theme_id=1594),
            MasterKeyTheme(name="트로이목마", theme_id=1593),
        ]
    ),
    MasterKeyCafe(
        name="안양점",
        store_id=13,
        theme_list=[
            MasterKeyTheme(name="데자뷰", theme_id=652),
            MasterKeyTheme(name="운수좋은날", theme_id=650),
            MasterKeyTheme(name="우주대미남", theme_id=648),
            MasterKeyTheme(name="사랑과전쟁", theme_id=649),
            MasterKeyTheme(name="레드럼", theme_id=651)
        ]
    ),
    MasterKeyCafe(
        name="대구동성로로데오점",
        store_id=14,
        theme_list=[
            MasterKeyTheme(name="젊은날", theme_id=1244),
            MasterKeyTheme(name="필라멘트", theme_id=1245),
            MasterKeyTheme(name="Overtime", theme_id=1246),
            MasterKeyTheme(name="가위", theme_id=1247),
        ]
    ),
    MasterKeyCafe(
        name="강남점",
        store_id=16,
        theme_list=[
            MasterKeyTheme(name="이자카야 츠이오쿠", theme_id=42),
            MasterKeyTheme(name="히로인", theme_id=43),
            MasterKeyTheme(name="메르헨 수호대", theme_id=44),
            MasterKeyTheme(name="도시괴담 Part.1 ‘The Day of Horror’", theme_id=46),
            MasterKeyTheme(name="토끼와거북이", theme_id=45)
        ]
    ),
    MasterKeyCafe(
        name="천안신부점",
        store_id=18,
        theme_list=[
            MasterKeyTheme(name="라퓨타", theme_id=1084),
            MasterKeyTheme(name="하루살이", theme_id=1085),
            MasterKeyTheme(name="터널", theme_id=1089),
            MasterKeyTheme(name="코드명:MK", theme_id=1086),
            MasterKeyTheme(name="트러블메이커", theme_id=1087),
            MasterKeyTheme(name="패럿가이", theme_id=1088)
        ]
    ),
    MasterKeyCafe(
        name="부산서면점",
        store_id=19,
        theme_list=[
            MasterKeyTheme(name="집으로", theme_id=1445),
            MasterKeyTheme(name="칼퇴", theme_id=1442),
            MasterKeyTheme(name="세이프티룸", theme_id=1443),
            MasterKeyTheme(name="모모게임", theme_id=1444)
        ]
    ),
    MasterKeyCafe(
        name="홍대상수점",
        store_id=20,
        theme_list=[
            MasterKeyTheme(name="선물", theme_id=348),
            MasterKeyTheme(name="기억연구소", theme_id=345),
            MasterKeyTheme(name="도시괴담 Part.2 The Abandoned Office", theme_id=347),
            MasterKeyTheme(name="레이더스", theme_id=346),
            MasterKeyTheme(name="흥보와 놀보", theme_id=344),
            MasterKeyTheme(name="어느가을날", theme_id=343),
        ]
    ),
    MasterKeyCafe(
        name="잠실점",
        store_id=21,
        theme_list=[
            MasterKeyTheme(name="이스케이프플랜", theme_id=238),
            MasterKeyTheme(name="어게인", theme_id=341),
            MasterKeyTheme(name="그리고 아무도 없었다", theme_id=237),
            MasterKeyTheme(name="블랙룸:쉽게 만들어진 방", theme_id=239),
            MasterKeyTheme(name="샵보이스", theme_id=240),
            MasterKeyTheme(name="더매치:마지막전쟁", theme_id=242)
        ]
    ),
    MasterKeyCafe(
        name="화정점",
        store_id=23,
        theme_list=[
            MasterKeyTheme(name="시간여행", theme_id=915),
            MasterKeyTheme(name="현월", theme_id=910),
            MasterKeyTheme(name="헬프미", theme_id=911),
            MasterKeyTheme(name="싸움의기술:zero", theme_id=912),
            MasterKeyTheme(name="B지하철13호선", theme_id=913),
            MasterKeyTheme(name="묘몽", theme_id=914),
        ]
    ),
    MasterKeyCafe(
        name="프라임청주점",
        store_id=24,
        theme_list=[
            MasterKeyTheme(name="환생시험", theme_id=1197),
            MasterKeyTheme(name="샵보이스", theme_id=1193),
            MasterKeyTheme(name="자수성가", theme_id=1194),
            MasterKeyTheme(name="방과후13교시", theme_id=1195),
            MasterKeyTheme(name="이상한나라", theme_id=1196),
        ]
    ),
    MasterKeyCafe(
        name="건대점",
        store_id=26,
        theme_list=[
            MasterKeyTheme(name="D-Day", theme_id=170),
            MasterKeyTheme(name="DELIVER", theme_id=171),
            MasterKeyTheme(name="36.5 마온술사의 정원", theme_id=172),
        ]
    ),
    MasterKeyCafe(
        name="평택점",
        store_id=27,
        theme_list=[
            MasterKeyTheme(name="대탈출2", theme_id=799),
            MasterKeyTheme(name="쌩얼", theme_id=796),
            MasterKeyTheme(name="집으로", theme_id=797),
            MasterKeyTheme(name="MSI 미제사건 전담반", theme_id=798),
            MasterKeyTheme(name="사귀", theme_id=800),
            MasterKeyTheme(name="시간전당포", theme_id=801),
        ]
    ),
    MasterKeyCafe(
        name="건대로데오",
        store_id=28,
        theme_list=[
            MasterKeyTheme(name="선고", theme_id=174),
            MasterKeyTheme(name="사악한 악마와 달콤한 공장", theme_id=173),
            MasterKeyTheme(name="뱀파이어 헌터", theme_id=175),
            MasterKeyTheme(name="찰리", theme_id=176),
            MasterKeyTheme(name="팬텀", theme_id=177)
        ]
    ),
    MasterKeyCafe(
        name="강남프라임",
        store_id=29,
        theme_list=[
            MasterKeyTheme(name="ECHO (에코) - Beginning Dawn", theme_id=51),
            MasterKeyTheme(name="별의별", theme_id=48),
            MasterKeyTheme(name="Do THE G", theme_id=49),
            MasterKeyTheme(name="어웨이큰", theme_id=47),
            MasterKeyTheme(name="덫", theme_id=50),
        ]
    ),
    MasterKeyCafe(
        name="동탄프라임",
        store_id=30,
        theme_list=[
            MasterKeyTheme(name="우가우가", theme_id=773),
            MasterKeyTheme(name="종이왕국", theme_id=774),
            MasterKeyTheme(name="페이소스", theme_id=772),
            MasterKeyTheme(name="인스톨", theme_id=771)
        ]
    ),
    MasterKeyCafe(
        name="노원점",
        store_id=31,
        theme_list=[
            MasterKeyTheme(name="이모션 (EMOTION)", theme_id=541),
            MasterKeyTheme(name="일탈", theme_id=540),
            MasterKeyTheme(name="타임크랙 (TIME CRACK)", theme_id=543),
            MasterKeyTheme(name="통제구역", theme_id=542),
        ]
    ),
    MasterKeyCafe(
        name="프라임신촌퍼블릭",
        store_id=32,
        theme_list=[
            MasterKeyTheme(name="인투더와일드", theme_id=295),
            MasterKeyTheme(name="그도... 그럴 것이다", theme_id=296),
            #MasterKeyTheme(name="그리고 아무도 없었다", theme_id=1142),
            MasterKeyTheme(name="SCENE : 404 NOT FOUND", theme_id=297),
        ]
    ),
    # MasterKeyCafe(
    #     name="플레이포인트랩강남점",
    #     store_id=35,
    #     theme_list=[
    #         MasterKeyTheme(name="리허설", theme_id=1137),
    #         MasterKeyTheme(name="갱생", theme_id=1135),
    #         MasterKeyTheme(name="더맨", theme_id=1134),
    #         MasterKeyTheme(name="체험살해현장", theme_id=1136),
    #     ]
    # ),
]
