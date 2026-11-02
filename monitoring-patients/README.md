# Système de monitoring de patients

## Français

**Ce que fait le projet :** l'application lit le fichier `data/patients.txt` (format `ID:1234;NAME:Doe;HR:85;TEMP:37.2;STATUS:OK`) et crée un objet `Patient` par ligne. Elle met à jour le statut de chaque patient, puis affiche les patients critiques (fréquence cardiaque > 100 bpm ou température > 38,5 °C) et leur nombre. Si une ligne est mal formée ou si le fichier est absent, une boîte d'erreur s'affiche.

Organisation MVC :
- `model.py` : classe `Patient` ;
- `utils.py` : lecture du fichier avec une expression régulière, exception `InvalidPatientDataError` ;
- `controller.py` : traitement des données ;
- `view.py` : interface graphique ;
- `main.py` : point d'entrée.

**Technologies :** Python, PyQt5, module `re`, exceptions personnalisées, architecture MVC.

**Lancer le projet :**
```bash
pip install -r requirements.txt
python main.py
```
Cliquer ensuite sur « Analyser ».

## English

**What it does:** the app reads `data/patients.txt` and creates one `Patient` object per line. It updates each patient's status, then shows the critical patients (heart rate > 100 bpm or temperature > 38.5 °C) and how many there are. If a line is malformed or the file is missing, an error dialog appears.

MVC layout: `model.py` (`Patient` class), `utils.py` (file parsing with a regular expression, custom exception), `controller.py` (data processing), `view.py` (interface), `main.py` (entry point).

**Technologies:** Python, PyQt5, `re` module, custom exceptions, MVC architecture.

**How to run:**
```bash
pip install -r requirements.txt
python main.py
```
Then click "Analyser".
