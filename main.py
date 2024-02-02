from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

for count in range(1, 2):
    driver = webdriver.Chrome()
    driver.get(f'https://rozetka.com.ua/ua/mobile-phones/c80003/page={count}/')

    phones = driver.find_elements(By.CSS_SELECTOR, '.goods-tile__heading')
    coasts = driver.find_elements(By.CSS_SELECTOR, '.goods-tile__price-value')
    phone_urls = driver.find_elements(By.CSS_SELECTOR, '.goods-tile__picture')

    with open('phones.txt', 'a', encoding='utf-8') as file:
        for phone, coast, phone_url in zip(phones, coasts, phone_urls):
            phone_title = phone.get_attribute('title')
            coast_value = coast.text
            phone_link = phone_url.get_attribute('href')
            img_url = phone_url.find_element(By.TAG_NAME, 'img')
            img_link = img_url.get_attribute('src')

            file.write(f"Phone: {phone_title}\nPrice: {coast_value}\nLink: {phone_link}\nImage: {img_link}\n\n")

    driver.quit()
