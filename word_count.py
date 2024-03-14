archivo = open("lorem_ipsum.txt", "r") 
texto = archivo.read()
print(texto)

#determinar numero de caracteres distintos del texto
caracteres = set(texto)
ca = len([c for c in caracteres if c != " "])

print("El número de caracteres distintos es: ", (ca))

#determinar numero de palabras distintas del texto
f_s = texto.split()
s = set(f_s)
print("El número de caracteres distintos es: ",len(s))












