from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def buscarPccom(marca, movil):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.get("https://www.pccomponentes.com/smartphone-moviles")
    navegador.maximize_window()
    elem = navegador.find_element_by_xpath('//*[@id="acc-fil-0"]/div/a/span[1]')
    elem.submit()
    print(elem)
#    navegador.close()

buscarPccom("Samsung" ,"Galaxy S10")