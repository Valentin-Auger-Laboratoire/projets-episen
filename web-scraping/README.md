# TP Web scraping

## Français

**Ce que fait le projet :** un TP en 6 parties sur l'extraction de données sur le web.

| Fichier | Contenu |
|---|---|
| `partie_1_statique.py` | Récupère les titres de section d'une page Wikipedia (requests + BeautifulSoup) |
| `partie_2_limites.py` | Montre qu'une requête classique ne récupère aucune offre sur Indeed, car le contenu est chargé en JavaScript |
| `partie_3_interaction.py` | Ouvre Chrome avec Selenium, fait défiler la page et récupère le HTML rendu |
| `partie_4_selenium.py` | Extrait les 10 premiers intitulés d'offres d'emploi depuis la page rendue |
| `partie_5_6_export.py` | Extrait l'intitulé, l'entreprise et le lieu de chaque offre (en ignorant les fiches incomplètes), puis exporte en `resultats.json` et `resultats.csv` |

**Technologies :** Python, requests, BeautifulSoup4, Selenium (Chrome), csv, json.

**Lancer le projet :**
```bash
pip install -r requirements.txt
python partie_1_statique.py
```
Les parties 3 à 6 nécessitent Google Chrome (Selenium 4 télécharge le pilote automatiquement). Les sélecteurs CSS d'Indeed changent souvent et le site peut bloquer les robots, donc il est possible qu'aucun résultat ne soit récupéré.

## English

**What it does:** a 6-part lab on extracting data from the web:
1. scraping a static page (Wikipedia);
2. showing the limits of plain requests on a JavaScript site (Indeed);
3. to 4. automating a browser with Selenium;
5. to 6. robust extraction, then export to JSON and CSV.

**Technologies:** Python, requests, BeautifulSoup4, Selenium (Chrome), csv, json.

**How to run:**
```bash
pip install -r requirements.txt
python partie_1_statique.py
```
Parts 3 to 6 need Google Chrome. Indeed's CSS selectors change often and the site may block bots, so you may get no results.
