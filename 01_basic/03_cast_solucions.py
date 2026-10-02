###
# Solucions - conversió de tipus (casting)
###

# Exercici 1
# Demana quants paquets ha rebut un encaminador, converteix la resposta a enter
# i suma-hi 1200 paquets.
paquets_rebuts = int(input("Quants paquets ha rebut l'encaminador? "))
total_paquets = paquets_rebuts + 1200
print(f"Total de paquets: {total_paquets}")

# Exercici 2
# Converteix la velocitat introduïda a Mbps a MB/s.
velocitat_mbps = float(input("Velocitat de la connexió en Mbps: "))
velocitat_mbs = velocitat_mbps / 8
print(f"Velocitat equivalent: {velocitat_mbs:.2f} MB/s")