from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
from utils import get_data

class GoalkeepersPanel(QWidget):
    def __init__(self, goalkeepers_data):
        super().__init__()

        layout = QVBoxLayout()

        self.goalkeepers_data = goalkeepers_data

        goalkeepers_table_view = QTableView(self)
        goalkeepers_model = QStandardItemModel(self)

        # Przykładowy DataFrame dla panelu "Goalkeepers"
        #goalkeepers_data = get_data.get_gks()
        goalkeepers_model.setHorizontalHeaderLabels(goalkeepers_data.columns)

        # Wypełnienie tabeli danymi z DataFrame
        for row_index, row_data in goalkeepers_data.iterrows():
            for col_index, cell_value in enumerate(row_data):
                item = QStandardItem(str(cell_value))
                goalkeepers_model.setItem(row_index, col_index, item)

        goalkeepers_table_view.setModel(goalkeepers_model)
        goalkeepers_table_view.resizeColumnsToContents()
        layout.addWidget(goalkeepers_table_view)

        self.setLayout(layout)
