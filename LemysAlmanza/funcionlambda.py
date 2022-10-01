#funcion Tradicional para sumar
def sumar(numero1,numero2):
    return numero1 + numero2
#funcion lambda
sumarnumeros=lambda numero1,numero2:numero1+numero2

#llamaado la tradicional
print(sumar(5,10))
#llamado lambda
print(sumarnumeros(5,10))