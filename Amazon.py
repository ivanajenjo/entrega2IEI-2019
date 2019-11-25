from selenium import webdriver
import time

def buscarAmazon(movil):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.maximize_window()
    navegador.get("https://www.amazon.es/gp/browse.html?node=931491031&ref_=nav_em_T1_0_4_12_2__tele")
    elem = navegador.find_element_by_id("twotabsearchtextbox")
    elem.send_keys(movil)
    elem.submit()
    time.sleep(5)
    #WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "celwidget slot=SEARCH_RESULTS template=SEARCH_RESULTS widgetId=search-results index=2")))
    listaElementos = navegador.find_elements_by_xpath("//*[contains(@class, 'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28')]")
    print(len(listaElementos))
    j = 3
    resultado = list()
    for i in listaElementos:
        elementoActual = i
        try:
            nombre = elementoActual.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div["+str(j)+"]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")
            print(nombre.text)
        except:
            print("No se ha encontrado nombre")
            break
        #print(nombre.text)
        try:
            precio = elementoActual.find_element_by_xpath(
                """/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div["""+str(j)+"""]/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[1]/span[2]/span[1]""")
        except:
            precio = elementoActual.find_element_by_xpath(
                """/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div["""+str(j)+"""]/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[1]/span[2]/span[1]""")
        print(precio.text)
        resultado.append((nombre.text + " " + precio.text + " Amazon"))
        j = j + 1
    print(resultado)

buscarAmazon("Xiaomi mi 9T")