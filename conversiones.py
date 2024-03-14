import sys
# generamos un diccionario
sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
peso_chileno = float(sys.argv[4])



# convertir a pesos chilenos. Moneda a convetir conversiones.py "Moneda a convertir"
diccionario = { 
    "sol_peruano": 0.0046,
    "peso_argentino": 0.093,
    "dolar_americano": 0.00132,
    "peso_chileno" : 10000,
    }

print(f"Los 1000 pesos equivalen a: ")
print(f"{sol_peruano*peso_chileno} Soles")
print(f"{peso_argentino*peso_chileno} Pesos")
print(f"{dolar_americano*peso_chileno} Dolares")


