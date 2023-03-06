from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_pption():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    return chrome_options


def get_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=get_chrome_pption())
    return driver
