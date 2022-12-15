# Importaciones
from selenium.webdriver.common.by import By
import Config

# Scraper de información
degree = Config.driver.find_element(By.XPATH, "//*[@data-testid='TemperatureValue']").text
state = Config.driver.find_element(By.XPATH, "//*[@data-testid='wxPhrase']").text
sunrise = Config.driver.find_element(By.XPATH, "//*[@data-testid='SunsetValue']").text
humidity = Config.driver.find_element(By.XPATH, "//*[@data-testid='PercentageValue']").text
visibility = Config.driver.find_element(By.XPATH, "//*[@data-testid='VisibilityValue']").text

# Enseñar información
print(f"The temperature is {degree} celscius")
print(f"El clima está {state}")
print(f"La humedad es de {humidity}")
print(f"La visibilidad es de {visibility}")
