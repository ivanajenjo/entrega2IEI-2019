from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def buscarPccom(marca, movil):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.get("https://www.pccomponentes.com")
    navegador.maximize_window()
    ventanacookies = navegador.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/button")
    if ventanacookies != None :
        print("Detectado caja de cookies")
        ventanacookies.click()
    elem = navegador.find_element_by_name("query")
    elem.send_keys(movil)
    elem.send_keys(Keys.RETURN)
    element = navegador.find_element_by_css_selector('#acc-fil-538 > div > ul > li:nth-child(1) > a')
    if element != None:
        element.click()
        print("Pulsado sobre Telefonos")

buscarPccom("Samsung" ,"Galaxy S10")