from functools import partial
from tkinter import *

def buscarFnac(marca, movil):
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    busqueda = marca + " " + movil
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.get("https://www.fnac.es")
    navegador.maximize_window()
    ventanacookies = navegador.find_element_by_xpath("/html/body/aside/div/button")
    if ventanacookies != None :
        print("Detectado caja de cookies")
        ventanacookies.click()
    cajabusqueda = navegador.find_element_by_id("Fnac_Search")
    cajabusqueda.send_keys(busqueda)
    cajabusqueda.submit()
    element = navegador.find_element_by_css_selector('#col_gauche > div > div.nav > div.content > ul > li:nth-child(1) > ul > li:nth-child(1) > span')
    if element != None:
        element.click()
        print("Pulsado sobre Telefonos")
    elem = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[1]/div/div/ul/li[7]/span')))
    element = navegador.find_element_by_css_selector('#col_gauche > div > div.sticky > div.Filters.js-SearchFilters > div.js-FiltersContainer.js-FiltersContainer--vendor > div > a.Filters-choice.js-Filters-choice.js-Filters-choice--vendor-fnacdarty.isActive > label > span.Filters-choiceLabel')
    if element != None:
        element.click()
        print("Pulsado Vendedor Fnac")
    elem = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[2]/div[2]/span/ul/li/a')))
    listaElementos = navegador.find_elements_by_xpath("//*[contains(@class, 'Article-itemGroup')]")
    print(len(listaElementos))
    j = 1
    resultado = list()
    for i in listaElementos:
        elementoActual = i
        nombre = elementoActual.find_element_by_xpath("/html/body/div[3]/div/div[7]/div/div["+str(j)+"]/article/div[2]/div/p[1]")
        print(nombre.text)
        try:
            precio = elementoActual.find_element_by_xpath("/html/body/div[3]/div/div[7]/div/div["+str(j)+"]/article/div[3]/div/div/div/div/div[3]/span[2]")
        except:
            precio = elementoActual.find_element_by_xpath("/html/body/div[3]/div/div[7]/div/div["+str(j)+"]/article/div[3]/div/div/div/div/div[1]/a/strong")
        print(precio.text)
        resultado.append((nombre.text + " " + precio.text))
        j = j+1
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
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.get("https://www.pccomponentes.com")
    navegador.maximize_window()
    ventanacookies = navegador.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/button")
    if ventanacookies != None:
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
        resultado.append((nombre.text + " " + precio.text))
        j = j + 1
    print(resultado)
    navegador.close()

def botonBuscar(marca, movil):
    print(chk_pccom_state.get())
    print(chk_fnac_state.get())
    if chk_fnac_state.get():
        buscarFnac(str(marca), str(movil))
    if chk_pccom_state.get():
        buscarPccom(str(marca), str(movil))


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

items=["Samsung Galaxy S10+",
           "Xiaomi mi 9t",
           "Apple iPhone 11 pro max"]

lista = Listbox(width=70, height=15)
lista.grid(row=4, columnspan=4)
lista.insert(0,*items)

window.mainloop()
