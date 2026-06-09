#DrugStore 


# Productos={

#     1:{"Nombre": "WEED", "Precio": 3000},
#     2:{"Nombre": "LSD", "Precio": 5000},
#     3:{"Nombre": "MUSHROOMS", "Precio": 7000},
#     4:{"Nombre": "CRACK", "Precio": 6000},
#     4:{"Nombre": "METANPHETAMINE", "Precio": 7000},
#     5:{"Nombre": "CIGARETTES", "Precio": 2000},
#     6:{"Nombre": "BEERS", "Precio": 1500},

# }



# def mostrar():
#  for cod, datos in Productos.items():
#     print("-"*30)
#     print(f"({cod}).- {datos['Nombre']} - ${datos['Precio']}")
#             #ID        #Nombre lista        #Precio lista
#     print("-"*30)

# def eliminar():
#     mostrar()
#     delete=int(input("Ingrese el numero del Producto a ELIMINAR: "))
#     del Productos[delete]

# def Editar():
#     mostrar()
#     actu=int(input("Que Producto quiere RENOMBRAR?: "))
#     nombre=input("Ingrese el nuevo nombre: ")
#     Productos[actu]={"Nombre": nombre,}
#     print("Actualizado con exito")

# def agregar():
#     add=input("Ingrese el nombre del Producto a AGREGAR: ")
#     price=input("Ingrese el precio del Producto a AGREGAR: ")
    
    # Productos[4]={"Nombre": pkm, "Nivel": nvl}
    # list(Productos.keys())[-1] +1       #ESTO SE UTIIZA PARA QUE AL REGISTRAR UN NOMBRE AL DICCIONARIO, EL VALOR NUMERICO VAYA AUMENTANDO

#     Productos[list(Productos.keys())[-1] +1]={"Nombre": add, "Precio": price}

# def comprar():
#     mostrar()
#     try:
    
#         buy=int(input("Que producto desea COMPRAR?: "))
#         print(f"Usted ha comprado {Productos[comprar]["Nombre"]} Por un valor de: {Productos["Precio"]}")


#     except ValueError:
#         print("ERROR")

    #INCOMPLETO, MIRAR LA RESOLUCION EN EL REPOSITORIO


# def boleta():
#     print("PlaceHolder")

# def MenuProducto():

#     while True:
#         try:
#             print("1.- Agregar Producto")
#             print("2.- Eliminar Producto")
#             print("3.- Editar Producto")
#             print("4.- Mostrar Producto")
#             print("5.- Carrito")
#             print("6.- Boleta")
#             print("7.- Salir")
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
#                     comprar()
#                 case 6:
#                     boleta()
#                 case 7:
#                     print("Saliendo")
#                     break

#                 case _:
#                     print("Opción Invalida")


#         except ValueError as e:
#             print("ERROR: Solo numeros enteros. Error", e)    

# MenuProducto()