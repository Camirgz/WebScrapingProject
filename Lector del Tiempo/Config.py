# Librerías
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = r'C:\Users\chromedriver.exe'
driver = webdriver.Chrome(service=Service(driver_path))

# Inicializamos el navegador
driver.get('https://servicioselectorales.tse.go.cr/chc/consulta_cedula.aspx')
