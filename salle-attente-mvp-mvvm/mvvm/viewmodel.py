

from PyQt6.QtCore import QObject, pyqtSignal
from model import Patient

class PatientViewModel(QObject):
    # Signaux pour notifier la vue des changements
    patients_changed = pyqtSignal(list)
    message_changed = pyqtSignal(str, str) # message, couleur

    def __init__(self, repository):
        super().__init__()
        self.repository = repository

    def add_patient(self, nom, age, motif):
        # Validation
        if not nom or not motif:
            self.message_changed.emit("Erreur : Champs vides", "red")
            return
        if age <= 0:
            self.message_changed.emit("Erreur : Âge invalide", "red")
            return

        # Mise à jour du modèle
        nouveau_patient = Patient(nom, age, motif)
        self.repository.add_patient(nouveau_patient)
        
        # Notification de succès et mise à jour de la liste
        self.message_changed.emit(f"Patient {nom} ajouté !", "green")
        self.refresh()

    def remove_patient(self, index):
        if index >= 0:
            self.repository.remove_patient(index)
            self.refresh()
        else:
            self.message_changed.emit("Sélectionnez un patient", "orange")

    def refresh(self):
        # On prépare les chaînes de caractères pour la vue
        patients = self.repository.get_all_patients()
        display_list = [f"{p.nom} - {p.age} ans - {p.motif}" for p in patients]
        self.patients_changed.emit(display_list)