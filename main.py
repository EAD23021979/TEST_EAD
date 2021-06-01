# *************************************************
# * PROGRAMACION DE LAS MATRICES*
# *************************************************
# PARA DEBUGUERA REEPLAZA POR NADA "#DEBUGMODE 	|"

 
 
import string #importo funciones para tener el abecedario en una lista.


class Tateti:
	Lista_user1 = []
	Lista_user2 = []
	Partido_Cerrado = 0
	VL = 0
	lista_de_opciones_matriz = []
	winall_auto_step2 = []

	def __init__(self, origen="consola"):
		self.origen = origen

	def input_usuario(self, msg, test_value=""):
		if self.origen == "consola":
			return input(msg)
		elif self.origen == "test":
			return test_value

	def definir_matriz(self, tamanio=3):
		try:
			self.VL = int(self.input_usuario("De qué tamaño requerimos la matriz: " ))
		except Exception:
			self.VL = tamanio
		if self.VL < 3:
			self.VL = tamanio
		return

	def input_jugador(self, numero_jugador, jugada=None):
		if numero_jugador == "1":
			ficha = "X"
		else:
			ficha = "0"
		if self.origen == "test":
			input_user = jugada
		else:
			input_user = self.input_usuario("Elija un opción Jugador %s [%s]: " % (numero_jugador, ficha)).upper()


		while input_user not in self.lista_de_opciones_matriz or input_user in ("X", "0"):
			input_user = self.input_usuario("Elija un opción Jugador 1 [X]: ").upper()

		if input_user in self.lista_de_opciones_matriz:
			if numero_jugador == "1":
				self.Lista_user1.append(input_user)
				termino_el_partido = self.validacion_ganadores(self.Lista_user1)
				if termino_el_partido == 1:
					print("GANO EL JUGADOR 1 [X]")
					return
			else:
				self.Lista_user2.append(input_user)
				termino_el_partido = self.validacion_ganadores(self.Lista_user2)
				if termino_el_partido == 1:
					print("GANO EL JUGADOR 2 [0]")
					return
			
			self.lista_de_opciones_matriz = [ficha if i == input_user else i for i in self.lista_de_opciones_matriz]
			# print(self.lista_de_opciones_matriz)
			self.print_matriz(self.lista_de_opciones_matriz)
		# DEBUGMODE print ("Lista_user1: ", Lista_user1)
		# DEBUGMODE print ("Lista_user2:", Lista_user2)

		else:
			print("Crap")

	def inicializar_tablero(self):
		self.definir_matriz()
		list_count = []
		for i in range (self.VL):
			list_count.append(i)

		self.VL1 = self.VL
		# Genera la Lista ganadora, que es una lista de listas.
		WinAll_Auto_Step1 = [] #Genera la lista de items ganadores sin agruparlos, pero en orden del 1 al n -> Ejemplo A1,A2,A3


		#Letra_ABC(0)
		for a in list_count:

			for i in range(self.VL):
				#print ("I", i)
				#print ("self.VL", self.VL)
				letra = self.Letra_ABC(a)
				WinAll_Auto_Step1.append(letra + str(i+1)) #saco la A y le meto la función. WinAll_Auto_Step1.append("A"+str(i+1))
		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(1)+str(i+1))
		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(2)+str(i+1))
		for a in list_count:

			for i in range(self.VL):
				#print ("I", i)
				#print ("self.VL", self.VL)
				WinAll_Auto_Step1.append(self.Letra_ABC(i)+str(a+1))


		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(i)+str())

		for i in range(self.VL):
			WinAll_Auto_Step1.append(self.Letra_ABC(i)+str(i+1)) # Diagonal
		for i in range(self.VL):
			WinAll_Auto_Step1.append(self.Letra_ABC(2-i)+str(i+1)) # Diagonal
		# for i in range(self.VL):

		# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(1))
		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(2))
		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(3))

		self.winall_auto_step2=[] #Agrupa los resultados en elemento de 3 componentes -> ['A1','A2','A3'],['B1','B2','B3']
		#print (len(WinAll_Auto_Step1))

		# Go -Este paso es el que genera los Segmentos de elementos agrupados de a 3 o 4 o lo que defina self.VL. Que en resumen serán los segmentos que si algun jugador agruapa lo hace ganar
		for i in range (0,len(WinAll_Auto_Step1),self.VL):
			#print(i)
			self.winall_auto_step2.append(list(WinAll_Auto_Step1[i:i+self.VL]))


		# ******************************************************************************************
		# Generar la lista de  opciones a elegir para generar la matriz
		# ******************************************************************************************

		self.lista_de_opciones_matriz = []

		for a in list_count:

			for i in range(self.VL):
				#print ("I", i)
				#print ("self.VL", self.VL)
				self.lista_de_opciones_matriz.append(self.Letra_ABC(a)+str(i+1))


		#print("Lista_de_Opciones_matri", self.lista_de_opciones_matriz)




		#*********** PRINTS PARA CONTROLAR LOS RESULTADOS ******************************
		#print(WinAll_Auto_Step1)

		#print("Lista de elementos previos a la ganadora", WinAll_Auto_Step1)
		#DEBUGMODE print("Lista de Segmentos Ganadora", self.winall_auto_step2)

		#DEBUGMODE print("Cantidad de combinaciones pata ganar", len(self.winall_auto_step2))

		# Con las siguiente 4 Linea se genera  la matriz a presentar en el front End

		self.print_matriz(self.lista_de_opciones_matriz)

		print(" ")
		# print ("Lista Jugador 1" , Lista_user1)
		# print ("Lista Jugador 2" , Lista_user2)
		# print (" ")
		# print(len(winall))
		# print_matriz()
		# print (" ")

	def empezar(self):
		
		self.inicializar_tablero()

		turno = 0
		termino_el_juego = 1  # Si etemino del juego es 0 se terminó el juego

		while termino_el_juego == 1:

			turno = turno + 1
			# DEBUGMODE print ("Turno:" ,turno)
			# self.winall_auto_step2=Actualizar_lista ()
			# print ("SISMO",self.winall_auto_step2)
			# Contar_X(self.winall_auto_step2)
			# Entrada Jugardor 1
			if turno > (self.VL * self.VL):
				print("TABLAS")
				break

			self.input_jugador("1")

			termino_el_partido = self.validacion_ganadores(self.Lista_user1)
			# print (termino_el_partido)
			# print ("Partido_Cerrado After F", Partido_Cerrado)
			if termino_el_partido == 1:
				print("GANO EL JUGADOR 1 [X]")
				break
			else:
				pass

			# Entrada Jugardor 2

			turno = turno + 1
			# DEBUGMODE print ("Turno",turno)
			# Actualizar_lista () # No entiendo porqué si actulizo la lista, cuando la toma para valider en el while lo hace con la antigua.
			# print ("EMi",self.winall_auto_step2) # Acá es donde se envidencia que la liata self.winall_auto_step2 no es la que debería ser luego de correr la función.
			if turno > (self.VL * self.VL):
				print("TABLAS")
				break

			self.input_jugador("2")

			termino_el_partido = self.validacion_ganadores(self.Lista_user2)
			# print (termino_el_partido)
			# print ("Partido_Cerrado After F", Partido_Cerrado)
			if termino_el_partido == 1:
				print("GANO EL JUGADOR 2 [0]")
				break

		print("FIN DEL JUEGO")

	@staticmethod
	def Letra_ABC(posicion):
		abecedario = list(string.ascii_uppercase)
		letra = abecedario[posicion]
		return letra

	def print_matriz(self, lista):
		print ("******"*self.VL)

		Matriz_front_end= []

		for i in range (0,len(lista),self.VL):
			Matriz_front_end.append(list(lista[i:i+self.VL]))

		for i in Matriz_front_end:
			print (i)

		print ("******"*self.VL)
		return Matriz_front_end

	def validacion_ganadores(self, listaPlayer): #Esta función valida si la lista de alguno de los ganadore es GANADORA

		Partido_Cerrado = 0

		for a in self.winall_auto_step2:
			comparando = []
			#DEBUGMODE print ("Fun_self.winall_auto_step2", self.winall_auto_step2)
			#DEBUGMODE print ("FunC(a)", a)
			if len(comparando) <= self.VL:

				for i in listaPlayer:
					if i in a:
						#DEBUGMODE print ("ListaJugador a comparar",listaPlayer)# Lista_user1:  ['B2', 'A2', 'B1']
						#DEBUGMODE print ("Lista que compara", a) #a=['A2', 'B2', 'C2']
						comparando.append(i)
						if len(comparando) >= self.VL:
							print(comparando)
							#DEBUGMODE print ("HAY GANADOR querido")
							#DEBUGMODE print ("Partido_Cerrado Func", Partido_Cerrado)
							return 1

					else:
						if len(comparando) >= self.VL:
							break

			else:
				break

		print ("out of loop")

