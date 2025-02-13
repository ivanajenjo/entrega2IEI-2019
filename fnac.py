def buscarFnac(marca, movil):
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    import time
    busqueda = marca + " " + movil
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.get("https://www.fnac.es")
    navegador.maximize_window()
    ventanacookies = navegador.find_element_by_xpath("/html/body/aside/div/button")
    if ventanacookies != None:
        print("Detectado caja de cookies")
        ventanacookies.click()
    cajabusqueda = navegador.find_element_by_id("Fnac_Search")
    cajabusqueda.send_keys(busqueda)
    cajabusqueda.submit()
    try:
        element = navegador.find_element_by_css_selector(
            '#col_gauche > div > div.nav > div.content > ul > li:nth-child(1) > ul > li:nth-child(1) > span')
        if element != None:
            element.click()
            print("Pulsado sobre Telefonos")
    except:
        print("Teléfono no disponible")
        return("Teléfono no disponible en Fnac")
    elem = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[1]/div/div/ul/li[7]/span')))
    try:
        element = navegador.find_element_by_css_selector(
            '#col_gauche > div > div.sticky > div.Filters.js-SearchFilters > div.js-FiltersContainer.js-FiltersContainer--vendor > div > a.Filters-choice.js-Filters-choice.js-Filters-choice--vendor-fnacdarty.isActive > label > span.Filters-choiceLabel')
    except:
        print("No existe vendedor fnac")
    time.sleep(5)
    if element != None:
        try:
            element.click()
        except:
            print("")
        print("Pulsado Vendedor Fnac")
    try:
        elem = WebDriverWait(navegador, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[2]/div[2]/span/ul/li/a')))
    except:
        print("No se ha encontrado elemento")
    listaElementos = navegador.find_elements_by_xpath("//*[contains(@class, 'Article-itemGroup')]")
    print(len(listaElementos))
    j = 1
    resultado = list()
    for i in listaElementos:
        elementoActual = i
        nombre = elementoActual.find_element_by_xpath(
            "/html/body/div[3]/div/div[7]/div/div[" + str(j) + "]/article/div[2]/div/p[1]")
        print(nombre.text)
        try:
            precio = elementoActual.find_element_by_xpath(
                "/html/body/div[3]/div/div[7]/div/div[" + str(j) + "]/article/div[3]/div/div/div/div/div[3]/span[2]")
        except:
            precio = elementoActual.find_element_by_xpath(
                "/html/body/div[3]/div/div[7]/div/div[" + str(j) + "]/article/div[3]/div/div/div/div[1]/a/strong")
        print(precio.text)
        resultado.append((nombre.text + " " + precio.text + " Fnac"))
        j = j + 1
    print(resultado)
    navegador.close()
    return resultado

if __name__ == '__main__':
    buscarFnac("Samsung", "Galaxy s10")


