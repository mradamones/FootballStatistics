from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QGuiApplication
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QLabel, QDialog, QRadioButton, QButtonGroup, \
    QPushButton, QHBoxLayout, QHeaderView, QComboBox
from classificator import predictions as pred


# spytac, czy skupiac sie na naprawianiu takich rzeczy jak labele kolumn
class PositionPanel(QWidget):
    def __init__(self, fields_data):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Position Panel")
        layout.addWidget(label)

        self.fields_data = fields_data

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

        for _, row in self.fields_data[selected_columns].iterrows():
            row_items = [QStandardItem(str(row[column_name])) for column_name in selected_columns]
            self.model.appendRow(row_items)

        for column_index in range(self.model.columnCount()):
            self.table_view.horizontalHeader().setSectionResizeMode(column_index, QHeaderView.ResizeMode.Stretch)
            self.table_view.setColumnWidth(column_index, self.table_view.columnWidth(0))

        self.table_view.doubleClicked.connect(self.show_radio_buttons)

    def show_filter_dialog(self):
        filter_dialog = self.FilterDialog(self.fields_data, self)
        filter_dialog.exec()

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

        classificator_buttons = []

        knn_button = QRadioButton("K-Neighbors Classifier")
        classificator_buttons.append(knn_button)
        layout.addWidget(knn_button)
        svc_button = QRadioButton("SVC")
        classificator_buttons.append(svc_button)
        layout.addWidget(svc_button)
        rfc_button = QRadioButton("Random Forest Classificator")
        classificator_buttons.append(rfc_button)
        layout.addWidget(rfc_button)
        gnb_button = QRadioButton("Gaussian Naive Bayes")
        classificator_buttons.append(gnb_button)
        layout.addWidget(gnb_button)
        mlp_button = QRadioButton("MLP Classificator")
        classificator_buttons.append(mlp_button)
        layout.addWidget(mlp_button)
        dtc_button = QRadioButton("Decision Tree Classificator")
        classificator_buttons.append(dtc_button)
        layout.addWidget(dtc_button)

        button_group = QButtonGroup(dialog)
        for i, radio_button in enumerate(classificator_buttons):
            button_group.addButton(radio_button, i)

        def accept_dialog():
            selected_option = button_group.checkedId()
            current_index = self.table_view.currentIndex()
            row_number = current_index.row()

            selected_row = self.fields_data.iloc[row_number]
            series1 = selected_row

            if selected_option == 0:
                alg = 'knn'
            elif selected_option == 1:
                alg = 'svc'
            elif selected_option == 2:
                alg = 'rfc'
            elif selected_option == 3:
                alg = 'gnb'
            elif selected_option == 4:
                alg = 'mlp'
            elif selected_option == 5:
                alg = 'dtc'
            predicted_position, real_position = pred.make_prediction(alg, row_number)
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

            label_real_pos = QStandardItem("Actual position")
            real_pos = QStandardItem(real_position)
            label_pred_pos = QStandardItem("Optimal position")
            pred_pos = QStandardItem(predicted_position)
            result_model2.appendRow([label_real_pos, real_pos])
            result_model2.appendRow([label_pred_pos, pred_pos])

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
    # TODO - move FilterDialog to another file
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
