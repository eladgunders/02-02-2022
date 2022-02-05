from PyQt5 import QtWidgets, QtCore
from datetime import datetime
import time


class ClockThread(QtCore.QThread):
    def run(self):
        while True:
            time.sleep(0.1)
            window.clock_label.setText(str(datetime.now().isoformat(" ", "seconds")))


class ClockWidget(QtWidgets.QWidget):
    clock = 'Hello'

    def __init__(self):
        super(ClockWidget, self).__init__()
        self.setStyleSheet('font-size: 15px;')
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)
        self.clock_label = QtWidgets.QLabel(str(ClockWidget.clock)) 
        self.main_layout.addWidget(self.clock_label)
        self.clock_thread = ClockThread()
        self.clock_thread.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ClockWidget()
    window.show()
    sys.exit(app.exec_())
