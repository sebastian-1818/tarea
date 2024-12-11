import csv

file_path = 'products.csv'  # Ruta del archivo CSV original
updated_file_path = 'products_updated.csv'  

with open(file_path, mode='r') as file:  
    csv_reader = csv.DictReader(file)  # Usamos DictReader para interpretar cada fila como un diccionario
    # Obtener los nombres de las columnas existentes y añadir la columna 'total_value'
    fieldnames = csv_reader.fieldnames + ['total_value']  

    with open(updated_file_path, mode='w', newline='') as updated_file:  
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)  # Preparamos el escritor con los nuevos encabezados
        csv_writer.writeheader()  

        # Iterar sobre las filas del archivo original
        for row in csv_reader:
            # Calcular el valor total (precio * cantidad) y agregarlo a la nueva columna
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)  # Escribir la fila actualizada en el nuevo archivo
