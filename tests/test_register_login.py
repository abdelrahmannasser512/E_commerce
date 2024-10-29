from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.register import Register
from pages.login import WebLoginPage

import time



def test_register(browser):
      register_page=Register(browser)
      register_page.load()
      time.sleep(5)


      register_page.select_gender()
      
      register_page.select_first_name()
      register_page.select_last_name()
      register_page.select_e_mail()
      register_page.select_pass_word()
      register_page.select_confirm_pass_word()
      register_page.click_register()

      

def test_login(browser):
    login_page=WebLoginPage(browser)
    login_page.load()
    login_page.select_the_e_mail()
    login_page.select__the_pass_word()
    login_page.select_login()
   
    
    # login_page.click_myaccount()
    # time.sleep(5)
    # login_page.click_change_password()
    # time.sleep(5)
    login_page.change_currency()
    
    login_page.get_computer_topleftelement()
    # time.sleep(5)
    login_page.get_apparel_tag()
    # time.sleep(5)
    login_page.get_add_cart_nike()
    # time.sleep(5)

    login_page.select_print()

    login_page.select_size_color_print()
    # time.sleep(5)
    

    
    
    #login_page.product_quantity()
    time.sleep(2)

    login_page.add_to_cart_nike()
    time.sleep(3)
    
    
    # time.sleep(5)
    login_page.click_shopping_cart_icon()
    time.sleep(2)
    login_page.click_terms()

    login_page.click_checkout()
    time.sleep(2)
    login_page.checkout_page_company()
    login_page.change_page_country()
    login_page.checkout_page_city()
    login_page.checkout_page_myadressone()
    login_page.checkout_page_zipcode()
    login_page.checkout_page_phoneno()
    xpaths = ['//*[@id="billing-buttons-container"]/button[4]','//*[@id="shipping-method-buttons-container"]/button',
              '//*[@id="payment-method-buttons-container"]/button','//*[@id="payment-info-buttons-container"]/button',
              '//*[@id="confirm-order-buttons-container"]/button','/html/body/div[6]/div[3]/div/div/div/div[2]/div/div[3]/button']
    for x in xpaths:
         login_page.click_continue(x)


    
    time.sleep(10)
    







     


    
# def test_go_my_account(browser):
#     home_page=Home_Page(browser)
#     home_page.load
#     home_page.Click_Myaccount()
#     time.sleep(10)
    
    

