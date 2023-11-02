from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView


class GoalkeepersPanel(QWidget):
    def __init__(self, goalkeepers_data):
        super().__init__()
        layout = QVBoxLayout()
        self.goalkeepers_data = goalkeepers_data
        goalkeepers_table_view = QTableView(self)
        goalkeepers_table_view.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        goalkeepers_model = QStandardItemModel(self)
        goalkeepers_model.setHorizontalHeaderLabels(goalkeepers_data.columns)
        for row_index, row_data in goalkeepers_data.iterrows():
            for col_index, cell_value in enumerate(row_data):
                item = QStandardItem(str(cell_value))
                goalkeepers_model.setItem(row_index, col_index, item)

        goalkeepers_table_view.setModel(goalkeepers_model)
        goalkeepers_table_view.resizeColumnsToContents()
        layout.addWidget(goalkeepers_table_view)
        self.setLayout(layout)
