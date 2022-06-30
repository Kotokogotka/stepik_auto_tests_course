import os
from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Заполняем поля
    namee = browser.find_element(By.NAME, "firstname")
    namee.send_keys("Andrey")
    last = browser.find_element(By.NAME, "lastname")
    last.send_keys("Zaka")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("zaka@yandex.ru")
    current_dir = os.path.abspath("C:/Users/asics/Desktop") # находим директорию файла
    file_name = "text.txt" # указываем имя файла
    file_path = os.path.join(current_dir, file_name) # путь до файла
    element = browser.find_element(By.ID, "file") # ищим кнопку загрузки
    element.send_keys(file_path) # отправляем файл
    time.sleep(2)
    button = browser.find_element(By.CLASS_NAME, "btn-primary").click() # клик по кнопке Submit


finally:
    time.sleep(12) #прочтем и посмотрим, что произойдет
    browser.quit()