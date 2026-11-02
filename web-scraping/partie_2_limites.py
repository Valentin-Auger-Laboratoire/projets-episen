

import requests
from bs4 import BeautifulSoup

# On teste sur Indeed comme suggéré dans le TP (Site dynamique)
url = "https://fr.indeed.com/jobs?q=informatique&l=%C3%8Ele-de-France"
headers = {"User-Agent": "Mozilla/5.0"}

print(f"Tentative de scraping classique sur : {url}")
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# On cherche les cartes d'emploi (normalement class 'job_seen_beacon')
jobs = soup.find_all("div", class_="job_seen_beacon")

print(f"\nNombre d'offres trouvées avec requests : {len(jobs)}")
if len(jobs) == 0:
    print("ÉCHEC : Aucune donnée n'a été récupérée. Le contenu est probablement chargé par JavaScript.")