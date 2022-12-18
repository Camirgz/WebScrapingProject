# Get cities temperature
import Config
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Berlin
berlin = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[1]/span[1]").text
berlintemp = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[1]/span[2]").text

# Buenos Aires
buenosaires = Config.driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[3]/span[1]").text
buenosairestemp = Config.driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[3]/span[2]").text

# Ciudad de México
cdmx = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[4]/span[1]").text
cdmxtemp = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[4]/span[2]").text

# Estambul
estambul = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[7]/span[1]").text
estambultemp = Config.driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[7]/span[2]").text

# Londres
londres = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[9]/span[1]").text
londrestemp = Config.driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[9]/span[2]").text

# Madrid
madrid = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[11]/span[1]").text
madridtemp = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/a[11]/span[2]").text

print(berlin, berlintemp)
print(buenosaires, buenosairestemp)
print(cdmx, cdmxtemp)
print(estambul, estambultemp)
print(londres, londrestemp)
print(madrid, madridtemp)