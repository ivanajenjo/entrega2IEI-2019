from selenium import webdriver


def buscarFnac(marca, movil):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.get("https://www.fnac.es")
    navegador.maximize_window()
    ventanacookies = navegador.find_element_by_xpath("/html/body/aside/div/button")
    if ventanacookies != None :
        print("Detectado caja de cookies")
        ventanacookies.click()
    cajabusqueda = navegador.find_element_by_id("Fnac_Search")
    cajabusqueda.send_keys(movil)
    cajabusqueda.submit()
    element = navegador.find_element_by_css_selector('#col_gauche > div > div.nav > div.content > ul > li:nth-child(1) > ul > li:nth-child(1) > span')
    if element != None:
        element.click()
        print("Pulsado Sobre telefonos")
    listaElementos = navegador.find_elements_by_xpath("//*[contains(@class, 'Article-itemGroup')]")
    print(len(listaElementos))
    j = 1
    for i in listaElementos:
        elementoActual = i
        navegacion = elementoActual.find_element_by_xpath("/html/body/div[3]/div/div[7]/div/div["+str(j)+"]/article/div[2]/div/p[1]")
        print(navegacion.text)
        j = j+1


buscarFnac("Samsung", "Galaxy S10")

