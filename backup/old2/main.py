from PyQt5 import QtWidgets, uic
import os
import mysql.connector

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, 'ui')

from ui.ui_tela_unidade import Ui_tela_unidade
from ui.ui_tela_login import Ui_tela_login
from ui.ui_tela_botao_lista import Ui_tela_botao_lista
from ui.ui_tela_lista import Ui_tela_lista

class TelaUnidade(QtWidgets.QMainWindow, Ui_tela_unidade):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chama_tela_login)

    def chama_tela_login(self):
        if self.radioButton.isChecked():
            print("Conectado à database rebral1")
            self.close()
            tela_login.show()
        else:
            print("Erro: Nenhuma unidade selecionada")

class TelaLogin(QtWidgets.QMainWindow, Ui_tela_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_voltar.clicked.connect(self.voltar)

    def login(self):
        nome_usuario = self.lineEdit_login.text()
        senha = self.lineEdit_senha.text()
        self.label_4.setText("")

        try:
            banco = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="login"
            )
            cursor = banco.cursor()
            cursor.execute(f"SELECT senha FROM contas WHERE username = '{nome_usuario}'")
            resultado = cursor.fetchone()
            banco.close()

            if resultado and senha == resultado[0]:
                self.lineEdit_login.clear()
                self.lineEdit_senha.clear()
                self.close()
                tela_botao_lista.show()
            else:
                self.label_4.setText("Dados de login incorretos!")
        except Exception as e:
            print(f"Erro ao validar o login: {e}")
            self.label_4.setText("Erro na conexão!")

    def voltar(self):
        self.close()
        tela_unidade.show()

class TelaBotaoLista(QtWidgets.QMainWindow, Ui_tela_botao_lista):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.escolher_lista)

    def escolher_lista(self):
        try:
            banco = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="login"
            )
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM contas")
            dados_lidos = cursor.fetchall()
            banco.close()

            terceira_tela.tableWidget.setRowCount(len(dados_lidos))
            terceira_tela.tableWidget.setColumnCount(3)

            for i, linha in enumerate(dados_lidos):
                for j in range(3):
                    terceira_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(linha[j])))

            self.close()
            terceira_tela.show()
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

class TerceiraTela(QtWidgets.QMainWindow, Ui_tela_lista):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.voltar)

    def voltar(self):
        self.close()
        tela_botao_lista.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    tela_unidade = TelaUnidade()
    tela_login = TelaLogin()
    tela_botao_lista = TelaBotaoLista()
    terceira_tela = TerceiraTela()
    tela_unidade.show()
    app.exec()