from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime

# 현재 날짜
now = datetime.now()
now_date = now.strftime('%Y-%m-%d')

# 방탈출 매장 URL
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.dpsnnn.com/reserve"
driver.get(url)

driver.implicitly_wait(1)

result = driver.find_elements(by=By.XPATH,
                value="//td[contains(@data-date,'2023-3-14')]/div/div[3]/"
                    "div[contains(@class, 'booking_list  hide_badge')]/a/div/div/span[1][contains(text(), '행복')]")

textList = map((lambda element: element.text), result)
data = []
for text in textList:
    text_final = text[-5:]
    date_time = now_date + " " + text_final
    theme = "57"
    line = (date_time, theme)
    data.append(line)
print(data)

