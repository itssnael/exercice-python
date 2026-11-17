# Étape 4 : Importation des packages[cite: 12]
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Étape 3 : Lien de l'API XML du site www.infoclimat.fr[cite: 12]
url = "http://www.infoclimat.fr/public-api/gfs/xml?_ll=48.85341,2.3488&_auth=UUsDFFQqXX9TflNkUyUGL1c%2FAzYOeAUiBHhVNg9qXiMDaFMyUjJcOlc5VyoEKwo8Un8FZgA7ADBXPAF5CXsHZlE7A29UP106UzxTNlN8Bi1XeQNiDi4FIgRjVTQPfF48A2lTNFIvXD5XJlc3BDYKOlJ%2BBXoAPgA%2FVz0BYgltB2ZRNwNmVDNdPFMjUy5TZQZjVzIDMA43BT8EYlU1D2BebwM1U2NSNVw8VyZXNwQxCjhSZwViADYAOVc3AXkJewcdUUEDelR3XX1TaVN3U34GZ1c6Azc%3D&_c=d10bc23ad3e113e78e4553a10915cc6c"

# Exécution de la requête HTTP GET et lecture du texte brut[cite: 9, 10]
reponse = requests.get(url)
contenu_txt = reponse.text

# Lecture du contenu XML avec BeautifulSoup[cite: 12]
soup = BeautifulSoup(contenu_txt, "xml")

# Étape 7 : Demander à l'utilisateur de saisir la durée prévisionnelle[cite: 12]
saisie = input("Saisissez une durée prévisionnelle (3, 6, 9..., 192) pour la ville de Paris: ")
duree_heures = int(saisie)

# Étape 8 : Calcul de l'heure cible en ajoutant la durée à l'heure actuelle[cite: 12]
heure_actuelle = datetime.now()
duree = timedelta(hours=duree_heures)
heure_cible = heure_actuelle + duree

# Recherche de la balise <echeance> correspondant à la durée saisie
echeance_cible = soup.find("echeance", hour=str(duree_heures))

# Étape 5 : Récupération de la température prévisionnelle à "2m"[cite: 12]
balise_temp = echeance_cible.find("temperature").find("level", val="2m")
temp_kelvin = float(balise_temp.text)

# Les températures sont indiquées en degré Kelvin dans l'API, on convertit en Celsius[cite: 12]
temp_celsius = round(temp_kelvin - 273.15)

# Étape 8 : Affichage du résultat final selon l'heure de consultation avec le style demandé[cite: 12]
print(f"La température prévisionnelle de Paris à {heure_cible.hour}h sera de {temp_celsius}° Celsius.")