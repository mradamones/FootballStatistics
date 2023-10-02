import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedWidget, QHBoxLayout
from main_menu_panel import MainMenuPanel
from goalkeepers_panel import GoalkeepersPanel
from field_players_panel import FieldPlayersPanel
from compare_panel import ComparePanel
from utils import get_data as gd
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('FootballStatistics')
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        button_layout = QHBoxLayout()

        main_menu_button = QPushButton('Main Menu', self)
        main_menu_button.clicked.connect(self.show_main_menu)
        button_layout.addWidget(main_menu_button)

        goalkeepers_button = QPushButton('Goalkeepers', self)
        goalkeepers_button.clicked.connect(self.show_goalkeepers)
        button_layout.addWidget(goalkeepers_button)

        field_players_button = QPushButton('Field Players', self)
        field_players_button.clicked.connect(self.show_field_players)
        button_layout.addWidget(field_players_button)

        compare_button = QPushButton('Compare', self)
        compare_button.clicked.connect(self.show_compare_panel)
        button_layout.addWidget(compare_button)

        layout.addLayout(button_layout)

        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        # Wczytaj dane i przekaż je do paneli
        goalkeepers_data = gd.get_gks()
        time.sleep(1)  # Opóźnienie 1 sekundy
        defenders_data = gd.get_def()
        time.sleep(1)  # Opóźnienie 1 sekundy
        midfielders_data = gd.get_mids()
        time.sleep(1)  # Opóźnienie 1 sekundy
        forwards_data = gd.get_fwds()
        # TODO - użyć pickle do zapisania dataframeów i żeby ładowało z pliku, a w programie w menu kontekstowym dać pobierz najnowsze i nadpisać pliki pickle

        self.main_menu_panel = MainMenuPanel()
        self.stacked_widget.addWidget(self.main_menu_panel)

        self.goalkeepers_panel = GoalkeepersPanel(goalkeepers_data)
        self.stacked_widget.addWidget(self.goalkeepers_panel)

        self.field_players_panel = FieldPlayersPanel(defenders_data, midfielders_data, forwards_data)
        self.stacked_widget.addWidget(self.field_players_panel)

        self.compare_panel = ComparePanel(defenders_data, midfielders_data, forwards_data)
        self.stacked_widget.addWidget(self.compare_panel)

    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_panel)

    def show_goalkeepers(self):
        self.stacked_widget.setCurrentWidget(self.goalkeepers_panel)

    def show_field_players(self):
        self.stacked_widget.setCurrentWidget(self.field_players_panel)

    def show_compare_panel(self):
        self.stacked_widget.setCurrentWidget(self.compare_panel)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
