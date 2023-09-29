import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
from utils import get_data as gd

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, df = pd.DataFrame(), parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.ItemDataRole.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Orientation.Horizontal:
            return self._df.columns[section]
        if orientation == QtCore.Qt.Orientation.Vertical:
            return self._df.index[section]

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.ItemDataRole.DisplayRole:
                return str(self._df.iloc[index.row(), index.column()])
        return None

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return self._df.columns.size

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    model = PandasModel(gd.get_mids())
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.show()
    sys.exit(app.exec())
