#Crear un programa de registros de juegos
#Preguntar cuantos juegos son
#Debe preguntar al usuario Nombre del juego:
#- Al menos 5 caracteres
#- No debe incluir espacios y todas las mayusculas 

#Preguntar precio
#- Solo numeros enteros positivos
#- Si vale mas de 20000 es indie pero menos de 40000
#- Si vale 40000 o mas, es triple A
#- Mostrar al final cuantos hay de cada categoria

#Clasificación
#- E para todos (-12)
#- +12 para adolescentes (12 y 17)
#- M para personas +18

#MOSTRAR RESUMEN

#Ej: hay 4 indies, y 5 de estudio. Solo 3 con clasificación E

#USO DE TRY- EXCEPT OBLIGATORIO


# juegos=0
# indie=0
# estudio=0

# clasif_E=0
# clasif_12=0
# clasif_M=0


# while True:
#     try:
#         juegos=int(input("Cuantos juegos desea registrar?: "))

#         if juegos >0:
#             print("ERROR: Valor invalido")
#             break
#         else:
#             print("Debe ingresar un digito mayor a 0")

#     except ValueError:
#         print("ERROR: Ingrese un valor numerico")    


# for i in range(juegos):
#     print(F"INGRESE EL JUEGO {i}")

#     while True:
#         name=(input("Ingrese nombre del juego"))
        
#         if len(name) >=5 and name.isupper() and " " not in name:
#             break
#         else:
#             print("ERROR: Minimo 5 caracteres, sin espacios y en mayusculas")

#INCOMPLETO, TERMINAR EN CASA.



     
#ACTIVIDAD 2.5.3 EN AVA "RESOLVIENDO PROBLEMAS CON PYTHON"

# saldo=-100000
# op=0
# while op != 3:
#     try:
#         print("1.- PAGO DE TARJETA DE CREDITO")
#         print("2.- SIMULACIÓN DE COMPRAS")
#         print("3.- SALIR")
#         op=int(input())

#         match op:
#             case 1:
                
#                     monto=int(input(f"Deuda actual ({saldo}) Ingrese monto: "))
                    
#                     if monto <0:
#                         print("ERROR: Ingrese un valor mayor a 0")

#                     elif monto >100000:
#                         print("ERROR: Limite alcanzado")
                
#                     else:
#                         print("Transacción Completa")
#                         monto=monto-saldo
#                         print(f"Saldo: {monto}")

#             case 2:
#                 print()
        
#     except ValueError as e:
#         print("ERROR:", e)

#SIN TERMINAR, ACABAR EN LA CASA

#REVISAR REPOSITORIO GITHUB DEL PROFE, SECCION 002D, "TallerPrueba"
















































































































































































































































































































































































































































