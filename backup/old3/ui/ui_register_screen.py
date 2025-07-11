from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterScreen(object):
    def setupUi(self, RegisterScreen):
        RegisterScreen.setObjectName("RegisterScreen")
        RegisterScreen.resize(400, 250)
        self.centralwidget = QtWidgets.QWidget(RegisterScreen)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.line_username = QtWidgets.QLineEdit()
        self.line_username.setPlaceholderText("Usuário")
        self.verticalLayout.addWidget(self.line_username)
        self.line_password = QtWidgets.QLineEdit()
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setPlaceholderText("Senha")
        self.verticalLayout.addWidget(self.line_password)
        self.line_confirm_password = QtWidgets.QLineEdit()
        self.line_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_confirm_password.setPlaceholderText("Confirmar Senha")
        self.verticalLayout.addWidget(self.line_confirm_password)
        self.combo_role = QtWidgets.QComboBox()
        self.combo_role.addItem("Usuário")
        self.combo_role.addItem("Administrador")
        self.verticalLayout.addWidget(self.combo_role)
        self.btn_register = QtWidgets.QPushButton("Cadastrar")
        self.verticalLayout.addWidget(self.btn_register)
        self.label_status = QtWidgets.QLabel("")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_status)
        RegisterScreen.setCentralWidget(self.centralwidget)
        self.retranslateUi(RegisterScreen)
        QtCore.QMetaObject.connectSlotsByName(RegisterScreen)

    def retranslateUi(self, RegisterScreen):
        _translate = QtCore.QCoreApplication.translate
        RegisterScreen.setWindowTitle(_translate("RegisterScreen", "Cadastrar Usuário"))
