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

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Introdueix la latencia: "))
p_perduts=float(input("Introdueix el procentatge de paquets perduts: "))

if(latencia<0 and latencia>100):
    print("Latencia fora de rang")
elif latencia<= 30 and p_perduts<=1:
    print("La conexio es excelent")
elif latencia <= 80 and p_perduts<=3:
    print("Conexio bona")
elif latencia<= 150 and p_perduts<=5:
    print("Conexio acceptable")
else:
    print("Conexio deficient")



# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

pla=int(input("Introdueix el tipus de pla que tens, prem la tecla 1 per el basic o prem la tecla 0 per el plus: "))
c_mensual=float(input("Introdueix el teu consum mensual de gb: "))
preu_tot =0.0

if pla == 1 and c_mensual>0 :
    print("Has escollit el pla basic amb un cost de 10 euros i 10 gb, cada GB adicional costa 1.50 euros")
    if c_mensual>10 :
        preu_tot=10+c_mensual*1.50
        print(f"El preu total es de {preu_tot}")
    else:
        print(f"El preu total es de {preu_tot+10}euros")
        
    
elif pla ==0  and c_mensual>0:
    print("Has escollit el pla plus amb un cost de 20 euros i 10 GB, cada GB adicional costa 0.75 euros ")
    if c_mensual>30 :
        preu_tot=20+c_mensual*0.75
        print(f"El preu total es de {preu_tot}")
    else:
        print(f"El preu total es de {preu_tot+20}euros")

else :
    print("Pla desconegut o consum no valid")
    

# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.


# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

