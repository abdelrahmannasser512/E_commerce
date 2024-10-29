from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select


class WebLoginPage:

      LOGIN_URL=r"https://demo.nopcommerce.com/login?returnUrl=%2F"
      themail=(By.XPATH,'//*[@id="Email"]')
      thepassword=(By.XPATH,"//input[@id='Password']")
      changepassword=(By.XPATH,"//a[@href='/customer/changepassword']")
         

      def __init__(self,browser):
            self.browser=browser
         
      def load(self):
            #      self.browser.delete_all_cookies()
                 
            self.browser.get(WebLoginPage.LOGIN_URL)
                 


                 
        
      def select_the_e_mail(self):
            select_login_e_mail=self.browser.find_element(*WebLoginPage.themail)
            select_login_e_mail.send_keys("abdelrahmannasser512@gmail.com")

      def select__the_pass_word(self):
            select_login_password=self.browser.find_element(*WebLoginPage.thepassword)
            select_login_password.send_keys("rhrS!Jr5FPaKuV")

      def select_login(self):
            lognbutton=(By.XPATH,"//button[contains(.,'Log in')][@class='button-1 login-button']")
            click_login_button  = self.browser.find_element(*lognbutton)
            rememberme=(By.XPATH,'//*[@id="RememberMe"]')
            rememberme_button=self.browser.find_element(*rememberme)
            ActionChains(self.browser).click(rememberme_button).perform()
            time.sleep(2)
            ActionChains(self.browser).click(click_login_button).perform()
              
              
              
     #     def click_myaccount(self):
              
     #          myaccount=(By.XPATH,"//a[contains(@class,'ico-account')]")
              
     #          click_myaccount_button = self.browser.find_element(*myaccount)
              
     #          ActionChains(self.browser).click(click_myaccount_button).perform()


            click_login_button  = self.browser.find_element(*WebLoginPage.loginbutton)
      def click_change_password(self):
               click_change_pass=self.browser.find_element(*self.changepassword)
               ActionChains(self.browser).click(click_change_pass).perform()
      def change_currency(self):
            self.browser.maximize_window()
            time.sleep(3)
               
            change_currency_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "customerCurrency")))
                                          
             
               
            # change_currency_button=self.browser.find_element(By.ID,"customerCurrency")
               

               
               #idvalue=change_currency_button.get_attribute("ID")
            ActionChains(self.browser).click(change_currency_button).perform()
               
            us_dollar=self.browser.find_element(By.XPATH,"//select[@id='customerCurrency']/option[1]")
            euro=self.browser.find_element(By.XPATH,"//select[@id='customerCurrency']/option[2]")
            usdollar_selected=False
               
            if euro.get_attribute("selected") :
                time.sleep(3)
                
                 
                change_currency_button.send_keys(Keys.ARROW_UP+Keys.ENTER )
                
                
            #     change_currency_button = WebDriverWait(self.browser, 5).until(
            # EC.presence_of_element_located((By.ID, "customerCurrency")))
            #     s= Select(change_currency_button)
            #     element=s.first_selected_option

                
            #     dollarsymbolelement = WebDriverWait(self.browser, 10).until(
            # EC.presence_of_element_located((By.XPATH, "//span[contains(.,'$1,200.00')]")))
            #     self.browser.execute_script("arguments[0].scrollIntoView();", dollarsymbolelement)

            #     assert element.text =="US Dollar"
            #     assert dollarsymbolelement.text =="$1,200.00"
                     


            else:
                time.sleep(3)

                
                
                change_currency_button.send_keys(Keys.ARROW_DOWN+Keys.ENTER )
            #     eurosymbol=(By.XPATH,"//span[contains(.,'€1032.00')]")
            #     self.browser.execute_script("arguments[0].scrollIntoView();", eurosymbol)
                
            #     change_currency_button = WebDriverWait(self.browser, 5).until(
            # EC.presence_of_element_located((By.ID, "customerCurrency")))
            #     s= Select(change_currency_button)
            #     element=s.first_selected_option
                
            #     time.sleep(3)
            #     eurosymbolelement = WebDriverWait(self.browser, 10).until(
            # EC.presence_of_element_located((By.XPATH, "//span[contains(.,'€1032.00')]")))
            #     assert element.text  =="Euro"
            #     assert eurosymbolelement.text =="€1032.00"
            # #    self.browser.delete_all_cookies()
            time.sleep(3)
               
                     
                
                     
                     
                     
               
                     
                     
                     
                     
                     
               
               

               

               
               
              
               
      def get_computer_topleftelement(self):
            time.sleep(5)
            getcomputericon=(By.XPATH,"/html/body/div[6]/div[2]/ul[1]/li[1]/a")
            getcomputericon2=(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']")
            getcomputericon3=(By.CSS_SELECTOR,"body > div:nth-child(7) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)")
            getdesktopicon=(By.XPATH,"(//a[@href='/desktops'])[1]")
            #getcomputericonelement=self.browser.find_element(*getcomputericon)
            #getcomputericonelement2=self.browser.find_element(*getcomputericon2)
            getcomputericonelement3=self.browser.find_element(*getcomputericon3)
            getdesktopiconelement=self.browser.find_element(*getdesktopicon)
               
               
               
               
            #    ActionChains(self.browser).move_to_element(getcomputericonelement
            #    ).perform()
            #    ActionChains(self.browser).move_to_element(getcomputericonelement2
            #    ).perform()
            ActionChains(self.browser).move_to_element(getcomputericonelement3
             ).perform()
            time.sleep(3)
               
            ActionChains(self.browser).click(getdesktopiconelement
            ).perform()
               

            
             
      def get_apparel_tag(self):
            time.sleep(4)
            getappareltag=(By.XPATH,"//a[normalize-space()='apparel']")
            getappareltagbutton=self.browser.find_element(*getappareltag)
            ActionChains(self.browser).click(getappareltagbutton).perform()
            time.sleep(2)
      def get_add_cart_nike(self):
            getaddtocartnike=(By.XPATH,"""//button[contains(@onclick,'catalog("/addproducttocart/catalog/24/1/1"),!1')]""")
            getaddtocartnikebutton=self.browser.find_element(*getaddtocartnike)
            ActionChains(self.browser).click(WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, """//button[contains(@onclick,'catalog("/addproducttocart/catalog/24/1/1"),!1')]""")))).perform()
            time.sleep(2)
      def select_size_color_print(self):
            get_size_element=(By.ID,"product_attribute_6")
            get_size_element_button=self.browser.find_element(*get_size_element)
            ActionChains(self.browser).click(WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID,"product_attribute_6")))).perform()
               
            get_size_element_button.send_keys(Keys.ARROW_DOWN )
               
            ActionChains(self.browser).click(get_size_element_button).perform()

               

               
            get_color_element=(By.ID,"product_attribute_7")
            get_color_element_button=self.browser.find_element(*get_color_element)
            ActionChains(self.browser).click(get_color_element_button).perform()
               
            get_color_element_button.send_keys(Keys.ARROW_DOWN )
               

            ActionChains(self.browser).click(get_color_element_button).perform()

      def select_print(self):
            get_select_element=(By.XPATH,"//li[2]//span[@class='attribute-square']")
            get_select_element_button=self.browser.find_element(*get_select_element)
               
            ActionChains(self.browser).click(get_select_element_button).perform()
               
               
      def product_quantity(self):
            get_product_quantity=(By.XPATH,"//input[contains(@id,'24')]")
               
            get_product_quantity_element=get_product_quantity.find_element(*get_product_quantity)
               
            get_product_quantity_element.send_keys(  Keys.BACK_SPACE + "2"+Keys.ENTER)
               

               
               
               
      def add_to_cart_nike(self):
            get_add_to_cart=(By.ID,"add-to-cart-button-24")
            get_add_to_cart_element=self.browser.find_element(*get_add_to_cart)
            ActionChains(self.browser).click(get_add_to_cart_element).perform()
            time.sleep(3)

               
      def click_shopping_cart_icon(self):
            get_shopping_icon=(By.XPATH,"//span[@class='cart-label']")
            get_shopping_icon_element=self.browser.find_element(*get_shopping_icon)
            ActionChains(self.browser).click(get_shopping_icon_element).perform()
               
               
      def click_terms(self):
            get_click_terms_element=(By.ID,"termsofservice")
            get_click_terms_element_button=self.browser.find_element(*get_click_terms_element)
               
            ActionChains(self.browser).click(WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID,"termsofservice")))).perform()
               
               
      def click_checkout(self):
            get_click_checkout_element=(By.ID,"checkout")
            get_click_checkout_element_button=self.browser.find_element(*get_click_checkout_element)
               
            ActionChains(self.browser).click(WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID,"checkout")))).perform()
            time.sleep(4)
      def checkout_page_company(self):
            get_click_company_element=(By.ID,"BillingNewAddress_Company")
            get_click_company_element_button=self.browser.find_element(*get_click_company_element)
            get_click_company_element_button.send_keys("mycompanyname")
            time.sleep(4)
      def checkout_page_city(self):
            get_click_city_element=(By.ID,"BillingNewAddress_City")
            get_click_city_element_button=self.browser.find_element(*get_click_city_element)
            get_click_city_element_button.send_keys("BillingNewAddress_City")
            time.sleep(4)
      def checkout_page_myadressone(self):
            get_click_myadressone_element=(By.ID,"BillingNewAddress_Address1")
            get_click_myadressone_element_button=self.browser.find_element(*get_click_myadressone_element)
            get_click_myadressone_element_button.send_keys("BillingNewAddress_Address1")
            time.sleep(4)
      def checkout_page_zipcode(self):
            get_click_zipcode_element=(By.ID,"BillingNewAddress_ZipPostalCode")
            get_click_zipcode_element_button=self.browser.find_element(*get_click_zipcode_element)
            get_click_zipcode_element_button.send_keys(11702)
            time.sleep(4)
      def checkout_page_phoneno(self):
            get_click_phoneno_element=(By.XPATH,'//*[@id="BillingNewAddress_PhoneNumber"]')
            get_click_phoneno_element_button=self.browser.find_element(*get_click_phoneno_element)
            get_click_phoneno_element_button.send_keys(1122662215)
            time.sleep(4)
      def change_page_country(self):
            get_click_country_element=(By.XPATH,"""//*[@id="BillingNewAddress_CountryId"][@name='BillingNewAddress.CountryId']""")
            get_select_usa_element=(By.XPATH,'//*[@id="BillingNewAddress_CountryId"]/option[2]')
            get_click_usa_element_button=self.browser.find_element(*get_click_country_element)
            time.sleep(2)
            # ActionChains(self.browser).move_to_element(get_click_country_element
            #  ).perform()
            # ActionChains(self).click(get_click_country_element).perform()

            get_click_usa_element_button.send_keys(Keys.ENTER)
            get_click_usa_element_button.send_keys(Keys.ARROW_DOWN)
            get_click_usa_element_button.send_keys(Keys.ARROW_DOWN)
            get_click_usa_element_button.send_keys(Keys.ENTER)

            # ActionChains(self.browser).move_to_element(get_click_usa_element_button
            #  ).perform()
            # ActionChains(self).click(get_click_usa_element_button).perform()
      def click_continue(self, xpath):
            get_continue_element=(By.XPATH,xpath)#'//*[@id="billing-buttons-container"]/button[4]')
            get_continue_element_button=self.browser.find_element(*get_continue_element)
            get_continue_element_button.send_keys(Keys.ENTER)
            time.sleep(3)
            
      def continuetwo(self):
            get_continue_element=(By.XPATH,'//*[@id="billing-buttons-container"]/button[4]')
            get_continue_element_button=self.browser.find_element(*get_continue_element)
            get_continue_element_button.send_keys(Keys.ENTER)
            time.sleep(3)
      # def clcik_continue_confrim(self):
      #       get_c_element_confirm=(By.XPATH,'//*[@id="billing-buttons-container"]/button[4]')
      def contiuethree(self):
            get_continue_element=(By.XPATH,'//*[@id="shipping-method-buttons-container"]/button')
            get_continue_element_button=self.browser.find_element(*get_continue_element)
            get_continue_element_button.send_keys(Keys.ENTER)
            time.sleep(3)
      def continuefour(self):
            get_continue_element=(By.XPATH,'//*[@id="payment-method-buttons-container"]/button')
            get_continue_element_button=self.browser.find_element(*get_continue_element)
            get_continue_element_button.send_keys(Keys.ENTER)
            time.sleep(3)
      def confirm(self):
            get_continue_element=(By.XPATH,'//*[@id="payment-info-buttons-container"]/button')
            get_continue_element_button=self.browser.find_element(*get_continue_element)
            get_continue_element_button.send_keys(Keys.ENTER)
            time.sleep(3)

            
      def confirmlast(self):
            get_continue_element=(By.XPATH,'//*[@id="confirm-order-buttons-container"]/button')
            get_continue_element_button=self.browser.find_element(*get_continue_element)
            get_continue_element_button.send_keys(Keys.ENTER)
            time.sleep(3)
      def confirmlastlast(self):
            get_continue_element=(By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/div/div[3]/button')
            get_continue_element_button=self.browser.find_element(*get_continue_element)
            get_continue_element_button.send_keys(Keys.ENTER)
            time.sleep(3)





      

            
            

            
      
         
               

 



         
         

         





               







               







               


               

         
               
         



          
                
            

                 
         
         