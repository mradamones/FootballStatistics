from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QLabel, QComboBox


class FieldPlayersPanel(QWidget):
    def __init__(self, defenders_data, midfielders_data, forwards_data, fields_data):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Field Players Panel")
        layout.addWidget(label)

        self.defenders_data = defenders_data
        self.midfielders_data = midfielders_data
        self.forwards_data = forwards_data
        self.fields_data = fields_data

        self.column_selector = QComboBox()
        layout.addWidget(self.column_selector)

        self.table_view = QTableView()
        self.table_view.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        layout.addWidget(self.table_view)

        self.setLayout(layout)
        self.model = QStandardItemModel(self)
        self.selected_data = self.defenders_data

        self.column_selector.addItem("Defenders")
        self.column_selector.addItem("Midfielders")
        self.column_selector.addItem("Forwards")
        self.column_selector.addItem("All field players")
        self.column_selector.currentIndexChanged.connect(self.update_table)

        self.update_table()

    def update_table(self):
        selected_data = self.selected_data

        self.model.clear()

        selected_columns = []

        if self.column_selector.currentText() == "Defenders":
            selected_data = self.defenders_data
            selected_columns = selected_data.columns.tolist()
        elif self.column_selector.currentText() == "Midfielders":
            selected_data = self.midfielders_data
            selected_columns = selected_data.columns.tolist()
        elif self.column_selector.currentText() == "Forwards":
            selected_data = self.forwards_data
            selected_columns = selected_data.columns.tolist()
        elif self.column_selector.currentText() == "All field players":
            selected_data = self.fields_data
            selected_columns = selected_data.columns.tolist()

        for column_name in selected_columns:
            self.model.setHorizontalHeaderItem(self.model.columnCount(), QStandardItem(column_name))  # Dodaj do modelu

        for _, row in selected_data.iterrows():
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)
        self.table_view.setModel(self.model)
        self.table_view.resizeColumnsToContents()
