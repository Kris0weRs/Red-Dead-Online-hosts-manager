import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

class Programm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('files/RDO password manager.ui', self)
        self.setWindowTitle('RDO hosts manager')
        self.pathing.hide()
        self.clearing.hide()
        self.right.clicked.connect(self.right_clicked)
        self.left.clicked.connect(self.left_clicked)
        self.add.clicked.connect(self.add_clicked)
        self.something.clicked.connect(self.something_clicked)
        self.pathing.clicked.connect(self.pathing_clicked)
        self.clearing.clicked.connect(self.clearing_clicked)

        self.del1.clicked.connect(self.del1_clicked)
        self.del2.clicked.connect(self.del2_clicked)
        self.del3.clicked.connect(self.del3_clicked)
        self.del4.clicked.connect(self.del4_clicked)
        self.del5.clicked.connect(self.del5_clicked)

        self.b1.clicked.connect(self.b1_clicked)
        self.b2.clicked.connect(self.b2_clicked)
        self.b3.clicked.connect(self.b3_clicked)
        self.b4.clicked.connect(self.b4_clicked)
        self.b5.clicked.connect(self.b5_clicked)
        self.alls.clicked.connect(self.all_clicked)

        self.path = f'{os.environ.get("USERPROFILE")}/AppData/Local/RDO password manager'
        self.shit = '<?xml version="1.0" encoding="UTF-8"?>\n<CDataFileMgr__ContentsOfDataFileXml>\n <disabledFiles />\n <includedXmlFiles itemType="CDataFileMgr__DataFileArray" />\n <includedDataFiles />\n <dataFiles itemType="CDataFileMgr__DataFile">\n  <Item>\n   <filename>platform:/data/cdimages/scaleform_platform_pc.rpf</filename>\n   <fileType>RPF_FILE</fileType>\n  </Item>\n  <Item>\n   <filename>platform:/data/ui/value_conversion.rpf</filename>\n   <fileType>RPF_FILE</fileType>\n  </Item>\n  <Item>\n   <filename>platform:/data/ui/widgets.rpf</filename>\n   <fileType>RPF_FILE</fileType>\n  </Item>\n  <Item>\n   <filename>platform:/textures/ui/ui_photo_stickers.rpf</filename>\n   <fileType>RPF_FILE</fileType>\n  </Item>\n  <Item>\n   <filename>platform:/textures/ui/ui_platform.rpf</filename>\n   <fileType>RPF_FILE</fileType>\n  </Item>\n  <Item>\n   <filename>platform:/data/ui/stylesCatalog</filename>\n   <fileType>aWeaponizeDisputants</fileType> <!-- collision -->\n  </Item>\n  <Item>\n   <filename>platform:/data/cdimages/scaleform_frontend.rpf</filename>\n   <fileType>RPF_FILE_PRE_INSTALL</fileType>\n  </Item>\n  <Item>\n   <filename>platform:/textures/ui/ui_startup_textures.rpf</filename>\n   <fileType>RPF_FILE</fileType>\n  </Item>\n  <Item>\n   <filename>platform:/data/ui/startup_data.rpf</filename>\n   <fileType>RPF_FILE</fileType>\n  </Item>\n	<Item>\n		<filename>platform:/boot_launcher_flow.#mt</filename>\n		<fileType>STREAMING_FILE</fileType>\n		<registerAs>boot_flow/boot_launcher_flow</registerAs>\n		<overlay value="false" />\n		<patchFile value="false" />\n	</Item>\n </dataFiles>\n <contentChangeSets itemType="CDataFileMgr__ContentChangeSet" />\n <patchFiles />\n</CDataFileMgr__ContentsOfDataFileXml>'
        self.setting = False
        self.fuck = False
        self.check_files()
        self.count = 1
        self.counter = 1
        self.update()
        self.update_page()

    def check_files(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        if not os.path.exists(self.path + '/passwords'):
            with open(self.path + '/passwords', 'x') as file:
                file.write('')
        if not os.path.exists(self.path + '/path'):
            self.log.setText("Путь папки отсутствует")
            self.add.setText("Добавить путь папки")
            self.alls.hide()
            self.something.hide()
            self.hide()
            self.setting = True

    def add_clicked(self):
        if not self.setting:
            if not self.intext.toPlainText() == '':
                with open(self.path + '/passwords') as file:
                    txt = file.read().split()
                    txt.append(self.intext.toPlainText())
                    with open(self.path + '/passwords', 'w') as file:
                        file.write(' '.join(txt))
                self.log.setText("Был добавлен " + self.intext.toPlainText())
            self.update()
            self.update_page()
        else:
            if os.path.exists(self.intext.toPlainText()):
                with open(self.path + '/path', 'x') as file:
                    if "startup.meta" in self.intext.toPlainText():
                        file.write(self.intext.toPlainText())
                    else:
                        file.write(self.intext.toPlainText() + "/startup.meta")
                self.setting = False
                self.add.setText("Добавить")
                self.alls.show()
                self.something.show()
                self.update()
                self.update_page()
                self.log.setText("Путь установлен")
            else:
                self.log.setText('Такого пути не существует')
        self.intext.clear()

    def pathing_clicked(self):
        os.remove(self.path + "/path")
        self.something_clicked()
        self.check_files()

    def clearing_clicked(self):
        with open(self.path + '/passwords', 'w') as file:
            file.write('')
        self.something_clicked()

    def something_clicked(self):
        if not self.fuck:
            self.pathing.show()
            self.clearing.show()
            self.alls.hide()
            self.intext.hide()
            self.hide()
            self.fuck = True
        else:
            self.pathing.hide()
            self.clearing.hide()
            self.alls.show()
            self.intext.show()
            self.update()
            self.update_page()
            self.fuck = False


    def b1_clicked(self):
        self.choosing(self.pass1.text())

    def b2_clicked(self):
        self.choosing(self.pass2.text())

    def b3_clicked(self):
        self.choosing(self.pass3.text())

    def b4_clicked(self):
        self.choosing(self.pass4.text())

    def b5_clicked(self):
        self.choosing(self.pass5.text())

    def all_clicked(self):
        self.choosing('')

    def del1_clicked(self):
        self.deleting(0)

    def del2_clicked(self):
        self.deleting(1)

    def del3_clicked(self):
        self.deleting(2)

    def del4_clicked(self):
        self.deleting(3)

    def del5_clicked(self):
        self.deleting(4)

    def deleting(self, what):
        with open(self.path + '/passwords') as file:
            txt = file.read().split()
            sus = txt[what + (5 * (self.count - 1))]
            txt.pop(what + (5 * (self.count - 1)))
            with open(self.path + '/passwords', 'w') as file:
                file.write(' '.join(txt))
        self.log.setText(" Был удалён " + str(sus))
        self.update()
        self.update_page()

    def choosing(self, what):
        with open(self.path + '/path') as file:
            txt = file.read()
            if what != '':
                with open(txt, 'w') as file:
                    file.write(self.shit + str(what))
            else:
                if os.path.exists(txt):
                    os.remove(txt)
        if what != '':
            self.log.setText("Был выбран " + str(what))
        else:
            self.log.setText("Был выбран общий сервер")

    def right_clicked(self):
        if self.count < self.counter:
            self.count += 1
        self.update()
        self.update_page()

    def left_clicked(self):
        if self.count > 1:
            self.count -= 1
        self.update()
        self.update_page()

    def update_page(self):
        self.num.setText(str(self.count) + "/" + str(self.counter))

    def hide(self):
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.pass1.hide()
        self.pass2.hide()
        self.pass3.hide()
        self.pass4.hide()
        self.pass5.hide()
        self.del1.hide()
        self.del2.hide()
        self.del3.hide()
        self.del4.hide()
        self.del5.hide()

    def showing(self, nun, text):
        if nun == 1:
            self.b1.show()
            self.pass1.show()
            self.pass1.setText(text)
            self.del1.show()
        if nun == 2:
            self.b2.show()
            self.pass2.show()
            self.pass2.setText(text)
            self.del2.show()
        if nun == 3:
            self.b3.show()
            self.pass3.show()
            self.pass3.setText(text)
            self.del3.show()
        if nun == 4:
            self.b4.show()
            self.pass4.show()
            self.pass4.setText(text)
            self.del4.show()
        if nun == 5:
            self.b5.show()
            self.pass5.show()
            self.pass5.setText(text)
            self.del5.show()

    def update(self):
        with open(self.path + '/passwords') as file:
            txt = file.read().split()
            c = len(txt)
            self.counter = 1
            while c > 5:
                self.counter += 1
                c -= 5
            self.hide()
            if self.counter < self.count:
                self.count = self.counter
            if self.count == self.counter:
                if c >= 1:
                    self.showing(1, txt[0 + (5 * (self.count - 1))])
                if c >= 2:
                    self.showing(2, txt[1 + (5 * (self.count - 1))])
                if c >= 3:
                    self.showing(3, txt[2 + (5 * (self.count - 1))])
                if c >= 4:
                    self.showing(4, txt[3 + (5 * (self.count - 1))])
                if c >= 5:
                    self.showing(5, txt[4 + (5 * (self.count - 1))])
            else:
                self.showing(1, txt[0 + (5 * (self.count - 1))])
                self.showing(2, txt[1 + (5 * (self.count - 1))])
                self.showing(3, txt[2 + (5 * (self.count - 1))])
                self.showing(4, txt[3 + (5 * (self.count - 1))])
                self.showing(5, txt[4 + (5 * (self.count - 1))])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programm()
    ex.show()
    sys.exit(app.exec_())