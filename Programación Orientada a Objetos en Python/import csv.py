import csv

# Leer un archivo CSV completo y mostrar cada fila
"""
with open('products.csv', mode='r') as file:  # Abre el archivo CSV en modo lectura
    csv_reader = csv.DictReader(file)  # Utiliza DictReader para leer el archivo como un diccionario
    for row in csv_reader:  # Itera sobre cada fila del archivo CSV
        print(row)  # Muestra la fila completa (cada fila es un diccionario con claves las columnas)
"""

# Mostrar la información por columnas específicas (producto y precio)
with open('products.csv', mode='r') as file:  # Abrimos el archivo CSV en modo lectura
    csv_reader = csv.DictReader(file)  # Usamos DictReader para interpretar cada fila como un diccionario
    for row in csv_reader:  # Iteramos sobre cada fila del archivo
        # Accedemos a los valores de las columnas 'name' y 'price' usando las claves del diccionario
        print(f"Producto: {row['name']}, Precio: {row['price']}")
