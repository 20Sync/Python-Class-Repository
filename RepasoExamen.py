# ==========================================
# 1. DICCIONARIOS DE DATOS (DADOS EN EL ET)
# ==========================================

# productos = {modelo: [marca, pantalla, RAM, disco, GB, procesador, video]}
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', 'IT', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', 'IT', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', 'IT', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', 'IT', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', 'IT', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', 'IT', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

# stock = {modelo: [precio, stock]}
stock = {
    '8475HD': [387990, 10], 
    '2175HD': [327990, 4], 
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], 
    '123FHD': [290890, 32], 
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 
    'UWU131HD': [349990, 1], 
    'FS1230HD': [249990, 0]
}

# ==========================================
# 2. REQUISITOS / FUNCIONES OBLIGATORIAS
# ==========================================

# Opción 1: Sumar el stock total de una marca particular
def stock_marca(marca):
    total_stock = 0
    # Recorremos el diccionario de productos para buscar la marca
    for modelo, datos in productos.items():
        # datos[0] es la Marca. Usamos .lower() para que sea indiferente de mayúsculas/minúsculas
        if datos[0].lower() == marca.lower():
            # Si el modelo existe en el inventario de stock, sumamos su cantidad (posición 1)
            if modelo in stock:
                total_stock += stock[modelo][1]
    
    print(f"El stock es: {total_stock}")


# Opción 2: Búsqueda filtrada por rango de precios
def búsqueda_precio(p_min, p_max):
    elementos_encontrados = []
    
    for modelo, datos_prod in productos.items():
        marca = datos_prod[0]
        
        # Verificamos si el modelo está en el diccionario stock
        if modelo in stock:
            precio = stock[modelo][0]
            cantidad_stock = stock[modelo][1]
            
            # Filtro: Debe estar en el rango de precio Y tener stock disponible (> 0)
            if p_min <= precio <= p_max and cantidad_stock > 0:
                # El formato exigido por el PDF es "Marca--Modelo"
                elementos_encontrados.append(f"{marca}--{modelo}")
                
    if elementos_encontrados:
        # Ordenar alfabéticamente
        elementos_encontrados.sort()
        print(f"Los notebooks entre los precios consultas son: {elementos_encontrados}")
    else:
        print("No hay notebooks en ese rango de precios.")


# Opción 3: Actualizar el precio de un modelo (Retorna True o False)
def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p  # Modifica el precio en la lista asociada a la llave
        return True
    return False


# ==========================================
# 3. CONTROLADOR PRINCIPAL (MENU PRINCIPAL)
# ==========================================
while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    
    opcion = input("Ingrese opción: ")
    
    if opcion == '1':
        marca_ingresada = input("Ingrese marca a consultar: ")
        stock_marca(marca_ingresada)
        
    elif opcion == '2':
        # Bucle para manejar excepciones hasta que ingresen enteros correctos
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                # Si no hay error al convertir a int, llamamos a la función y rompemos el bucle interno
                búsqueda_precio(p_min, p_max)
                break
            except ValueError:
                print("Debe ingresar valores enteros!!\n")
                
    elif opcion == '3':
        while True:
            mod = input("Ingrese modelo a actualizar: ")
            # Validamos que el precio sea entero usando una captura simple
            try:
                nuevo_precio = int(input("Ingrese precio nuevo: "))
            except ValueError:
                print("Precio inválido. Intente de nuevo.")
                continue
                
            # Capturamos el return (True o False) de la función
            if actualizar_precio(mod, nuevo_precio):
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")
                
            # Preguntar si desea continuar modificando
            respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
            if respuesta != 'si':
                break  # Sale al menú principal
                
    elif opcion == '4':
        print("Programa finalizado.")
        break  # Rompe el bucle principal (cierra el script)
        
    else:
        print("Debe seleccionar una opción válida!!")