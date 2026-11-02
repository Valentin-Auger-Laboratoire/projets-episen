

from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Étape 1 : Ouvrir la page
driver = webdriver.Chrome() # Assure-toi d'avoir le driver installé
url = "https://fr.indeed.com/jobs?q=informatique&l=%C3%8Ele-de-France"

print(f"Ouverture du navigateur pour : {url}")
driver.get(url)

# Étape 3 : Attendre le chargement
print("Attente de 5 secondes pour le chargement du JavaScript...")
time.sleep(5) 

# Étape 2 : Récupérer le HTML rendu
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Extraction des données
# Note : Les classes CSS d'Indeed changent souvent, ceci est un exemple
offres = soup.find_all("h2", class_="jobTitle")

print("\n--- OFFRES TROUVÉES AVEC SELENIUM ---")
for index, offre in enumerate(offres[:10]): # On limite aux 10 premières
    print(f"{index+1}. {offre.get_text(strip=True)}")

# Fermeture
driver.quit()