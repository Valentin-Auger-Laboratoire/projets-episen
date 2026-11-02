

from model import Patient

class PatientPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Connexion des boutons aux méthodes
        self.view.btn_ajouter.clicked.connect(self.handle_add_patient)
        self.view.btn_supprimer.clicked.connect(self.handle_remove_patient)
        
        self.refresh_view()

    def handle_add_patient(self):
        # Récupère les données depuis la vue
        nom, age, motif = self.view.get_patient_input()

        # Logique de validation
        if not nom or not motif:
            self.view.set_message("Erreur : Nom et Motif requis", "red")
            return
        if age <= 0:
            self.view.set_message("Erreur : L'âge doit être > 0", "red")
            return

        # Mise à jour du modèle
        nouveau_patient = Patient(nom, age, motif)
        self.model.add_patient(nouveau_patient)
        
        self.view.clear_inputs()
        self.view.set_message(f"Patient {nom} ajouté !", "green")
        self.refresh_view() #

    def handle_remove_patient(self):
        index = self.view.get_selected_index()
        if index >= 0:
            self.model.remove_patient(index)
            self.refresh_view()
        else:
            self.view.set_message("Veuillez sélectionner un patient", "orange")

    def refresh_view(self):
        patients = self.model.get_all_patients()
        # Affichage : Nom - âge ans - motif
        display_list = [f"{p.nom} - {p.age} ans - {p.motif}" for p in patients]
        self.view.set_patients(display_list)