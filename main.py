from functools import partial
from tkinter import *


def buscarFromFnac(marca, movil):
    import fnac
    fnac.buscarFnac(str(marca), str(movil))


def main():
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

    buscar = Button(text="Buscar", command=partial(buscarFromFnac, marca_text.get(), model_text.get()))
    buscar.grid(row=2, column=2)

    items=["Samsung Galaxy S10+",
           "Xiaomi mi 9t",
           "Apple iPhone 11 pro max"]

    lista = Listbox(width=70, height=15)
    lista.grid(row=4, columnspan=4)
    lista.insert(0,*items)

    window.mainloop()

if __name__ == "__main__":
    main()