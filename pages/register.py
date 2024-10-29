

from selenium.webdriver.common.by import By


from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time





class Register:
    URL= r"https://demo.nopcommerce.com/register?returnUrl=%2F"
    gender=(By.ID,"gender-male")
    first_name=(By.ID,"FirstName")
    last_name=(By.ID,"LastName")
    email=(By.ID,"Email")
    password=(By.ID,"Password")
    confirm_password=(By.ID,"ConfirmPassword")
    register=(By.XPATH,"//button[@id='register-button']")
    def __init__(self,browser):
        self.browser=browser

    def load(self):
        self.browser.get(Register.URL)

    def select_gender(self):
        self.browser.maximize_window()
        male_gender_selection_element  = self.browser.find_element(*Register.gender)
        ActionChains(self.browser).click(WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "gender-male")))).perform()

    def select_first_name(self):
         select_first_name_blank=self.browser.find_element(*Register.first_name)
         select_first_name_blank.send_keys("Abdelrahman")

    def select_last_name(self):
         select_last_name_blank=self.browser.find_element(*Register.last_name)
         select_last_name_blank.send_keys("sayednasserahmed")

    def select_e_mail(self):
         select_email=self.browser.find_element(*Register.email)
         select_email.send_keys("abdelrahmannasser512@gmail.com")

    def select_pass_word(self):
         select_password=self.browser.find_element(*Register.password)
         select_password.send_keys("rhrS!Jr5FPaKuV")

    def select_confirm_pass_word(self):
         select_confirm_password=self.browser.find_element(*Register.confirm_password)
         select_confirm_password.send_keys("rhrS!Jr5FPaKuV")

    def click_register(self):
        time.sleep(5)
        register_button  = self.browser.find_element(*Register.register)
        self.browser.execute_script("arguments[0].scrollIntoView();", register_button)
        ActionChains(self.browser).click(register_button).perform()
        time.sleep(3)



                 
    



         
    

        



