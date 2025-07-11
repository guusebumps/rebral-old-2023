from PyQt5 import uic, QtWidgets
import mysql.connector
import os

# Caminho base para os arquivos .ui
BASE_DIR = os.path.join(os.getcwd(), "rebral", "outros")

# Carregando telas com caminhos otimizados
tela_unidade = uic.loadUi(os.path.join(BASE_DIR, "tela_unidade.ui"))
tela_login = uic.loadUi(os.path.join(BASE_DIR, "bella_login.ui"))
terceira_tela = uic.loadUi(os.path.join(BASE_DIR, "tela_lista.ui"))
tela_botao_lista = uic.loadUi(os.path.join(BASE_DIR, "tela_botao_lista.ui"))

def conecta_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="login"
    )

def login():
    tela_login.label_4.setText("")
    nome_usuario = tela_login.lineEdit_login.text()
    senha = tela_login.lineEdit_senha.text()

    try:
        banco = conecta_banco()
        cursor = banco.cursor()
        cursor.execute(f"SELECT senha FROM contas WHERE username = '{nome_usuario}'")
        resultado = cursor.fetchone()
        banco.close()

        if resultado and senha == resultado[0]:
            tela_login.lineEdit_login.setText("")
            tela_login.lineEdit_senha.setText("")
            tela_login.close()
            tela_botao_lista.show()
        else:
            tela_login.label_4.setText("Dados de login incorretos!")
    except Exception as e:
        print(f"Erro ao validar o login: {e}")
        tela_login.label_4.setText("Erro na conexão ou consulta!")

def escolher_lista():
    try:
        banco = conecta_banco()
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM contas")
        dados_lidos = cursor.fetchall()
        banco.close()

        terceira_tela.tableWidget.setRowCount(len(dados_lidos))
        terceira_tela.tableWidget.setColumnCount(3)

        for i, linha in enumerate(dados_lidos):
            for j in range(3):
                terceira_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(linha[j])))

        tela_botao_lista.close()
        terceira_tela.show()

    except Exception as e:
        print(f"Erro ao carregar a lista: {e}")

def volta_tela_unidade():
    tela_login.close()
    tela_unidade.show()
    print("Desconectado da database rebral1")

def volta_tela_login():
    terceira_tela.close()
    tela_login.show()

def volta_tela_botao_lista():
    terceira_tela.close()
    tela_botao_lista.show()

def chama_tela_login():
    if tela_unidade.radioButton.isChecked():
        print("Conectado à database rebral1")
        tela_unidade.close()
        tela_login.show()

        # Conexões dos botões
        terceira_tela.pushButton_2.clicked.connect(volta_tela_botao_lista)
        tela_botao_lista.pushButton.clicked.connect(escolher_lista)
        tela_login.pushButton_voltar.clicked.connect(volta_tela_unidade)
        tela_login.pushButton_entrar.clicked.connect(login)
    else:
        print("Erro: Nenhuma unidade selecionada")

# Configuração da aplicação
app = QtWidgets.QApplication([])
tela_unidade.pushButton.clicked.connect(chama_tela_login)
tela_login.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)

tela_unidade.show()
app.exec()
