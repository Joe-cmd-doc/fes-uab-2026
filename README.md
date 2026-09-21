# Fonaments d'Enginyeria de Software
Repositori per l'assignatura de FES de la UAB curs acadèmic 2026/2027

## Índex

1. Entendre com funciona un programa.
2. Representar problemes mitjançant algoritmes.
3. Utilitzar estructures de control per prendre decisions i repetir processos.
4. Organitzar el codi de manera estructurada i modular.
5. Comprendre la relació entre software i hardware.
6. Treballar amb dades i persistència.
7. Aplicar la programació a sistemes, xarxes i telecomunicacions.
8. Desenvolupar solucions cada vegada més completes.

## Contingut del repositori

En aquest repositori hi haurà principalment codi escrit en **Python**, que servirà
per comprendre millor els conceptes de l'assignatura de Fonaments d'Enginyeria de
Software mitjançant exemples pràctics.

### Exemple bàsic

El fitxer [`exemple.py`](exemple.py) conté un primer programa en Python que mostra
un missatge per pantalla amb la funció `print()`.

### Notebook de Jupyter

El fitxer [`explicacio_exemple.ipynb`](explicacio_exemple.ipynb) es pot obrir amb
Jupyter Notebook o amb VS Code i l'extensió de Jupyter. Inclou explicacions
pas a pas de cada línia de l'exemple i cel·les de Python que es poden executar.

### 01 - Conceptes bàsics de Python

La carpeta [`01_basic`](01_basic/) conté els primers exemples pràctics de
Python:

- [`01_print.py`](01_basic/01_print.py): mostrar informació per pantalla amb `print()`.
- [`02_types.py`](01_basic/02_types.py): conèixer els principals tipus de dades.
- [`03_cast.py`](01_basic/03_cast.py): convertir valors entre diferents tipus.
- [`04_variables.py`](01_basic/04_variables.py): crear i modificar variables, utilitzar f-strings i seguir convencions de noms.
- [`05_input.py`](01_basic/05_input.py): llegir dades de l'usuari amb `input()` i convertir-les a nombres.

També inclou [`exercicis-basics.py`](01_basic/exercicis-basics.py), amb vuit exercicis
per practicar aquests conceptes, i [`soluciones.py`](01_basic/soluciones.py),
amb una possible solució per a cadascun.

### Executar un fitxer Python des del terminal

1. Obre un terminal a la carpeta principal del repositori.
2. Comprova que Python està instal·lat:

	```powershell
	python --version
	```

	Si aquesta comanda no funciona a Windows, prova `py --version`.

3. Entra a la carpeta dels conceptes bàsics:

	```powershell
	cd 01_basic
	```

4. Executa el fitxer que vulguis. Per exemple:

	```powershell
	python 01_print.py
	```

5. Per executar un altre exemple, substitueix el nom del fitxer:

	```powershell
	python 02_types.py
	python 03_cast.py
	python 04_variables.py
	python 05_input.py
	```

	El fitxer `05_input.py` demana dades per teclat. Escriu la resposta i prem
	`Enter`.

6. Per tornar a la carpeta principal del repositori, executa:

	```powershell
	cd ..
	```

