from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestOfParametrization():


    @pytest.mark.parametrize('url', ['https://stepik.org/lesson/236895/step/1',
                                     'https://stepik.org/lesson/236896/step/1',
                                     'https://stepik.org/lesson/236897/step/1',
                                     'https://stepik.org/lesson/236898/step/1',
                                     'https://stepik.org/lesson/236899/step/1',
                                     'https://stepik.org/lesson/236903/step/1',
                                     'https://stepik.org/lesson/236904/step/1',
                                     'https://stepik.org/lesson/236905/step/1'])
    def test_parametrization_and_markers(self, browser, url):
        browser.get(url)
        answer_field_wait = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'ember66')))
        answer_field = browser.find_element_by_id("ember67")
        answer = math.log(int(time.time()))
        answer_field.send_keys(str(answer))
        submit_button = browser.find_element_by_css_selector("button")
        submit_button.click()
        result_message_wait = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'pre')))
        message = browser.find_element_by_tag_name('pre').text
        assert message == 'Correct!', "Optional feedback isn't 'Correct!'"

    time.sleep(3)
