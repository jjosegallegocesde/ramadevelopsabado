#FUNCION TRADICIONAL PARA SUMAR 2 NUMEROS
def sumar(numero1, numero2):
    return(numero1+numero2)

#INVOCANDO LA FUNCION SUMAR
resultado= sumar(5,10)
print(f'la suma es: {resultado}')

if resultado>10:
    print('gana')
else:
    print('pierde')

