import tkinter
from tkinter import messagebox
#---------------------------------------------------------------
#Inicio de proyecto calculadora con botones y configuracion grafica sencilla.
#by jeff mcwill
#El proyecto lo empeze y termine el 2 de octubre de 2022 corregi ciertos errores para que la calculadora te notifique de ciertos errores en el programa.
#ahora funciona perfectamente, da las sumas,restas,multiplicacion y division. Cosas sencillas.
#posee tambien un icono hecho por mi mismo, con pixelart y transformado en ico.
#---------------------------------------------------------------
#variables importantes.

raiz=tkinter.Tk()
raiz.title("Calculadora By JeffMcWill")
raiz.geometry("300x200")
raiz.iconbitmap('icono.ico')

#---------------------------------------------------------------
#FUNCIONES DE LA CALCULADORA...
def FuncionSuma():
	valor1=entry_valor1.get()
	valor2=entry_valor2.get()
	label_resultado.grid(row=8,column=1)
	try:
		if valor1 == "" or valor2 == "":
			label_resultado["text"] = "Por favor agregue numeros."
		else:
			resultado=int(valor1) + int(valor2)
			label_resultado["text"] = resultado
	except ValueError:
		label_resultado["text"] = "Valores no soportados."

def FuncionResta():
	valor1=entry_valor1.get()
	valor2=entry_valor2.get()
	label_resultado.grid(row=8,column=1)
	try:
		if valor1 == "" or valor2 == "":
			label_resultado["text"] = "Por favor agregue numeros."
		else:
			resultado=int(valor1) - int(valor2)
			label_resultado["text"] = resultado
	except ValueError:
		label_resultado["text"] = "Valores no soportados."

def FuncionMultiplicacion():
	valor1=entry_valor1.get()
	valor2=entry_valor2.get()
	label_resultado.grid(row=8,column=1)
	try:
		if valor1 == "" or valor2 == "":
			label_resultado["text"] = "Por favor agregue numeros."
		else:
			resultado=int(valor1) * int(valor2)
			label_resultado["text"] = resultado
	except ValueError:
		label_resultado["text"] = "Valores no soportados."

def FuncionDivision():
	valor1=entry_valor1.get()
	valor2=entry_valor2.get()
	label_resultado.grid(row=8,column=1)
	try:
		if valor1 == "" or valor2 == "":
			label_resultado["text"] = "Por favor agregue numeros."
		else:
			resultado=int(valor1) / int(valor2)
			label_resultado["text"] = resultado
	except ValueError:
		label_resultado["text"] = "Valores no soportados."
	except ZeroDivisionError:
		label_resultado["text"] = "Division por 0 no soportada."		

#---------------------------------------------------------------
#Labels #etiquetas que van al lado de los entrys o titulos de ciertas funciones.

label_titulo=tkinter.Label(raiz,text="//Calculadora Simplista//")
label_valor1=tkinter.Label(raiz,text="*Escriba Valor 1")
label_valor2=tkinter.Label(raiz,text="*Escriba Valor 2")
label_resultado=tkinter.Label(raiz,text="Resultado: ")

#---------------------------------------------------------------
#Entrys #entrada de comandos.

entry_valor1=tkinter.Entry(raiz)
entry_valor2=tkinter.Entry(raiz)

#---------------------------------------------------------------
#Botones para ingreso de comandos. #DESPUES se le agrega el Command= para poder agregarle las funciones.

boton_de_Suma=tkinter.Button(raiz,text="//Suma//",command=FuncionSuma)
boton_de_Resta=tkinter.Button(raiz,text="//Resta//",command=FuncionResta)
boton_de_Multiplicacion=tkinter.Button(raiz,text="//Multiplicacion//",command=FuncionMultiplicacion)
boton_de_Division=tkinter.Button(raiz,text="//Division//",command=FuncionDivision)
#boton_de_resultado=tkinter.Button(raiz,text="Resultado")

#---------------------------------------------------------------
#Grids para ubicar en el tkinter.

label_titulo.grid(row=1,column=1)
label_valor1.grid(row=2,column=0)
label_valor2.grid(row=3,column=0)
entry_valor1.grid(row=2,column=1)
entry_valor2.grid(row=3,column=1)
boton_de_Suma.grid(row=4,column=1)
boton_de_Resta.grid(row=5,column=1)
boton_de_Multiplicacion.grid(row=6,column=1)
boton_de_Division.grid(row=7,column=1)
label_resultado.grid(row=8,column=0)

#---------------------------------------------------------------
#Funcion especial para que aparezca el resultado de las funciones en el programa.
label_resultado=tkinter.Label(raiz)
label_resultado.grid(row=8,column=1)
#---------------------------------------------------------------
#Ejecutador final del codigo.
raiz.mainloop()