#      -5  -4 -3  -2 -1
# lista=[10, 6, 20, 4, 16]
#      0   1  2   3   4

# print(lista)
# print(lista[-1])
# print("-"*30) # Linea divisoria


# for i in lista:
#     print(i)

# lista.append(64) #Agrega un digito a una lista

# print("-"*30) #Linea divisoria

# for i in lista:
#     print(i)

#=============================================================================

#Cree una lista de 4 frutas
#y muestrelas cada una

# fruta=["Manzana", "Pera", "Sandia", "Platano"]
# fruta.remove("Pera")
# for f in fruta:
#     print(f)

# print("-"*30)

# print(fruta[0])

#APUNTES:

#Append: Para agregar un int o string al final de mi lista
#Insert: Para agregar un int o string en un numero de mi lista que quiera
#Remove: Para borrar un string de mi lista
#Pop: Para eliminar un elemento de una lista con numeros
#=============================================================================

# MENU POKEMON - POKEDEX

# pokemons=["Pikachu", "Charizard"]
# def mostrar():
#     c=1
#     for p in pokemons:
#         print(c,"-", p)
#         c+=1
#     print("-"*30)
# def eliminar():
#     mostrar()
#     delete=input("Ingrese el nombre del pokemon a liberar: ")
#     pokemons.pop(delete-1)
# def renombrar():
#     mostrar()
#     actu=int(input("Que pokemon quiere renombrar?: "))
#     pokemons[actu-1]=input("Cual será el nombre nuevo?: ")
#     print("Actualizado con exito")
# def agregar():
#     add=input("Ingrese el nuevo pokemon: ")
#     pokemons.append(add)
# def MenuPokemon():

#     while True:
#         try:
#             print("1.- Agregar Pokemon")
#             print("2.- Eliminar Pokemon")
#             print("3.- Renombrar Pokemon")
#             print("4.- Mostrar Pokemon")
#             print("5.- Salir")
#             op=int(input("Seleccione una opción: "))
#             match op:
#                 case 1:
#                     agregar()
                    
#                 case 2:
#                     eliminar()

#                 case 3:
#                     renombrar()

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