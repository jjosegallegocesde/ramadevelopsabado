#Fuuncion tradicioanl para sumar dos numeros
def sumar(num1, num2):
    return num1 + num2

#Invocando la funcion sumar
resultado = sumar(5, 10)
print(f'La suma es: {resultado}')

if resultado > 10:
    print("¡Ganaste!")
else: 
    print("¡Perdiste!")