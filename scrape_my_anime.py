import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import pandas


def scrape_mal():

    #s = Service('/Users/pranay_gupta/Downloads/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    #driver = webdriver.Chrome(service=s)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    #driver = webdriver.Chrome(options=chrome_options)
    rank = []
    title = []
    score = []
    driver.get('https://myanimelist.net/topanime.php?limit=0')
    driver.find_element(By.XPATH, '//a[normalize-space()="Top TV Series"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[@data-v-923b7c2a=""]').click()
    for i in range(4):
        rows = driver.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            rank.append(row.find_element(By.XPATH, "./td[1]").text)
            #print(row.find_element(By.XPATH, "./td[1]").text)
            title.append(row.find_element(By.XPATH, "./td[2]").text)
            #print(row.find_element(By.XPATH, "./td[2]").text)
            score.append(row.find_element(By.XPATH, "./td[3]").text)
            #print(row.find_element(By.XPATH, "./td[3]").text)

        driver.find_element(By.CSS_SELECTOR, "div[class='di-b ac pt16 pb16 pagination icon-top-ranking-page-bottom'] "
                                         "a[class='link-blue-box next']").click()
    driver.quit()
    data_frame = pandas.DataFrame({'rank': rank, 'title': title, 'score': score})
    # #data_frame.to_csv('MAL_rankings.csv', index=False)
    return data_frame

if __name__ == "__main__":
    scrape_mal()

