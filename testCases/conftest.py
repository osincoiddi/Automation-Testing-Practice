
import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from datetime import datetime

@pytest.fixture
def setup(browser):
    if browser=="edge":
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launching edge browser")
        return driver
    elif browser=="firefox":
        driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("Launching firefox browser")
        return driver
    else:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching chrome browser")
        return driver


def pytest_addoption(parser):
 parser.addoption("--browser") #This gets the value from hooks

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")#This returns browser value to setup method


##Generating HTML report##

#Hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name']='AutomationTestingPractice'
    config._metadata['Module Name']='PageObject'

#Hook to delete/modify environment info for html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)

#Hook for specifying report/folder directory
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now=datetime.now()
    config.option.htmlpath=os.path.abspath(os.path.curdir)+"\\reports\\"+now.strftime("%d-%m-%Y-%H-%M-%S")+"_report.html"




