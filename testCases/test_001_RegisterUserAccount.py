
import pytest
from selenium import webdriver
from PageObject.RegisterUserAccount import RegisterUserAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from Utilities.readproperties import ReadConfig
from Utilities.customLog import LogGen


class Test_001_Register_User_Account:
    url="https://testautomationpractice.blogspot.com/"
    # url=Readconfig.get_ApplicationURL()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_Reg_Account(self,setup):
        self.driver=setup
        # self.driver=webdriver.Chrome()
        # self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


        self.rua=RegisterUserAccount(self.driver)
        self.rua.click_Home_Tab()
        self.rua.setName("Ama")
        self.rua.setEmail("tiyumiddi@gmail.com")
        # self.email=randomString.random_String_generator()+'@gmail.com'
        # self.rua.setEmail(self.email)
        self.rua.setPhone_Number("7007007007")
        self.rua.setAddress("504 Greenlawn Dr")
        self.rua.clickGenderBtn()
        self.rua.clickDays()
        # self.rua.clickCountryDropdown()
        self.rua.selectCountry("United States")
        self.rua.clickColorOption()
        self.rua.selectSort()
        self.rua.clickDate()
        self.rua.clickSubmitBtn()
        self.driver.quit()




