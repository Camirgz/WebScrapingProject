import Config
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# San José
findsjo = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div/div[1]/div[1]/form/input")
findsjo.send_keys("San José", Keys.ARROW_DOWN, Keys.ARROW_DOWN)
findsjo.click()

finddiario = Config.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[3]/a[3]/span")
finddiario.click()

# sjotemp = Config.driver.find_element(By.XPATH, "").text
# print(sjotemp)

# Config.driver.quit()