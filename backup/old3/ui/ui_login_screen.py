from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(LoginScreen)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.line_username = QtWidgets.QLineEdit()
        self.line_username.setPlaceholderText("Usuário")
        self.verticalLayout.addWidget(self.line_username)
        self.line_password = QtWidgets.QLineEdit()
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setPlaceholderText("Senha")
        self.verticalLayout.addWidget(self.line_password)
        self.btn_login = QtWidgets.QPushButton("Entrar")
        self.verticalLayout.addWidget(self.btn_login)
        self.label_status = QtWidgets.QLabel("")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_status)
        LoginScreen.setCentralWidget(self.centralwidget)
        self.retranslateUi(LoginScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "Login"))
