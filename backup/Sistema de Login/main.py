from PyQt5 import  uic,QtWidgets
from colorama import Cursor
import mysql.connector
import time
import datetime

# Constantes
caracteres_min_senha = 8

# Tela inicial
def chama_tela_login():
    tela_inicial.close()
    tela_login.show()
    tela_login.label_2.setText("")

def chama_tela_cadastro():
    tela_inicial.close()
    tela_cadastro.show()
    tela_cadastro.label_6.setText("")
    tela_cadastro.label_7.setText("")
    tela_cadastro.label_9.setText("")


# Tela de login
def login():
    x = time.localtime()
    nome_usuario = tela_login.lineEdit_login.text()
    senha = tela_login.lineEdit_senha.text()

    try:
        banco_login = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
        cursor = banco_login.cursor()
        cursor.execute("SELECT password FROM login WHERE username = '{}'".format(nome_usuario))
        # cursor.execute("SELECT AES_DECRYPT(password,'senhadachave') AS password FROM login WHERE username = '{}'".format(nome_usuario))
        # # cursor.execute("SELECT CAST(AES_DECRYPT(password,'senhadachave') as char) FROM login WHERE username = '{}'".format(nome_usuario))
        senha_bd = cursor.fetchone()[0]
        banco_login.close()

        if senha == senha_bd:
            tela_login.lineEdit_login.setText("")
            tela_login.lineEdit_senha.setText("")
            tela_login.close()
            tela_principal.show()
            tela_principal.label_User.setText(nome_usuario)

            banco_email = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
            cursor = banco_email.cursor()
            cursor.execute("SELECT `e-mail` FROM login WHERE username = '{}'".format(nome_usuario))
            email_db = cursor.fetchone()[0]
            banco_email.close()

            print(email_db)
            tela_principal.label_email.setText(str(email_db))

            banco_idade = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
            cursor = banco_idade.cursor()
            cursor.execute("SELECT data_nascimento FROM login WHERE username = '{}'".format(nome_usuario))
            data_nascimento_db = cursor.fetchone()[0]
            data_nascimento_db_str = str(data_nascimento_db)
            banco_idade.close()

            print(data_nascimento_db_str)
            ano_db = int(str(data_nascimento_db_str[0]) + str(data_nascimento_db_str[1]) + str(data_nascimento_db_str[2]) + str(data_nascimento_db_str[3]))
            mes_db = (str(data_nascimento_db_str[5]) + str(data_nascimento_db_str[6]))
            dia_db = (str(data_nascimento_db_str[8]) + str(data_nascimento_db_str[9]))

            dia = str(x[2])
            mes = str(x[1])
            ano = int(str(x[0]))

            if (int(dia) < 10):
                dia = ("0" + str(dia))
                print("Dia formatado: " + dia)

            if (int(mes) < 10):
                mes = ("0" + str(mes))
                print("Mês formatado: " + mes)            

            ano_nascimento = ano - ano_db
            tela_principal.label_3.setText(str(ano_nascimento))
        else:
            tela_login.label_2.setText("Dados de login incorretos!")
            print("Dados de login incorretos!")

    except Exception as e:
        print("Error: ", e)
        tela_login.label_2.setText("Erro ao fazer login")

    print(ano_nascimento)

def volta_tela_login():
    tela_login.close()
    tela_inicial.show()

# Tela de cadastro
def cadastrar():
    email_cadastrado = tela_cadastro.lineEdit_email.text()
    usuario_cadastrado = tela_cadastro.lineEdit_username.text()
    senha_cadastrada = tela_cadastro.lineEdit_password.text()
    confirma_senha = tela_cadastro.lineEdit_password2.text()    

    if len(senha_cadastrada) >= caracteres_min_senha:

        if senha_cadastrada == confirma_senha:

            banco_cadastro = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
            cursor = banco_cadastro.cursor()
            comando_SQL_cadastro = ("INSERT INTO login (`e-mail`,username,password,data_nascimento) VALUES (%s,%s,%s,%s)")
            # comando_SQL_cadastro = ("INSERT INTO login (`e-mail`,username,password) VALUES (%s,%s,AES_ENCRYPT(%s, 'senhadachave'))")
            dados_cadastro = (str(email_cadastrado),str(usuario_cadastrado),str(senha_cadastrada),str(data_formatada))
            cursor.execute(comando_SQL_cadastro,dados_cadastro)
            banco_cadastro.commit()
            banco_cadastro.close()
            tela_cadastro.lineEdit_email.setText("")
            tela_cadastro.lineEdit_username.setText("")
            tela_cadastro.lineEdit_password.setText("")
            tela_cadastro.lineEdit_password2.setText("")
            tela_cadastro.label_6.setText("")
            tela_cadastro.label_7.setText("Cadastrado com sucesso!")
            print("Cadastrado com sucesso!")
        else:
            tela_cadastro.label_6.setText("As senhas não coincidem!")
            print("As senhas não coincidem!")
    else:
        tela_cadastro.label_6.setText("Sua senha deve possuir mais de 8 dígitos!")
        tela_cadastro.label_7.setText("")
        print("Sua senha deve possuir mais de 8 dígitos!")

def volta_tela_cadastro():
    tela_cadastro.close()
    tela_inicial.show()

def escolhe_data_nascimento():
    tela_calendario.show()
    tela_calendario.label.setText("")

def seleciona_data_nascimento():
    global data_formatada

    data = str(tela_calendario.calendarWidget.selectedDate())
    data_formatada = data[19:30].replace(", ", "-").replace(")", "")
    tela_calendario.label.setText("Data selecionada: " + data_formatada)

def confirma_data_nascimento():
    tela_cadastro.label_9.setText(data_formatada)
    tela_calendario.close()

# Tela principal
def volta_tela_principal():
    tela_principal.close()
    tela_inicial.show()

app=QtWidgets.QApplication([])
tela_inicial=uic.loadUi(r"tela_inicial.ui")
tela_login=uic.loadUi(r"tela_login.ui")
tela_cadastro=uic.loadUi(r"tela_cadastro.ui")
tela_calendario=uic.loadUi(r"tela_calendario.ui")
tela_principal=uic.loadUi(r"tela_final.ui")

tela_inicial.pushButton.clicked.connect(chama_tela_login)
tela_inicial.pushButton_2.clicked.connect(chama_tela_cadastro)

tela_login.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
tela_login.pushButton.clicked.connect(login)
tela_login.pushButton_voltar.clicked.connect(volta_tela_login)

tela_cadastro.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro.lineEdit_password2.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro.pushButton.clicked.connect(cadastrar)
tela_cadastro.pushButton_2.clicked.connect(volta_tela_cadastro)
tela_cadastro.pushButton_3.clicked.connect(escolhe_data_nascimento)

tela_calendario.calendarWidget.selectionChanged.connect(seleciona_data_nascimento)
tela_calendario.pushButton.clicked.connect(confirma_data_nascimento)

tela_principal.pushButton.clicked.connect(volta_tela_principal)

# Abre o Banco de Dados e Cria Tabela
banco_create_table = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
cursor = banco_create_table.cursor()
cursor.execute("CREATE TABLE if not exists login (id INT NOT NULL AUTO_INCREMENT,  email VARCHAR(110) NOT NULL,  email VARCHAR(110) NOT NULL,  username VARCHAR(45) NOT NULL,  password VARCHAR(45) NOT NULL,  data_nascimento DATE NULL,  PRIMARY KEY (id))DEFAULT CHARACTER SET = utf8mb4;")
banco_create_table.commit()
banco_create_table.close()

tela_inicial.show()
app.exec()