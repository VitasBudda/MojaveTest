from selenium import webdriver
from test_pages.login_page import LoginPage


BASE_URL = 'http://localhost:3000/login'

TEST_USER_USERNAME = 'VitasActivated'
TEST_USER_EMAIL = 'jiwor10449@64ge.com'
TEST_USER_PASSWORD = 'MySecurePassword123'
INVALID_USER_EMAIL = 'invalid_user@gmail.com'
INVALID_USER_PASSWORD = 'invalid_password'
TEST_CHAT_MESSAGE = 'some test message'


def create_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    return webdriver.Chrome(options=options)


def run_tests():
    driver = create_web_driver()
    driver.get(BASE_URL)

    # login page tests
    login_page = LoginPage(driver)

    # test login client errors
    login_page.submit_login_expecting_failure()
    client_form_errors = login_page.get_client_form_errors()
    assert len(client_form_errors) > 0

    # test login server errors
    login_page.type_email(INVALID_USER_EMAIL)
    login_page.type_password(INVALID_USER_PASSWORD)
    login_page.submit_login_expecting_failure()

    server_form_errors = login_page.get_server_form_errors()
    assert len(server_form_errors) > 0

    # login with existing credentials
    login_page.type_email(TEST_USER_EMAIL)
    login_page.type_password(TEST_USER_PASSWORD)
    game_page = login_page.submit_login_expecting_success()

    game_page.type_chat_msg(TEST_CHAT_MESSAGE)
    game_page.submit_chat_msg()
    messages = game_page.get_chat_messages()
    assert (TEST_USER_USERNAME, TEST_CHAT_MESSAGE) in messages

    print('All tests were passed successfully')


if __name__ == '__main__':
    try:
        run_tests()
    except Exception as e:
        print('An exception was thrown during running tests: ' + str(e))
