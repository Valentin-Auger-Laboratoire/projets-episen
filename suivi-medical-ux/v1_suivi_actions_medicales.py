

import sys, json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QComboBox

class SuiviMedical(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Suivi des actions patients")
        layout = QVBoxLayout(self)

        # Zone d'ajout
        self.saisie = QLineEdit()
        btn_ajout = QPushButton("Ajouter")
        btn_ajout.clicked.connect(self.ajouter)
        layout.addWidget(self.saisie)
        layout.addWidget(btn_ajout)

        # Liste des actions
        self.liste = QListWidget()
        layout.addWidget(self.liste)

        # Boutons d'action
        self.btn_termine = QPushButton("Marquer comme terminée")
        self.btn_termine.clicked.connect(self.terminer)
        self.btn_supprimer = QPushButton("Supprimer l'action")
        self.btn_supprimer.clicked.connect(self.supprimer)
        layout.addWidget(self.btn_termine)
        layout.addWidget(self.btn_supprimer)

        # Gestion des fichiers
        fichiers_layout = QHBoxLayout()
        btn_save = QPushButton("Sauvegarder")
        btn_save.clicked.connect(self.sauvegarder)
        btn_load = QPushButton("Charger")
        btn_load.clicked.connect(self.charger)
        fichiers_layout.addWidget(btn_save)
        fichiers_layout.addWidget(btn_load)
        layout.addLayout(fichiers_layout)

    def ajouter(self):
        if self.saisie.text(): # Empêcher ajout vide
            self.liste.addItem(f"( ) {self.saisie.text()}")
            self.saisie.clear()

    def terminer(self):
        item = self.liste.currentItem()
        if item: # Vérifier sélection
            item.setText(item.text().replace("( )", "[X]")) # Marquer comme terminée

    def supprimer(self):
        item = self.liste.currentItem()
        if item: self.liste.takeItem(self.liste.row(item)) # Supprimer action 

    def sauvegarder(self):
        data = [self.liste.item(i).text() for i in range(self.liste.count())]
        with open('actions.json', 'w') as f:
            json.dump(data, f) # Sauvegarde JSON 

    def charger(self):
        try:
            with open('actions.json', 'r') as f:
                data = json.load(f)
                self.liste.clear()
                self.liste.addItems(data)
        except: pass

app = QApplication(sys.argv)
win = SuiviMedical()
win.show()
sys.exit(app.exec())