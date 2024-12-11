import os 

#obtener el director actual 
"""cwd = os.getcwd() # Obtiene el directorio de trabajo actual
print("Directorio de trabajo actual", cwd)"""

#Listar los archivos.txt
"""txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]# Crea una lista de archivos .txt en el directorio actual
print("Archivos txt:", txt_files)"""

#Renombramos archivos 
os.rename('caperucita.txt', 'cuento.txt')  # Vuelve a listar los archivos .txt
print('Archivo renombrado')

#listar los archivos .txt