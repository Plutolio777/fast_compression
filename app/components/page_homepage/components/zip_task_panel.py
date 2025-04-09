from siui.components import SiLabel, SiTitledWidgetGroup, SiOptionCardPlane
from siui.core import SiGlobal, SiColor


class TaskCard(SiOptionCardPlane):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedHeight(300)
        title = SiLabel()
        title.setText("aaaaaaaaaa")

        self.body().addWidget(title)
        self.adjustSize()

    def reloadStyleSheet(self):
        super().reloadStyleSheet()

        # self.outfit_label_lower.setStyleSheet("background-color: {}".format(SiGlobal.siui.colors["INTERFACE_BG_A"]))
        # self.outfit_label_upper.setStyleSheet("background-color: {}".format(SiGlobal.siui.colors["INTERFACE_BG_C"]))

        self.outfit_label_lower.setStyleSheet(f"background-color: {self.getColor(SiColor.BUTTON_PANEL)}")
        self.outfit_label_upper.setStyleSheet(f"background-color: {self.getColor(SiColor.BUTTON_PANEL)}")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        print(123123123123123, event.size())


class ZipTaskPanel(SiLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tasks = []

        self.group = SiTitledWidgetGroup(self)

        with self.group as group:
            group.setAdjustWidgetsSize(True)
            group.addTitle("智能压缩决策")
            group.addWidget(TaskCard())
            group.addWidget(TaskCard())
            group.addWidget(TaskCard())

        group.adjustSize()
        self.adjustSize()
        self.parent().adjustSize()

    def adjustSize(self):
        super().adjustSize()
        print(12312513, self.group.height())
        self.resize(self.width(), self.group.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        width = event.size().width()
        print(width)
        self.group.setFixedWidth(width - 32)
