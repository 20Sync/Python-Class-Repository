# Crear un gestor de estacionamiento
# Un estacionamiento tiene 4 pisos
# y cada piso tiene 10 espacios
# Preguntar cuando entra un vehiculo, que tipo de vehiculo es

# Tipos de vehiculos:

# Vehiculo ligero: 2000
# Vehiculo mediano: 3000
# Vehiculo pesado: 3500


# Luego, acomodarlo en algun lugar de algun piso disponible
# El menu debe tener las siguientes alternativas:

#1.- Ingresar vehiculo
#2.- Contar ganancias
#3.- Contar vehiculos
#4.- Mostrar


# parking={

#     1:[],
#     2:[],
#     3:[],
#     4:[]



# }














































# Ante cualquier duda revisar en el AVA la solución del jairito en mensajes del curso de basketball viernes



# SOLUCIONATORIO - PROFESOR


# parking={
#     1:[],
#     2:[],
#     3:[],
#     4:[]

# }
# def ingresAuto():
#     valor=0
#     print("Ingresar vehiculo nuevo")
#     tipo=int(input("Que tipo es?: \n1.-Ligero\n2.-Mediano\n3.-Pesado"))
#     if tipo==1:
#         valor=2000
#     elif tipo==2:
#         valor=3000
#     elif tipo==3:
#         valor=3500
#     else:
#         print("Vehiculo invalido")
#     piso=int(input("EN que piso va?: "))
#     if piso in [1,2,3,4] and valor>0 :
#         if len(parking[piso])<10:
#             parking[piso].append(valor)
#             print("Agregado al piso", piso)
#         else:
#             print("Piso lleno")
#     else:
#         print("Piso no válido")


# def calculaGanancias():
#     totalGanancias=0
#     print("Contando Ganancias")
#     for piso in parking.values():
#         totalGanancias+=sum(piso)
#     print(f"El total recaudado es {totalGanancias}")


# def cuentAutos():
#     totalAutos=0
#     for piso in parking.values():
#         totalAutos+=len(piso)
#     print("El total de autos en el parking es:", totalAutos)


# def muestrAutos():
#     for h, t in parking.items():
#         print(h, ".- ", t)

# def parkingAutos():
#     while True:
#         try:
#             print('''1.- ingresar vehiculo
#                      2.- contar ganancias
#                      3.- contar vehiculos
#                      4.- Mostrar
#                      5.- Salir''')
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     ingresAuto()
#                 case 2:
#                     calculaGanancias()
#                 case 3:
#                     cuentAutos()
#                 case 4:
#                     muestrAutos()
#                 case 5:
#                     print("Saliendo")
#                     break
#                 case _:
#                     print("Opción inválida")
#         except Exception as e:
#             print("Error:", e)

# parkingAutos()





# EJERCICIO 2 

# Crear un gestor de pacientes
# Al agregar un nombre se debe validar que no este vacio y que contenga mas de 8 caracteres
# Previsiones de salud: Fonasa, Isapre y Fodesa
# Al ingresar un paciente se debe poner la temperatura
# Crear una función que valide si esta grave o no, para que este grave debe tener más de 39



# pacientes=[

#     {"Nombre": "Jairo Medina", "Previsión": "Fonasa", "Temperatura": 36,
#      "Grave": False}
    
# ]

# def Agregar():
#     name=input("Ingrese el nombre del paciente: ")
#     pacientes.append(name)

# def Eliminar():
#     print("")

# def Mostrar():
#     print("-"*30)
#     c=1
#     for p in pacientes:
#         print(c,"-", p)
#         c+=1
#         print("-"*30)



# while True:
#     try:
#         print("1.- Ingresar Paciente")
#         print("2.- Eliminar Paciente")
#         print("3.- Mostrar Pacientes")
#         op=int(input(": "))
#         match op:
#             case 1:
#                 Agregar()
#             case 2:
#                 Agregar()
#             case 3:
#                 Mostrar()


#     except ValueError as e:
#         print("Error", e)

