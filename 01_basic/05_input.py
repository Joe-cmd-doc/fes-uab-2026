###
# 05 - Entrada de dades de l'usuari (input()) - versió simplificada
# La funció input() permet obtenir dades de l'usuari a través de la consola.
###

# import os
# os.system("cls") #deprecated fer una actualització*

# Per obtenir dades de l'usuari, es fa servir la funció input()
# La funció input() rep un missatge que es mostra a l'usuari
# i retorna el valor que aquest introdueix
# nom = input("Hola, com et dius?\n")
# print(f"Hola {nom}, encantat de conèixer-te")
# print("Hola " + nom + ", encantat de conèixer-te")

# Tingues en compte que la funció input() retorna una cadena de text
# Per obtenir un nombre, cal convertir aquesta cadena a un tipus numèric
# edat = input("Quants anys tens?\n")

# print(f"D'aquí a 3 anys tindràs {int(edat) + 3} anys")  # Això no funcionarà com esperem
# edat = int(edat)
# print(f"Tens {edat} anys")

# La funció input() també pot retornar diversos valors
# Per fer-ho, l'usuari els ha de separar amb un espai
print("Obtenir diversos valors alhora")
pais, ciutat = input("A quin país i a quina ciutat vius?\n").split()

# print(f"Vius a {ciutat}, {pais}")
print(f"Vius a {ciutat}, {pais}")