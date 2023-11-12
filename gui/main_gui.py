import pickle
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedWidget, QHBoxLayout, \
    QDialog, QLabel
from compare_panel import ComparePanel
from field_players_panel import FieldPlayersPanel
from goalkeepers_panel import GoalkeepersPanel
from main_menu_panel import MainMenuPanel
from position_panel import PositionPanel
from utils import get_data as gd


class DataDialog(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Załadować dane z pliku, czy pobrać najnowsze z internetu?")
        layout.addWidget(label)

        load_button = QPushButton('Załaduj z pliku')
        load_button.clicked.connect(self.reject)
        layout.addWidget(load_button)

        download_button = QPushButton('Pobierz najnowsze')
        download_button.clicked.connect(self.on_download_clicked)
        layout.addWidget(download_button)

        self.move(100, 0)

    def on_load_clicked(self):
        goalkeepers_pickle = open('../data/goalkeepers', 'rb')
        goalkeepers_data = pickle.load(goalkeepers_pickle)
        goalkeepers_pickle.close()
        defenders_pickle = open('../data/defenders', 'rb')
        defenders_data = pickle.load(defenders_pickle)
        defenders_pickle.close()
        midfielders_pickle = open('../data/midfielders', 'rb')
        midfielders_data = pickle.load(midfielders_pickle)
        midfielders_pickle.close()
        forwards_pickle = open('../data/forwards', 'rb')
        forwards_data = pickle.load(forwards_pickle)
        forwards_pickle.close()
        fields_pickle = open('../data/fields', 'rb')
        fields_data = pickle.load(fields_pickle)
        fields_pickle.close()
        self.reject()
        return goalkeepers_data, defenders_data, midfielders_data, forwards_data, fields_data

    def on_download_clicked(self):
        goalkeeping, adv_goalkeeping, play_time, misc, standard, passing, pass_types, defense, possession, shooting, creation = gd.get_all_tables()
        goalkeepers_data = gd.get_gks(goalkeeping, adv_goalkeeping, misc, play_time)
        defenders_data = gd.get_def(standard, passing, pass_types, defense, possession, misc, play_time)
        midfielders_data = gd.get_mids(standard, shooting, passing, pass_types, creation, defense, possession, misc, play_time)
        forwards_data = gd.get_fwds(standard, shooting, passing, pass_types, creation, possession, misc, play_time)
        fields_data = gd.get_field(standard, shooting, passing, pass_types, creation, defense, possession, misc, play_time)
        goalkeepers_pickle = open('../data/goalkeepers', 'wb')
        pickle.dump(goalkeepers_data, goalkeepers_pickle)
        goalkeepers_pickle.close()
        defenders_pickle = open('../data/defenders', 'wb')
        pickle.dump(defenders_data, defenders_pickle)
        defenders_pickle.close()
        midfielders_pickle = open('../data/midfielders', 'wb')
        pickle.dump(midfielders_data, midfielders_pickle)
        midfielders_pickle.close()
        forwards_pickle = open('../data/forwards', 'wb')
        pickle.dump(forwards_data, forwards_pickle)
        forwards_pickle.close()
        fields_pickle = open('../data/fields', 'wb')
        pickle.dump(fields_data, fields_pickle)
        fields_pickle.close()
        self.reject()
        return goalkeepers_data, defenders_data, midfielders_data, forwards_data, fields_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        dialog = DataDialog()

        if dialog.exec() == QDialog.DialogCode.Rejected:
            goalkeepers_data, defenders_data, midfielders_data, forwards_data, fields_data = dialog.on_load_clicked()
            self.initUI(goalkeepers_data, defenders_data, midfielders_data, forwards_data, fields_data)
        else:
            goalkeepers_data, defenders_data, midfielders_data, forwards_data, fields_data = dialog.on_download_clicked()
            self.initUI(goalkeepers_data, defenders_data, midfielders_data, forwards_data, fields_data)

    def initUI(self, goalkeepers_data, defenders_data, midfielders_data, forwards_data, fields_data):
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

        position_button = QPushButton('Find ideal position', self)
        position_button.clicked.connect(self.show_position_panel)
        button_layout.addWidget(position_button)

        layout.addLayout(button_layout)

        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        self.main_menu_panel = MainMenuPanel()
        self.stacked_widget.addWidget(self.main_menu_panel)

        self.goalkeepers_panel = GoalkeepersPanel(goalkeepers_data)
        self.stacked_widget.addWidget(self.goalkeepers_panel)

        self.field_players_panel = FieldPlayersPanel(defenders_data, midfielders_data, forwards_data, fields_data)
        self.stacked_widget.addWidget(self.field_players_panel)

        self.compare_panel = ComparePanel(goalkeepers_data, fields_data)
        self.stacked_widget.addWidget(self.compare_panel)

        self.position_panel = PositionPanel(fields_data)
        self.stacked_widget.addWidget(self.position_panel)

    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_panel)

    def show_goalkeepers(self):
        self.stacked_widget.setCurrentWidget(self.goalkeepers_panel)

    def show_field_players(self):
        self.stacked_widget.setCurrentWidget(self.field_players_panel)

    def show_compare_panel(self):
        self.stacked_widget.setCurrentWidget(self.compare_panel)

    def show_position_panel(self):
        self.stacked_widget.setCurrentWidget(self.position_panel)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
