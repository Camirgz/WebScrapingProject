# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Navigation Options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = r'C:\Users\chromedriver.exe'
driver = webdriver.Chrome(service=Service(driver_path))

# Navigator
driver.get('https://weather.com/weather/today/l/c71832b54454644e6c9d1dee74b801e368e1bee82cd6368acc47945d415a4469')




