recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Output
print(recordatorios)

#Insertar evento 02-02-2021
evento = ['2021-02-02', "06:00", "Empezar el Año"]
recordatorios.insert(1,['2021-02-02', "06:00", "Empezar el Año"])
print(recordatorios)

#Remover fecha 15-06-2021
recordatorios.remove(['2021-07-15', "13:00", "No hacer nada es feriado"])
print(recordatorios)

#insertar evento 16-06-2021
recordatorios.insert(3,['2021-07-16', "13:00", "No hacer nada es feriado"])
print(recordatorios)

#Remover 01-05-2021
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])
print(recordatorios)

#insertar cena de Navidad 24-12-2021
recordatorios.insert(4,['2021-12-24', '22:00', 'Navidad'])
print(recordatorios)

#insertar cena de Año Nuevo 31-12-2021
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])
print(recordatorios)