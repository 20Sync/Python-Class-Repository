#Uso y explicación de diccionarios


# alumno={
#     "Nombre": "Agusto Pinochet",
#     "Edad": 64,
#     "Nacionalidad": "Chilena"
# }

# print(alumno)
# print(alumno["Nombre"])

# alumno()

#TERMINAR DE HACERLO EN LA CASA

#EJERCICIO 1

# MENU POKEMON - POKEDEX

# pokemons={

#         1: {"Nombre": "Pikachu", "Nivel": 19},
#         2: {"Nombre": "Charizard", "Nivel": 16},
#         3: {"Nombre": "Eevee", "Nivel": 12}
#     #keys   #Values
# }


# def mostrar():
#     for p, z in pokemons.items():
#          print(f"{p}.- {z["Nombre"]} Nivel: {z["Nivel"]} ")
#     print("-"*30)

# def eliminar():
#     mostrar()
#     delete=int(input("Ingrese el numero del pokemon a liberar: "))
#     del pokemons[delete]

# def Editar():
#     mostrar()
#     actu=int(input("Que pokemon quiere renombrar?: "))
#     nombre=input("Ingrese el nuevo nombre: ")
#     nivel=input("Ingrese el nivel: ")
#     pokemons[actu]={"Nombre": nombre, "Nivel": nivel}
#     print("Actualizado con exito")

# def agregar():
#     pkm=input("Ingrese el nombre del pokemon: ")
#     nvl=input("Ingrese el nivel del pokemon: ")

#     pokemons[list(pokemons.keys())[-1] +1]={"Nombre": pkm, "Nivel": nvl}         #ESTO SE UTIIZA PARA QUE AL REGISTRAR UN NOMBRE AL DICCIONARIO, EL VALOR NUMERICO VAYA AUMENTANDO
    

# def MenuPokemon():

#     while True:
#         try:
#             print("1.- Agregar Pokemon")
#             print("2.- Eliminar Pokemon")
#             print("3.- Editar Pokemon")
#             print("4.- Mostrar Pokemon")
#             print("5.- Salir")
#             op=int(input("Seleccione una opción: "))
#             match op:
#                 case 1:
#                     agregar()
                    
#                 case 2:
#                     eliminar()

#                 case 3:
#                     Editar()

#                 case 4:
#                     mostrar()
#                 case 5:
#                     print("Saliendo")
#                     break

#                 case _:
#                     print("Opción Invalida")


#         except ValueError as e:
#             print("ERROR: Solo numeros enteros. Error", e)    

# MenuPokemon()

#APUNTES

# pokemons.keys() #Muestra las keys (1,2,3)
# pokemons.values() #Muestra los values (Pares de datos)
# pokemons.items() #Muestra los dos datos


