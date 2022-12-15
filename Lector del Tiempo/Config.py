# Librerías
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = r'C:\Users\chromedriver.exe'
driver = webdriver.Chrome(service=Service(driver_path))

# Navegador
driver.get('https://weather.com/es-CR/tiempo/hoy/l/CSXX0009:1:CS?Goto=Redirected')


