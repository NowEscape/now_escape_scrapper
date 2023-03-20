from typing import Final

SHERLOCK_HOMES_URL: Final = "https://sherlock-holmes.co.kr/reservation/res_schedule.php?sido={SIDO}&bno={BNO}&date={DATE}&tno="


class SherlockHomesTheme:

    def __init__(self, theme_name: str, theme_id: int):
        self.theme_name = theme_name
        self.theme_id = theme_id


class SherlockHomesCafe:
    def __init__(self, region1: str, region2: str, sido: int, bno: int, theme_list: list[SherlockHomesTheme]):
        self.region1 = region1
        self.region2 = region2
        self.sido = sido
        self.bno = bno
        self.theme_list = theme_list


SHERLOCK_HOMES_CAFE_LIST: Final = [
    SherlockHomesCafe(
        region1="서울특별시",
        region2="노원점",
        sido=1,
        bno=57,
        theme_list=[
            SherlockHomesTheme(theme_name="황금 감옥 : 와캄", theme_id=548),
            SherlockHomesTheme(theme_name="지프리트의 심장", theme_id=549),
            SherlockHomesTheme(theme_name="스토커", theme_id=545),
            SherlockHomesTheme(theme_name="파라오의 심판", theme_id=547),
            SherlockHomesTheme(theme_name="도둑들", theme_id=544),
            SherlockHomesTheme(theme_name="미녀와야수2", theme_id=546),
        ],
    ),
    SherlockHomesCafe(
        region1="서울특별시",
        region2="노량진점",
        sido=1,
        bno=48,
        theme_list=[
            SherlockHomesTheme(theme_name="어린왕자", theme_id=636),
            SherlockHomesTheme(theme_name="빛과 그림자:화이트의죽음2", theme_id=637),
            SherlockHomesTheme(theme_name="반하셨군요?", theme_id=638),
            SherlockHomesTheme(theme_name="중고로운 평화나라", theme_id=639),
        ],
    ),
    SherlockHomesCafe(
        region1="서울특별시",
        region2="대학로점",
        sido=1,
        bno=88,
        theme_list=[
            SherlockHomesTheme(theme_name="미녀와야수(대학로)", theme_id=507),
            SherlockHomesTheme(theme_name="드림 인베이더(대학로ver)", theme_id=510),
            SherlockHomesTheme(theme_name="혼:원혼의저주 (대학로)", theme_id=511),
            SherlockHomesTheme(theme_name="무속인 살인사건(대학로)", theme_id=509),
            SherlockHomesTheme(theme_name="위험한 레시피(대학로)", theme_id=508),
        ],
    ),
    SherlockHomesCafe(
        region1="서울특별시",
        region2="성신여대점",
        sido=1,
        bno=54,
        theme_list=[
            SherlockHomesTheme(theme_name="호텔:사라진 다이아몬드", theme_id=523),
            SherlockHomesTheme(theme_name="크라임씬", theme_id=524),
            SherlockHomesTheme(theme_name="보헤미아 왕국의 스캔들", theme_id=526),
            SherlockHomesTheme(theme_name="빛과 그림자:화이트의죽음2", theme_id=525),
        ],
    ),
    # 위의 SHERLOCK_HOMES_MAP과 동일한 순서로 신림2호점 추가
    SherlockHomesCafe(
        region1="서울특별시",
        region2="신림2호점",
        sido=1,
        bno=77,
        theme_list=[
            SherlockHomesTheme(theme_name="무속인 살인사건", theme_id=591),
            SherlockHomesTheme(theme_name="미녀와야수", theme_id=594),
            SherlockHomesTheme(theme_name="도둑들", theme_id=593),
            SherlockHomesTheme(theme_name="빛과 그림자", theme_id=592),
        ],
    ),
    SherlockHomesCafe(
        region1="서울특별시",
        region2="잠실1호점",
        sido=1,
        bno=35,
        theme_list=[
            SherlockHomesTheme(theme_name="무속인 살인사건", theme_id=246),
            SherlockHomesTheme(theme_name="빛과 그림자", theme_id=247),
            SherlockHomesTheme(theme_name="위험한 레시피", theme_id=248),
            SherlockHomesTheme(theme_name="산속의 여인", theme_id=249),
            SherlockHomesTheme(theme_name="웨딩크루즈 살인사건", theme_id=252),
            SherlockHomesTheme(theme_name="학교괴담 태훈이의 죽음", theme_id=250),
            SherlockHomesTheme(theme_name="미대교수의 비밀", theme_id=251),
        ],
    ),
    SherlockHomesCafe(
        region1="서울특별시",
        region2="잠실2호점",
        sido=1,
        bno=67,
        theme_list=[
            SherlockHomesTheme(theme_name="랑슈 뷰티연구소", theme_id=253),
            SherlockHomesTheme(theme_name="단잠", theme_id=254),
            SherlockHomesTheme(theme_name="퓨처리스트", theme_id=255),
        ],
    ),
    SherlockHomesCafe(
        region1="서울특별시",
        region2="종각점",
        sido=1,
        bno=69,
        theme_list=[
            SherlockHomesTheme(theme_name="숙제", theme_id=563),
            SherlockHomesTheme(theme_name="호텔:사라진 다이아몬드", theme_id=564),
            SherlockHomesTheme(theme_name="프로젝트:노아", theme_id=565),
            SherlockHomesTheme(theme_name="빛과 그림자:화이트의죽음2", theme_id=566),
            SherlockHomesTheme(theme_name="죽음의 신", theme_id=567),
        ],
    ),
    SherlockHomesCafe(
        region1="경기도",
        region2="구리점",
        sido=9,
        bno=41,
        theme_list=[
            SherlockHomesTheme(theme_name="호텔:사라진 다이아몬드", theme_id=860),
            SherlockHomesTheme(theme_name="무속인 살인사건", theme_id=861),
            SherlockHomesTheme(theme_name="미녀와야수", theme_id=862),
            SherlockHomesTheme(theme_name="반고흐의방", theme_id=863),
            SherlockHomesTheme(theme_name="혼:원혼의저주", theme_id=864),
        ],
    ),
    SherlockHomesCafe(
        region1="경기도",
        region2="뉴안양점",
        sido=9,
        bno=81,
        theme_list=[
            SherlockHomesTheme(theme_name="웨딩크루즈 살인사건-2탄", theme_id=663),
            SherlockHomesTheme(theme_name="파노라마", theme_id=664),
            SherlockHomesTheme(theme_name="파란지붕집", theme_id=665),
            SherlockHomesTheme(theme_name="노량진 고시생의 사랑-여자편", theme_id=666),
            SherlockHomesTheme(theme_name="중고로운 평화나라", theme_id=667),
        ],
    ),

    SherlockHomesCafe(
        region1="경기도",
        region2="동탄점",
        sido=9,
        bno=79,
        theme_list=[
            SherlockHomesTheme(theme_name="던전을 부탁해", theme_id=781),
            SherlockHomesTheme(theme_name="좀비여친", theme_id=782),
            SherlockHomesTheme(theme_name="호텔:사라진 다이아몬드", theme_id=783),
            SherlockHomesTheme(theme_name="지옥의 배달부", theme_id=784),
            SherlockHomesTheme(theme_name="거짓말", theme_id=785),
            SherlockHomesTheme(theme_name="귀신이 산다", theme_id=786),
        ],
    ),
    SherlockHomesCafe(
        region1="경기도",
        region2="부천점",
        sido=9,
        bno=64,
        theme_list=[
            SherlockHomesTheme(theme_name="프로젝트:노아", theme_id=973),
            SherlockHomesTheme(theme_name="사각사각", theme_id=974),
            SherlockHomesTheme(theme_name="호텔:사라진 다이아몬드", theme_id=976),
            SherlockHomesTheme(theme_name="지옥의 배달부", theme_id=975),
        ],
    ),
    SherlockHomesCafe(
        region1="경기도",
        region2="분당야탑점",
        sido=9,
        bno=62,
        theme_list=[
            SherlockHomesTheme(theme_name="빛과 그림자:화이트의죽음2", theme_id=832),
            SherlockHomesTheme(theme_name="혼:원혼의저주", theme_id=833),
            SherlockHomesTheme(theme_name="반고흐의방", theme_id=834),
            SherlockHomesTheme(theme_name="무속인 살인사건", theme_id=835),
            SherlockHomesTheme(theme_name="도둑들-문제도둑", theme_id=836),
        ],
    ),
    SherlockHomesCafe(
        region1="경기도",
        region2="서현점",
        sido=9,
        bno=87,
        theme_list=[
            SherlockHomesTheme(theme_name="Molaq : 성 밖 이야기", theme_id=837),
            SherlockHomesTheme(theme_name="Below : 성 안 이야기", theme_id=838),
            SherlockHomesTheme(theme_name="대영어시대 : Age of English", theme_id=839),
        ],
    ),
    SherlockHomesCafe(
        region1="경기도",
        region2="의정부점",
        sido=9,
        bno=61,
        theme_list=[
            SherlockHomesTheme(theme_name="프로젝트:노아", theme_id=885),
            SherlockHomesTheme(theme_name="노량진 고시생의 사랑-여자편", theme_id=886),
            SherlockHomesTheme(theme_name="빛과 그림자:화이트의죽음2", theme_id=887),
            SherlockHomesTheme(theme_name="미녀와야수", theme_id=888),
            SherlockHomesTheme(theme_name="호텔:사라진 다이아몬드(의정부버전)", theme_id=889),
        ],
    ),
    SherlockHomesCafe(
        region1="경기도",
        region2="평택점",
        sido=9,
        bno=80,
        theme_list=[
            SherlockHomesTheme(theme_name="반고흐의방", theme_id=807),
            SherlockHomesTheme(theme_name="혼:원혼의저주", theme_id=808),
            SherlockHomesTheme(theme_name="도둑들", theme_id=809),
            SherlockHomesTheme(theme_name="미녀와야수", theme_id=810),
            SherlockHomesTheme(theme_name="지옥의 배달부", theme_id=811),
        ],
    ),
    SherlockHomesCafe(
        region1="인천광역시",
        region2="구월인천점",
        sido=4,
        bno=13,
        theme_list=[
            SherlockHomesTheme(theme_name="파란지붕집", theme_id=1023),
            SherlockHomesTheme(theme_name="던전을 부탁해", theme_id=1024),
            SherlockHomesTheme(theme_name="좀비여친", theme_id=1025),
            SherlockHomesTheme(theme_name="사라민", theme_id=1026),
            SherlockHomesTheme(theme_name="지옥의 라이더", theme_id=1027),
            SherlockHomesTheme(theme_name="호텔:사라진 다이아몬드", theme_id=1028),
        ],
    ),
    SherlockHomesCafe(
        region1="인천광역시",
        region2="부평점",
        sido=4,
        bno=45,
        theme_list=[
            SherlockHomesTheme(theme_name="수상한형제들", theme_id=1029),
            SherlockHomesTheme(theme_name="이상한 나라의 초대 [부평]", theme_id=1030),
            SherlockHomesTheme(theme_name="지하감옥", theme_id=1031),
            SherlockHomesTheme(theme_name="혼:원혼의저주", theme_id=1032),
            SherlockHomesTheme(theme_name="[NEW]나쁜놈 나쁜놈 나쁜놈", theme_id=1033),
        ],
    ),
    SherlockHomesCafe(
        region1="충청 대전 세종",
        region2="대전 신세계백화점",
        sido=12,
        bno=85,
        theme_list=[
            SherlockHomesTheme(theme_name="지프리트의 심장", theme_id=1154),
            SherlockHomesTheme(theme_name="죽음의 신", theme_id=1155),
            SherlockHomesTheme(theme_name="세번째밤", theme_id=1156),
            SherlockHomesTheme(theme_name="언더월드", theme_id=1157),
            SherlockHomesTheme(theme_name="무한의 던전 (20분)", theme_id=1158),
            SherlockHomesTheme(theme_name="피플인사이드 (40분)", theme_id=1159),
        ],
    ),
    SherlockHomesCafe(
        region1="충청 대전 세종",
        region2="아산점",
        sido=12,
        bno=86,
        theme_list=[
            SherlockHomesTheme(theme_name="노룸", theme_id=1073),
            SherlockHomesTheme(theme_name="악마를 보았다", theme_id=1074),
            SherlockHomesTheme(theme_name="대마법사 오셀로", theme_id=1075),
            SherlockHomesTheme(theme_name="말못해", theme_id=1076),
            SherlockHomesTheme(theme_name="[프리미엄]귀로여관 (70분)", theme_id=1077),
        ],
    ),
    SherlockHomesCafe(
        region1="충청 대전 세종",
        region2="천안1호점",
        sido=12,
        bno=14,
        theme_list=[
            SherlockHomesTheme(theme_name="마법사의 세계", theme_id=1096),
            SherlockHomesTheme(theme_name="호텔:사라진 다이아몬드", theme_id=1097),
            SherlockHomesTheme(theme_name="이상한 나라의 초대", theme_id=1098),
            SherlockHomesTheme(theme_name="무속인 살인사건", theme_id=1099),
            SherlockHomesTheme(
                theme_name="[19금]찰리와 늠름한(?) 바나나 공장", theme_id=1100
            ),
        ],
    ),
    SherlockHomesCafe(
        region1="충청 대전 세종",
        region2="천안2호점",
        sido=12,
        bno=74,
        theme_list=[
            SherlockHomesTheme(
                theme_name="[프리미엄 테마]미즈몰리아와 수수께끼의 책", theme_id=1101
            ),
            SherlockHomesTheme(theme_name="TIED", theme_id=1102),
            SherlockHomesTheme(theme_name="인생은 실전이다 종만아", theme_id=1103),
            SherlockHomesTheme(theme_name="던전:비밀의문", theme_id=1104),
        ],
    ),
    SherlockHomesCafe(
        region1="충청 대전 세종",
        region2="청주점",
        sido=12,
        bno=70,
        theme_list=[
            SherlockHomesTheme(theme_name="반고흐의방", theme_id=1198),
            SherlockHomesTheme(theme_name="무속인 살인사건", theme_id=1199),
            SherlockHomesTheme(theme_name="빛과 그림자:화이트의죽음2", theme_id=1200),
            SherlockHomesTheme(theme_name="도둑들", theme_id=1201),
            SherlockHomesTheme(theme_name="크라임씬", theme_id=1202),
        ],
    ),
    SherlockHomesCafe(
        region1="전라 광주",
        region2="여수점",
        sido=13,
        bno=44,
        theme_list=[
            SherlockHomesTheme(theme_name="크라임씬", theme_id=1751),
            SherlockHomesTheme(theme_name="이상한 나라의 초대", theme_id=1752),
            SherlockHomesTheme(theme_name="빛과 그림자:화이트의죽음2", theme_id=1753),
            SherlockHomesTheme(theme_name="무속인 살인사건", theme_id=1754),
            SherlockHomesTheme(theme_name="할머니는 마법사", theme_id=1755),
            SherlockHomesTheme(theme_name="전기톱 살인사건", theme_id=1756),
            SherlockHomesTheme(theme_name="파라오의 심판", theme_id=1757),
        ],
    ),
    SherlockHomesCafe(
        region1="경상도",
        region2="대구동성로점",
        sido=15,
        bno=84,
        theme_list=[
            SherlockHomesTheme(theme_name="지프리트의 심장", theme_id=1286),
            SherlockHomesTheme(theme_name="황금 감옥 : 와캄", theme_id=1287),
            SherlockHomesTheme(theme_name="랑슈 뷰티연구소", theme_id=1288),
            SherlockHomesTheme(theme_name="단잠", theme_id=1289),
        ],
    ),
]
