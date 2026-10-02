###
# Solucions - variables
###

# Exercici 1
# Desa i mostra les dades d'un encaminador amb una f-string.
nom_encaminador = "Router oficina"
ubicacio = "Planta baixa"
nombre_ports = 8
encaminador_engegat = True

print(
    f"Encaminador: {nom_encaminador}; ubicació: {ubicacio}; "
    f"ports: {nombre_ports}; engegat: {encaminador_engegat}"
)

# Exercici 2
# Calcula les dades que queden i actualitza el càlcul amb un consum nou.
dades_incloses_gb = 20
dades_consumides_gb = 12.5
dades_restants_gb = dades_incloses_gb - dades_consumides_gb
print(f"Dades restants: {dades_restants_gb} GB")

dades_consumides_gb = 18
dades_restants_gb = dades_incloses_gb - dades_consumides_gb
print(f"Dades restants després de l'actualització: {dades_restants_gb} GB")