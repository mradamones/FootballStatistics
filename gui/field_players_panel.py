from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QLabel, QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd


class FieldPlayersPanel(QWidget):
    def __init__(self, defenders_data, midfielders_data, forwards_data):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Field Players Panel")
        layout.addWidget(label)

        self.defenders_data = defenders_data
        self.midfielders_data = midfielders_data
        self.forwards_data = forwards_data

        self.column_selector = QComboBox()  # ComboBox do wyboru kolumn
        layout.addWidget(self.column_selector)

        self.setLayout(layout)

        # Tutaj możesz dodać kod do wczytywania danych do tabeli lub inne operacje

        # Utwórz model dla tabeli
        self.model = QStandardItemModel(self)

        # Domyślnie wybierz pierwszy zbiór danych
        self.selected_data = self.midfielders_data

        self.column_selector.addItem("Midfielders")
        self.column_selector.addItem("Forwards")
        self.column_selector.currentIndexChanged.connect(self.update_table)

        self.update_table()

    def update_table(self):
        selected_data = self.selected_data

        # Oczyść model
        self.model.clear()

        # Wybierz interesujące cię kolumny i dodaj je do ComboBox i modelu
        selected_columns = ["Player", "Nation", "Squad"]  # Tutaj podaj nazwy kolumn

        for column_name in selected_columns:
            self.model.setHorizontalHeaderItem(self.model.columnCount(), QStandardItem(column_name))  # Dodaj do modelu

        # Wypełnij tabelę danymi z wybranego zbioru danych
        for _, row in selected_data[selected_columns].iterrows():
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)

        self.table_view.setModel(self.model)  # Ustaw model tabeli

        # Automatyczne dostosowanie szerokości kolumn
        self.table_view.resizeColumnsToContents()
