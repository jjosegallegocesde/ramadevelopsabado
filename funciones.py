#funcion tradicional para sumar dos numeros
def sumar(numero1, numero2):
    return numero1 + numero2
#invocando la funcion sumar

resultado = sumar (10,5)
print(f"La suma de los números  es {resultado}.")

if resultado > 10:
    print("Ganaste")
else:
    print("Perdiste")