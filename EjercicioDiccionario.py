# DrugStore 


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
    
#     Productos[4]={"Nombre": pkm, "Nivel": nvl}
#     list(Productos.keys())[-1] +1       #ESTO SE UTIIZA PARA QUE AL REGISTRAR UN NOMBRE AL DICCIONARIO, EL VALOR NUMERICO VAYA AUMENTANDO

#     Productos[list(Productos.keys())[-1] +1]={"Nombre": add, "Precio": price}

# def comprar():
#     mostrar()
#     try:
    
#         buy=int(input("Que producto desea COMPRAR?: "))
#         print(f"Usted ha comprado {Productos[comprar]["Nombre"]} Por un valor de: {Productos["Precio"]}")


#     except ValueError:
#         print("ERROR")

#     # INCOMPLETO, MIRAR LA RESOLUCION EN EL REPOSITORIO


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



#EJERCICIO 2

#REFACTORIZAR EL CODIGO DEL PROFESOR 

#   RETO 1:
# Cambiar el menu 5 para que sea recursivo
# Hacer que el usuario siga comprando hasta que presione salir


#   RETO 2:
# Mejorar la boleta
# Que tenga un mensaje de bienvenida
# Luego enlistar los productos:
#
# Prod 1---$5000
# Prod 2---$5000
# Prod 3---$5000
# Prod 4---$5000
# 
# Total a pagar + IVA
# Mensaje de cierre


# productos={
#     1:{"nombre":"Uva", "precio": 2000 },
#     2:{"nombre":"Palta", "precio": 4000 },
#     3:{"nombre":"Pera", "precio": 1500 }
# } 

# usar como ejemplo el menu CRUD de pokemon
# para hacerlo con  productos y relizar el
# menu a continuacion


# '''
#             print("1.- Agregar Producto")
#             print("2.- Eliminar Producto")
#             print("3.- Actualizar Producto")
#             print("4.- Mostrar Productos")
#             print("5.- Comprar Productos")
#             print("6.- Crear Boleta (calcula IVA) y Salir")
#             op=int(input("Seleccione una opcion: "))'''

### SOLUCION

# menuProductos()

# print(list(productos.keys())[-1]+1)
# productos={
#     1:{"nombre":"Uva", "precio": 2000 },
#     2:{"nombre":"Palta", "precio": 4000 },
#     3:{"nombre":"Pera", "precio": 1500 }
# } 



# carrito=[]
# def mostrar():
#     for p, z in productos.items():
#         print(f"{p}.- {z['nombre']} - {z['precio']}")
#     print("-"*30)


# def eliminar():
#     mostrar()
    # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
    # pokemons.remove(borrar_pokemon)
#     try:
#         borrar_producto=int(input("Cual es el producto que va a eliminar ?: "))
#         if borrar_producto in productos:
#             del productos[borrar_producto]
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("Debe ingresar un número válido")
# def actualizar():


#     mostrar()
#     try:
#         key=int(input("que producto desea actualizar: "))
#         if key in productos:
#             nombre=input("Ingrese el nombre del producto: ")
#             precio=int(input("Ingrese el precio del producto: "))
#             productos[key]={"nombre":nombre, "precio": precio }
#             print("actualizado con exito")
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("ID o precio inválido")


# def agregar():
#     pkm=input("Ingrese el nombre del producto: ")
#     try:
#         nvl=int(input("Ingrese el precio del producto: "))
#     except ValueError:
#         print("Precio inválido, usando 0")
#         nvl=0
#     productos[list(productos.keys())[-1]+1]={"nombre":pkm, "precio": nvl }


# def compra():

#     mostrar()
#     while True:
#         try:
#             comprar=int(input("Cual producto desea comprar ?: "))
#             if comprar in productos:
#                 print(f"Usted ha comprado {productos[comprar]['nombre']} por un valor de {productos[comprar]['precio']}")
#                 carrito.append(productos[comprar])
#                 mostrar()
#                 print("4.- Salir")

#             if comprar == 4:
#                 print("Saliendo...")
#                 break

#             else:
#                 print("Producto no existe")
#         except ValueError:
#             print("Debe ingresar un número válido")



# def boleta():
#     total=0
#     print("-"*30, "0", "-"*30)
#     print("Gracias por comprar en PichulaStore")

#     for p in carrito:
#         try:
#             total+=int(p["precio"])
#             print(p["nombre"], "----$", p["precio"])


#         except (ValueError, TypeError):
#             print(f"Precio inválido para {p.get('nombre','?')}, contando como 0")
#     iva=total*0.19
#     print("-"*30, "0", "-"*30)
#     print(f"El total de su compra es {total} y el IVA es {iva}")
#     print(f"El total a pagar es  {total+iva} ")
#     print("Gracias por comprar en PichulaStore")
#     print("-"*30, "0", "-"*30)


# def menuProductos():
#     while True:
#         try:
#             print("1.- Agregar Producto")
#             print("2.- Eliminar Producto")
#             print("3.- Actualizar Producto")
#             print("4.- Mostrar Productos")
#             print("5.- Comprar Productos")
#             print("6.- Crear Boleta (calcula IVA) y Salir")
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     agregar()
#                 case 2:
#                     eliminar()
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     compra()
#                 case 6:
#                     boleta()
#                     break
#                 case _:
#                     print("Opcion Invalida")

#         except ValueError as e:
#             print("Solo numeros enteros. Error",e)


# menuProductos()