

class Patient:
    def __init__(self, nom: str, age: int, motif: str):
        self.nom = nom
        self.age = age
        self.motif = motif

class PatientRepository:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def remove_patient(self, index: int):
        if 0 <= index < len(self.patients):
            del self.patients[index]

    def get_all_patients(self):
        return self.patients.copy()