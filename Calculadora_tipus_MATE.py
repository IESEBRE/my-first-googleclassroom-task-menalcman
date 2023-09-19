from tkinter import *
from functools import partial

# Configuració de l'arrel
root = Tk()
root.title("Calculadora")
root.iconbitmap("@calc.xbm")
root.resizable(False, False)

# Configuració del frame
frame1 = Frame(root, width=678, height=456)
frame1.pack()

# Assignació de la variable StringVar per al contingut de 'Entry "entrada"

valor_entrada = StringVar()


# Funcionalitat del botó de Neteja

def netejar_la_pantalla():
    if entrada.get() == "" or entrada.get() == " ":
        alerta = Tk()
        alerta.resizable(False, False)
        alerta.config(width=250, height=123)
        alerta.title("Advertència")
        missatge = Label(alerta, text="No hi ha text per esborrar")
        missatge.place(anchor="center", x=100, y=53)
    else:
        valor_entrada.set("")



# Funcionalitat dels botons numèrics

def introduir_numero(numero):
    valor_entrada.set(entrada.get() + str(numero))


# Funcionalitat del botó de desfer

def desfer():
    text_entrada = entrada.get()
    desfeta = text_entrada[:-1]
    valor_entrada.set(desfeta)
    if text_entrada == "" or text_entrada == " ":
        alerta = Tk()
        alerta.resizable(False, False)
        alerta.config(width=250, height=123)
        alerta.title("Advertència")
        missatge = Label(alerta, text="No hi ha text per desfer")
        missatge.place(anchor="center", x=100, y=53)


# Implementació de l'entrada de text
entrada = Entry(frame1, width=55, justify="right", textvariable=valor_entrada)
entrada.grid(row=0, column=0, columnspan=7)
# Implementació dels botons de la fila 1

boto7 = Button(frame1, text="7", width=6, command=partial(introduir_numero, 7))
boto7.grid(row=1, column=0)


boto8 = Button(frame1, text="8", width=6, command=partial(introduir_numero, 8))
boto8.grid(row=1, column=1)

boto9 = Button(frame1, text="9", width=6, command=partial(introduir_numero, 9))
boto9.grid(row=1, column=2)

boto_div = Button(frame1, text="÷", width=6)
boto_div.grid(row=1, column=3)

boto_desfer = Button(frame1, text="Desfés", width=6, command=desfer)
boto_desfer.grid(row=1, column=4)

boto_neteja = Button(frame1, text="Neteja", width=6, command=netejar_la_pantalla, bg="red")
boto_neteja.grid(row=1, column=5)

# Implementació de la fila 2

boto4 = Button(frame1, text="4", width=6, command=partial(introduir_numero, 4))
boto4.grid(row=2, column=0)

boto5 = Button(frame1, text="5", width=6, command=partial(introduir_numero, 5))
boto5.grid(row=2, column=1)

boto6 = Button(frame1, text="6", width=6, command=partial(introduir_numero, 6))
boto6.grid(row=2, column=2)

boto_mult = Button(frame1, text="x", width=6)
boto_mult.grid(row=2, column=3)

boto_parentesi1 = Button(frame1, text="(", width=6)
boto_parentesi1.grid(row=2, column=4)

boto_parentesi2 = Button(frame1, text=")", width=6)
boto_parentesi2.grid(row=2, column=5)

# Implementació de la fila 3

boto1 = Button(frame1, text="1", width=6, command=partial(introduir_numero, 1))
boto1.grid(row=3, column=0)

boto2 = Button(frame1, text="2", width=6, command=partial(introduir_numero, 2))
boto2.grid(row=3, column=1)

boto3 = Button(frame1, text="3", width=6, command=partial(introduir_numero, 3))
boto3.grid(row=3, column=2)

boto_resta = Button(frame1, text="-", width=6)
boto_resta.grid(row=3, column=3)

boto1_exp2 = Button(frame1, text="x²", width=6)
boto1_exp2.grid(row=3, column=4)

boto_arrel2 = Button(frame1, text="√", width=6)
boto_arrel2.grid(row=3, column=5)

# Implementació de la fila 4

boto0 = Button(frame1, text="0", width=6, command=partial(introduir_numero, 0))
boto0.grid(row=4, column=0)

boto_coma = Button(frame1, text=",", width=6)
boto_coma.grid(row=4, column=1)

boto_percent = Button(frame1, text="%", width=6)
boto_percent.grid(row=4, column=2)

boto_suma = Button(frame1, text="+", width=6)
boto_suma.grid(row=4, column=3)

boto_igual = Button(frame1, text="=", width=15, bg="#5b7aeb")
boto_igual.grid(row=4, column=4, columnspan=2)

























root.mainloop()