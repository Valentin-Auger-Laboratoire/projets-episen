from model import Patient
from utils import load_data


def build_patients(data: list) -> list:
    """
    Transforme une liste de dictionnaires en liste d'objets Patient.

    Paramètre :
        data (list) : liste de dictionnaires

    Retour :
        list : liste d'objets Patient
    """
    patients = []

    # Transformation dictionnaires → objets Patient
    for d in data:
        p = Patient(**d)

        # Mise à jour automatique du statut
        p.status = "ALERT" if p.is_critical() else "OK"

        patients.append(p)

    return patients


def analyze(filepath: str):
    """
    Fonction principale de traitement :
    - lit les données
    - crée des objets Patient
    - détecte les patients critiques

    Retour :
        tuple : (tous les patients, patients critiques)
    """
    patients = build_patients(load_data(filepath))

    # Filtrage des patients critiques
    critical_patients = [p for p in patients if p.is_critical()]

    return patients, critical_patients


def get_critical_patients(filepath: str) -> list:
    """
    Charge les données depuis le fichier, construit les objets Patient
    puis retourne uniquement les patients critiques.

    Paramètre :
        filepath (str) : chemin vers le fichier de données

    Retour :
        list : liste d'objets Patient critiques
    """
    return analyze(filepath)[1]
