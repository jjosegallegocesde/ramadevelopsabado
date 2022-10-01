#Funcion tradicional para sumardos numeros
def sumar(num1,num2):
    return num1+num2

#invocar la funcion
resultado=sumar(5,10)
print(f'la suma es {resultado}')

if resultado>10:
    print('Ganaste cualquier bobada')
else:
    print('Perdiste')