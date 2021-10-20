from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("first_program.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUI(window)
window.show()
app.exec_()
