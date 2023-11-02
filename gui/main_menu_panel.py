from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd


class MainMenuPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        for i in range(4):
            table_view = QTableView(self)
            table_view.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
            model = QStandardItemModel(self)
            table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            table_view.setModel(model)

            data = {'Column 1': ['A', 'B', 'C'],
                    'Column 2': [1, 2, 3]}
            df = pd.DataFrame(data)

            for row_index, row_data in df.iterrows():
                for col_index, cell_value in enumerate(row_data):
                    item = QStandardItem(str(cell_value))
                    model.setItem(row_index, col_index, item)

            table_view.resizeColumnsToContents()

            row = i // 2
            col = i % 2
            grid_layout.addWidget(table_view, row, col)

        self.setLayout(layout)
