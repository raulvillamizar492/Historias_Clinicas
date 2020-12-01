import os
os.system('cls')
print("")
print("*˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚*˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚*")
print("˚                           Bienvenido                            ˚")
print("˚                 Historias clinicas del Hospital                 ˚")
print("˚                                                                 ˚")
print("*˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚*")
print("")

# **********************
# * VARIABLES GLOBALES *
# **********************
running = True
database = list()




# ********************
# *     FUNCIONES    *
# ********************

def show_menu():

	print("")
	print("")
	print("\t\t■  1 - Cargar Paciente")
	print("\t\t■  2 - Buscar Paciente")
	print("\t\t■  3 - Listar Paciente")
	print("\t\t■  4 - Salir")
	print("")
	print("")
	res= input("INGRESA UNA OPCION ==> ")
	print("")
	print("")
	os.system('cls')
	return res

def response_validate(r):
	validated = False
	num_res = 0
	#Digit verifica si la entrada es un numero
	if response.isdigit():
		num_res = int(response)
		if num_res >= 1 and num_res <= 4:
			msg = "Esta en rango"
			validated = True
		else:
			msg ="Fuera de rango"

	else:
		msg = "Entrada Incorrecta" 
	return validated, num_res, msg
def search(y):
	for x in range(len(database)):
		if  database[x]["nombre"].lower() == name.lower():	
			print("")
			print("<-------------- Paciente Encontrado!! -------------->")
			print("")
			print("")						
			print("PACIENTE",name," | H. CLINICA ->",database[x]["historia"])
			print("")
			print("")
			print("********************************************************")
			print("********************************************************")
			finded = True
		else:
			finded = False
	if finded == False:
		print("Paciente no Encontrado")
		
				
					



# ********************
# *  LOOP PRINCIPAL  *
# ********************

while running:
	response = show_menu()
	validated, num_res, msg = response_validate(response)
	if validated:
		if num_res == 1:
			name=input("Por favor ingresar el nombre del paciente -->>  ")
			history=input("Ingrese la historia clinica del paciente -->>  ")
			paciente = {"nombre":name,"historia":history}
			database.append(paciente)
			print(database)

		elif num_res == 2:
			name = input("Ingrese el nombre del paciente..")
			search(name)

		elif num_res == 3:
			print("")
			print("*˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚*˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚*")
			print("˚             Listado De Pacientes          ˚")
			print("*˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚*")
			print("")

			for x in range(len(database)):
				print("Nombre --> ".rjust(10), database[x]["nombre"], "\tHistoria C --> ".rjust(10), database[x]["historia"])

			print("")
			print("")	
			print("Fin de lista....")
		else:
			
			running = False
	else:
		msg.upper()
		print(msg)


print("")
print("Aplicacion Finalizada")
print("")



		



	