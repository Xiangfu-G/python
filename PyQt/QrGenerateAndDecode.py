from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QFileDialog, QSlider, QLabel
from PyQt5.QtGui import QPalette, QPixmap, QIcon
from PyQt5.QtCore import Qt
from PIL import Image
from PIL.ImageQt import ImageQt
import sys
import qrcode
import cv2
import numpy as np


# 界面
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(610, 500))
        MainWindow.setMaximumSize(QtCore.QSize(610, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(270, 330, 321, 121))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_1.setText("")
        self.pb_1.setObjectName("pb_1")
        self.gridLayout.addWidget(self.pb_1, 0, 1, 1, 1)
        self.pb_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_4.setText("")
        self.pb_4.setObjectName("pb_4")
        self.gridLayout.addWidget(self.pb_4, 0, 4, 1, 1)
        self.pb_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_5.setText("")
        self.pb_5.setObjectName("pb_5")
        self.gridLayout.addWidget(self.pb_5, 0, 5, 1, 1)
        self.pb_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_6.setText("")
        self.pb_6.setObjectName("pb_6")
        self.gridLayout.addWidget(self.pb_6, 0, 6, 1, 1)
        self.pb_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_0.setText("")
        self.pb_0.setObjectName("pb_0")
        self.gridLayout.addWidget(self.pb_0, 0, 0, 1, 1)
        self.pb_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_2.setText("")
        self.pb_2.setObjectName("pb_2")
        self.gridLayout.addWidget(self.pb_2, 0, 2, 1, 1)
        self.pb_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_3.setText("")
        self.pb_3.setObjectName("pb_3")
        self.gridLayout.addWidget(self.pb_3, 0, 3, 1, 1)
        self.pb_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_7.setText("")
        self.pb_7.setObjectName("pb_7")
        self.gridLayout.addWidget(self.pb_7, 0, 7, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 281, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_color_code = QtWidgets.QLabel(self.layoutWidget)
        self.label_color_code.setMinimumSize(QtCore.QSize(80, 0))
        self.label_color_code.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_color_code.setFont(font)
        self.label_color_code.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_code.setObjectName("label_color_code")
        self.horizontalLayout.addWidget(self.label_color_code)
        self.lineEdit_color_code = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_color_code.setObjectName("lineEdit_color_code")
        self.horizontalLayout.addWidget(self.lineEdit_color_code)
        self.pb_color_enter = QtWidgets.QPushButton(self.layoutWidget)
        self.pb_color_enter.setObjectName("pb_color_enter")
        self.horizontalLayout.addWidget(self.pb_color_enter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pb_openfile = QtWidgets.QPushButton(self.tab_2)
        self.pb_openfile.setGeometry(QtCore.QRect(24, 40, 71, 23))
        self.pb_openfile.setObjectName("pb_openfile")
        self.lineEdit_filepath = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_filepath.setGeometry(QtCore.QRect(100, 40, 161, 23))
        self.lineEdit_filepath.setObjectName("lineEdit_filepath")
        self.lineEdit_filepath.setReadOnly(True)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 70, 231, 21))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slider_depth = QtWidgets.QSlider(self.layoutWidget1)
        self.slider_depth.setOrientation(QtCore.Qt.Horizontal)
        self.slider_depth.setObjectName("slider_depth")
        self.horizontalLayout_2.addWidget(self.slider_depth)
        self.label_depth = QtWidgets.QLabel(self.layoutWidget1)
        self.label_depth.setObjectName("label_depth")
        self.horizontalLayout_2.addWidget(self.label_depth)
        self.radioButton_0 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_0.setGeometry(QtCore.QRect(30, 10, 51, 16))
        self.radioButton_0.setChecked(True)
        self.radioButton_0.setObjectName("radioButton_0")
        self.radioButton_1 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_1.setGeometry(QtCore.QRect(100, 10, 81, 16))
        self.radioButton_1.setObjectName("radioButton_1")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 231, 441))
        self.groupBox.setObjectName("groupBox")
        self.toolBox = QtWidgets.QToolBox(self.groupBox)
        self.toolBox.setGeometry(QtCore.QRect(10, 20, 211, 401))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolBox.setFont(font)
        self.toolBox.setToolTip("")
        self.toolBox.setObjectName("toolBox")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 211, 323))
        self.page_1.setObjectName("page_1")
        self.label_0 = QtWidgets.QLabel(self.page_1)
        self.label_0.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_0.setObjectName("label_0")
        self.lineEdit_url = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_url.setGeometry(QtCore.QRect(10, 30, 191, 20))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.toolBox.addItem(self.page_1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 211, 323))
        self.page_2.setObjectName("page_2")
        self.textEdit = QtWidgets.QTextEdit(self.page_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 191, 240))
        self.textEdit.setObjectName("textEdit")
        self.label_words_nums = QtWidgets.QLabel(self.page_2)
        self.label_words_nums.setGeometry(QtCore.QRect(50, 256, 95, 16))
        self.label_words_nums.setMinimumSize(QtCore.QSize(95, 0))
        self.label_words_nums.setMaximumSize(QtCore.QSize(95, 16777215))
        self.label_words_nums.setObjectName("label_words_nums")
        self.pb_clean_text = QtWidgets.QPushButton(self.page_2)
        self.pb_clean_text.setGeometry(QtCore.QRect(150, 255, 50, 20))
        self.pb_clean_text.setText("清空")
        self.pb_clean_text.setObjectName("pb_clean_text")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 211, 323))
        self.page_3.setObjectName("page_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 191, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_1.setMinimumSize(QtCore.QSize(50, 0))
        self.label_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(130, 20))
        self.lineEdit_name.setMaximumSize(QtCore.QSize(130, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_tel = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_tel.setMinimumSize(QtCore.QSize(130, 20))
        self.lineEdit_tel.setMaximumSize(QtCore.QSize(130, 20))
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tel)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_qq = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_qq.setMinimumSize(QtCore.QSize(130, 20))
        self.lineEdit_qq.setMaximumSize(QtCore.QSize(130, 20))
        self.lineEdit_qq.setObjectName("lineEdit_qq")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_qq)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_mail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_mail.setMinimumSize(QtCore.QSize(130, 20))
        self.lineEdit_mail.setMaximumSize(QtCore.QSize(130, 20))
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_mail)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_company = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_company.setMinimumSize(QtCore.QSize(130, 20))
        self.lineEdit_company.setMaximumSize(QtCore.QSize(130, 20))
        self.lineEdit_company.setObjectName("lineEdit_company")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_company)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(50, 0))
        self.label_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_website = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_website.setMinimumSize(QtCore.QSize(130, 20))
        self.lineEdit_website.setMaximumSize(QtCore.QSize(130, 20))
        self.lineEdit_website.setObjectName("lineEdit_website")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_website)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 211, 323))
        self.page_4.setObjectName("page_4")
        self.pb_openfile_decode = QtWidgets.QPushButton(self.page_4)
        self.pb_openfile_decode.setGeometry(10, 8, 100, 25)
        self.pb_openfile_decode.setObjectName("pb_openfile_decode")
        self.pb_decode = QtWidgets.QPushButton(self.page_4)
        self.pb_decode.setGeometry(120, 8, 80, 25)
        self.pb_decode.setObjectName("pb_decode")
        self.lineEdit_filepath_decode = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_filepath_decode.setGeometry(11, 40, 190, 23)
        self.lineEdit_filepath_decode.setObjectName("lineEdit_fliepath_decode")
        self.lineEdit_filepath_decode.setReadOnly(True)
        self.label_decode = QtWidgets.QLabel(self.page_4)
        self.label_decode.setGeometry(11, 70, 80, 20)
        self.label_decode.setObjectName("label_decode")
        self.result_decode = QtWidgets.QTextBrowser(self.page_4)
        self.result_decode.setGeometry(11, 95, 190, 180)
        self.result_decode.setObjectName("result_decode")
        self.toolBox.addItem(self.page_4, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 10, 321, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_result = QtWidgets.QLabel(self.groupBox_2)
        self.label_result.setGeometry(QtCore.QRect(29, 22, 261, 261))
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.label_remind = QtWidgets.QLabel(self.groupBox_2)
        self.label_remind.setGeometry(QtCore.QRect(10, 290, 111, 16))
        self.label_remind.setObjectName("label_remind")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuLanguage = QtWidgets.QMenu(self.menu)
        self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menu.addSeparator()
        self.menu.addAction(self.actionSave_as)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_color_code.setText(_translate("MainWindow", "颜色代码"))
        self.pb_color_enter.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "颜色"))
        self.pb_openfile.setText(_translate("MainWindow", "打开文件"))
        self.label_depth.setText(_translate("MainWindow", " 透明度:100%"))
        self.radioButton_0.setText(_translate("MainWindow", "logo"))
        self.radioButton_1.setText(_translate("MainWindow", "background"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图片"))
        self.groupBox.setTitle(_translate("MainWindow", "选择类型"))
        self.label_0.setText(_translate("MainWindow", "输入链接:"))
        self.lineEdit_url.setText(_translate("MainWindow", "http://"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), _translate("MainWindow", "链接"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">点击清空按钮来进行输入</p></body></html>"))
        self.label_words_nums.setText(_translate("MainWindow", "字符:    0/200"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "文本"))
        self.label_1.setText(_translate("MainWindow", "姓名"))
        self.label_2.setText(_translate("MainWindow", "电话"))
        self.label_3.setText(_translate("MainWindow", "QQ"))
        self.label_4.setText(_translate("MainWindow", "邮箱"))
        self.label_5.setText(_translate("MainWindow", "公司"))
        self.label_6.setText(_translate("MainWindow", "博客"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "名片"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "解码"))
        self.pb_openfile_decode.setText("打开二维码图片")
        self.pb_decode.setText("进行解码")
        self.label_decode.setText(_translate("MainWindow", "解码结果："))
        self.groupBox_2.setTitle(_translate("MainWindow", "二维码"))
        self.label_remind.setText(_translate("MainWindow", "按下F5获取二维码"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionSave_as.setText(_translate("MainWindow", "另存为"))


''' -------------------------------- 核心方法 -------------------------------- '''


def QR_qrcode(data, size=5, imagepath=None, color='#000000', if_background=False, depth=255):
    try:
        qr = qrcode.QRCode(
            version=4,  # 精度，默认6
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,  # 尺寸，默认5
            border=3)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=color)
        img = img.convert('RGBA')  # 设为彩色

        if imagepath != None:  # 如果打开了图片
            logo = Image.open(imagepath)  # 二维码中心的图片
            logo = logo.convert('RGBA')
            img_w, img_h = img.size  # 二维码尺寸由box_size参数设定

            if if_background == True:  # 如果选择了背景图模式
                print("背景图模式")
                logo = change(logo, depth)  # 将logo图作为背景图，调整背景图透明度
                logo = logo.resize((img_w, img_h), Image.ANTIALIAS)  # 将背景图大小缩放至和二维码图像一致
                datas = img.getdata()  # 获取二维码图像数据
                new_data = list()
                for item in datas:  # 将二维码图像中白色像素点透明化
                    if item[0] == 255 and item[1] == 255 and item[2] == 255:
                        new_data.append((255, 255, 255, 0))
                    else:
                        new_data.append(item)
                img.putdata(new_data)  # 更新二维码图像
                logo.paste(img, (0, 0), img)  # 将背景图和二维码图像重叠
                img = logo
            elif if_background == False:
                print("Logo模式")
                logo_w = int(img_w / 4)
                logo_h = int(img_h / 4)
                logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)
                w = int((img_w - logo_w) / 2)  # logo在二维码中的位置
                h = int((img_h - logo_h) / 2)
                img.paste(logo, (w, h), logo)
        return img
    except:
        pass


def change(logo, depth=255):
    x, y = logo.size
    for i in range(x):
        for j in range(y):
            # 取四个通道的值，然后用切片取前三个不变，最后一个改为指定值
            c = logo.getpixel((i, j))
            c = c[:-1] + (depth,)
            logo.putpixel((i, j), c)
    return logo


# 功能
class MaForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MaForm, self).__init__()
        self.setupUi(self)
        self.callback_function()
        # 生成的图像
        self.myImage = Image.Image()
        # 图标
        self.toolBox.setItemIcon(0, QIcon(":resource/url.ico"))
        self.toolBox.setItemIcon(1, QIcon(":resource/text.ico"))
        self.toolBox.setItemIcon(2, QIcon(":resource/card.ico"))
        self.toolBox.setItemIcon(3, QIcon(":resource/text.ico"))
        # 参数
        self.color_list = ['#000000', '#DC143C', '#FFA500', '#FFD700', '#90EE90',
                           '#40E0D0', '#00BFFF', '#BA55D3']  # 颜色列表
        self.color_now = '#000000'  # 默认为黑色
        self.edit_list = ['lineEdit_url', 'lineEdit_name', 'lineEdit_tel', 'lineEdit_qq', 'lineEdit_mail',
                          'lineEdit_company', 'lineEdit_website', 'lineEdit_color_code', 'lineEdit_filepath',
                          ]  # 文本框列表

        # 界面控件设置
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.white)
        self.label_result.setAutoFillBackground(True)
        self.label_result.setPalette(palette)  # 设置结果图区域的label为白色背景
        self.slider_depth.setValue(100)  # 滑块默认值100
        self.slider_depth.setTickPosition(QSlider.TicksAbove)  # 设置刻度的位置，刻度在下方
        self.slider_depth.setSingleStep(10)
        self.slider_depth.setTickInterval(20)  # 设置刻度的间隔
        # self.actionEnglish.setChecked(True)  # 默认为英文界面
        for n in range(0, len(self.edit_list)):  # 设置文本框清空提示，多行文本无该功能
            getattr(self, self.edit_list[n]).setClearButtonEnabled(True)
        for n in range(0, len(self.color_list)):  # 设置按钮颜色
            getattr(self, 'pb_%s' % n).setStyleSheet("background-color: " + self.color_list[n])

    # 连接槽函数
    def callback_function(self):
        self.pb_clean_text.clicked.connect(self.clean_words)  # 清空多行文本
        self.textEdit.textChanged.connect(self.show_words)  # 显示字数
        self.pb_openfile_decode.clicked.connect(self.openFile_decode)
        self.pb_openfile.clicked.connect(self.openFile)  # 打开图片
        self.pb_decode.clicked.connect(self.decode)  # 进行解码
        self.slider_depth.valueChanged.connect(self.setDepth)  # 更改透明度
        self.slider_depth.sliderReleased.connect(self.getQR)  # 释放滑块时执行生成 ->
        self.radioButton_0.toggled.connect(self.getQR)  # 单选按钮切换时执行生成 ->
        self.pb_color_enter.clicked.connect(self.change2logo)
        self.pb_color_enter.clicked.connect(self.set_myColor)  # 点击Enter按钮设置颜色，同时修改单项按钮为logo项，并并执行生成 ->
        for n in range(0, 8):  # 颜色按钮被点击时更改颜色代码, 同时修改单项按钮为logo项，并执行生成 ->
            getattr(self, 'pb_%s' % n).pressed.connect(lambda c=n: self.setColor(c))
            getattr(self, 'pb_%s' % n).pressed.connect(self.change2logo)
            getattr(self, 'pb_%s' % n).pressed.connect(self.getQR)
        self.actionSave_as.triggered.connect(self.saveAs)  # 菜单栏-另存为
        self.toolBox.currentChanged.connect(self.show_status)  # 选择不同栏目时在状态栏显示说明信息

    # 清空输入
    def clean_words(self):
        self.textEdit.setText("")

    # 显示字数
    def show_words(self):
        nums = len(self.textEdit.toPlainText())
        self.label_words_nums.setText(self.tr('字符: ') + ' ' * (3 - len(str(nums))) + f'{nums}/200')
        if nums >= 200:
            QMessageBox.about(self, self.tr('提示'), self.tr('字数限制在200以内！'))
            self.textEdit.setReadOnly(True)
        else:
            self.textEdit.setReadOnly(False)

    # 重写键盘事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.textEdit.setReadOnly(False)
        if event.key() == Qt.Key_F5:
            self.getQR()

    # 打开二维码图片
    def openFile_decode(self):
        filepath, filetype = QFileDialog.getOpenFileName(self, self.tr('选择图片'), './', '(*.jpg);;(*.png)')
        self.lineEdit_filepath_decode.setText(filepath)

    # 二维码解码
    def decode(self):
        dec = cv2.QRCodeDetector()
        val, _, _ = dec.detectAndDecode(
            cv2.imdecode(np.fromfile(self.lineEdit_filepath_decode.text(), dtype=np.uint8), 1))
        self.result_decode.setText(val)

    # 设置默认颜色按钮
    def setColor(self, c):
        self.color_now = self.color_list[c]
        self.lineEdit_color_code.setText(self.color_now)

    # 手动设置颜色代码
    def set_myColor(self):
        if self.lineEdit_color_code.text() != "":
            self.color_now = self.lineEdit_color_code.text()
        self.getQR()

    # 选中logo项
    def change2logo(self):
        self.radioButton_0.setChecked(True)

    # 打开图片文件
    def openFile(self):
        filepath, filetype = QFileDialog.getOpenFileName(self, self.tr('选择图片'), './', '(*.jpg);;(*.png)')
        self.lineEdit_filepath.setText(filepath)

    # 显示图片透明度
    def setDepth(self):
        d = self.slider_depth.value()
        self.label_depth.setText(' 透明度:' + ' ' * (3 - len(str(d))) + '%s%%' % d)

    # 生成二维码
    def getQR(self):
        data_flag = self.toolBox.currentIndex()  # 数据类型（所选栏目）
        data = ''
        if data_flag == 0:  # URL
            data = self.lineEdit_url.text()
        elif data_flag == 1:  # TEXT
            data = self.textEdit.toPlainText()
        elif data_flag == 2:  # CARD
            name = self.lineEdit_name.text()
            tel = self.lineEdit_tel.text()
            qq = self.lineEdit_qq.text()
            mail = self.lineEdit_mail.text()
            company = self.lineEdit_company.text()
            website = self.lineEdit_website.text()
            data = f'MECARD:N:{name};ORG:{company};TEL:{tel};EMAIL:{mail};URL:{website};NOTE:QQ :{qq};'  # MECARD格式的电子名片
        color = self.color_now  # 颜色
        imagepath = self.lineEdit_filepath.text()  # 图片路径
        depth = float(self.slider_depth.value()) / 100  # 透明度
        filetype = imagepath[imagepath.rfind('.'):].lower()  # 文件后缀小写
        path = imagepath[:imagepath.rfind('.')] + filetype  # 重置路径
        # 执行生成
        try:
            if self.radioButton_0.isChecked() and imagepath != '':  # 选择logo且打开了图片
                print("选择了Logo，执行QR_qrcode")
                imgfile = QR_qrcode(data, imagepath=path, color=color)
            elif self.radioButton_1.isChecked() and imagepath != '':  # 选择background且打开了图片
                print("选择Background，执行QR_qrcode")
                dialog = WaitDialog()
                dialog.show()
                imgfile = QR_qrcode(data, size=5, imagepath=path, color='#000000', if_background=True,
                                    depth=int(depth * 255))
            elif imagepath == '':  # 无图
                print("无图，执行QR_qrcode")
                imgfile = QR_qrcode(data, color=color)
            self.myImage = imgfile
            pix = QPixmap.fromImage(ImageQt(imgfile))
            pix = pix.scaled(self.label_result.width(), self.label_result.height())
            self.label_result.setPixmap(pix)  # 加载图片
        except:
            pass

    # 另存为
    def saveAs(self):
        try:
            img = self.myImage
            filepath, filetype = QFileDialog.getSaveFileName(self, self.tr("保存二维码图片为"), 'test_qr.png',
                                                             '(*.png)')
            img.save(filepath)
        except:
            QMessageBox.about(self, self.tr('提示'), self.tr('没有生成新的二维码！'))

    # 状态栏
    def show_status(self):
        msg = 'hhh'
        data_flag = self.toolBox.currentIndex()  # 数据类型（所选栏目）
        if data_flag == 0:  # 链接
            msg = self.tr(' ---> 说明：请输入正确的链接')
        elif data_flag == 1:  # 文本
            msg = self.tr(' ---> 说明：请输入无格式文本')
        elif data_flag == 2:  # 名片
            msg = self.tr(' ---> 说明：请填写个人名片')
        elif data_flag == 3:  # 解码
            msg = self.tr(' ---> 说明：请选择图片开始解码')
        self.statusbar.showMessage(msg, 4600)


# 参数设置弹窗
class WaitDialog(QDialog):
    def __init__(self):
        super(WaitDialog, self).__init__()
        self.setWindowTitle("等待")
        self.resize(180, 40)
        self.lb = QLabel("请稍等......", self)
        self.lb.resize(170, 30)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MaForm()
    w.setWindowTitle("二维码生成与解码")
    w.show()
    sys.exit(app.exec())
