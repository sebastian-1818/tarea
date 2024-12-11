import statistics
import csv

# Leer los datos de ventas mensuales desde un archivo csv
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file: 
    reder = csv.DictReader(file) # Lectura del archivo CSV como un diccionario
    for row in reader:
        month = row['month']
        sales = int(row['sles'])
        monthly_sales[month] = sales # Guardar las ventas en el diccionario con el mes como clave
        
sales = list(monthly_sales.values())
#print(sales)

#Hallar la media 
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#Hallar la mediana 
mean_sales = statistics.median(sales)
print(f"La mediana es: {mean_sales}")

#Hallar la moda 
mean_sales = statistics.mode(sales)
print(f"La media es: {mean_sales}")

#Desviacion Estandar 
stdev_sales = statistics.stdev(sales)
print(f"La desviacion estandar es:{stdev_sales}")

#Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La mediana es: {variance_sales}")
# Calcular el rango de las ventas (diferencia entre el máximo y el mínimo)
max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')