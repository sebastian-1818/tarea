import csv
# Función para leer un archivo CSV
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        header = next(reader) # Lee la primera fila como encabezados
        data = [] # Lista donde se almacenará la información
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}  # Crea un diccionario por cada fila
            data. append(country_dict) # Agrega el diccionario a la lista
        return data  # Retorna la lista de diccionarios
        
 # Punto de entrada del programa           
if __name__=='__main__':
    read_csv('./app/data.csv')
    print(data[0])