import sys
from PyQt5.QtWidgets import QApplication
from view import MainWindow


def main():
    """
    Point d'entrée principal de l'application.
    """
    # Création de l'application
    app = QApplication(sys.argv)

    # Création de la fenêtre principale
    window = MainWindow()
    window.show()

    # Boucle principale
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
