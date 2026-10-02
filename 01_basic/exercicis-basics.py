###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
nom = "Marc"
ciutat = "Badalona"
print(f"El meu nom és {nom} i visc a {ciutat}")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
numero = "12345"
numero_enter = int(numero)
numero_float = float(numero)
print(f"El número enter és: {numero_enter}")
print(f"El número float és: {numero_float}")
numero_float = 3.99
numero_enter = int(numero_float)
print(f"El número enter és: {numero_enter}")

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí
name = "Joel"
age = 21
height = 1.74
print(f"Hola! Em dic {name}, tinc {age} anys i faig {height} metres")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

pi = 3.14159
rounded_pi = round(pi)
division_result = rounded_pi // 2
print(f"El resultat de la divisió entera entre {rounded_pi} i 2 és: {division_result}")

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí
celsius = float(input("Quina és la temperatura en graus Celsius? "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} graus Celsius equivalen a {fahrenheit} graus Fahrenheit")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
total = float(input("Quin és el total del compte? "))
percentage = float(input("Quin és el percentatge de propina? "))
tip = total * (percentage / 100)
total_final = total + tip
print(f"La propina és: {tip:.2f}€")
print(f"El total final que s'ha de pagar és: {total_final:.2f}€")
print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí
password = input("Quina és la teva contrasenya? ")
if len(password) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")