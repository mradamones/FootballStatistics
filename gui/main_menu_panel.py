from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
import utils.main_views as mv


class MainMenuPanel(QWidget):
    def __init__(self, goalkeepers_data, fields_data):
        super().__init__()

        layout = QVBoxLayout()

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.goalkeepers_data = goalkeepers_data
        self.fields_data = fields_data

        views_and_data = [
            ("Golden Boot", mv.get_golden_boot(self.fields_data)),
            ("Goals & Assists", mv.get_ga(self.fields_data)),
            ("Golden Glove", mv.get_glove(self.goalkeepers_data)),
            ("Most Passes", mv.get_passes(self.fields_data)),
        ]

        for i, (view_name, data_function) in enumerate(views_and_data):
            table_view = QTableView(self)
            table_view.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
            model = QStandardItemModel(self)
            table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            table_view.setModel(model)

            # Get data using the specified function
            data = data_function

            # Set headers
            model.setHorizontalHeaderLabels(data.columns)

            # Ensure that the model has a fixed number of rows (e.g., 10)
            model.setRowCount(15)

            # Populate the table with data
            for row_index, row_data in enumerate(data.itertuples()):
                for col_index, cell_value in enumerate(row_data[1:]):
                    item = QStandardItem(str(cell_value) if pd.notna(cell_value) else "")
                    model.setItem(row_index, col_index, item)

            table_view.resizeColumnsToContents()

            # Add table to the grid layout
            row = i // 2
            col = i % 2
            grid_layout.addWidget(table_view, row, col)

        self.setLayout(layout)
