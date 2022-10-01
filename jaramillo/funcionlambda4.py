
nombre = input(f'dame tu nombre: ')
edad = input(f'dame tu edad: ')
ocupacion = input(f'dame tu ocupacion: ')

adiccionario = lambda nombre,edad,ocupacion : {'nombre':nombre,'edad':edad,'ocupacion':ocupacion}

print(adiccionario(nombre,edad,ocupacion))