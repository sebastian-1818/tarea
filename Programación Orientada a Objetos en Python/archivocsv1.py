import csv

# Definir un nuevo producto en forma de diccionario
new_product = {
    'name': 'Wireless Charger', 
    'price': 75,  
    'quantity': 100,  # Cantidad disponible
    'brand': 'ChargerMaster',  # Marca del producto
    'category': 'Accessories',  # Categoría del producto
    'entry_date': '2024-07-01'  # Fecha de ingreso al inventario
}

# Abrir el archivo CSV en modo de 'append' (agregar al final del archivo)
with open('products.csv', mode='a', newline='') as file:

    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    
    # Si el archivo está vacío, escribir la cabecera (los nombres de las columnas)
    if file.tell() == 0:  # file.tell() devuelve la posición actual del archivo; si es 0, el archivo está vacío
        csv_writer.writeheader()  # Se scribir las cabeceras basadas en las claves del diccionario

    # Escribir la fila con los datos del nuevo producto
    csv_writer.writerow(new_product)
