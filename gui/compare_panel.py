from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QLabel, QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
from utils import get_data as gd


class ComparePanel(QWidget):
    def __init__(self, defenders_data, midfielders_data, forwards_data):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Compare Panel")
        layout.addWidget(label)

        self.defenders_data = defenders_data
        self.midfielders_data = midfielders_data
        self.forwards_data = forwards_data

        self.table_view = QTableView(self)
        layout.addWidget(self.table_view)

        self.column_selector = QComboBox()  # ComboBox do wyboru kolumn
        layout.addWidget(self.column_selector)

        self.setLayout(layout)

        # Tutaj możesz dodać kod do wczytywania danych do tabeli lub inne operacje

        # Pobierz dane (np. z funkcji get_data)
        #data = gd.get_mids()  # Zakładam, że masz funkcję get_data do wczytania danych

        # Utwórz model dla tabeli
        self.model = QStandardItemModel(self)

        # Wybierz interesujące cię kolumny i dodaj je do ComboBox i modelu
        selected_columns = ["Player", "Nation", "Squad"]  # Tutaj podaj nazwy kolumn

        for column_name in selected_columns:
            self.column_selector.addItem(column_name)  # Dodaj do ComboBox
            self.model.setHorizontalHeaderItem(self.model.columnCount(), QStandardItem(column_name))  # Dodaj do modelu

        self.table_view.setModel(self.model)  # Ustaw model tabeli

        # Wypełnij tabelę danymi
        for _, row in midfielders_data[selected_columns].iterrows():
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)

        self.table_view.resizeColumnsToContents()
