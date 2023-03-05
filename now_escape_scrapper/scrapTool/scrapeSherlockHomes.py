import time
from datetime import datetime, timedelta
from typing import Final, Dict

import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


SHERLOCK_HOMES_MAP: Final[Dict] = {
    "url": "https://sherlock-holmes.co.kr/reservation",
    "cafeList": [
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "노원점",
            "themeList": [
                {
                    "themeName": "황금 감옥 : 와캄",
                    "themeId": "548"
                },
                {
                    "themeName": "지프리트의 심장",
                    "themeId": "549"
                },
                {
                    "themeName": "스토커",
                    "themeId": "545"
                },
                {
                    "themeName": "파라오의 심판",
                    "themeId": "547"
                },
                {
                    "themeName": "도둑들",
                    "themeId": "544"
                },
                {
                    "themeName": "미녀와야수2",
                    "themeId": "546"
                }
            ]
        },
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "노량진점",
            "themeList": [
                {
                    "themeName": "어린왕자",
                    "themeId": "636"
                },
                {
                    "themeName": "빛과 그림자:화이트의죽음2",
                    "themeId": "637"
                },
                {
                    "themeName": "반하셨군요?",
                    "themeId": "638"
                },
                {
                    "themeName": "중고로운 평화나라",
                    "themeId": "639"
                }
            ]
        },
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "대학로점",
            "themeList": [
                {
                    "themeName": "미녀와야수(대학로)",
                    "themeId": "507"
                },
                {
                    "themeName": "드림 인베이더(대학로ver)",
                    "themeId": "510"
                },
                {
                    "themeName": "혼:원혼의저주 (대학로)",
                    "themeId": "511"
                },
                {
                    "themeName": "무속인 살인사건(대학로)",
                    "themeId": "509"
                },
                {
                    "themeName": "위험한 레시피(대학로)",
                    "themeId": "508"
                }
            ]
        },
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "성신여대점",
            "themeList": [
                {
                    "themeName": "호텔:사라진 다이아몬드",
                    "themeId": "523"
                },
                {
                    "themeName": "크라임씬",
                    "themeId": "524"
                },
                {
                    "themeName": "보헤미아 왕국의 스캔들",
                    "themeId": "526"
                },
                {
                    "themeName": "빛과 그림자:화이트의죽음2",
                    "themeId": "525"
                }
            ]
        },
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "신림2호점",
            "themeList": [
                {
                    "themeName": "무속인 살인사건",
                    "themeId": "591"
                },
                {
                    "themeName": "미녀와야수",
                    "themeId": "594"
                },
                {
                    "themeName": "빛과 그림자",
                    "themeId": "592"
                },
                {
                    "themeName": "도둑들",
                    "themeId": "593"
                }
            ]
        },
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "잠실1호점",
            "themeList": [
                {
                    "themeName": "빛과 그림자",
                    "themeId": "247"
                },
                {
                    "themeName": "무속인 살인사건",
                    "themeId": "246"
                },
                {
                    "themeName": "위험한 레시피",
                    "themeId": "248"
                },
                {
                    "themeName": "산속의 여인",
                    "themeId": "249"
                },
                {
                    "themeName": "[3세대] 웨딩크루즈 살인사건",
                    "themeId": "252"
                },
                {
                    "themeName": "[3세대] 학교괴담 태훈이의 죽음",
                    "themeId": "250"
                },
                {
                    "themeName": "[3세대] 미대교수의 비밀",
                    "themeId": "251"
                }
            ]
        },
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "잠실2호점",
            "themeList": [
                {
                    "themeName": "랑슈 뷰티연구소",
                    "themeId": "253"
                },
                {
                    "themeName": "단잠",
                    "themeId": "254"
                },
                {
                    "themeName": "퓨처리스트",
                    "themeId": "255"
                }
            ]
        },
        {
            "region1ForScrap": "서울특별시",
            "region2ForScrap": "종각점",
            "themeList": [
                {
                    "themeName": "숙제",
                    "themeId": "563"
                },
                {
                    "themeName": "호텔:사라진 다이아몬드",
                    "themeId": "564"
                },
                {
                    "themeName": "프로젝트:노아",
                    "themeId": "565"
                },
                {
                    "themeName": "빛과 그림자:화이트의죽음2",
                    "themeId": "566"
                },
                {
                    "themeName": "죽음의 신",
                    "themeId": "567"
                }
            ]
        },
        {
            "region1ForScrap": "경기도",
            "region2ForScrap": "구리점",
            "themeList": [
                {
                    "themeName": "호텔:사라진 다이아몬드",
                    "themeId": "860"
                },
                {
                    "themeName": "무속인 살인사건",
                    "themeId": "861"
                },
                {
                    "themeName": "미녀와야수",
                    "themeId": "862"
                },
                {
                    "themeName": "반고흐의방",
                    "themeId": "863"
                },
                {
                    "themeName": "혼:원혼의저주",
                    "themeId": "864"
                }
            ]
        },
        {
            "region1ForScrap": "경기도",
            "region2ForScrap": "뉴안양점",
            "themeList": [
                {
                    "themeName": "웨딩크루즈 살인사건-2탄",
                    "themeId": "663"
                },
                {
                    "themeName": "파노라마",
                    "themeId": "664"
                },
                {
                    "themeName": "파란지붕집",
                    "themeId": "665"
                },
                {
                    "themeName": "노량진 고시생의 사랑-여자편",
                    "themeId": "666"
                },
                {
                    "themeName": "중고로운 평화나라",
                    "themeId": "667"
                }
            ]
        },
        {
            "region1ForScrap": "경기도",
            "region2ForScrap": "동탄점",
            "themeList": [
                {
                    "themeName": "던전을 부탁해",
                    "themeId": "781"
                },
                {
                    "themeName": "좀비여친",
                    "themeId": "782"
                },
                {
                    "themeName": "호텔:사라진 다이아몬드",
                    "themeId": "783"
                },
                {
                    "themeName": "지옥의 배달부",
                    "themeId": "784"
                },
                {
                    "themeName": "거짓말",
                    "themeId": "785"
                },
                {
                    "themeName": "귀신이 산다",
                    "themeId": "786"
                }
            ]
        },
        {
            "region1ForScrap": "경기도",
            "region2ForScrap": "부천점",
            "themeList": [
                {
                    "themeName": "프로젝트:노아",
                    "themeId": "973"
                },
                {
                    "themeName": "사각사각",
                    "themeId": "974"
                },
                {
                    "themeName": "호텔:사라진 다이아몬드",
                    "themeId": "976"
                },
                {
                    "themeName": "지옥의 배달부",
                    "themeId": "975"
                }
            ]
        },
        {
            "region1ForScrap": "경기도",
            "region2ForScrap": "분당야탑점",
            "themeList": [
                {
                    "themeName": "빛과 그림자:화이트의죽음2",
                    "themeId": "832"
                },
                {
                    "themeName": "혼:원혼의저주",
                    "themeId": "833"
                },
                {
                    "themeName": "반고흐의방",
                    "themeId": "834"
                },
                {
                    "themeName": "무속인 살인사건",
                    "themeId": "835"
                },
                {
                    "themeName": "도둑들-문제도둑",
                    "themeId": "836"
                }
            ]
        },
        {
            "region1ForScrap": "경기도",
            "region2ForScrap": "서현점",
            "themeList": [
                {
                    "themeName": "Molaq : 성 밖 이야기",
                    "themeId": "837"
                },
                {
                    "themeName": "Below : 성 안 이야기",
                    "themeId": "838"
                },
                {
                    "themeName": "대영어시대 : Age of English",
                    "themeId": "839"
                }
            ]
        },
        {
            "region1ForScrap": "경기도",
            "region2ForScrap": "의정부점",
            "themeList": [
                {
                    "themeName": "프로젝트:노아",
                    "themeId": "885"
                },
                {
                    "themeName": "노량진 고시생의 사랑-여자편",
                    "themeId": "886"
                },
                {
                    "themeName": "빛과 그림자:화이트의죽음2",
                    "themeId": "887"
                },
                {
                    "themeName": "미녀와야수",
                    "themeId": "888"
                },
                {
                    "themeName": "호텔:사라진 다이아몬드(의정부버전)",
                    "themeId": "889"
                }
            ]
        },
        {
            "region1ForScrap": "경기도",
            "region2ForScrap": "평택점",
            "themeList": [
                {
                    "themeName": "반고흐의방",
                    "themeId": "807"
                },
                {
                    "themeName": "혼:원혼의저주",
                    "themeId": "808"
                },
                {
                    "themeName": "도둑들",
                    "themeId": "809"
                },
                {
                    "themeName": "미녀와야수",
                    "themeId": "810"
                },
                {
                    "themeName": "지옥의 배달부",
                    "themeId": "811"
                }
            ]
        },
        {
            "region1ForScrap": "인천광역시",
            "region2ForScrap": "구월인천점",
            "themeList": [
                {
                    "themeName": "파란지붕집",
                    "themeId": "1023"
                },
                {
                    "themeName": "던전을 부탁해",
                    "themeId": "1024"
                },
                {
                    "themeName": "좀비여친",
                    "themeId": "1025"
                },
                {
                    "themeName": "사라민",
                    "themeId": "1026"
                },
                {
                    "themeName": "지옥의 라이더",
                    "themeId": "1027"
                },
                {
                    "themeName": "호텔:사라진 다이아몬드",
                    "themeId": "1028"
                }
            ]
        },
        {
            "region1ForScrap": "인천광역시",
            "region2ForScrap": "부평점",
            "themeList": [
                {
                    "themeName": "수상한형제들",
                    "themeId": "1029"
                },
                {
                    "themeName": "이상한 나라의 초대 [부평]",
                    "themeId": "1030"
                },
                {
                    "themeName": "지하감옥",
                    "themeId": "1031"
                },
                {
                    "themeName": "혼:원혼의저주",
                    "themeId": "1032"
                },
                {
                    "themeName": "[NEW]나쁜놈 나쁜놈 나쁜놈",
                    "themeId": "1033"
                }
            ]
        },
        {
            "region1ForScrap": "충청 대전 세종",
            "region2ForScrap": "대전 신세계백화점",
            "themeList": [
                {
                    "themeName": "지프리트의 심장",
                    "themeId": "1154"
                },
                {
                    "themeName": "죽음의 신",
                    "themeId": "1155"
                },
                {
                    "themeName": "세번째밤",
                    "themeId": "1156"
                },
                {
                    "themeName": "언더월드",
                    "themeId": "1157"
                },
                {
                    "themeName": "무한의 던전 (20분)",
                    "themeId": "1158"
                },
                {
                    "themeName": "피플인사이드 (40분)",
                    "themeId": "1159"
                }
            ]
        },
        {
            "region1ForScrap": "충청 대전 세종",
            "region2ForScrap": "아산점",
            "themeList": [
                {
                    "themeName": "노룸",
                    "themeId": "1073"
                },
                {
                    "themeName": "악마를 보았다",
                    "themeId": "1074"
                },
                {
                    "themeName": "대마법사 오셀로",
                    "themeId": "1075"
                },
                {
                    "themeName": "말못해",
                    "themeId": "1076"
                },
                {
                    "themeName": "[프리미엄]귀로여관 (70분)",
                    "themeId": "1077"
                }
            ]
        },
        {
            "region1ForScrap": "충청 대전 세종",
            "region2ForScrap": "천안1호점",
            "themeList": [
                {
                    "themeName": "마법사의 세계",
                    "themeId": "1096"
                },
                {
                    "themeName": "호텔:사라진 다이아몬드",
                    "themeId": "1097"
                },
                {
                    "themeName": "이상한 나라의 초대",
                    "themeId": "1098"
                },
                {
                    "themeName": "무속인 살인사건",
                    "themeId": "1099"
                },
                {
                    "themeName": "[19금]찰리와 늠름한(?) 바나나 공장",
                    "themeId": "1100"
                }
            ]
        },
        {
            "region1ForScrap": "충청 대전 세종",
            "region2ForScrap": "천안2호점",
            "themeList": [
                {
                    "themeName": "[프리미엄 테마]미즈몰리아와 수수께끼의 책",
                    "themeId": "1101"
                },
                {
                    "themeName": "TIED",
                    "themeId": "1102"
                },
                {
                    "themeName": "인생은 실전이다 종만아",
                    "themeId": "1103"
                },
                {
                    "themeName": "던전:비밀의문",
                    "themeId": "1104"
                }
            ]
        },
        {
            "region1ForScrap": "충청 대전 세종",
            "region2ForScrap": "청주점",
            "themeList": [
                {
                    "themeName": "반고흐의방",
                    "themeId": "1198"
                },
                {
                    "themeName": "무속인 살인사건",
                    "themeId": "1199"
                },
                {
                    "themeName": "빛과 그림자:화이트의죽음2",
                    "themeId": "1200"
                },
                {
                    "themeName": "도둑들",
                    "themeId": "1201"
                },
                {
                    "themeName": "크라임씬",
                    "themeId": "1202"
                }
            ]
        },
        {
            "region1ForScrap": "전라 광주",
            "region2ForScrap": "여수점",
            "themeList": [
                {
                    "themeName": "크라임씬",
                    "themeId": "1751"
                },
                {
                    "themeName": "이상한 나라의 초대",
                    "themeId": "1752"
                },
                {
                    "themeName": "빛과 그림자:화이트의죽음2",
                    "themeId": "1753"
                },
                {
                    "themeName": "무속인 살인사건",
                    "themeId": "1754"
                },
                {
                    "themeName": "할머니는 마법사",
                    "themeId": "1755"
                },
                {
                    "themeName": "전기톱 살인사건",
                    "themeId": "1756"
                },
                {
                    "themeName": "파라오의 심판",
                    "themeId": "1757"
                }
            ]
        },
        {
            "region1ForScrap": "경상도",
            "region2ForScrap": "대구동성로점",
            "themeList": [
                {
                    "themeName": "지프리트의 심장",
                    "themeId": "1286"
                },
                {
                    "themeName": "황금 감옥 : 와캄",
                    "themeId": "1287"
                },
                {
                    "themeName": "랑슈 뷰티연구소",
                    "themeId": "1288"
                },
                {
                    "themeName": "단잠",
                    "themeId": "1289"
                }
            ]
        }
    ]
}

def get_theme_name(theme_name):
    return theme_name + " &nbsp;"

def scrap_sherlock_homes_theme():
    connection = mysql.connector.connect(user="nowadmin", password="Nowescape1!",
                                         host="nowescape-db.cvafksmpbb8z.ap-northeast-2.rds.amazonaws.com",
                                         charset="utf8mb4",
                                         db="now_escape")
    cur = connection.cursor(prepared=True)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    # linux 환경에서 필요한 option
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # 방탈출 매장 URL
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    driver.get(SHERLOCK_HOMES_MAP["url"])

    driver.implicitly_wait(3)

    data_for_insert_db = []
    now = datetime.now()

    for cafe in SHERLOCK_HOMES_MAP["cafeList"]:
        driver.find_element(by=By.ID, value="selectArea").find_element(by=By.XPATH,
                                                                       value=f"//option[text()='{cafe['region1ForScrap']}']").click()
        driver.implicitly_wait(2)

        driver.find_element(by=By.ID, value="selectBranch").find_element(by=By.XPATH,
                                                                         value=f"option[text()='{cafe['region2ForScrap']}']").click()

        driver.implicitly_wait(2)

        driver.find_element(by=By.ID, value="res_date").click()

        driver.implicitly_wait(2)

        for dateDelta in range(7):
            date = now + timedelta(dateDelta)
            date_str = date.strftime('%Y-%m-%d')
            element = driver.find_element(by=By.ID, value="ui-datepicker-div") \
                .find_element(by=By.XPATH, value=f"table/tbody/tr/td/a[text()='{date.day}']")
            driver.execute_script("arguments[0].click();", element)

            time.sleep(1)
            for theme in cafe["themeList"]:
                print(date, theme)
                result = driver\
                    .find_element(by=By.XPATH, value=f"//h2[contains(text(),'{theme['themeName']}')]")\
                    .find_elements(by=By.XPATH, value="../div[2]/div/a/p[1]").copy()
                textList = map((lambda element: element.text), result)
                for text in textList:
                    date_time = date_str + " " + text
                    line = (date_time, theme["themeId"])
                    data_for_insert_db.append(line)

    print(data_for_insert_db)


    theme_id_list = []

    for cafe in SHERLOCK_HOMES_MAP["cafeList"]:
        for theme in cafe["themeList"]:
            theme_id_list.append(theme["themeId"])

    cur.execute("DELETE FROM theme_date WHERE theme_id IN (" + ','.join(str(e) for e in theme_id_list) + ")")
    cur.executemany("INSERT IGNORE INTO theme_date(theme_time,theme_id, is_open) VALUES(?, ?, 1)", data_for_insert_db)
    connection.commit()

scrap_sherlock_homes_theme()
