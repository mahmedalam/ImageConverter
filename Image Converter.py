import sys
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PIL import Image
import pillow_avif
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.exportBtn.setEnabled(False)
        self.window.show()

        self.ui.openBtn.clicked.connect(lambda: self.openFile())
        self.ui.exportBtn.clicked.connect(lambda: self.saveFile())


    def openFile(self):
        self.openFilePath = QFileDialog.getOpenFileName(self, "Open File", "", "All Supported Images(*.png *.jpg *.jpeg *.webp *.avif)")[0]
        if self.openFilePath:
            self.ui.exportBtn.setEnabled(True)

    def saveFile(self):
        self.saveFilePath = QFileDialog.getSaveFileName(self, "Save File", "", "All Supported Images(*.png *.jpeg *.webp)")[0]
        if self.saveFilePath:
            self.ui.exportBtn.setEnabled(False)
            threading.Thread(target=self.converter, args=[]).start()


    def converter(self):
        # PNG
        if self.ui.typeComboBox.currentText() == "PNG":
            img = Image.open(self.openFilePath)
            if self.saveFilePath.endswith(".png"):
                img.save(self.saveFilePath, format="PNG")
            else:
                img.save(f"{self.saveFilePath}.png", format="PNG")

        # JPEG
        if self.ui.typeComboBox.currentText() == "JPEG":
            img = Image.open(self.openFilePath)
            img = img.convert("RGB")
            if self.saveFilePath.endswith(".jpeg"):
                img.save(self.saveFilePath, format="JPEG", quality=100, optimize=True)
            else:
                img.save(f"{self.saveFilePath}.jpeg", format="JPEG", quality=50, optimize=True)

        # WEBP
        if self.ui.typeComboBox.currentText() == "WEBP":
            img = Image.open(self.openFilePath)
            if self.saveFilePath.endswith(".webp"):
                img.save(self.saveFilePath, format="WEBP")
            else:
                img.save(f"{self.saveFilePath}.webp", format="WEBP")

        self.ui.exportBtn.setEnabled(True)




app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
