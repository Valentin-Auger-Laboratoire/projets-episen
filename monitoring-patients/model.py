class Patient:
    """
    Représente un patient supervisé par le système de monitoring.
    """

    def __init__(self, patient_id: int, name: str, heart_rate: int,
                 temperature: float, status: str):
        # Initialisation des attributs
        self.patient_id = patient_id
        self.name = name
        self.heart_rate = heart_rate
        self.temperature = temperature
        self.status = status

    def is_critical(self) -> bool:
        """
        Détermine si le patient est en situation critique.

        Un patient est considéré comme critique si :
        - sa fréquence cardiaque est strictement supérieure à 100
        ou
        - sa température est strictement supérieure à 38.5
        """
        return self.heart_rate > 100 or self.temperature > 38.5

    def __str__(self) -> str:
        """
        Représentation textuelle lisible d'un patient.
        Exemple :
        Patient 5678 - Smith | HR: 120 bpm | TEMP: 39.1 °C | STATUS: ALERT
        """
        return (f"Patient {self.patient_id} - {self.name} | "
                f"HR: {self.heart_rate} bpm | "
                f"TEMP: {self.temperature} °C | "
                f"STATUS: {self.status}")
