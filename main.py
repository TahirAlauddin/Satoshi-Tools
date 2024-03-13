from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from ui_welcome import Ui_MainWindow
from ui_main import Ui_MainWindow as Ui_HomeWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Ui_Components()
        
    # This method initializes UI components.
    def Ui_Components(self):
        self.ui.openSoftwareBtn.clicked.connect(self.openSoftware)
        self.ui.haveLicenseBtn.clicked.connect(self.haveLicense)
        self.ui.buyLicenseBtn.clicked.connect(self.buyLicense)
        self.ui.centralwidget.setStyleSheet(self.ui.centralwidget.styleSheet() + f'* {{ background: #011526; color: #F2F0D8; font: 9pt "{fontName}"; }}' )


    def buyLicense(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('www.satoshitools.com'))

    def haveLicense(self):
        # This will instantiate the main app window and show it
        self.homeWindow = HomeWindow()
        self.homeWindow.show()
        self.close()  # Close the current welcome window

    def openSoftware(self):
        # This function performs the same action as haveLicense, assuming both buttons lead to the main app
        self.homeWindow = HomeWindow()
        self.homeWindow.show()
        self.close()  # Close the welcome window
        
    
class HomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()

        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        self.Ui_components()

    def Ui_components(self):
        self.ui.flashBtn.clicked.connect(self.viewBlockchain)
        self.ui.contactBtnLabel.mousePressEvent = self.contactSatoshi
        self.ui.loadWalletBtn.clicked.connect(self.loadWallet)
        self.ui.viewBlockchainBtn.clicked.connect(self.sendFlash)
        self.ui.reloadBtn.clicked.connect(self.reload)
        self.ui.stylesheet.setStyleSheet(self.ui.stylesheet.styleSheet() + f'* {{ background: #011526; color: #F2F0D8; font: 9pt "{fontName}"; }}' )


    def sendFlash(self):
        # Displays a notification message when the send flash button is clicked
        QtWidgets.QMessageBox.information(self, "Notification", "No transactions yet. Send flash coins to view.")

    def contactSatoshi(self, event):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('www.satoshitools.com'))

    def loadWallet(self):
        # Opens a file dialog to let the user select a wallet file
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Wallet File", "", "All Files (*)", options=options)
        if fileName:
            # Show a message popup confirming the file upload
            QtWidgets.QMessageBox.information(self, "File Uploaded", f"Wallet file '{fileName}' was successfully uploaded.")
            self.ui.lineEdit.setText(fileName)

    def viewBlockchain(self):
        # Shows an unactivated project message with a Buy License button
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Unactivated Project")
        msgBox.setText("Buy licence now with a button.")
        buyLicenseButton = msgBox.addButton("Buy Licence", QtWidgets.QMessageBox.ActionRole)
        msgBox.addButton(QtWidgets.QMessageBox.Cancel)
        msgBox.exec_()

        if msgBox.clickedButton() == buyLicenseButton:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl('www.satoshitools.com'))

    def reload(self):
        # TODO: Implement functionality to reload the view or data
        pass


if __name__ == '__main__':    
    
    app = QtWidgets.QApplication(sys.argv)
    fontpath = 'ARMTBR.ttf'
    fontName = "Arial Rounded MT Bold"
    try:
        # Load the TTF font file
        fontId = QtGui.QFontDatabase.addApplicationFont(fontpath)
        if fontId == -1:
            print("Failed to load font")
        else:
            # Get the font family name
            fontFamilies = QtGui.QFontDatabase.applicationFontFamilies(fontId)
            if fontFamilies:
                fontName = fontFamilies[0]
    except:
        print("error")

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
