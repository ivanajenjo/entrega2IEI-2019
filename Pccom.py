from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

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
    time.sleep(5)
    WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/ul/li[1]/a')))
    listaElementos = navegador.find_elements_by_xpath ( "//*[contains(@class, 'tarjeta-articulo expandible')]" )
    print(len(listaElementos))
    j = 1
    resultado = list()
    for i in listaElementos:
        elementoActual = i
        nombre = elementoActual.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[3]/div/div["+str(j)+"]/article/div[1]/header/h3")
        print(nombre.text)
        precio = elementoActual.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[3]/div/div["+str(j)+"]/article/div[1]/div[2]/div")
        print(precio.text)
        resultado.append((nombre.text + " " + precio.text))
        j = j + 1
    print(resultado)

buscarPccom("Samsung" ,"Galaxy S10")