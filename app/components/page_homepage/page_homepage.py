from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from siui.components import SiPixLabel
from siui.components.button import SiPushButtonRefactor
from siui.components.option_card import SiOptionCardLinear, SiOptionCardPlane
from siui.components.page import SiPage
from siui.components.slider import SiSliderH
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import (
    SiDenseHContainer,
    SiDenseVContainer,
    SiLabel,
    SiLineEdit,
    SiLongPressButton,
    SiPushButton,
    SiSimpleButton,
    SiSwitch,
)
from siui.core import GlobalFont, Si, SiColor, SiGlobal, SiQuickEffect, GlobalFontSize
from siui.gui import SiFont

from .components.themed_option_card import ThemedOptionCardPlane


class ExampleHomepage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 滚动区域
        self.scroll_container = SiTitledWidgetGroup(self)

        # 整个顶部
        self.head_area = SiLabel(self)
        self.head_area.setFixedHeight(450)

        # 创建背景底图和渐变
        self.background_image = SiPixLabel(self.head_area)
        self.background_image.setFixedSize(1366, 300)
        self.background_image.setBorderRadius(6)
        self.background_image.load("./img/homepage_background.png")

        self.background_fading_transition = SiLabel(self.head_area)
        self.background_fading_transition.setGeometry(0, 100, 0, 200)
        self.background_fading_transition.setStyleSheet(
            """
            background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 {}, stop:1 {})
            """.format(SiGlobal.siui.colors["INTERFACE_BG_B"],
                       SiColor.trans(SiGlobal.siui.colors["INTERFACE_BG_B"], 0))
        )

        # 创建大标题和副标题
        self.title = SiLabel(self.head_area)
        self.title.setGeometry(64, 0, 500, 128)
        self.title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title.setText("Fast Compression")
        self.title.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.title.setFont(SiFont.tokenized(GlobalFont.XL_MEDIUM))

        self.subtitle = SiLabel(self.head_area)
        self.subtitle.setGeometry(64, 72, 500, 48)
        self.subtitle.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.subtitle.setText("An intelligent compression and archiving platform")
        self.subtitle.setStyleSheet("color: {}".format(SiColor.trans(SiGlobal.siui.colors["TEXT_A"], 0.9)))
        self.subtitle.setFont(SiFont.tokenized(GlobalFont.S_MEDIUM))

        # 创建一个水平容器
        self.container_for_cards = SiDenseHContainer(self.head_area)
        self.container_for_cards.move(0, 130)
        self.container_for_cards.setFixedHeight(310)
        self.container_for_cards.setAlignment(Qt.AlignCenter)
        self.container_for_cards.setSpacing(32)

        # 添加卡片
        self.option_card_project = ThemedOptionCardPlane(self)
        self.option_card_project.setTitle("GitHub Repo")
        self.option_card_project.setFixedSize(218, 270)
        self.option_card_project.setThemeColor("#855198")
        self.option_card_project.setDescription(
            "check PyQt-SiliconUI Repository on GitHub to get the latest release, report errors, provide suggestions and more.")  # noqa: E501
        self.option_card_project.setURL("https://github.com/ChinaIceF/PyQt-SiliconUI")

        self.option_card_example = ThemedOptionCardPlane(self)
        self.option_card_example.setTitle("Examples")
        self.option_card_example.setFixedSize(218, 270)
        self.option_card_example.setThemeColor("#7573aa")
        self.option_card_example.setDescription(
            "Check examples to understand how to use PyQt-SiliconUI to develop your first work.")  # noqa: E501
        self.option_card_example.setURL("Examples are Coming soon...")

        # 添加到水平容器
        self.container_for_cards.addPlaceholder(64 - 32)
        self.container_for_cards.addWidget(self.option_card_project)
        self.container_for_cards.addWidget(self.option_card_example)

        # 添加到滚动区域容器
        self.scroll_container.addWidget(self.head_area)

        # SiQuickEffect.applyDropShadowOn(self.container_for_cards, color=(0, 0, 0, 80), blur_radius=48)

        # 下方区域标签
        self.body_area = SiLabel(self)
        self.body_area.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        self.body_area.resized.connect(lambda _: self.scroll_container.adjustSize())

        # 下面的 titledWidgetGroups
        self.titled_widget_group = SiTitledWidgetGroup(self.body_area)
        self.titled_widget_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        self.titled_widget_group.resized.connect(lambda size: self.body_area.setFixedHeight(size[1]))
        self.titled_widget_group.move(64, 0)

        # 开始搭建界面
        # 控件的线性选项卡

        self.titled_widget_group.setSpacing(16)
        self.titled_widget_group.addTitle("体验智能压缩")
        self.titled_widget_group.addWidget(WidgetsExamplePanel(self))

        self.titled_widget_group.addTitle("体验智能解压")
        self.titled_widget_group.addWidget(OptionCardsExamplePanel(self))

        self.titled_widget_group.addPlaceholder(64)

        # 添加到滚动区域容器
        self.body_area.setFixedHeight(self.titled_widget_group.height())
        self.scroll_container.addWidget(self.body_area)

        # 添加到页面
        self.setAttachment(self.scroll_container)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        w = event.size().width()
        self.body_area.setFixedWidth(w)
        self.background_image.setFixedWidth(w)
        self.titled_widget_group.setFixedWidth(w - 128)
        self.background_fading_transition.setFixedWidth(w)


class WidgetsExampleOptionCardPlane(SiOptionCardPlane):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WidgetsExamplePanel(SiDenseVContainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAdjustWidgetsSize(True)
        self.setSpacing(12)

        # 第一个水平容器
        container_h_a = SiDenseHContainer(self)
        container_h_a.setFixedHeight(500)
        container_h_a.setAdjustWidgetsSize(True)

        # 上面的两个选项卡，按钮和开关
        # 按钮
        self.option_card_button = WidgetsExampleOptionCardPlane(self)
        self.option_card_button.setTitle("智能压缩")
        self.option_card_button.body().setSpacing(5)

        option_card_button_container_h = SiDenseHContainer(self)
        option_card_button_container_h.setFixedHeight(32)

        button_a = SiPushButton(self)
        button_a.resize(128, 32)
        button_a.attachment().setText("Push Button")

        button_b = SiPushButton(self)
        button_b.resize(128, 32)
        button_b.setUseTransition(True)
        button_b.attachment().setText("Themed")

        button_c = SiLongPressButton(self)
        button_c.resize(128, 32)
        button_c.attachment().setText("Hold-to-Confirm")

        option_card_button_container_h.addWidget(button_a)
        option_card_button_container_h.addWidget(button_b)
        option_card_button_container_h.addWidget(button_c)

        self.upload_panel = UploadPanel(self)

        self.option_card_button.body().addWidget(self.upload_panel)
        self.option_card_button.body().addWidget(option_card_button_container_h)

        container_h_a.addWidget(self.option_card_button)
        # 添加两个水平容器到自己

        self.addWidget(container_h_a)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        print(event.size())
        self.option_card_button.setFixedWidth(event.size().width())
        print(self.option_card_button.container.width())
        self.upload_panel.setFixedWidth(event.size().width() - self.option_card_button.spacing())
        # self.option_card_slider.setFixedWidth(event.size().width() - 300 - 16)


class OptionCardsExamplePanel(SiDenseVContainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setAdjustWidgetsSize(True)
        self.setSpacing(12)

        # 线性选项卡
        attached_button_a = SiPushButton(self)
        attached_button_a.resize(128, 32)
        attached_button_a.attachment().setText("Attachment")

        attached_button_b = SiPushButton(self)
        attached_button_b.resize(32, 32)
        attached_button_b.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_attach_regular"))

        self.option_card_linear_attaching = SiOptionCardLinear(self)
        self.option_card_linear_attaching.setTitle("Attach Widgets",
                                                   "The linear option card provides a horizontal container where any control can be added,\nwith no limit on the number")
        self.option_card_linear_attaching.load(SiGlobal.siui.iconpack.get("ic_fluent_attach_regular"))
        self.option_card_linear_attaching.addWidget(attached_button_a)
        self.option_card_linear_attaching.addWidget(attached_button_b)

        # <- ADD
        self.addWidget(self.option_card_linear_attaching)

        # 平面选项卡
        header_button = SiSimpleButton(self)
        header_button.setFixedHeight(32)
        header_button.attachment().setText("Header Attachment")
        header_button.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_window_header_horizontal_regular"))
        header_button.adjustSize()

        body_label = SiLabel(self)
        body_label.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
        body_label.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_B"]))
        body_label.setText("SiOptionCardPlane provides three containers: header, body, and footer."
                           "\nHeader and Footer are SiDenseHContainer, while body is a SiDenseVContainer."
                           "\nHere is the body container, where you can realize your interface function. Enjoy it!")

        footer_button_a = SiSimpleButton(self)
        footer_button_a.resize(32, 32)
        footer_button_a.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_pen_regular"))
        footer_button_a.setHint("Draw")

        footer_button_b = SiSimpleButton(self)
        footer_button_b.resize(32, 32)
        footer_button_b.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_eyedropper_regular"))
        footer_button_b.setHint("Eyedropper")

        footer_button_c = SiSimpleButton(self)
        footer_button_c.resize(32, 32)
        footer_button_c.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_save_regular"))
        footer_button_c.setHint("Save")

        self.option_card_plane_beginning = SiOptionCardPlane(self)
        self.option_card_plane_beginning.setTitle("Plane Option Card")
        self.option_card_plane_beginning.header().addWidget(header_button, side="right")
        self.option_card_plane_beginning.body().addWidget(body_label, side="top")
        self.option_card_plane_beginning.footer().setFixedHeight(64)
        self.option_card_plane_beginning.footer().setSpacing(8)
        self.option_card_plane_beginning.footer().setAlignment(Qt.AlignCenter)
        self.option_card_plane_beginning.footer().addWidget(footer_button_a, side="left")
        self.option_card_plane_beginning.footer().addWidget(footer_button_b, side="left")
        self.option_card_plane_beginning.footer().addWidget(footer_button_c, side="left")
        self.option_card_plane_beginning.adjustSize()

        # <- ADD
        self.addWidget(self.option_card_plane_beginning)

        # 解释按钮
        button_description = SiSimpleButton(self)
        button_description.attachment().setText("See More")
        button_description.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_apps_add_in_regular"))
        button_description.colorGroup().assign(SiColor.BUTTON_OFF, "#2C2930")
        button_description.colorGroup().assign(SiColor.BUTTON_ON, "#2C2930")
        button_description.reloadStyleSheet()
        button_description.resize(210, 32)

        # 查看更多容器
        container_v_button = SiDenseVContainer(self)
        container_v_button.setAlignment(Qt.AlignCenter)
        container_v_button.addWidget(button_description)

        self.addWidget(container_v_button)


class UploadPanel(SiLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spacing_ = 24
        # self.setFixedHeight(100)
        self.setFixedHeight(300)
        self.setCursor(Qt.PointingHandCursor)

        # 构建组成外观的控件
        self.outfit_label_lower = SiLabel(self)
        self.outfit_label_lower.setFixedStyleSheet("border: 1.5px dashed #3b373f; border-radius: 12px")
        # self.outfit_label_lower.setFixedStyleSheet("border-radius: 6px")
        # self.outfit_label_lower.setFixedStyleSheet("border-radius: 6px")

        self.outfit_label_upper = SiLabel(self)
        self.outfit_label_upper.setFixedStyleSheet("border: 1.5px dashed #3b373f; border-radius: 12px")

        self.demo_simple_button_a = SiSimpleButton(self)
        self.demo_simple_button_a.resize(96, 32)
        self.demo_simple_button_a.attachment().load(
            b'<svg t="1744106682523" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4422" width="64" height="64"><path d="M239.317333 810.666667l-8.533333-1.28C173.226667 801.152 128 750.805333 128 689.152c0-51.157333 31.146667-94.72 75.050667-112.725333L256.170667 554.666667 256 495.36a213.333333 213.333333 0 0 1 420.437333-51.328l15.189334 61.354667 63.104 3.370666C832.853333 512.853333 896 578.346667 896 659.584c0 84.053333-67.413333 151.04-149.333333 151.04H725.333333v85.333333h21.333334c129.621333 0 234.666667-105.813333 234.666666-236.373333 0-126.293333-98.304-229.461333-222.08-236.074667A298.666667 298.666667 0 0 0 170.666667 495.488v1.962667a206.933333 206.933333 0 0 0-128 191.658666c0 104.192 76.458667 190.421333 175.957333 204.8v2.048H298.666667v-85.333333H239.317333z" fill="#bfbfbf" p-id="4423"></path><path d="M512 512l219.477333 219.477333h-120.704L512 632.618667l-98.858667 98.858666H292.522667L512 512z" fill="#bfbfbf" p-id="4424"></path><path d="M554.666667 597.333333v298.666667h-85.333334v-298.666667h85.333334z" fill="#bfbfbf" p-id="4425"></path></svg>')
        self.demo_simple_button_a.attachment().setSvgSize(64, 64)
        self.demo_simple_button_a.setHint("点击上传文件")
        self.demo_simple_button_a.setBorderRadius(12)

    def adjustSize(self):
        print(1)
        self.resize(self.width(), 3)

    def reloadStyleSheet(self):
        print(2)
        super().reloadStyleSheet()

        self.outfit_label_lower.setStyleSheet("background-color: {}".format(SiGlobal.siui.colors["INTERFACE_BG_C"]))
        self.outfit_label_upper.setStyleSheet("background-color: {}".format(SiGlobal.siui.colors["INTERFACE_BG_C"]))

    def spacing(self):
        print(3)
        """
        获取容器与边缘左右的间隔
        :return: 间隔
        """
        return self.spacing_

    def resizeEvent(self, event):
        super().resizeEvent(event)
        size = event.size()
        print(size)
        w, h = size.width(), size.height()
        print(w, h)
        self.demo_simple_button_a.setGeometry(0, 0, w-32, h)

        self.outfit_label_lower.setGeometry(0, 8, w-32, h-8)  # 防止上边出现底色毛边
        self.outfit_label_upper.resize(w-32, h)
