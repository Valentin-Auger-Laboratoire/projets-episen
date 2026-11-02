

import sys
from PyQt6.QtWidgets import QApplication
from model import PatientRepository
from view import PatientView
from presenter import PatientPresenter

def main():
    app = QApplication(sys.argv)

    # Instanciation des composants
    model = PatientRepository()
    view = PatientView()
    
    # Le Presenter fait le lien entre les deux
    presenter = PatientPresenter(model, view)

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()