from selenium import webdriver
import time
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
    time.sleep(5)
    #WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "celwidget slot=SEARCH_RESULTS template=SEARCH_RESULTS widgetId=search-results index=2")))
    listaElementos = navegador.find_elements_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div[3]")
    print(len(listaElementos))
    print("a")

buscarAmazon("Samsung Galaxy S10")