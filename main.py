# *************************************************
# * PROGRAMACION DE LAS MATRICES*
# *************************************************
# PARA DEBUGUERA REEPLAZA POR NADA "#DEBUGMODE 	|"
Lista_user1 = []
Lista_user2 = []
 
Partido_Cerrado = 0
 
 
import string #importo funciones para tener el abecedario en una lista.
 
def Letra_ABC(posicion):
	abecedario =list(string.ascii_uppercase)
	letra = abecedario[posicion]
	return letra
 
def print_matriz(lista):
 
 
	print ("******"*VL)
 
	Matriz_front_end= []
 
	for i in range (0,len(lista),VL):
		Matriz_front_end.append(list(lista[i:i+VL]))
 
	for i in Matriz_front_end:
		print (i)
 
	print ("******"*VL)
	return Matriz_front_end
 
VL = int(input("De qué tamaño requerimos la matriz: " ))
 
while VL<3:
	print ()
	VL = int(input("El valor minimo es 3. por favor vuelva a ingresar el tamaño de la matriz deseada: " ))
 
list_count =[]
for i in range (VL):
	list_count.append(i)
	#print(list_count)
 
VL1=VL
# Genera la Lista ganadora, que es una lista de listas.
WinAll_Auto_Step1=[] #Genera la lista de items ganadores sin agruparlos, pero en orden del 1 al n -> Ejemplo A1,A2,A3
 
 
#Letra_ABC(0)
for a in list_count:
 
	for i in range(VL):
		#print ("I", i)
		#print ("VL", VL)
		WinAll_Auto_Step1.append(Letra_ABC(a)+str(i+1)) #saco la A y le meto la función. WinAll_Auto_Step1.append("A"+str(i+1))
# for i in range(VL):
# 	WinAll_Auto_Step1.append(Letra_ABC(1)+str(i+1))
# for i in range(VL):
# 	WinAll_Auto_Step1.append(Letra_ABC(2)+str(i+1))
for a in list_count:
 
	for i in range(VL):
		#print ("I", i)
		#print ("VL", VL)
		WinAll_Auto_Step1.append(Letra_ABC(i)+str(a+1))
 
 
# for i in range(VL):
# 	WinAll_Auto_Step1.append(Letra_ABC(i)+str())
 
for i in range(VL):
	WinAll_Auto_Step1.append(Letra_ABC(i)+str(i+1)) # Diagonal
for i in range(VL):
	WinAll_Auto_Step1.append(Letra_ABC(2-i)+str(i+1)) # Diagonal
# for i in range(VL):
 
# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(1))
# for i in range(VL):
# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(2))
# for i in range(VL):
# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(3))
 
WinAll_Auto_Step2=[] #Agrupa los resultados en elemento de 3 componentes -> ['A1','A2','A3'],['B1','B2','B3']
#print (len(WinAll_Auto_Step1))
 
# Go -Este paso es el que genera los Segmentos de elementos agrupados de a 3 o 4 o lo que defina VL. Que en resumen serán los segmentos que si algun jugador agruapa lo hace ganar
for i in range (0,len(WinAll_Auto_Step1),VL):
	#print(i)
	WinAll_Auto_Step2.append(list(WinAll_Auto_Step1[i:i+VL]))
 
 
# ******************************************************************************************
# Generar la lista de  opciones a elegir para generar la matriz
# ******************************************************************************************
 
Lista_de_Opciones_matriz=[]
 
for a in list_count:
 
	for i in range(VL):
		#print ("I", i)
		#print ("VL", VL)
		Lista_de_Opciones_matriz.append(Letra_ABC(a)+str(i+1))
 
 
#print("Lista_de_Opciones_matri", Lista_de_Opciones_matriz)
 
 
 
 
#*********** PRINTS PARA CONTROLAR LOS RESULTADOS ******************************
#print(WinAll_Auto_Step1)
 
#print("Lista de elementos previos a la ganadora", WinAll_Auto_Step1)
#DEBUGMODE print("Lista de Segmentos Ganadora", WinAll_Auto_Step2)
 
#DEBUGMODE print("Cantidad de combinaciones pata ganar", len(WinAll_Auto_Step2))
 
# Con las siguiente 4 Linea se genera  la matriz a presentar en el front End
 
print_matriz(Lista_de_Opciones_matriz)
#DEBUGMODE print (Lista_user1)
#DEBUGMODE print (Lista_user2)
 
# print (winall)
# print (len(winall))
# print (WinAll2)
#pprint.pprint(WinAll_Auto_Step1, 3)
 
# **************************************
# Inicio de la protramación de Juego
# ***************************************
 
 
def Contar_X(fila):
 
	contador = 0	
 
	for i in fila:
		if i == "X":
			contador = contador + 1
	#print (contador)
	return (contador)
 
 
def Actualizar_lista():
	filaAll= Fila1+Fila2+Fila3
	#print ("Print de la función:",filaAll)
	print("PRINT DE LA FUNCION", filaAll)
	return filaAll
 
def Validación_Ganadores(ListaGanadora,listaPlayer): #Esta función valida si la lista de alguno de los ganadore es GANADORA
 
	comparando=[]
	Partido_Cerrado = 0
 
	for a in WinAll_Auto_Step2:
		comparando =[]
		#DEBUGMODE print ("Fun_WinAll_Auto_Step2", WinAll_Auto_Step2)
		#DEBUGMODE print ("FunC(a)", a)
		if len(comparando)<=VL:
 
			for i in listaPlayer:
				if i in a:
					#DEBUGMODE print ("ListaJugador a comparar",listaPlayer)# Lista_user1:  ['B2', 'A2', 'B1']
					#DEBUGMODE print ("Lista que compara", a) #a=['A2', 'B2', 'C2']
					comparando.append(i)
					#DEBUGMODE print ("hay coincidencia?:",comparando)
					#DEBUGMODE print (len(comparando))
					if len(comparando)>=VL:
						#DEBUGMODE print(comparando)
						Partido_Cerrado = Partido_Cerrado + 1
						#DEBUGMODE print ("HAY GANADOR querido")
						#DEBUGMODE print ("Partido_Cerrado Func", Partido_Cerrado)
						return Partido_Cerrado
						break
 
					else:
						#DEBUGMODE print ("NO HAY GANADOR")
 
						#return hay_ganador
						a
				else:
					if len(comparando)>=VL:
						break
					else:
						#DEBUGMODE print ("no Match")
						comparando =[]
						#DEBUGMODE print("Comparando_limpio", comparando)
		else:
			break
 
	print ("out of loop")
 
 
#Listas que acumulan lo elegido por aca User
Lista_user1 = []
Lista_user2 = []
Matriz_front_end =[]
hay_ganador = []
 
termino_el_juego = 1 # Si etemino del juego es 0 se terminó el juego
 
 
print (" ")
#print ("Lista Jugador 1" , Lista_user1)
#print ("Lista Jugador 2" , Lista_user2)
#print (" ")
#print(len(winall))
#print_matriz()
#print (" ")
 
contador = 0 # Define el inicio del cotador de jugadas 
turno = 0
 
 
while termino_el_juego == 1:
 
	turno = turno + 1
	#DEBUGMODE print ("Turno:" ,turno)
	#WinAll_Auto_Step2=Actualizar_lista ()
	#print ("SISMO",WinAll_Auto_Step2)
	# Contar_X(WinAll_Auto_Step2)
	# Entrada Jugardor 1
	if turno> (VL*VL):
		print ("TABLAS")
		break
 
	input_user1= input("Elija un opción Jugaror 1 [X]: ").upper()
	#input_user1= input_user1a.upper()
	#DEBUGMODE print (input_user1)
	#print (input_user1)
 
	while input_user1 not in Lista_de_Opciones_matriz or input_user1 in ("X","0") :
 
		input_user1= input("Elija un opción Jugaror 1 [X]: ").upper()
 
	if input_user1 in Lista_de_Opciones_matriz:
		Lista_user1.append(input_user1)
		Lista_de_Opciones_matriz = ["X" if i==input_user1 else i for i in Lista_de_Opciones_matriz]
		#print(Lista_de_Opciones_matriz)
		print_matriz(Lista_de_Opciones_matriz)
		#DEBUGMODE print ("Lista_user1: ", Lista_user1)
		#DEBUGMODE print ("Lista_user2:", Lista_user2)
 
	else:
		print("Crap Judador1")
 
# VALIDAR SI GANÓ Jugaror 1?
 
	termino_el_partido = Validación_Ganadores(WinAll_Auto_Step2,Lista_user1)
	#print (termino_el_partido)
	#print ("Partido_Cerrado After F", Partido_Cerrado)
	if termino_el_partido == 1:
		print ("GANO EL JUGADOR 1 [X]")
		break
	else:
	 	pass		
 
# Entrada Jugardor 2
 
	turno = turno + 1
	#DEBUGMODE print ("Turno",turno)
	#Actualizar_lista () # No entiendo porqué si actulizo la lista, cuando la toma para valider en el while lo hace con la antigua.
	#print ("EMi",WinAll_Auto_Step2) # Acá es donde se envidencia que la liata WinAll_Auto_Step2 no es la que debería ser luego de correr la función.
	if turno>(VL*VL):
		print ("TABLAS")
		break
 
	input_user2= input("Elija un opción Judador 2 [0]: ").upper()
 
	while input_user2 not in Lista_de_Opciones_matriz or input_user1 in ("X","0") :
 
		input_user2= input("Elija un opción Jugaror 2 [0]: ").upper()
 
	if input_user2 in Lista_de_Opciones_matriz:
		Lista_user2.append(input_user2)
		Lista_de_Opciones_matriz = ["0" if i==input_user2 else i for i in Lista_de_Opciones_matriz]
		print_matriz(Lista_de_Opciones_matriz)
		#DEBUGMODE print ("Lista_user1: ", Lista_user1)
		#DEBUGMODE print ("Lista_user2:", Lista_user2)
 
	else:
			print("Crapjugador2")
 
# VALIDAR SI GANÓ Jugaror 2?
 
	termino_el_partido = Validación_Ganadores(WinAll_Auto_Step2,Lista_user2)
	#print (termino_el_partido)
	#print ("Partido_Cerrado After F", Partido_Cerrado)
	if termino_el_partido == 1:
		print ("GANO EL JUGADOR 2 [0]")
		break
	else:
		pass
 
print ("FIN DEL JUEGO")
