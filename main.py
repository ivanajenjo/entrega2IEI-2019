from tkinter import *

def main():
    window = Tk()
    window.title("Entrega 2 IEI")
    window.geometry('1024x680')

    model_text = StringVar()
    model_label = Label(window, text='Modelo', font=('bold', 14), pady=20, padx=20)
    model_label.grid(row=0, column=0)
    model_entry = Entry(window, textvariable=model_text)
    model_entry.grid(row=0, column=1)

    marcas = {"Samsung", "LG", "Xiaomi", "Huawei"}
    marca_label = Label(window, text='Marca', font=('bold', 14), pady=20, padx=20)
    marca_label.grid(row=0, column=2)
    marca_text = StringVar()
    marca_option = OptionMenu(window, marca_text, *marcas, )
    marca_option.grid(row=0, column=3)

    window.mainloop()


if __name__ == "__main__":
    main()