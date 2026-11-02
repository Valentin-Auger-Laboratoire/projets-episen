

import csv
import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def extraire_jobs(url):
    """Fonction propre pour extraire les données (Partie 5)"""
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5) # Attente du JS
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    cards = soup.find_all('div', class_='job_seen_beacon')
    
    data_extracted = []
    
    for card in cards:
        # Extraction sécurisée (Partie 5 : Robustesse)
        try:
            titre = card.find('h2', class_='jobTitle').get_text(strip=True)
            # Indeed utilise des data-testid pour les entreprises/lieux
            entreprise = card.find('span', {'data-testid': 'company-name'}).get_text(strip=True)
            lieu = card.find('div', {'data-testid': 'text-location'}).get_text(strip=True)
            
            data_extracted.append({
                "intitulé": titre,
                "entreprise": entreprise,
                "localisation": lieu
            })
        except AttributeError:
            continue # Saute l'élément si une info manque
            
    driver.quit()
    return data_extracted

# --- Partie 6 : Export des données ---
url_cible = "https://fr.indeed.com/jobs?q=informatique&l=%C3%8Ele-de-France"
resultats = extraire_jobs(url_cible)

# Export JSON
with open("resultats.json", "w", encoding="utf-8") as f:
    json.dump(resultats, f, indent=4, ensure_ascii=False)

# Export CSV
if resultats:
    with open("resultats.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=resultats[0].keys())
        writer.writeheader()
        writer.writerows(resultats)

print(f"TP Terminé : {len(resultats)} offres exportées en JSON et CSV.")