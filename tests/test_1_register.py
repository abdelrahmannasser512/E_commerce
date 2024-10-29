from pages.register import Register
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_register(browser):
    register_page=Register(browser)
    wait = WebDriverWait(browser,10)
    register_page.load()
    register_page.select_gender()
    register_page.select_first_name()
    register_page.select_last_name()
    register_page.select_e_mail()
    register_page.select_pass_word()
    register_page.select_confirm_pass_word()
    register_page.click_register()

    time.sleep(10)
    

