#funcion tradicional para sumar

def sumar(numero1,numero2):
    return numero1 + numero2

#Invocando la funcion sumar 
resultado = sumar(5,10)
print(f"La suma es: {resultado}")

if resultado > 10:
    print("Ganaste")
else:
    print("Perdiste")