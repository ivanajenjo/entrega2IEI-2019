from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def buscarAmazon(movil):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.maximize_window()
    navegador.get("https://www.amazon.es/gp/browse.html?node=931491031&ref_=nav_em_T1_0_4_12_2__tele")
    elem = navegador.find_element_by_id("twotabsearchtextbox")
    elem.send_keys(movil)
    elem.submit()
    delay = 3
    try:
        elem = WebDriverWait(navegador, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-size-medium a-color-base a-text-normal')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    elem = navegador.find_element_by_class_name("a-size-medium a-color-base a-text-normal")
    print(elem.text)
    navegador.close()

buscarAmazon("Samsung Galaxy S10")