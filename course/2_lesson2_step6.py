from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    res = calc(x)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    browser.execute_script("window.scrollBy(0, 100);")

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(res)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()

    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


