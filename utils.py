from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def wait_url_changed(driver: WebDriver, old_url, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.url_changes(old_url))
    except Exception:
        return False
    return True


def wait_for_element(driver: WebDriver, element_selector, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
    except Exception:
        return False
    return True


def wait_for_element_disappeared(driver: WebDriver, element_selector, timeout):
    try:
        WebDriverWait(driver, timeout).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
    except Exception:
        return False
    return True


def clear_input(element):
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
