#leer un archivo linea 
with open ("cuento./caperucita.txt","r") as file:
  for lineas in file:
   print(lineas.strip()) #elimina los espacios o saltos de línea al final de cada línea
  
#Leer todas las lineas en una lista 
with open("cuento./caperucita.txt", "r") as file:
   lines = file.readlines()
   print(lines)
   
'''with open("cuento./caperucita.txt","a") as file:
           file.write("\n\nBy:ChatGPT")''' # Agregamos un pie de página con el autor (ChatGPT)
           
#Sobreescribir el texto
'''with open("caperucita.txt", "w") as file:
    file.write("\n\nBy:ChatGPT")'''# Sobrescribimos todo el archivo con solo esta línea