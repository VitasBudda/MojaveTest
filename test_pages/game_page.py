from selenium.webdriver.remote.webdriver import WebDriver

from utils import wait_for_element

CHAT_FIELD_SELECTOR = '#chat_textarea'
SUBMIT_CHAT_SELECTOR = '#send_message'
MSG_USERNAME_SELECTOR = 'li.message div.name'
MSG_CONTENT_SELECTOR = 'li.message div.text'
ELEMENT_VISIBLE_TIMEOUT = 2


class GamePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def type_chat_msg(self, message):
        wait_for_element(self.driver, CHAT_FIELD_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        chat_field = self.driver.find_element_by_css_selector(CHAT_FIELD_SELECTOR)
        chat_field.send_keys(message)

        return GamePage(self.driver)

    def submit_chat_msg(self):
        wait_for_element(self.driver, SUBMIT_CHAT_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        submit_btn = self.driver.find_element_by_css_selector(SUBMIT_CHAT_SELECTOR)
        submit_btn.click()

        return GamePage(self.driver)

    def get_chat_messages(self):
        wait_for_element(self.driver, MSG_USERNAME_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        chat_usernames = self.driver.find_elements_by_css_selector(MSG_USERNAME_SELECTOR)
        usernames = [x.text for x in chat_usernames]

        wait_for_element(self.driver, MSG_CONTENT_SELECTOR, timeout=ELEMENT_VISIBLE_TIMEOUT)
        chat_texts = self.driver.find_elements_by_css_selector(MSG_CONTENT_SELECTOR)
        texts = [x.text for x in chat_texts]

        return [(i, j) for i, j in zip(usernames, texts)]
