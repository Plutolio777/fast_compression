from app.main_window import MainWindow
from PyQt5.QtWidgets import QApplication

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()