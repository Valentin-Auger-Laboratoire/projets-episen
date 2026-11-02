import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QTextEdit, QMessageBox
)

from controller import analyze


class MainWindow(QWidget):
    """
    Fenêtre principale de l'application de monitoring.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Système de monitoring de patients")
        self.resize(700, 500)

        # Chemin du fichier de données, relatif au dossier du projet
        self.data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "data", "patients.txt")

        self.setup_ui()

    def setup_ui(self):
        """
        Initialise les composants graphiques.
        """
        self.layout = QVBoxLayout()

        self.title_label = QLabel("Analyse des patients critiques")
        self.info_label = QLabel(
            "Cliquer sur le bouton ci-dessous pour analyser les données du fichier."
        )

        self.analyze_button = QPushButton("Analyser")
        self.analyze_button.clicked.connect(self.analyze_patients)

        self.result_label = QLabel("Résultats :")
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        self.counter_label = QLabel("Nombre de patients critiques : 0")

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.info_label)
        self.layout.addWidget(self.analyze_button)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.result_area)
        self.layout.addWidget(self.counter_label)

        self.setLayout(self.layout)

    def analyze_patients(self):
        """
        Lance l'analyse des patients et affiche les résultats.
        """
        self.result_area.clear()

        try:
            # Appel du controller
            patients, critical = analyze(self.data_file)
        # Gestion des erreurs (ex : fichier absent, ligne mal formée)
        except Exception as e:
            self.counter_label.setText("Nombre de patients critiques : 0")
            QMessageBox.critical(self, "Erreur", str(e))
            return

        # Affichage de tous les patients
        output = "Tous les patients :\n"
        output += "\n".join(str(p) for p in patients)

        # Liste des patients critiques
        output += "\n\nPatients critiques :\n"
        if critical:
            output += "\n".join(str(p) for p in critical)
        else:
            output += "Aucun patient critique détecté."

        self.result_area.setText(output)
        self.counter_label.setText(f"Nombre de patients critiques : {len(critical)}")
