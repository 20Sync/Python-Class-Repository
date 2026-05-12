
# Programa de ejecución

#Ejemplo 1

# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except:
#         print("ERROR: debe ingresar valores numericos")

#=============================================================

# Uso de Deteccion De Errores

#Ejemplo 2

# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except ValueError as er:
#         print("ERROR", er)
#         print("Debe ingresar valores numericos")


#============================================================

#Ejercicio 1

# op=0
# total=0
# while op != 4:
#     try:
#         print("1.- PC $500.000")
#         print("2.- LGTV $450.000")
#         print("3.- MICROONDAS $100.000")
#         print("4.- SALIR")
#         op=int(input())
#     except ValueError as e:
#         print("ERROR", e)
#         print("Solo se aceptan numeros enteros")
#     match op:
#         case 1:
#             print(f"El total a pagar es: {500000*1.19}" )
#             total+=500000*1.19
#         case 2:
#             print(f"El total a pagar es: {450000*1.19}")
#             total+=450000*1.19
#         case 3:
#             print(f"El total a pagar es: {100000*1.19}")
#             total+=100000*1.19
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar es {total}")

#=============================================================

#Ejercicio 2


# while True:
#     try:
#         num=int(input("Ingrese la cantidad de notas: "))
#         break
#     except:
#         print("Solo numeros enteros")

# suma=0

# for i in range(num):
#     while True:    
#         try:
#             nota=float(input("Ingresa la nota: "))
#             break
#         except ValueError:
#             print("Solo numeros decimales")
#     suma=suma+nota
# prom=suma/num
# print("El promedio es: ", prom)
# if prom >= 4:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")


#============================================================

#Ejercicio 3

#Hacer un programa de ayuda de venta de tickets

# while True:
#     try:
#         op=int(input("Cuantos pasajes deseas vender?: "))
#         break
#     except ValueError as a:
#         print("ERROR", a)
#         print("Ingrese valores numericos")

# total=0
# for i in range (op):
#     while True:
#         try:    
#             print(f"Ingrese el precio del {i+1} pasaje ")
#             pre=int(input())
#             total+=pre
#             break
#         except ValueError as e:
#             print("ERROR", e)
#             print("Ingrese valores numericos")
# print(f"Total: {total}")

                
