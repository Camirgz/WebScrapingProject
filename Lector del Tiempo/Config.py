# Library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Navigation Options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = r'C:\Users\chromedriver.exe'
driver = webdriver.Chrome(service=Service(driver_path))

# Navigator
driver.get('https://weather.com/es-CR/tiempo/hoy/l/CSXX0009:1:CS?Goto=Redirected')


