from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    s = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(s)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.ID, "solve")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()