from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
    command_executor='http://192.168.56.7:4444/wd/hub',
    options=options
)
