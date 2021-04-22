"""Gui file generated by qt5 lib
"""

import os
import sys

import PySide2.QtGui as QtGui
from math_lib.math_lib import MathLib
from PySide2 import QtCore
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget


class calc_main(QWidget):
    def __init__(self):
        super(calc_main, self).__init__()
        self.setFixedSize(320, 530)
        self.setWindowTitle("DUCK_calc")
        self.window_calc = None
        self.load_ui()
        self.equation = ""
        self.result = "0"

        self.window_calc.ac.clicked.connect(lambda: self.clear_all())
        self.window_calc.ce.clicked.connect(lambda: self.clear_last())

        self.window_calc.equals.clicked.connect(self.compute)

        self.window_calc.dot.clicked.connect(lambda: self.add_dot())
        self.window_calc.parenthesis.clicked.connect(lambda: self.end_parenthesis())

        self.window_calc.div.clicked.connect(lambda: self.pushed_button("/"))
        self.window_calc.mult.clicked.connect(lambda: self.pushed_button("*"))
        self.window_calc.sub.clicked.connect(lambda: self.pushed_button("-"))
        self.window_calc.sum.clicked.connect(lambda: self.pushed_button("+"))
        self.window_calc.sqrt.clicked.connect(lambda: self.pushed_button("_"))
        self.window_calc.pwr.clicked.connect(lambda: self.pushed_button("^"))
        self.window_calc.sin.clicked.connect(lambda: self.pushed_button("sin"))
        self.window_calc.cos.clicked.connect(lambda: self.pushed_button("cos"))

        self.window_calc.num0.clicked.connect(lambda: self.pushed_number("0"))
        self.window_calc.num1.clicked.connect(lambda: self.pushed_number("1"))
        self.window_calc.num2.clicked.connect(lambda: self.pushed_number("2"))
        self.window_calc.num3.clicked.connect(lambda: self.pushed_number("3"))
        self.window_calc.num4.clicked.connect(lambda: self.pushed_number("4"))
        self.window_calc.num5.clicked.connect(lambda: self.pushed_number("5"))
        self.window_calc.num6.clicked.connect(lambda: self.pushed_number("6"))
        self.window_calc.num7.clicked.connect(lambda: self.pushed_number("7"))
        self.window_calc.num8.clicked.connect(lambda: self.pushed_number("8"))
        self.window_calc.num9.clicked.connect(lambda: self.pushed_number("9"))

    def pushed_button(self, type_):
        if (type_ == "sin") or (type_ == "cos"):
            self.equation += type_ + "("
        else:
            self.equation += type_
        self.update_all()

    def pushed_number(self, num):
        self.equation += num
        self.update_all()

    def add_dot(self):
        self.equation += "."
        self.update_all()

    def end_parenthesis(self):
        self.equation += ")"
        self.update_all()

    def clear_all(self):
        self.equation = ""
        self.result = "0"
        self.update_all()

    def clear_last(self):
        self.equation = self.equation[:-1]
        self.update_all()

    def update_all(self):
        self.window_calc.equation_label.setText(self.equation)
        self.window_calc.result_label.setText(self.result)

    def compute(self):
        if self.equation == "":
            return
        self.result_string = MathLib.solve_mathematic_problem(self.equation)
        if self.result_string is not None:
            self.window_calc.result_label.setText(str(self.result_string))
        else:
            self.window_calc.result_label.setText("ERROR")

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "ui/gui.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window_calc = loader.load(ui_file, self)
        ui_file.close()
        icon_src = os.path.join(os.path.dirname(__file__), "data/duck-calc.png")
        icon = QtGui.QIcon()
        icon.addFile(icon_src)
        self.setWindowIcon(icon)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    widget = calc_main()
    widget.show()
    sys.exit(app.exec_())
