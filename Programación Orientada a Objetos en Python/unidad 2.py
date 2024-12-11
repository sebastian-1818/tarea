with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)# end='' para evitar doble salto de línea
    file.write('nuevas cosas en este archivo\n')
    file.write('otra linea\n')
    file.write('mas linea\n')