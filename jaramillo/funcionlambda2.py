def clasificar(numero):
    return numero%2

clasificarl = lambda numero : numero%2==0

print(clasificar(4))
print(clasificarl(4))

if(clasificarl(100)):
    print("es multiplo")
else:
    print("no es multiplo")