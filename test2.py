from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    inp1 = browser.find_element(By.NAME, "firstname")
    inp1.send_keys('firstname')
    inp2 = browser.find_element(By.NAME, "lastname")
    inp2.send_keys('lastname')
    inp3 = browser.find_element(By.NAME, "email")
    inp3.send_keys('email@email.com')

    fileb = browser.find_element(By.ID, "file")
    fileb.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()