from copyreg import constructor
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterUserAccount():
     # locators
     home_tab_xpath = "//div[@id='PageList2']//a[normalize-space()='Home']"
     name_input_box_xpath = "//input[@id='name']"
     email_input_box_xpath = "//input[@id='email']"
     phone_input_box_xpath = "//input[@id='phone']"
     address_input_box_xpath = "//textarea[@id='textarea']"
     gender_radio_btn_xapth = "//input[@id='female']"
     days_check_box_xpath = "//label[normalize-space()='Tuesday']"
     country_dropdown_xpath = "//select[@id='country']"
     color_option_xpath = "//select[@id='colors']//option[3]"
     select_sort_list_xpath = "//option[@value='cat']"
     date_picker_xpath = "//input[@id='datepicker']"
     submit_btn_xpath = "//button[@class='submit-btn']"

     # constructor
     def __init__(self, driver):
         self.driver = driver

         # action methods
     def click_Home_Tab(self):
         self.driver.find_element(By.XPATH,self.home_tab_xpath).click()

     def setName(self,name):
         self.driver.find_element(By.XPATH,self.name_input_box_xpath).send_keys(name)

     def setEmail(self,email):
         self.driver.find_element(By.XPATH,self.email_input_box_xpath).send_keys(email)

     def setPhone_Number(self,phone):
         self.driver.find_element(By.XPATH,self.phone_input_box_xpath).send_keys(phone)

     def setAddress(self,address):
         self.driver.find_element(By.XPATH,self.address_input_box_xpath).send_keys(address)

     def clickGenderBtn(self):
         self.driver.find_element(By.XPATH,self.gender_radio_btn_xapth).click()

     def clickDays(self):
         self.driver.find_element(By.XPATH,self.days_check_box_xpath).click()

     def selectCountry(self,country):
         self.driver.find_element(By.XPATH,self.country_dropdown_xpath).click()


     def clickColorOption(self):
         self.driver.find_element(By.XPATH,self.color_option_xpath).click()

     def selectSort(self):
         # WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(By.XPATH,self.select_sort_list_xpath)).click()
         WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH,self.select_sort_list_xpath))).click()
     #Note:lamda is used for anonymous expressions. Either of the statements work

     def clickDate(self):
         self.driver.find_element(By.XPATH,self.date_picker_xpath).click()

     def clickSubmitBtn(self):
         self.driver.find_element(By.XPATH,self.submit_btn_xpath).click()





