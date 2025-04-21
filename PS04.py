from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

hatnotes = []
req = input('Введите начальный поисковый запрос WiKi: ')
browser = webdriver.Firefox()

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
#Проверяем по заголовку, тот ли сайт открылся
assert "Википедия" in browser.title
search_box = browser.find_element(By.ID, "searchInput")
#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
search_box.send_keys(req)
#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
while n := int(input('[0] Выход, [1] Листать параграфы, [2] Выбор подстатьи. ')):
    if n==1:
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        # Для перебора пишем цикл
        for paragraph in paragraphs:
            print(paragraph.text)
            input()
        print(f'{" параграфы закончились ":-^40}')
    elif n==2:
        hatnotes.clear()
        for element in browser.find_elements(By.TAG_NAME, "div"):
        # Чтобы искать атрибут класса
            cl = element.get_attribute("class")
            if cl == "mw-search-result-heading":
                hatnotes.append(element)

        if hatnotes:
            hatnote = random.choice(hatnotes)

            # Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link)
        else:
            print(f'{" подстатей нет ":-^40}')

browser.quit()

# a = browser.find_element(By.LINK_TEXT, "Солнечная система")
# #Добавляем клик на элемент
# a.click()