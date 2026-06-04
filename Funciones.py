#Funciones



# def funcion():
#     print("Ay")

# funcion()


#SIN ARGUMENTOS Y SIN RETORNO

# def resta(n1, n2):
#     print(f"El resultado de la resta {n1-n2}")

# resta(22, 13)


# CON ARGUMENTOS Y CON RETORNO

# def restaCret (n1, n2):

#  return n1-n2

# print(restaCret(9,3))


# CON VARIABLE

# def multiplica():
#     num1=5
#     num2=5
#     return num1*num2

# vari=multiplica()*4 #Esta variable multiplica el num1 y el num2 y el resultado de eso lo multiplica en 4

# print(vari) #Se invoca esa variable


#SIN VARIABLE

# def multiplica():
#    num1=8
#    num2=5
#    return num1*num2
# print(multiplica())


#ACTIVIDAD 1 / INCOMPLETA, CONTINUAR EN CASA


# def suma(n1, n2):
#     return n1+n2

# def resta(n1, n2):
#     return n1-n2

# def mult(n1, n2):
#     return n1*n2

# def div(n1, n2):
#     return n1/n2

# op=0
# total=0
# while True:
#     print("== CALCULADORA ==")
#     print("1.- Sumar")
#     print("2.- Restar")
#     print("3.- Multiplicar")
#     print("4.- Dividir")
#     print("5.- SALIR")
#     op=int(input())
#     match op:
#         case 1:
#             n1=int(input("Ingrese un numero: "))
#             n2=int(input("Ingrese otro numero: "))
#             print(f"El resultado es {n1+n2}") 

#         case 2:
#             n1=int(input("Ingrese un numero: "))
#             n2=int(input("Ingrese otr numero: "))
#             print(f"El resultado es {n1-n2}") 

#         case 3:
#             n1=int(input("Ingrese un numero: "))
#             n2=int(input("Ingrese otr numero: "))
#             print(f"El resultado es {n1*n2}") 

#         case 4:
#             n1=int(input("Ingrese un numero: "))
#             n2=int(input("Ingrese otr numero: "))
#             print(f"El resultado es {n1/n2}") 

#         case 5:
#             print("Saliendo")

#         case _:
#             print("Opcion invalida")



#ACTIVIDAD 2

#Crear un programa que calcule el IVA
#y retorne el valor con el IVA incluido


#Usar argumento y retorno

# def IVA(n):
#     return n*1.19


# neto=int(input("Ingrese el precio neto: "))

# print("El valor con IVA es: ", IVA(neto)) #los datos que ingrese el usuario se usaran en la funcion recien creada.


#ACTIVIDAD 3

#EN A.V.A HACER LA ACTIVIDAD 3.3.3 CON LISTAS