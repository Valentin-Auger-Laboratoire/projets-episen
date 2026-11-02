# Salle d'attente : MVP et MVVM

## Français

**Ce que fait le projet :** une application de gestion des patients d'une salle d'attente (nom, âge, motif de visite), avec ajout, suppression et validation de la saisie. La même application est écrite avec deux architectures, pour les comparer :

- `mvp/` : **Model-View-Presenter**. La vue est passive : le `PatientPresenter` connecte les boutons, valide les données et met la vue à jour.
- `mvvm/` : **Model-View-ViewModel**. Le `PatientViewModel` émet des signaux Qt (`patients_changed`, `message_changed`) auxquels la vue s'abonne.

Le modèle (`Patient`, `PatientRepository`) est le même dans les deux versions.

**Technologies :** Python, PyQt6 (widgets, signaux/slots), patrons d'architecture MVP et MVVM.

**Lancer le projet :**
```bash
pip install -r requirements.txt
cd mvp
python main.py
```
Pour la version MVVM, lancer `python main.py` depuis le dossier `mvvm/`.

## English

**What it does:** an app to manage the patients in a waiting room (name, age, reason for visit), with add, remove and input validation. The same app is written with two architectures, to compare them:

- `mvp/`: **Model-View-Presenter**. The view is passive: `PatientPresenter` connects the buttons, validates the data and updates the view.
- `mvvm/`: **Model-View-ViewModel**. `PatientViewModel` emits Qt signals (`patients_changed`, `message_changed`) that the view subscribes to.

The model (`Patient`, `PatientRepository`) is the same in both versions.

**Technologies:** Python, PyQt6, MVP and MVVM patterns.

**How to run:**
```bash
pip install -r requirements.txt
cd mvp
python main.py
```
For the MVVM version, run `python main.py` from the `mvvm/` folder.
