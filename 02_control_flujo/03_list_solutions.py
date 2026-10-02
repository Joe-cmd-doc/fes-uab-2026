###
# SOLUCIONS
###

# Exercici 1: El missatge secret
# Donada la llista següent:
# missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
# Fent servir slicing i concatenació, crea una llista nova que contingui només
# el missatge "secret".
print("\nExercici 1:")
mensaje = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
secreto = mensaje[5:]
print(secreto)

# Exercici 2: Intercanvi de posicions
# Donada la llista següent:
# numeros = [10, 20, 30, 40, 50]
# Intercanvia la primera i l'última posició fent servir només l'assignació per índex.
print("\nExercici 2:")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercanvi en una sola línia.
print(numeros)

# Exercici 3: L'entrepà de llistes
# Donades les llistes següents:
# pa_de_dalt = ["pa de dalt"]
# ingredients = ["pernil", "formatge", "tomàquet"]
# pa_de_sota = ["pa de sota"]
# Crea una llista anomenada entrepa que contingui, en aquest ordre, el pa de dalt,
# els ingredients i el pa de sota.
print("\nExercici 3:")
pa_de_dalt = ["pa de dalt"]
ingredients = ["pernil", "formatge", "tomàquet"]
pa_de_sota = ["pa de sota"]
entrepa = pa_de_dalt + ingredients + pa_de_sota
print(entrepa)

# Exercici 4: Duplicar una llista
# Donada una llista:
# lista = [1, 2, 3]
# Crea una llista nova que contingui duplicats els elements de la llista original.
# Exemple: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nExercici 4:")
lista = [1, 2, 3]
lista_duplicada = lista + lista
print(lista_duplicada)

# Exercici 5: Extreure l'element central
# Donada una llista amb un nombre senar d'elements, extreu-ne l'element central
# fent servir slicing.
# Exemple: llista = [10, 20, 30, 40, 50] -> L'element central és 30
print("\nExercici 5:")
lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])

# Exercici 6: Inversió parcial
# Donada una llista, inverteix-ne només la primera meitat (fent servir slicing
# i concatenació).
# Exemple: llista = [1, 2, 3, 4, 5, 6] -> Resultat: [3, 2, 1, 4, 5, 6]
print("\nExercici 6:")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)