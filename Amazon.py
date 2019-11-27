


def buscarAmazon(marca, movil):
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    import time
    busqueda = marca + " " + movil
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    #navegador = webdriver.Firefox(executable_path=r'C:\Users\ivana\PycharmProjects\Entrega2IEI\driver\geckodriver.exe')
    navegador.maximize_window()
    navegador.get("https://www.amazon.es/moviles-smartphones-libres/b/ref=amb_link_15?ie=UTF8&node=934197031&pf_rd_m=A1AT7YVPFBWXBL&pf_rd_s=merchandised-search-leftnav&pf_rd_r=AVW9X4MJY8SG5QSCZEE6&pf_rd_r=AVW9X4MJY8SG5QSCZEE6&pf_rd_t=101&pf_rd_p=cadc80ee-e6fb-44b6-91b9-706bc54ab022&pf_rd_p=cadc80ee-e6fb-44b6-91b9-706bc54ab022&pf_rd_i=931491031")
    elem = navegador.find_element_by_id("twotabsearchtextbox")
    elem.send_keys(busqueda)
    elem.submit()
    time.sleep(5)
    listaMoviles = navegador.find_elements_by_xpath("//*[contains(@class, 's-result-item')]")
    print("Número de lemento de la lista: " + str(len(listaMoviles)))
    resultado = list()
    j = 1
    for i in listaMoviles:
        movilactual = i
        waiting = WebDriverWait(navegador, 60)
        continuar = False
        try:
            descuento = navegador.find_element(By.XPATH("/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div["+str(j)+"]/div/span/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[2]/span[2]"))
            try:
                navegacion = navegador.find_element(By.XPATH("/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div["+str(j)+"]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span"))
                continuar = True
                resultado.append(navegacion.text)
            except:
                print("Banner")
            if continuar:
                try:
                    precio = navegador.find_element(By.XPATH("/html/body/div/div/div/div[2]/div/span[4]/div/div["+str(j)+"]/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[2]/span[2]"))
                    resultado.append(precio.text)
                    resultado.append(descuento.text)
                    resultado.append("AMAZON")
                except:
                    resultado.append(precio.text)
                    resultado.append("-")
                    resultado.append("AMAZON")
        except:
            print("Precio no disponible")
        j = j + 1
        try:
            time.sleep(1)
        except:
            print("No sleep")
    print(resultado)
    navegador.quit()
    return resultado

buscarAmazon("Apple", "iphone 11 pro")