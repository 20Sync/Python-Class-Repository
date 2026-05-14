
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


#============================================================

#Ejercicio 4 - Cajero

#Simula un cajero automatico con un saldo inicial de $100.000
#Solo se puede sacar/ingresar multiplos de 5.000

#(INCOMPLETO. VER LA SOLUCION EN EL DIRECTORIO PYTHON DEL PROFESOR.)


# clave=2007

# put=int(input("Ingrese clave: "))
# while put != clave:
#     print("Clave Erronea")
#     put=int(input("Ingrese clave: "))



# select=0
# op=0
# sueldo=100000
# cartera=5000


# while True:

#         print("BIENVENIDO AL SISTEMA")
#         print("1.- Depositar Dinero")
#         print("2.- Retirar Dinero")
#         print("3.- Salir")
#         select=int(input())
#         match select:
#             case 1:
#                 try:
#                     op=int(input(f" Saldo: ({sueldo}) Cartera: ({cartera}) Cuanto dinero desea depositar?: "))
#                     while op <1 or op >cartera:    
#                             print("Error, valor invalido")
#                             op=int(input(f" Saldo: ({sueldo}) Cartera: ({cartera}) Cuanto dinero desea depositar?: "))
                    
#                     if op %5000!=0:
#                         print("ERROR: Sollo puedes retirar multiplos de ")


#                     sueldo+=op
#                     cartera-=op
                        
#                     print(f'''   

#                         RESUMEN DE CUENTA:

#                         Saldo depositado: {op}  
#                         Saldo Restante: {sueldo}  
#                         Saldo Cartera: {cartera}


#                         ''')
                    
#                 except ValueError as a:
#                     print("ERROR: Ingrese un valor numerico")
#             case 2: 
#                 try:
#                     op=int(input(f" Saldo: ({sueldo}) Cuanto dinero desea retirar?: "))
#                     while op <5000 or op >sueldo:
#                         print("Error, valor invalido")
#                         op=int(input(f"Monto: ({sueldo}) Cuanto dinero desea retirar?: "))

#                     if op <5000!=0:
#                         print("ERROR: Ingrese valores multiplos de 5000")

#                     sueldo-=op
#                     cartera+=op
                        
#                     print(f'''   

#                         RESUMEN DE CUENTA:

#                         Saldo Retirado: {op}  
#                         Saldo Restante: {sueldo}  
#                         Saldo Cartera: {cartera}

#                         ''')
                    
#                 except ValueError as a:
#                     print("ERROR: Ingrese un valor numerico")
#             case 3:
#                 print("Saliendo")
                
#             case _:
#                 print("Opción Invalida")


 #USO DEL WHILE


# code=4545
# while True:
#     pasw=int(input("Ingrese el codigo de 4 digitos: "))
#     if pasw == code:
#         print("Bienvenido al sistema")
#         break

#     else:
#         print("Codigo Incorrecto")    


#Ejercicio 1


#Colectivo Femenino

# while True:
#     sex=input("ingrese su sexo (F/M): ").lower()

#     if sex == "m":
#         print("Chao machito")
#         break
#     else:
#         print("Bienvenida perrita")    
        


#TEMARIO PROXIMA PRUEBA 26-05

#-Manejo de errores
#-Uso del while
#-Try except