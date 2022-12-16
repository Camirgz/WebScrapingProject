# Get cities temperature
import Config
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# San José, Costa Rica
degree_CR = Config.driver.find_element(By.XPATH, "//*[@data-testid='TemperatureValue']").text
print(degree_CR)


elem = Config.driver.find_element(By.CLASS_NAME, "SearchInput--InputField--1UoCv Search--inputClass--1FEhl")
elem.send_keys("Madrid")
elem.send_keys(Keys.ENTER)


