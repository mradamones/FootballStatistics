from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QGuiApplication
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QLabel, QDialog, QRadioButton, QButtonGroup, \
    QPushButton, QHBoxLayout, QHeaderView, QComboBox
from utils import compare as cmp


class ComparePanel(QWidget):
    def __init__(self, goalkeepers_data, fields_data):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Compare Panel")
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
        self.filterButton = QPushButton("Filter")
        layout.addWidget(self.filterButton)
        self.filterButton.clicked.connect(self.show_filter_dialog)

        self.table_view.setModel(self.model)

        for _, row in self.selected_data[selected_columns].iterrows():
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)

        for column_index in range(self.model.columnCount()):
            self.table_view.horizontalHeader().setSectionResizeMode(column_index, QHeaderView.ResizeMode.Stretch)
            self.table_view.setColumnWidth(column_index, self.table_view.columnWidth(0))

        self.table_view.doubleClicked.connect(self.show_radio_buttons)

    def show_filter_dialog(self):
        filter_dialog = self.FilterDialog(self.selected_data, self)
        filter_dialog.exec()

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

    # TODO - add flags as icons (github flag-icons)
    def show_radio_buttons(self, index):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Option")
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        dialog_size = dialog.size()

        x = (screen_geometry.width() - dialog_size.width()) / 2
        y = (screen_geometry.height() - dialog_size.height()) / 2
        dialog.move(int(x), int(y) - 200)

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

        button_group = QButtonGroup(dialog)
        for i, radio_button in enumerate(similarity_buttons):
            button_group.addButton(radio_button, i)

        def accept_dialog():
            selected_option = button_group.checkedId()
            current_index = self.table_view.currentIndex()
            row_number = current_index.row()

            selected_row = self.selected_data.iloc[row_number]
            series1 = selected_row

            if selected_option == 0:
                print("Selected Manhattan similarity")
                series2, min_diff = cmp.similar_manhattan(self.selected_data, row_number)
            elif selected_option == 1:
                print("Selected Euclidean similarity")
                series2, min_diff = cmp.similar_euclidean(self.selected_data, row_number)
            elif selected_option == 2:
                print("Selected Pearson similarity")
                series2, min_diff = cmp.similar_pearson(self.selected_data, row_number)
            elif selected_option == 3:
                print("Selected Average similarity")
                series2, min_diff = cmp.similar_avg(self.selected_data, row_number)
            elif selected_option == 4:
                print("Selected Cosine similarity")
                series2, min_diff = cmp.similar_cosine(self.selected_data, row_number)

            dialog.close()

            result_dialog = QDialog(self)
            result_dialog.setWindowTitle("Comparison Results")
            result_dialog.resize(800, 400)
            screen = QGuiApplication.primaryScreen()
            screen_geometry = screen.availableGeometry()
            dialog_size = result_dialog.size()
            x = (screen_geometry.width() - dialog_size.width()) / 2
            y = (screen_geometry.height() - dialog_size.height()) / 2
            result_dialog.move(int(x) - 400, int(y) - 200)
            layout = QVBoxLayout(result_dialog)
            result_table1 = QTableView(result_dialog)
            result_table2 = QTableView(result_dialog)
            result_table1.horizontalHeader().setStretchLastSection(True)
            result_table2.horizontalHeader().setStretchLastSection(True)
            horizontal_layout = QHBoxLayout()
            layout.addLayout(horizontal_layout)
            horizontal_layout.addWidget(result_table1)
            horizontal_layout.addWidget(result_table2)

            result_model1 = QStandardItemModel(result_dialog)
            result_model2 = QStandardItemModel(result_dialog)

            for key, value in series1.items():
                key_item = QStandardItem(str(key))
                value_item = QStandardItem(str(value))
                result_model1.appendRow([key_item, value_item])

            for key, value in series2.items():
                key_item = QStandardItem(str(key))
                value_item = QStandardItem(str(value))
                result_model2.appendRow([key_item, value_item])

            result_table1.setModel(result_model1)
            result_table2.setModel(result_model2)

            ok_button = QPushButton("OK")
            layout.addWidget(ok_button)
            ok_button.clicked.connect(result_dialog.accept)
            result_dialog.exec()

        ok_button = QPushButton("OK")
        layout.addWidget(ok_button)
        ok_button.clicked.connect(accept_dialog)
        dialog.exec()

    class FilterDialog(QDialog):
        def __init__(self, current_data, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Filter Players")
            self.current_data = current_data
            layout = QVBoxLayout()

            self.comboBox = QComboBox()
            self.comboBox.addItem("Select League")
            self.comboBox.addItem("Premier League")
            self.comboBox.addItem("La Liga")
            self.comboBox.addItem("Serie A")
            self.comboBox.addItem("Bundesliga")
            self.comboBox.addItem("Ligue 1")
            layout.addWidget(self.comboBox)

            self.filterButton = QPushButton("Filter")
            self.filterButton.clicked.connect(self.apply_filter)
            layout.addWidget(self.filterButton)

            self.setLayout(layout)

        def apply_filter(self):
            selected_league = self.comboBox.currentText()
            if selected_league == "Select League":
                filtered_data = self.current_data
            else:
                filtered_data = self.current_data[self.current_data['Comp'] == selected_league]

            self.parent().filtered_data = filtered_data
            self.parent().selected_data = filtered_data
            self.parent().update_filtered_table()
            self.close()

    def update_filtered_table(self):
        self.model.clear()

        selected_columns = ["Player", "Nation", "Squad", "Comp"]

        for column_name in selected_columns:
            self.model.setHorizontalHeaderItem(self.model.columnCount(),
                                               QStandardItem(column_name))  # Dodaj do modelu

        for _, row in self.filtered_data.iterrows():  # Aktualizuj dane z filtrowanymi danymi
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)
        self.table_view.setModel(self.model)
        for column_index in range(self.model.columnCount()):
            self.table_view.horizontalHeader().setSectionResizeMode(column_index, QHeaderView.ResizeMode.Stretch)
            self.table_view.setColumnWidth(column_index, self.table_view.columnWidth(0))

# TODO - dodać filtrowanie do goalkeepers i field
# TODO - panel porównania zawodników (%podobieństwa, wybrane statystyki, pokolorowane na zielono gdy lepszy wynik)