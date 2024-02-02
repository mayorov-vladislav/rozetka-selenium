from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def get_url():
    for count in range(1, 2):
        driver = webdriver.Chrome()
        driver.get(f'https://rozetka.com.ua/ua/mobile-phones/c80003/page={count}/')

        phone_urls = driver.find_elements(By.CSS_SELECTOR, '.goods-tile__picture')

        for i in phone_urls:
            phone_url = i.get_attribute('href')
            yield phone_url

        driver.quit()


def array():
    with open('full-info.txt', 'a', encoding='utf-8') as file:
        for phone_url in get_url():
            driver = webdriver.Chrome()
            driver.get(phone_url)

            phone = driver.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-title-block/div/div[1]/h1')
            phone_text = phone.text

            coast = driver.find_element(By.CSS_SELECTOR, '.product-price__big').text

            img_url = driver.find_element(By.CSS_SELECTOR, '.picture-container__picture')
            img_link = img_url.get_attribute('src')

            description = driver.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/p')
            description_text = description.text

            file.write(f"Phone: {phone_text}\nPrice: {coast}\nLink: {phone_url}\nImage: {img_link}\nDescription: {description_text}\n\n")

            driver.quit()


array()
