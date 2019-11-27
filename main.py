from tkinter import *

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
        resultado=list()
        resultado.append("Teléfono no disponible en FNAC")
        return (resultado)
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
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[2]/div[2]/span/ul/li/a')))
    except:
        print("No se ha encontrado elemento")
    listaElementos = navegador.find_elements_by_xpath("//*[contains(@class, 'Article-itemGroup')]")
    print(len(listaElementos))
    j = 1
    resultado = list()
    for i in listaElementos:
        precio = None
        elementoActual = i
        nombre = elementoActual.find_element_by_xpath(
            "/html/body/div[3]/div/div[7]/div/div[" + str(j) + "]/article/div[2]/div/p[1]")
        print(nombre.text)
        try:
            precio = elementoActual.find_element_by_xpath(
                "/html/body/div[3]/div/div[7]/div/div[" + str(j) + "]/article/div[3]/div/div/div/div/div[3]/span[2]")
        except:
            try:
                precio = elementoActual.find_element_by_xpath(
                "/html/body/div[3]/div/div[7]/div/div[" + str(j) + "]/article/div[3]/div/div/div/div/div[1]/a")
            except:
                print("No disponible")
        #print(precio.text)
        try:
            descuento = elementoActual.find_element_by_xpath("/html/body/div[3]/div/div[7]/div/div["+str(j)+"]/article/div[3]/div/div/div/div/div[1]/span")
        except:
            descuento = None
        if precio != None:
            if descuento != None:
                resultado.append((nombre.text + "; " + precio.text + "; Descuento: "+ descuento.text +"; Fnac"))
            else:
                resultado.append((nombre.text + "; " + precio.text + "; ;Fnac"))
        else:
            resultado.append((nombre.text + "; No disponible; ;Fnac"))
        j = j + 1
    print(resultado)
    navegador.close()
    return resultado

def buscarPccom(marca, movil):
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import time
    busqueda = "smartphon " + marca + " " + movil
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.get("https://www.pccomponentes.com")
    navegador.maximize_window()
    ventanacookies = navegador.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/button")
    if ventanacookies != None:
        print("Detectado caja de cookies")
        ventanacookies.click()
    elem = navegador.find_element_by_name("query")
    elem.send_keys(busqueda)
    elem.send_keys(Keys.RETURN)
    try:
        element = navegador.find_element_by_css_selector('#acc-fil-538 > div > ul > li:nth-child(1) > a')
    except:
        print("Telefono no disponible")
        return "Telefono no disponible"
    if element != None:
        try:
            element.click()
        except:
            print("No se ha podido seleccionar telefonos")
        print("Pulsado sobre Telefonos")
    time.sleep(5)
    WebDriverWait(navegador, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/ul/li[1]/a')))
    listaElementos = navegador.find_elements_by_xpath("//*[contains(@class, 'tarjeta-articulo expandible')]")
    print(len(listaElementos))
    j = 1
    resultado = list()
    for i in listaElementos:
        elementoActual = i
        nombre = elementoActual.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[3]/div/div[" + str(j) + "]/article/div[1]/header/h3")
        print(nombre.text)
        precio = elementoActual.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[3]/div/div[" + str(j) + "]/article/div[1]/div[2]/div")
        print(precio.text)
        try:
            descuento = elementoActual.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[3]/div/div["+str(j)+"]/article/div[1]/div[2]/div[2]/div[1]/span")
        except:
            descuento = None
        if descuento != None:
            resultado.append((nombre.text + "; " + precio.text + "; Descuento: "+ descuento.text +"; Pccomponentes"))
        else:
            resultado.append((nombre.text + "; " + precio.text + "; ; Pccomponentes"))
        j = j + 1
    print(resultado)
    navegador.close()
    return resultado

def buscarAmazon(marca, movil):
    from selenium import webdriver
    import time
    busqueda = marca + " " + movil
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.maximize_window()
    navegador.get("https://www.amazon.es/gp/browse.html?node=931491031&ref_=nav_em_T1_0_4_12_2__tele")
    elem = navegador.find_element_by_id("twotabsearchtextbox")
    elem.send_keys(busqueda)
    elem.submit()
    time.sleep(5)
    # WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "celwidget slot=SEARCH_RESULTS template=SEARCH_RESULTS widgetId=search-results index=2")))
    listaElementos = navegador.find_elements_by_xpath(
        "//*[contains(@class, 's-result-item')]")
    print(len(listaElementos))
    j = 3
    resultado = list()
    for i in listaElementos:
        descuento = None
        elementoActual = i
        try:
            nombre = elementoActual.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div[" + str(
                    j) + "]/div/span/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")
            print(nombre.text)
        except:
            try:
                nombre = elementoActual.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div[" + str(
                        j) + "]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")
            except:
                print("No se ha encontrado nombre")
                break
        # print(nombre.text)
        try:
            precio = elementoActual.find_element_by_xpath(
                """/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div[""" + str(
                    j) + """]/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[1]/span[2]/span[1]""")
        except:
            try:
                precio = elementoActual.find_element_by_xpath(
                    """/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div[""" + str(
                        j) + """]/div/span/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[1]/span[2]/span[1]""")
            except:
                break
        try:
            descuento = elementoActual.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div["+str(j)+"]/div/span/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[2]/span[1]")
        except:
            print("No descuento")
        print(precio.text)
        if descuento != None:
            resultado.append((nombre.text + "; " + precio.text + "; Descuento: " + descuento.text+ "; Amazon"))
        else:
            resultado.append((nombre.text + "; " + precio.text + "; ; Amazon"))
        j = j + 1
    print(resultado)
    navegador.close()
    return resultado

def botonBuscar(marca, movil):
    lista.delete(0, 'end')
    print(chk_pccom_state.get())
    print(chk_fnac_state.get())
    print(chk_amazon_state.get())
    fnac = {}
    amazon = {}
    pccom = {}
    if chk_fnac_state.get():
        fnac = buscarFnac(str(marca), str(movil))
    if chk_pccom_state.get():
        pccom = buscarPccom(str(marca), str(movil))
    if chk_amazon_state.get():
        amazon = buscarAmazon(str(marca), str(movil))
    convertir_resultados(fnac, pccom, amazon)

def convertirACsv(lista):
    import csv

    with open("csv.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL, delimiter= ";")
        for i in lista:
            print(i)
            wr.writerow(i.split(';'))
    print("escrito en csv")

def convertir_resultados(fnac, pccom, amazon):
    resultado = list()
    if chk_fnac_state:
        for i in fnac:
            resultado.append(i)
    if chk_pccom_state:
        for i in pccom:
            resultado.append(i)
    if chk_amazon_state:
        for i in amazon:
            resultado.append(i)
    lista.insert(0, *resultado)
    convertirACsv(resultado)

window = Tk()
window.title("Entrega 2 IEI")
#window.geometry('1024x680')

model_text = StringVar()
model_label = Label(window, text='Modelo', font=('bold', 14), pady=20, padx=20)
model_label.grid(row=0, column=0)
model_entry = Entry(window, textvariable=model_text)
model_entry.grid(row=0, column=1)

marcas = ["Samsung", "LG", "Xiaomi", "Huawei", "Sony", "Lenovo", "Apple", "Motorola", "One Plus"]
marcas.sort()
marca_label = Label(window, text='Marca', font=('bold', 14), pady=20, padx=20)
marca_label.grid(row=0, column=2)
marca_text = StringVar()
marca_option = OptionMenu(window, marca_text, *marcas, )
marca_option.grid(row=0, column=3)

chk_fnac_state = BooleanVar()
chk_fnac = Checkbutton(window, text='Fnac', var=chk_fnac_state)
chk_fnac.grid(row=1, column=0, sticky=W)

chk_amazon_state = BooleanVar()
chk_amazon = Checkbutton(window, text='Amazon', var=chk_amazon_state)
chk_amazon.grid(row=2, column=0, sticky=W)

chk_pccom_state = BooleanVar()
chk_pccom = Checkbutton(window, text='Pccomponentes', var=chk_pccom_state)
chk_pccom.grid(row=3, column=0, sticky=W)

buscar = Button(text="Buscar", command=lambda: botonBuscar(marca_text.get(), model_text.get()))
buscar.grid(row=2, column=2)

lista = Listbox(width=70, height=15)
lista.grid(row=4, columnspan=4)
scrollbar = Scrollbar(lista, orient="vertical")
lista.config(yscrollcommand=scrollbar.set)

window.mainloop()
