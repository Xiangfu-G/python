from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QSlider
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt
import sys
import QrMineWindow
from PIL import Image
import qrcode
from MyQR import myqr
import os


class Qr(QMainWindow, QrMineWindow.Ui_MainWindow):
    def __init__(self):
        super(Qr, self).__init__()
        self.setupUi(self)
        self.show_words()
        self.callback_function()
        # 颜色列表
        self.color_list = ['#000000', '#DC143C', '#FFA500', '#FFD700', '#90EE90',
                           '#40E0D0', '#00BFFF', '#BA55D3']
        # 界面控件设置
        for n in range(0, len(self.color_list)):  # 设置按钮颜色
            getattr(self, 'pb_%s' % n).setStyleSheet("background-color: " + self.color_list[n])

        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.white)
        self.label_result.setAutoFillBackground(True)
        self.label_result.setPalette(palette)  # 设置结果图区域的label为白色背景
        self.slider_depth.setValue(100)  # 滑块默认值100
        self.slider_depth.setTickPosition(QSlider.TicksAbove)  # 设置刻度的位置，刻度在下方
        self.slider_depth.setTickInterval(20)  # 设置刻度的间隔
        self.slider_depth.setSingleStep(10)

    def callback_function(self):
        self.pb_clean_text.clicked.connect(self.clean_words)
        self.textEdit.textChanged.connect(self.show_words)
        self.pb_color_enter.clicked.connect(self.change2logo)
        self.pb_color_enter.clicked.connect(self.set_myColor)
        self.pb_openfile.clicked.connect(self.openFile)
        self.slider_depth.valueChanged.connect(self.setDepth)
        # self.actionSave_as.triggered.connect(self.saveAs)
        self.toolBox.currentChanged.connect(self.show_status)

    # 显示字数
    def show_words(self):
        nums = len(self.textEdit.toPlainText())
        self.label_words_nums.setText(self.tr('Length: ') + ' ' * (3 - len(str(nums))) + f'{nums}/200')
        if nums > 200:
            QMessageBox.about(self, self.tr('Remind'), self.tr('Limit words to 200 !'))

    # 清空输入
    def clean_words(self):
        self.textEdit.setText("")

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
        # 执行生成二维码
        try:
            if self.radioButton_0.isChecked() and imagepath != '':  # 选择logo且打开了图片
                self.QR_qrcode(data, imagepath=imagepath, color=color)
            elif self.radioButton_1.isChecked() and imagepath != '':  # 选择background且打开了图片
                if filetype == ".gif":
                    QMessageBox.about(self, self.tr("Remind"), self.tr(
                        "Detected as GIF image, please wait...\n(*Note: transparency cannot be modified)"))
                    self.QR_myqr(data, path, 'test_qr.gif', size=3)  # gif底图缩小尺寸，限制透明度不变
                    QMessageBox.about(self, self.tr("Remind"),
                                      self.tr("Please check the generated GIF in the root directory !"))
                else:
                    self.QR_myqr(data, path, 'test_qr.png', contrast=depth)
            elif imagepath == '':  # 无图
                self.QR_qrcode(data, color=color)
            file = 'test_qr.png' if filetype != ".gif" else 'test_qr.gif'
            img = QPixmap(file).scaled(self.label_result.width(), self.label_result.height())  # 裁剪图片
            self.label_result.setPixmap(img)  # 加载图片

        except:
            pass
        # 颜色按钮被点击时更改颜色代码, 同时修改单项按钮为logo项，并执行生成
        for n in range(0, 8):
            getattr(self, 'pb_%s' % n).pressed.connect(lambda c=n: self.setColor(c))
            getattr(self, 'pb_%s' % n).pressed.connect(self.change2logo)
            getattr(self, 'pb_%s' % n).pressed.connect(self.getQR)

    def QR_qrcode(data, size=5, imagepath=None, color='#000000'):
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
                img_w, img_h = img.size  # 二维码尺寸由box_size参数设定
                # logo_w, logo_h = logo.size  # logo图片尺寸
                logo_w = int(img_w / 4)
                logo_h = int(img_h / 4)
                logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)
                w = int((img_w - logo_w) / 2)  # logo在二维码中的位置
                h = int((img_h - logo_h) / 2)
                logo = logo.convert('RGBA')
                img.paste(logo, (w, h), logo)

            img.save('test_qr.png')
        except:
            pass

    def QR_myqr(data, imagepath, filename, size=8, contrast=1.0):
        try:
            print("------\nbackground-image path:", imagepath)
            myqr.run(
                words=data,
                version=size,  # 大小1~40，默认8
                level='H',  # 纠错级别
                picture=imagepath,  # 底图
                colorized=True,  # 彩色
                contrast=contrast,  # 对比度
                brightness=1.0 + (1 - contrast),  # 亮度
                save_name=filename,
                save_dir=os.getcwd()  # 当前目录
            )
            print('get version_back')
        except:
            print('warning: background error')

    # 设置默认颜色按钮
    def setColor(self, c):
        self.color_now = self.color_list[c]
        self.lineEdit_color_code.setText(self.color_now)

    # 选中logo项
    def change2logo(self):
        self.radioButton_0.setChecked(True)

    # 手动设置颜色代码
    def set_myColor(self):
        if self.lineEdit_color_code.text() != "":
            self.color_now = self.lineEdit_color_code.text()
        self.getQR()

    # 打开图片文件
    def openFile(self):
        filepath, filetype = QFileDialog.getOpenFileName(self, self.tr('Choose image'), './',
                                                         '(*.png);;(*.jpg);;(*.gif)')
        self.lineEdit_filepath.setText(filepath)

    # 显示图片透明度
    def setDepth(self):
        d = self.slider_depth.value()
        self.label_depth.setText(' Depth:' + ' ' * (3 - len(str(d))) + '%s%%' % d)

    '''
    # 另存为
    def saveAs(self):
        try:
            img = Image.open('test_qr.png')
            filepath, filetype = QFileDialog.getSaveFileName(self, self.tr("Save QRcode image as"), 'test_qr.png',
                                                             '(*.png);;(*.gif)')
            img.save(filepath)
        except:
            QMessageBox.about(self, self.tr('Remind'), self.tr('No new QR code generated !'))
    '''

    # 状态栏消息
    def show_status(self):
        data_flag = self.toolBox.currentIndex()  # 数据类型（所选栏目）
        if data_flag == 0:  # URL
            msg = self.tr(' ---> Explain: Input the link address according to the format')
        elif data_flag == 1:  # TEXT
            msg = self.tr(' ---> Explain: Input unformatted text')
        elif data_flag == 2:  # CARD
            msg = self.tr(' ---> Explain: Electronic business card in MECARD format')
        elif data_flag == 3:  # HTML
            msg = self.tr(' ---> Explain: The function has not been realized yet...')
        self.statusbar.showMessage(msg, 4600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qr = Qr()
    qr.show()
    sys.exit(app.exec_())
