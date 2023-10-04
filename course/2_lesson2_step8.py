import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("firstname")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("lastname")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("email@mail.ru")

    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
