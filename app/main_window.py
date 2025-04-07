from PyQt5.QtCore import QThread, pyqtSignal

class CompressionThread(QThread):
    progress_signal = pyqtSignal(int)

    def run(self):
        # 模拟压缩任务
        for i in range(100):
            self.progress_signal.emit(i + 1)
            self.sleep(1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智能数据归档与压缩系统")
        self.setGeometry(100, 100, 600, 400)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(150, 250, 300, 30)

        self.compress_button = QPushButton("压缩文件", self)
        self.compress_button.setGeometry(250, 150, 100, 30)
        self.compress_button.clicked.connect(self.start_compression)

    def start_compression(self):
        self.thread = CompressionThread()
        self.thread.progress_signal.connect(self.update_progress)
        self.thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)
