

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, 
                             QSpinBox, QPushButton, QListWidget, QLabel)

class PatientView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Salle d'Attente - MVP")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Formulaire de saisie
        self.input_nom = QLineEdit()
        self.input_nom.setPlaceholderText("Nom du patient")
        
        self.input_age = QSpinBox()
        self.input_age.setRange(0, 150)
        
        self.input_motif = QLineEdit()
        self.input_motif.setPlaceholderText("Motif de visite")

        layout.addWidget(QLabel("Nom:"))
        layout.addWidget(self.input_nom)
        layout.addWidget(QLabel("Âge:"))
        layout.addWidget(self.input_age)
        layout.addWidget(QLabel("Motif:"))
        layout.addWidget(self.input_motif)

        # Boutons
        self.btn_ajouter = QPushButton("Ajouter Patient")
        self.btn_supprimer = QPushButton("Supprimer Sélection")
        layout.addWidget(self.btn_ajouter)
        layout.addWidget(self.btn_supprimer)

        # Liste et messages
        self.liste_patients = QListWidget()
        self.label_message = QLabel("")
        layout.addWidget(self.liste_patients)
        layout.addWidget(self.label_message)

        self.setLayout(layout)

    # Méthodes exposées au Presenter
    def get_patient_input(self):
        return self.input_nom.text(), self.input_age.value(), self.input_motif.text()

    def clear_inputs(self):
        self.input_nom.clear()
        self.input_age.setValue(0)
        self.input_motif.clear()

    def set_patients(self, items):
        self.liste_patients.clear()
        self.liste_patients.addItems(items)

    def set_message(self, msg, color="black"):
        self.label_message.setText(msg)
        self.label_message.setStyleSheet(f"color: {color};")

    def get_selected_index(self):
        return self.liste_patients.currentRow()