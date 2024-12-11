import csv  

# Leer un archivo CSV y mostrar cada fila como un diccionario
"""with open('products.csv', mode='r') as file:  # Abre el archivo en modo lectura
    csv_reader = csv.DictReader(file)  # Crea un lector que interpreta cada fila como un diccionario
    for row in csv_reader: 
        print(row)"""  # Imprime el diccionario de cada fila

# Mostrar la información específica de las columnas 'name' y 'price'
with open('products.csv', mode='r') as file:  # Abre el archivo nuevamente en modo lectura
    csv_reader = csv.DictReader(file)  # Crea otro lector para leer el archivo CSV
    for row in csv_reader:  # Itera sobre cada fila 
        print(f"Producto: {row['name']}, Precio: {row['price']}")  # Imprime el producto y su precio

        