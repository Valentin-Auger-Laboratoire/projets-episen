import re


class InvalidPatientDataError(Exception):
    """
    Exception levée lorsqu'une ligne du fichier patient
    ne respecte pas le format attendu.
    """
    pass


# Expression régulière pour capturer chaque champ d'une ligne
PATTERN = re.compile(
    r"ID:(?P<patient_id>\d+);NAME:(?P<name>[^;]+);HR:(?P<heart_rate>\d+);"
    r"TEMP:(?P<temperature>\d+(?:\.\d+)?);STATUS:(?P<status>\w+)"
)


def parse_line(line: str) -> dict:
    """
    Analyse une ligne du fichier patients et retourne un dictionnaire
    contenant les informations extraites.

    Format attendu :
    ID:1234;NAME:Doe;HR:85;TEMP:37.2;STATUS:OK

    Paramètre :
        line (str) : ligne à analyser

    Retour :
        dict : dictionnaire contenant les champs extraits

    Exceptions :
        InvalidPatientDataError : si la ligne est mal formée
    """
    line = line.strip()
    match = PATTERN.fullmatch(line)

    # Si la ligne ne correspond pas au format attendu → erreur
    if not match:
        raise InvalidPatientDataError(f"Ligne mal formée : {line}")

    # Construction du dictionnaire avec conversion des types
    data = match.groupdict()
    return {
        "patient_id": int(data["patient_id"]),     # ID : entier
        "name": data["name"],                      # nom : string
        "heart_rate": int(data["heart_rate"]),     # fréquence cardiaque : entier
        "temperature": float(data["temperature"]), # température : float
        "status": data["status"],                  # statut : string
    }


def load_data(filepath: str) -> list:
    """
    Charge les données du fichier et retourne une liste de dictionnaires.

    Paramètre :
        filepath (str) : chemin vers le fichier de données

    Retour :
        list : liste de dictionnaires représentant les patients

    Exceptions :
        FileNotFoundError : si le fichier n'existe pas
        InvalidPatientDataError : si une ligne est mal formée
    """
    patients_data = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for number, line in enumerate(f, start=1):
                # On ignore les lignes vides
                if not line.strip():
                    continue
                try:
                    patients_data.append(parse_line(line))
                except InvalidPatientDataError as e:
                    raise InvalidPatientDataError(f"Ligne {number} : {e}") from e
    except FileNotFoundError:
        raise FileNotFoundError(f"Fichier introuvable : {filepath}")

    return patients_data
