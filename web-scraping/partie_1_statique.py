

import requests
from bs4 import BeautifulSoup

# Étape 1 : Récupération
# On choisit une page simple (ici Wikipedia)
url = "https://fr.wikipedia.org/wiki/Web_scraping"
headers = {"User-Agent": "Mozilla/5.0"}

print(f"Récupération de la page : {url}")
response = requests.get(url, headers=headers)

# Affichage du code HTML (Étape 1.2)
# print(response.text) 

# Étape 2 : Analyse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Étape 3 : Extraction
# On cherche les titres de section (h2) et leur contenu
sections = soup.find_all("h2")

# Étape 4 : Structuration
data = []
for s in sections:
    titre = s.get_text().replace('[modifier | modifier le code]', '').strip()
    if titre:
        data.append({
            "titre": titre,
            "info": "Section Wikipedia"
        })

# Affichage propre
print("\n--- DONNÉES EXTRAITES ---")
for item in data:
    print(f"Titre : {item['titre']}")