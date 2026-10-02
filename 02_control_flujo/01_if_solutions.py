###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
print("\nExercici 1:")
num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))

if num1 > num2:
    print(f"{num1} és més gran que {num2}")
elif num2 > num1:
    print(f"{num2} és més gran que {num1}")
else:
    print("Els nombres són iguals")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
print("\nExercici 2:")
num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))
operacion = input("Introdueix l'operació (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        print("Error: no es pot dividir per zero.")
    else:
        resultado = num1 / num2
else:
    print("Operació no vàlida.")

if 'resultado' in locals(): # Comprova si existeix la variable resultado.
    print(f"El resultat és: {resultado}")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
print("\nExercici 3:")
anio = int(input("Introdueix un any: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} és un any de traspàs.")
else:
    print(f"{anio} no és un any de traspàs.")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
print("\nExercici 4:")
edad = int(input("Introdueix una edat: "))

if 0 <= edad <= 2:
    print("Nadó")
elif 3 <= edad <= 12:
    print("Infant")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adult")
elif edad >= 65:
    print("Persona gran")
else:
    print("Edat no vàlida.")