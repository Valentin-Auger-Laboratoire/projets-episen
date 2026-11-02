

import sys
from PyQt6.QtWidgets import QApplication
from model import PatientRepository
from viewmodel import PatientViewModel
from view import PatientView

def main():
    app = QApplication(sys.argv)
    
    model = PatientRepository()
    view_model = PatientViewModel(model)
    view = PatientView(view_model)
    
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()