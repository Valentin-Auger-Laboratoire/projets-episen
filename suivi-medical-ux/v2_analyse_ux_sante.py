

import sys
import json
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLineEdit, QPushButton, QListWidget, 
                             QLabel, QMessageBox, QComboBox)
from PyQt6.QtCore import Qt

class AppSanteUX(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface de Suivi Médical - Analyse UX")
        self.resize(600, 700)
        
        # Style CSS pour l'UI (Répond à la Partie 1 : Couleurs et Typo)
        # Bleu pour la neutralité, Rouge pour les alertes [cite: 164, 170]
        self.setStyleSheet("""
            QMainWindow { background-color: #F5F7FA; }
            QLabel { font-size: 14px; font-family: 'Segoe UI', Arial; color: #2D3748; }
            QPushButton { padding: 8px; border-radius: 4px; font-weight: bold; }
            QPushButton#btn_ajout { background-color: #3182CE; color: white; }
            QPushButton#btn_termine { background-color: #38A169; color: white; }
            QPushButton#btn_suppr { background-color: #E53E3E; color: white; }
            QLineEdit { padding: 8px; border: 1px solid #CBD5E0; border-radius: 4px; }
            QListWidget { background: white; border-radius: 5px; font-size: 14px; }
        """)

        # Widget Central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout_principal = QVBoxLayout(self.central_widget)

        # 1. ZONE D'AJOUT (Prévention des erreurs)
        self.layout_principal.addWidget(QLabel("<b>Nouvelle action médicale :</b>"))
        layout_saisie = QHBoxLayout()
        self.champ_action = QLineEdit()
        self.champ_action.setPlaceholderText("Ex: Mesurer tension artérielle...")
        self.btn_ajouter = QPushButton("Ajouter")
        self.btn_ajouter.setObjectName("btn_ajout")
        self.btn_ajouter.clicked.connect(self.ajouter_action)
        layout_saisie.addWidget(self.champ_action)
        layout_saisie.addWidget(self.btn_ajouter)
        self.layout_principal.addLayout(layout_saisie)

        # 2. FILTRE (Organisation des données)
        self.layout_principal.addWidget(QLabel("<b>Filtre d'affichage :</b>"))
        self.combo_filtre = QComboBox()
        self.combo_filtre.addItems(["Toutes les actions", "À faire", "Terminées"])
        self.layout_principal.addWidget(self.combo_filtre)

        # 3. LISTE DES ACTIONS
        self.liste_actions = QListWidget()
        self.layout_principal.addWidget(self.liste_actions)

        # 4. BOUTONS D'INTERACTION (Actions critiques)
        layout_boutons = QHBoxLayout()
        
        self.btn_terminer = QPushButton("Marquer Terminée")
        self.btn_terminer.setObjectName("btn_termine")
        self.btn_terminer.clicked.connect(self.marquer_terminee)
        
        self.btn_supprimer = QPushButton("Supprimer l'action")
        self.btn_supprimer.setObjectName("btn_suppr")
        self.btn_supprimer.clicked.connect(self.supprimer_action)
        
        layout_boutons.addWidget(self.btn_terminer)
        layout_boutons.addWidget(self.btn_supprimer)
        self.layout_principal.addLayout(layout_boutons)

        # 5. SAUVEGARDE (Gestion des fichiers)
        layout_fichiers = QHBoxLayout()
        btn_save = QPushButton("💾 Sauvegarder (JSON)")
        btn_save.clicked.connect(self.sauvegarder_donnees)
        btn_load = QPushButton("📂 Charger")
        btn_load.clicked.connect(self.charger_donnees)
        layout_fichiers.addWidget(btn_save)
        layout_fichiers.addWidget(btn_load)
        self.layout_principal.addLayout(layout_fichiers)

        # Données internes
        self.donnees = []

    def ajouter_action(self):
        texte = self.champ_action.text().strip()
        if not texte:
            # Message d'erreur explicite
            QMessageBox.warning(self, "Erreur de saisie", "L'action ne peut pas être vide.")
            return
        
        self.donnees.append({"action": texte, "terminee": False})
        self.champ_action.clear()
        self.mettre_a_jour_affichage()

    def marquer_terminee(self):
        index = self.liste_actions.currentRow()
        if index >= 0:
            self.donnees[index]["terminee"] = True
            self.mettre_a_jour_affichage()
        else:
            # Feedback visuel si rien n'est sélectionné
            QMessageBox.information(self, "Info", "Veuillez sélectionner une action.")

    def supprimer_action(self):
        index = self.liste_actions.currentRow()
        if index >= 0:
            # Confirmation avant action critique
            reponse = QMessageBox.question(self, "Confirmation", 
                                         "Voulez-vous vraiment supprimer cette action ?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reponse == QMessageBox.StandardButton.Yes:
                self.donnees.pop(index)
                self.mettre_a_jour_affichage()

    def mettre_a_jour_affichage(self):
        self.liste_actions.clear()
        for item in self.donnees:
            prefixe = "[X] " if item["terminee"] else "( ) "
            self.liste_actions.addItem(prefixe + item["action"])

    def sauvegarder_donnees(self):
        try:
            with open("suivi_medical.json", "w") as f:
                json.dump(self.donnees, f)
            QMessageBox.information(self, "Succès", "Données sauvegardées en JSON.")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Échec de sauvegarde : {e}")

    def charger_donnees(self):
        try:
            with open("suivi_medical.json", "r") as f:
                self.donnees = json.load(f)
            self.mettre_a_jour_affichage()
        except FileNotFoundError:
            QMessageBox.warning(self, "Fichier introuvable", "Aucune sauvegarde trouvée.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = AppSanteUX()
    fenetre.show()
    sys.exit(app.exec())