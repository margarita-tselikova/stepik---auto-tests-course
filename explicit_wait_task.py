from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button = browser.find_element_by_id('book')
    book_button.click()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(y)
    submit_button = browser.find_element_by_id('solve')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()