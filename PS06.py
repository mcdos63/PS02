#Код, написанный с использованием новых селекторов.
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

datas = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

parsed_data = []

for data in datas:
    try:
        name = data.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = data.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = data.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')


    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([name, price, url])

driver.quit()

with open("divan_svet.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)