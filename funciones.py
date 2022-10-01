#Funcion tradiccional para sumar 2 numeros
def sumar(numero1,numero2 ):
    return numero1 + numero2
#invocar la funcion sumar

resultado = sumar (5,10)
print(f"la suma es  {resultado}")

if resultado > 10:
    print("Ganastes")
else:
    print("Perdio")