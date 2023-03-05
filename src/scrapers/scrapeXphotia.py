from selenium import webdriver
import datetime
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 위치 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# linux 환경에서 필요한 option
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# 방탈출 매장 URL

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

# 예약 가능한 시간대를 크롤링할 페이지 주소
url = "https://www.xphobia.net/reservation/reservation_check.php"

driver.implicitly_wait(3)

# 크롬 브라우저로 페이지 접속
driver.get(url)

# 날짜 선택
today = datetime.date.today()
next_week = today + datetime.timedelta(days=7)

date_picker = driver.find_element_by_id('datepicker')
date_picker.click()
time.sleep(1)

date_selector = driver.find_element_by_xpath("//select[@class='ui-datepicker-month']")
date_selector.send_keys(str(next_week.month - 1))
time.sleep(1)

date_selector = driver.find_element_by_xpath("//select[@class='ui-datepicker-year']")
date_selector.send_keys(str(next_week.year))
time.sleep(1)

date_selector = driver.find_element_by_xpath("//a[text()='" + str(next_week.day) + "']")
date_selector.click()
time.sleep(1)

# 테마 선택
theme_selector = driver.find_element_by_id('cate_name')
themes = ['포비아 던전', '방탈출 카페', '미션 브레이크']

for theme in themes:
    theme_selector.send_keys(theme)
    time.sleep(1)

    # 지점 선택
    store_selector = driver.find_element_by_id('store_name')
    stores = store_selector.find_elements_by_tag_name('option')

    for store in stores[1:]:
        store_name = store.text
        store.click()
        time.sleep(1)

        # 테마 선택
        theme_selector = driver.find_element_by_id('cate_name')
        theme_selector.send_keys(theme)
        time.sleep(1)

        # 조회 버튼 클릭
        search_button = driver.find_element_by_id('check_btn')
        search_button.click()
        time.sleep(3)

        # 예약 가능한 시간 정보 파싱
        try:
            result_table = driver.find_element_by_id('result_tbl')
            result_rows = result_table.find_elements_by_tag_name('tr')
            for row in result_rows[1:]:
                time_slot = row.find_elements_by_tag_name('td')[0].text
                print(store_name, theme, time_slot)
        except:
            pass

# 크롬 드라이버 종료
driver.quit()