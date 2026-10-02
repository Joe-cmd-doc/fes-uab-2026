###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

rssi = float(input("Quin és el nivell de senyal rebut en dBm? "))
if rssi >= -50:
    print("La cobertura és excel·lent")
elif rssi >= -67:
    print("La cobertura és bona")
elif rssi >= -75:
    print("La cobertura és feble")
else:
    print("La cobertura és molt feble")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

power = float(input("Quin és la potència òptica rebuda en dBm? "))
if power >= -27 and power <= -8:
    print("El nivell és acceptable")
elif power < -27:
    print("El nivell és massa baix")
else:
    print("El nivell és massa alt")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = float(input("Quin és el consum de dades en GB? "))
if consum <= 20:
    print("El consum és dins del límit")
else:
    print(f"El consum és de {consum - 20} GB addicionals")
    
# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("Quin és l'indicador LOS del terminal òptic? ")
internet = input("Quin és l'indicador d'Internet del router? ")
if los == "encès" and internet == "encès":
    print("La connexió sembla funcionar correctament")
elif los == "encès" and internet == "apagat":
    print("Cal revisar el cable de fibra")
elif los == "apagat" and internet == "encès":
    print("Cal comprovar el servei del proveïdor")
else:
    print("La connexió sembla funcionar correctament")
    
# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

battery = float(input("Quin és el percentatge de bateria disponible al SAI? "))
if battery >= 0 and battery <= 100:
    if battery < 20:
        print("El nivell és crític")
    elif battery >= 20 and battery <= 49:
        print("El nivell és baix")
    else:
        print("El nivell és suficient")
else:
    print("El valor és fora del rang del 0 % al 100 %")

