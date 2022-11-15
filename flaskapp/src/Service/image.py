from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()

    # 새 창 띄우지 않기
    chrome_options.add_argument('headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    driver.implicitly_wait(3)

    return driver


def search_keyword(driver, keyword, goodId):
    search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)

    image = driver.find_elements(By.CSS_SELECTOR,
                                 '#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')

    a = image[0].get_attribute('src')
    urllib.request.urlretrieve(a, "images/"+str(goodId)+ ".jpg")


def search_images(rows):
    # 상품 목록
    driver = set_chrome_driver()

    for row in rows:
        keyword = row["goodName"]
        goodId = row["goodId"]
        try:
            search_keyword(driver, keyword, goodId)
            driver.back()
        except IndexError:
            driver = set_chrome_driver()
            search_keyword(driver, keyword, goodId)
            driver.back()


def list_chuck(arr, n):
    div = len(arr) // n
    return [arr[div * i:div * (i + 1)] for i in range(0, n - 1)] + [arr[div * (n - 1):len(arr)]]


