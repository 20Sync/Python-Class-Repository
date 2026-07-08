#      -5  -4 -3  -2 -1
# lista=[10, 6, 20, 4, 16]
#         0   1  2   3   4

# print(lista)
# print(lista[-1])
# # print("-"*30) # Linea divisoria


# for i in lista:
#     print(i)

# lista.append(64) #Agrega un digito a una lista

# print("-"*30) #Linea divisoria

# for i in lista:
#     print(i)

#=============================================================================

#Cree una lista de 4 frutas
#y muestrelas cada una

# fruta=["Manzana", "Pera", "Sandia"]
# print(fruta[0])

# fruta.insert(1, "Pene")
# print(fruta)

# fruta.remove("Pene")
# print(fruta)

# fruta.pop(0)
# print(fruta)

# fruta.append("Ay")
# print(fruta)

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
#         print("-"*30)
#         print(c,"-", p)
#         c+=1
#     print("-"*30)
# def eliminar():
#     mostrar()
#     delete=int(input("Ingrese el numero del pokemon a liberar: "))
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


videojuegos=["GTA 6", "FORTNITE", "ROCKET LEAGUE", "DARK SOULS 3"]

def mostrar():
    c=1
    for v in videojuegos:
        print("-"*30)
        print(f"{c}.-  {v}")
        c+=1
        print("-"*30)

def agregar():
    mostrar()
    add=input("INGRESAR NOMBRE DEL VIDEOJUEGO A AGREGAR: ")
    
    while True:
        if add.upper and len(add) > 3 and " " not in add: #Mientras el nombre este en mayusculas y sea mayor de 3 caracteres y sin espacios se agrega.
            videojuegos.append(add)
            break

        else:
            print("ERROR: Nombre en mayusculas, sin espacios y mayor de 3 caracteres")
            add=input("INGRESAR NOMBRE DEL VIDEOJUEGO A AGREGAR: ")

def eliminar():
    mostrar()
    delete=int(input("INGRESE EL JUEGO QUE DESEA ELIMINAR: "))
    videojuegos.pop(delete-1)

def renombrar():
    mostrar()
    renom=int(input("QUE VIDEOJUEGO DESEA RENOMBRAR?: "))
    videojuegos[renom-1]=input("INGRESE EL NOMBRE DEL NUEVO VIDEOJUEGO: ")

def tienda():
    while True:
        try:
            print("1.- Agregar Juegos")
            print("2.- Eliminar Juegos")
            print("3.- Renombrar Juegos")
            print("4.- Mostrar Juegos")
            print("5.- Salir")
            op=int(input())
            match op:
                case 1:
                    agregar()
                case 2:
                    eliminar()
                case 3:
                    renombrar()
                case 4:
                    mostrar()
                case 5:
                    print("Saliendo")
                    break
                case _:
                    print("ERROR: OPCIÓN INVALIDA")

        except ValueError:
            print("ERROR")

tienda()