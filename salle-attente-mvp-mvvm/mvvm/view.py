

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QSpinBox, 
                             QPushButton, QListWidget, QLabel)

class PatientView(QWidget):
    def __init__(self, view_model):
        super().__init__()
        self.vm = view_model
        self.setWindowTitle("Gestion Salle d'Attente - MVVM")
        self.setup_ui()
        self.bind_view_model()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.input_nom = QLineEdit()
        self.input_age = QSpinBox()
        self.input_age.setRange(0, 150)
        self.input_motif = QLineEdit()
        
        self.btn_ajouter = QPushButton("Ajouter")
        self.btn_supprimer = QPushButton("Supprimer")
        self.liste_patients = QListWidget()
        self.label_msg = QLabel("")

        layout.addWidget(QLabel("Nom:"))
        layout.addWidget(self.input_nom)
        layout.addWidget(self.input_age)
        layout.addWidget(self.input_motif)
        layout.addWidget(self.btn_ajouter)
        layout.addWidget(self.btn_supprimer)
        layout.addWidget(self.liste_patients)
        layout.addWidget(self.label_msg)
        self.setLayout(layout)

    def bind_view_model(self):
        # 1. La vue envoie des ordres au ViewModel
        self.btn_ajouter.clicked.connect(lambda: self.vm.add_patient(
            self.input_nom.text(), self.input_age.value(), self.input_motif.text()
        ))
        self.btn_supprimer.clicked.connect(lambda: self.vm.remove_patient(
            self.liste_patients.currentRow()
        ))

        # 2. La vue réagit aux notifications du ViewModel (Signaux)
        self.vm.patients_changed.connect(self.update_list)
        self.vm.message_changed.connect(self.update_message)

    def update_list(self, items):
        self.liste_patients.clear()
        self.liste_patients.addItems(items)
        self.input_nom.clear()
        self.input_motif.clear()

    def update_message(self, text, color):
        self.label_msg.setText(text)
        self.label_msg.setStyleSheet(f"color: {color};")