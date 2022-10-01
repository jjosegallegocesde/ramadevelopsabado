
#funciona lambda que clasifique si un numero es par
par =lambda numero:numero%2==0

print()
if(par(50)):
    print("el Numero es par")
else:
    print("el Numero No es Par")


#Función lambda que clasifique números mayores a 10 en una lista
lista=[10,45,30,22,5,12,15]
mayores=lambda numero:numero>10


for numero in lista:
  if(numero>10):
    if((mayores(numero))):
        print("es mayor")
    else:
        print("es menor")


       
#Función lambda que recibe nombre, edad y ocupación de una persona y devuelva un diccionario con esta información
datos=lambda nombre,edad,ocupacion:{nombre,edad,ocupacion}
print(datos("lemys",32,"almacenista"))


#Función lambda que sume dos números
sumar=lambda numero0,numero1:numero0+numero1

print(sumar(10,10))

#funcion que multiple un numero x 100
multiplicar=lambda numero:numero*100

print(multiplicar(10))



