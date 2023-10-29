from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QLabel, QComboBox, QDialog, QRadioButton, QButtonGroup, \
    QPushButton, QTextBrowser
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
from utils import compare as cmp


class ComparePanel(QWidget):
    def __init__(self, goalkeepers_data, defenders_data, midfielders_data, forwards_data, fields_data):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Compare Panel")
        layout.addWidget(label)

        self.goalkeepers_data = goalkeepers_data
        self.defenders_data = defenders_data
        self.midfielders_data = midfielders_data
        self.forwards_data = forwards_data
        self.fields_data = fields_data

        self.table_view = QTableView(self)
        layout.addWidget(self.table_view)

        self.column_selector = QComboBox()
        layout.addWidget(self.column_selector)

        self.setLayout(layout)

        self.model = QStandardItemModel(self)

        selected_columns = ["Player", "Nation", "Squad"]

        for column_name in selected_columns:
            self.column_selector.addItem(column_name)
            self.model.setHorizontalHeaderItem(self.model.columnCount(), QStandardItem(column_name))

        self.table_view.setModel(self.model)

        for _, row in midfielders_data[selected_columns].iterrows():
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)

        self.table_view.resizeColumnsToContents()

        self.table_view.doubleClicked.connect(self.show_radio_buttons)

    def show_radio_buttons(self, index):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Option")

        layout = QVBoxLayout(dialog)

        label = QLabel("Select an option:")
        layout.addWidget(label)

        similarity_buttons = []

        manhattan_button = QRadioButton("Manhattan similarity")
        similarity_buttons.append(manhattan_button)
        layout.addWidget(manhattan_button)
        euclidean_button = QRadioButton("Euclidean similarity")
        similarity_buttons.append(euclidean_button)
        layout.addWidget(euclidean_button)
        pearson_button = QRadioButton("Pearson similarity")
        similarity_buttons.append(pearson_button)
        layout.addWidget(pearson_button)
        avg_button = QRadioButton("Average similarity")
        similarity_buttons.append(avg_button)
        layout.addWidget(avg_button)
        cosine_button = QRadioButton("Cosine similarity")
        similarity_buttons.append(cosine_button)
        layout.addWidget(cosine_button)

        # Grupa przycisków typu radio
        button_group = QButtonGroup(dialog)
        for i, radio_button in enumerate(similarity_buttons):
            button_group.addButton(radio_button, i)

        # Obsługa akceptacji okna dialogowego po wybraniu opcji
        def accept_dialog():
            selected_option = button_group.checkedId()
            current_index = self.table_view.currentIndex()
            row_number = current_index.row()

            selected_row = self.fields_data.iloc[row_number]
            series1 = selected_row  # Przykładowa seria z danymi z wiersza

            if selected_option == 0:
                print("Selected Manhattan similarity")
                series2, min_diff = cmp.similar_manhattan(self.fields_data, row_number)
            elif selected_option == 1:
                print("Selected Euclidean similarity")
            elif selected_option == 2:
                print("Selected Pearson similarity")
            elif selected_option == 3:
                print("Selected Average similarity")
            elif selected_option == 4:
                print("Selected Cosine similarity")
            text_browser = QTextBrowser()
            text_browser.append("Series 1:")
            text_browser.append(series1.to_string())
            text_browser.append("\nSeries 2:")
            text_browser.append(series2.to_string())

            layout.addWidget(text_browser)

            dialog.adjustSize()
            dialog.accept()

        # Przycisk OK
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(accept_dialog)
        layout.addWidget(ok_button)

        dialog.exec()
