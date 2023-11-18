import plotly.express as px
import pandas as pd
import plotly.express as px
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QLabel, QDialog, QPushButton, QHeaderView, QComboBox, \
    QListWidgetItem, QListWidget, QMessageBox
import utils.modify_df as mod


class DiagramPanel(QWidget):
    def __init__(self, goalkeepers_data, fields_data):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Diagram Panel")
        layout.addWidget(label)

        self.goalkeepers_data = goalkeepers_data
        self.fields_data = fields_data
        self.selected_data = self.fields_data

        self.column_selector = QComboBox()
        layout.addWidget(self.column_selector)

        self.column_selector.addItem("All field players")
        self.column_selector.addItem("Goalkeepers")
        self.column_selector.currentIndexChanged.connect(self.update_table)

        self.table_view = QTableView(self)
        layout.addWidget(self.table_view)
        self.table_view.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.setLayout(layout)

        self.model = QStandardItemModel(self)

        selected_columns = ["Player", "Nation", "Squad", "Comp"]
        #self.filterButton = QPushButton("Filter")
        #layout.addWidget(self.filterButton)
        #self.filterButton.clicked.connect(self.show_filter_dialog)

        self.table_view.setModel(self.model)

        for _, row in self.fields_data[selected_columns].iterrows():
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)

        for column_index in range(self.model.columnCount()):
            self.table_view.horizontalHeader().setSectionResizeMode(column_index, QHeaderView.ResizeMode.Stretch)
            self.table_view.setColumnWidth(column_index, self.table_view.columnWidth(0))

        self.table_view.doubleClicked.connect(self.show_combobox_dialog)

    def show_combobox_dialog(self, index):
        player_name = self.model.item(index.row(), 0).text()
        list_widget = QListWidget(self)
        list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        selected_columns = self.selected_data.columns
        selected_columns = selected_columns.drop(['Rk', 'Player', 'Pos', 'Nation', 'Squad', 'Comp', 'Age', 'Born'])
        for column_name in selected_columns:
            item = QListWidgetItem(column_name)
            item.setCheckState(Qt.CheckState.Unchecked)
            list_widget.addItem(item)
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Select Options for {player_name}")
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(list_widget)

        def on_ok_button_clicked():
            selected_options = [list_widget.item(i).text() for i in range(list_widget.count()) if
                                list_widget.item(i).checkState() == Qt.CheckState.Checked]
            if 3 <= len(selected_options) <= 8:
                self.display_plot(selected_options, index.row(), player_name)
                dialog.accept()
            else:
                QMessageBox.warning(self, "Invalid Selection", "Please select between 3 and 8 options.")

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(on_ok_button_clicked)
        dialog_layout.addWidget(ok_button)
        dialog.setLayout(dialog_layout)
        result = dialog.exec()

    def display_plot(self, selected_options, idx, player_name):
        normalized_data = mod.min_max_normalize(self.selected_data[selected_options])
        player1 = normalized_data.iloc[idx]
        player_df = pd.DataFrame({
            "Category": normalized_data.columns,
            "Value": player1.values.tolist()
        })
        fig = px.line_polar(player_df, r='Value', theta='Category', line_close=True,
                            title=f"Plot for {player_name}", range_r=[0, 1])
        fig.update_traces(text=player_df['Value'].round(3), textposition='bottom center')
        fig.show()

    def update_table(self):
        self.model.clear()
        selected_columns = ["Player", "Nation", "Squad", "Comp"]
        if self.column_selector.currentText() == "Goalkeepers":
            self.selected_data = self.goalkeepers_data

        elif self.column_selector.currentText() == "All field players":
            self.selected_data = self.fields_data

        for column_name in selected_columns:
            self.model.setHorizontalHeaderItem(self.model.columnCount(), QStandardItem(column_name))  # Dodaj do modelu

        for _, row in self.selected_data.iterrows():
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)
        self.table_view.setModel(self.model)
        for column_index in range(self.model.columnCount()):
            self.table_view.horizontalHeader().setSectionResizeMode(column_index, QHeaderView.ResizeMode.Stretch)
            self.table_view.setColumnWidth(column_index, self.table_view.columnWidth(0))