from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QComboBox, QSlider, QFileDialog, QCheckBox, QFrame, QStackedWidget, QScrollArea
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("智能数据归档与压缩系统")
        self.setGeometry(100, 100, 1000, 600)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        main_layout = QHBoxLayout(central_widget)

        # 创建左侧导航栏
        self.create_sidebar(main_layout)

        # 创建右侧功能区域
        self.create_main_area(main_layout)

        # 设置主窗口的中央部件
        self.setCentralWidget(central_widget)

    def create_sidebar(self, layout):
        # 左侧导航栏的布局
        sidebar_layout = QVBoxLayout()

        # 导航栏背景色
        sidebar = QFrame(self)
        sidebar.setStyleSheet("background-color: #34495E; padding: 10px;")
        sidebar.setFixedWidth(240)
        sidebar.setLayout(sidebar_layout)

        # 导航栏菜单项
        self.create_menu_item(sidebar_layout, "压缩模块", "compress_icon.png")
        self.create_menu_item(sidebar_layout, "归档模块", "archive_icon.png")
        self.create_menu_item(sidebar_layout, "文件管理模块", "file_icon.png")

        layout.addWidget(sidebar)

    def create_menu_item(self, layout, text, icon_path):
        button = QPushButton(text, self)
        button.setStyleSheet("background-color: #2C3E50; color: white; padding: 15px; border: none; font-size: 16px; text-align: left;")
        button.setCursor(Qt.PointingHandCursor)
        button.clicked.connect(lambda: self.menu_item_click(text))
        button.setMinimumHeight(50)
        layout.addWidget(button)

    def menu_item_click(self, text):
        # 根据导航项显示不同的功能区域
        if text == "压缩模块":
            self.stacked_widget.setCurrentIndex(0)
        elif text == "归档模块":
            self.stacked_widget.setCurrentIndex(1)
        elif text == "文件管理模块":
            self.stacked_widget.setCurrentIndex(2)

    def create_main_area(self, layout):
        # 右侧操作区域（主内容区域）
        main_area_layout = QVBoxLayout()

        # 创建堆叠小部件 (QStackedWidget) 用于不同模块页面切换
        self.stacked_widget = QStackedWidget(self)
        main_area_layout.addWidget(self.stacked_widget)

        # 1. 创建压缩模块界面
        self.create_compression_module()

        # 2. 创建归档模块界面
        self.create_archive_module()

        # 3. 创建文件管理模块界面
        self.create_file_management_module()

        layout.addLayout(main_area_layout)

    def create_compression_module(self):
        compression_widget = QWidget(self)
        compression_layout = QVBoxLayout(compression_widget)

        compression_layout.addWidget(QLabel("选择文件或文件夹进行压缩"))

        # 文件选择按钮
        file_button = QPushButton("选择文件", self)
        file_button.clicked.connect(self.select_file)
        folder_button = QPushButton("选择文件夹", self)
        folder_button.clicked.connect(self.select_directory)
        compression_layout.addWidget(file_button)
        compression_layout.addWidget(folder_button)

        # 压缩算法选择
        compression_algorithm_label = QLabel("选择压缩算法", self)
        self.algorithm_combo = QComboBox(self)
        self.algorithm_combo.addItems(["ZIP", "TAR", "GZIP"])
        compression_layout.addWidget(compression_algorithm_label)
        compression_layout.addWidget(self.algorithm_combo)

        # 压缩级别设置
        compression_level_label = QLabel("压缩级别", self)
        self.compression_level_slider = QSlider(Qt.Horizontal, self)
        self.compression_level_slider.setRange(1, 9)
        compression_layout.addWidget(compression_level_label)
        compression_layout.addWidget(self.compression_level_slider)

        # 添加到堆叠小部件中
        self.stacked_widget.addWidget(compression_widget)

    def create_archive_module(self):
        archive_widget = QWidget(self)
        archive_layout = QVBoxLayout(archive_widget)

        archive_layout.addWidget(QLabel("选择文件或文件夹进行归档"))

        # 文件选择按钮
        file_button = QPushButton("选择文件", self)
        file_button.clicked.connect(self.select_file)
        folder_button = QPushButton("选择文件夹", self)
        folder_button.clicked.connect(self.select_directory)
        archive_layout.addWidget(file_button)
        archive_layout.addWidget(folder_button)

        # 存储层次选择
        importance_label = QLabel("选择文件重要性", self)
        self.importance_combo = QComboBox(self)
        self.importance_combo.addItems(["高", "中", "低"])
        archive_layout.addWidget(importance_label)
        archive_layout.addWidget(self.importance_combo)

        # 是否需要压缩选择
        compress_checkbox = QCheckBox("需要压缩", self)
        archive_layout.addWidget(compress_checkbox)

        # 压缩算法选择
        compress_algorithm_label = QLabel("选择压缩算法", self)
        self.archive_algorithm_combo = QComboBox(self)
        self.archive_algorithm_combo.addItems(["ZIP", "TAR", "GZIP"])
        archive_layout.addWidget(compress_algorithm_label)
        archive_layout.addWidget(self.archive_algorithm_combo)

        # 添加到堆叠小部件中
        self.stacked_widget.addWidget(archive_widget)

    def create_file_management_module(self):
        file_management_widget = QWidget(self)
        file_management_layout = QVBoxLayout(file_management_widget)

        file_management_layout.addWidget(QLabel("已归档的文件"))

        # 显示已归档文件列表
        self.file_list = QScrollArea(self)
        file_management_layout.addWidget(self.file_list)

        # 下载文件按钮
        download_button = QPushButton("下载文件", self)
        download_button.clicked.connect(self.download_file)
        file_management_layout.addWidget(download_button)

        # 添加到堆叠小部件中
        self.stacked_widget.addWidget(file_management_widget)

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if file:
            print(f"Selected file: {file}")

    def select_directory(self):
        folder = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder:
            print(f"Selected folder: {folder}")

    def download_file(self):
        selected_file = self.file_list.selectedItems()
        if selected_file:
            print(f"Downloading: {selected_file[0].text()}")
