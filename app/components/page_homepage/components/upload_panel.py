import dataclasses
import hashlib

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from siui.components.widgets import (
    SiDenseVContainer,
    SiLabel,
    SiSimpleButton,
)
from siui.core import GlobalFont, Si, SiColor, SiGlobal
from siui.gui import SiFont


class uploadFileRecord(SiLabel):

    def __init__(self, parent, text, record):
        super().__init__(parent)
        self.record = record
        self.left_spacing = 6
        self.text_button_spacing = 10

        self.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setFixedHeight(24)
        self.setFixedStyleSheet("border-radius: 4px")
        self.setText(text)

        self.close_button = SiSimpleButton(self)
        self.close_button.attachment().load(
            b'<svg t="1744183252943" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5532" width="24" height="24"><path d="M558.421333 511.914667l212.309334-212.138667a32.682667 32.682667 0 1 0-46.336-46.336L512 465.493333 299.52 253.44a32.682667 32.682667 0 1 0-46.250667 46.336l212.309334 212.138667-212.309334 212.224a32.682667 32.682667 0 1 0 46.336 46.336L512 558.250667l212.48 212.224a32.512 32.512 0 0 0 46.250667 0 32.682667 32.682667 0 0 0 0-46.336L558.421333 512z" fill="#999999" p-id="5533"></path></svg>')
        self.close_button.resize(self.height(), self.height())
        self.close_button.setGeometry(self.width() + self.text_button_spacing + self.left_spacing, 0, 24, 24)
        self.close_button.setCursor(Qt.PointingHandCursor)
        self.close_button.clicked.connect(lambda: self.parent().parent().remove_record(self))  # noqa
        # self.close_button.setFixedStyleSheet("border-radius: 4px")

        self.adjustSize()
        self.resize(self.width() + self.height() + self.left_spacing + self.text_button_spacing, self.height())

        self.close_button.reloadStyleSheet()
        self.reloadStyleSheet()
        self.show()

    def reloadStyleSheet(self):
        self.setStyleSheet(f"color: {self.getColor(SiColor.TEXT_B)};"
                           f"background-color: {self.getColor(SiColor.INTERFACE_BG_D)};"
                           f"padding-left: {self.left_spacing}px")

    def remove(self):
        parent: SiDenseVContainer = self.parent()
        parent.removeWidget(self)
        parent.adjustSize()
        pass


class UploadPanelButtonArea(SiLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon_text_spacing = 5
        self.setCursor(Qt.PointingHandCursor)
        # 构建组成外观的控件
        self.outfit_label_lower = SiLabel(self)
        # self.outfit_label_lower.setFixedStyleSheet("border: 1.5px dashed #3b373f; border-radius: 12px")
        self.outfit_label_upper = SiLabel(self)
        self.outfit_label_upper.setFixedStyleSheet("border: 1.4px dashed #c8c9cc; border-radius: 12px; ")

        self.tip_text = SiLabel(self)
        self.tip_text.setFixedWidth(200)
        self.tip_text.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
        self.tip_text.setFixedHeight(24)
        self.tip_text.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.tip_text.setText("拖拽或者点击上传文件")
        self.tip_text.setStyleSheet("color: {}".format(SiColor.trans(SiGlobal.siui.colors["TEXT_A"], 0.9)))
        self.tip_text.setFont(SiFont.tokenized(GlobalFont.S_NORMAL))

        self.upload_button = SiSimpleButton(self)
        self.upload_button.resize(100, 200)
        self.upload_button.attachment().load(
            b'<svg t="1744106682523" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4422" width="64" height="64"><path d="M239.317333 810.666667l-8.533333-1.28C173.226667 801.152 128 750.805333 128 689.152c0-51.157333 31.146667-94.72 75.050667-112.725333L256.170667 554.666667 256 495.36a213.333333 213.333333 0 0 1 420.437333-51.328l15.189334 61.354667 63.104 3.370666C832.853333 512.853333 896 578.346667 896 659.584c0 84.053333-67.413333 151.04-149.333333 151.04H725.333333v85.333333h21.333334c129.621333 0 234.666667-105.813333 234.666666-236.373333 0-126.293333-98.304-229.461333-222.08-236.074667A298.666667 298.666667 0 0 0 170.666667 495.488v1.962667a206.933333 206.933333 0 0 0-128 191.658666c0 104.192 76.458667 190.421333 175.957333 204.8v2.048H298.666667v-85.333333H239.317333z" fill="#bfbfbf" p-id="4423"></path><path d="M512 512l219.477333 219.477333h-120.704L512 632.618667l-98.858667 98.858666H292.522667L512 512z" fill="#bfbfbf" p-id="4424"></path><path d="M554.666667 597.333333v298.666667h-85.333334v-298.666667h85.333334z" fill="#bfbfbf" p-id="4425"></path></svg>')
        self.upload_button.attachment().setSvgSize(64, 64)
        self.upload_button.setHint("点击上传文件")
        self.upload_button.setBorderRadius(12)
        self.upload_button.clicked.connect(self.parent().upload_button_clicked)
        self.adjustSize()

    def reloadStyleSheet(self):
        super().reloadStyleSheet()
        self.outfit_label_lower.setStyleSheet("background-color: {}".format(SiGlobal.siui.colors["INTERFACE_BG_C"]))
        self.outfit_label_upper.setStyleSheet("background-color: {}".format(SiGlobal.siui.colors["INTERFACE_BG_C"]))

    def adjustSize(self):
        print("调整尺寸", self.width(), self.upload_button.height() + 3)
        self.resize(self.width(), self.upload_button.height() + 3)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        size = event.size()
        w, h = size.width(), size.height()
        print("resize", w, h)

        self.upload_button.setGeometry(0, 0, w - 32, h)
        self.tip_text.setGeometry(int(w / 2) - 93, int(h / 2) + self.tip_text.height() + self.icon_text_spacing,
                                  w - 300, self.tip_text.height())

        self.outfit_label_lower.setGeometry(0, 8, w - 32, h - 8)  # 防止上边出现底色毛边
        self.outfit_label_upper.resize(w - 32, h)

    def enterEvent(self, event):
        self.outfit_label_upper.setFixedStyleSheet(
            "border: 1.4px dashed qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #3498db, stop:1 #2ecc71); border-radius: 12px")
        pass

    def leaveEvent(self, event):
        self.outfit_label_upper.setFixedStyleSheet("border: 1.4px dashed #c8c9cc; border-radius: 12px; ")


class UploadPanel(SiDenseVContainer):

    @dataclasses.dataclass
    class FileRecord:
        file_path: str
        file_id: str = ""
        is_registered: bool = False

        def register(self):
            self.is_registered = True

        def __post_init__(self):
            md5_hash = hashlib.md5()
            md5_hash.update(self.file_path.encode('utf-8'))
            self.file_id = md5_hash.hexdigest()

        def __eq__(self, other):
            return self.file_id == other.file_id

        def __hash__(self):
            # 使用 file_id 作为哈希值
            return hash(self.file_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.upload_attachments_panel = None
        self.upload_attachment = set()
        self.setSpacing(12)
        self.setAdjustWidgetsSize(True)

        # 上传面板
        self.upload_panel = UploadPanelButtonArea(self)
        self.upload_panel.adjustSize()

        # 已上传文件工具面板
        self.tools_panel = SiDenseVContainer(self)
        # self.tools_panel.setAdjustWidgetsSize(True)
        self.tools_panel.setSpacing(4)
        self.tools_panel.setStyleSheet("background-color:red")
        self.addWidget(self.upload_panel)
        self.addWidget(self.tools_panel, "bottom")
        self.repaintUploadPanel()

    def repaintUploadPanel(self):
        print("重新绘制上传面板")
        for record in self.upload_attachment:
            record: UploadPanel.FileRecord
            if record.is_registered:
                continue
            a = uploadFileRecord(self.tools_panel, record.file_path, record)
            self.tools_panel.addWidget(a)
            self.tools_panel.arrangeWidget()
            record.register()
        self.tools_panel.adjustSize()
        self.adjustSize()
        self.parent().adjustSize()

    def remove_record(self, widget):
        record = widget.record
        self.tools_panel.removeWidget(widget)
        self.tools_panel.arrangeWidget()
        self.tools_panel.adjustSize()
        self.adjustSize()
        self.parent().adjustSize()
        self.upload_attachment.remove(record)

    def upload_button_clicked(self):
        """
        打开文件选择对话框并处理选择的文件
        """
        # 设置文件对话框选项
        options = QFileDialog.Options()
        # 可以选择使用原生对话框或Qt的对话框
        # options |= QFileDialog.DontUseNativeDialog

        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口
            "选择上传文件",  # 对话框标题
            "",  # 初始目录(空表示默认目录)
            "所有文件 (*);;文本文件 (*.txt);;图片文件 (*.png *.jpg *.jpeg)",  # 文件过滤器
            options=options
        )

        # 如果用户选择了文件(没有点击取消)
        if file_path:
            print(f"选择的文件路径: {file_path}")
            # 在这里添加你的文件处理逻辑
            # 例如: self.process_upload_file(file_path)

            # 可以更新UI显示选择的文件名
            new_record = UploadPanel.FileRecord(file_path)
            if new_record in self.upload_attachment:
                SiGlobal.siui.windows["MAIN_WINDOW"].LayerRightMessageSidebar().send(
                    "请勿添加重复文件！",
                    msg_type=4,
                    fold_after=1500,
                )
                return
            self.upload_attachment.add(new_record)
            self.repaintUploadPanel()
            return file_path
        else:
            print("用户取消了选择")
            return None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.upload_panel.setFixedWidth(event.size().width())
        self.tools_panel.setFixedWidth(event.size().width())
