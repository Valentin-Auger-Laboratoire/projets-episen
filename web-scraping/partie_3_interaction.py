

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Étape 1 : Ouvrir le navigateur
driver = webdriver.Chrome()
url = "https://fr.indeed.com/"

print(f"Ouverture de {url} pour tester les interactions...")
driver.get(url)

# Étape 3 : Attendre le chargement initial
time.sleep(3)

# Étape 4 : Interaction - Le Scroll (Spécifié dans le sujet Page 4)
print("Action : Scroll vers le bas de la page pour charger plus de contenu...")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# On attend pour voir l'effet du scroll
time.sleep(2)

# Étape 2 : Récupérer le HTML après interaction
html = driver.page_source
print(f"Capture du HTML rendu terminée ({len(html)} caractères).")

# Fermeture
driver.quit()
print("Test d'interaction terminé.")