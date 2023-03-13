#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números >40  

numeros = (50,45,20,30,40,87)
tuplaNumeros= list(numeros)
print(tuplaNumeros)
for x in numeros:
    if x >40:
        print(x)
