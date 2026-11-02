# Suivi médical et analyse UX/UI en santé

## Français

**Ce que fait le projet :** une application de bureau pour suivre les actions médicales d'un patient : ajouter une action, la marquer comme terminée, la supprimer, sauvegarder et charger la liste en JSON.

- `v1_suivi_actions_medicales.py` : la version de base.
- `v2_analyse_ux_sante.py` : la version retravaillée selon les principes UX/UI en santé :
  - code couleur (bleu pour les actions neutres, vert pour « terminée », rouge pour « supprimer ») ;
  - saisie vide refusée, message si aucune action n'est sélectionnée ;
  - **confirmation avant la suppression** ;
  - message de retour après la sauvegarde.

  Le filtre « À faire / Terminées » est présent dans l'interface mais n'est pas encore relié à la liste.

**Technologies :** Python, PyQt6 (QMainWindow, QListWidget, QComboBox, QMessageBox, feuilles de style Qt), JSON.

**Lancer le projet :**
```bash
pip install -r requirements.txt
python v1_suivi_actions_medicales.py
python v2_analyse_ux_sante.py
```
Les fichiers de sauvegarde (`actions.json`, `suivi_medical.json`) sont créés dans le dossier courant.

## English

**What it does:** a desktop app to track a patient's medical tasks: add a task, mark it as done, delete it, save and load the list as JSON.

- `v1_suivi_actions_medicales.py`: the basic version.
- `v2_analyse_ux_sante.py`: the version redesigned with healthcare UX/UI principles:
  - colour coding (blue for neutral actions, green for "done", red for "delete");
  - empty input rejected, message when no task is selected;
  - **confirmation before deleting**;
  - feedback message after saving.

  The "To do / Done" filter is in the interface but not yet connected to the list.

**Technologies:** Python, PyQt6, JSON.

**How to run:**
```bash
pip install -r requirements.txt
python v1_suivi_actions_medicales.py
python v2_analyse_ux_sante.py
```
Save files are written to the current directory.
