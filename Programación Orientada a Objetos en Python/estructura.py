squares = [x**2 for x in range(1,11)]
#print("cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius]
#print("temperatura en F:", fahrenheit)

#Numeros pareces
evens = [x for x in range (1,21) if x%2 ==0]
#print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
#print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(trasposed_row)
        
print(transposed)


