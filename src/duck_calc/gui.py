# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class calc_main(QWidget):
    def __init__(self):
        super(calc_main, self).__init__()
        self.setFixedSize(320, 530)
        self.setWindowTitle("DUCK_calc")
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "gui.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = calc_main()
    widget.show()
    sys.exit(app.exec_())
