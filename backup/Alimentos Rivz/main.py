import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import  uic,QtWidgets,QtGui
from colorama import Cursor
import mysql.connector
import time
import datetime

def escolhe_inserir():
    tela_inicial.show()
    tela_inicial.label_7.setText("")

def escolhe_adc_marca():
    tela_adc_marca.show()
    tela_adc_marca.label_2.setText("")

def escolhe_adc_nome():
    tela_adc_nome.show()
    tela_adc_nome.label_2.setText("")

def escolhe_adc_categoria():
    tela_adc_categoria.show()
    tela_adc_categoria.label_2.setText("")    

def adc_marca():

    adc_marca = tela_adc_marca.lineEdit.text()  

    banco_adc_marca = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    comando_SQL_marca = "INSERT INTO marcas_table (marcasc) VALUES (%s)"
    valor_marca = [(str(adc_marca))]
    cursor = banco_adc_marca.cursor()
    cursor.execute(comando_SQL_marca, valor_marca)
    print(adc_marca,"inserido na database com sucesso!")
    print("Inserido",cursor.rowcount,"coluna(s) de data.")
    banco_adc_marca.commit()
    banco_adc_marca.close()

    tela_adc_marca.lineEdit.setText("")
    tela_adc_marca.label_2.setText("Marca adicionada com sucesso!")
    tela_inicial.comboBox_marca.clear()
    combo_marca()

def adc_nome():

    adc_nome = tela_adc_nome.lineEdit.text()  

    banco_adc_nome = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    comando_SQL_nome = "INSERT INTO nomes_table (nomesc) VALUES (%s)"
    valor_nome = [(str(adc_nome))]
    cursor = banco_adc_nome.cursor()
    cursor.execute(comando_SQL_nome, valor_nome)
    print(adc_nome,"inserido na database com sucesso!")
    print("Inserido",cursor.rowcount,"coluna(s) de data.")
    banco_adc_nome.commit()
    banco_adc_nome.close()

    tela_adc_nome.lineEdit.setText("")
    tela_adc_nome.label_2.setText("nome adicionada com sucesso!")
    tela_inicial.comboBox_nome.clear()
    combo_nome()

def adc_categoria():

    adc_categoria = tela_adc_categoria.lineEdit.text()  

    banco_adc_categoria = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    comando_SQL_categoria = "INSERT INTO categorias_table (categoriasc) VALUES (%s)"
    valor_categoria = [(str(adc_categoria))]
    cursor = banco_adc_categoria.cursor()
    cursor.execute(comando_SQL_categoria, valor_categoria)
    print(adc_categoria,"inserido na database com sucesso!")
    print("Inserido",cursor.rowcount,"coluna(s) de data.")
    banco_adc_categoria.commit()
    banco_adc_categoria.close()

    tela_adc_categoria.lineEdit.setText("")
    tela_adc_categoria.label_2.setText("categoria adicionada com sucesso!")
    tela_inicial.comboBox_categoria.clear()
    combo_categoria()

def combo_marca():
    banco_combo_marca = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    cursor = banco_combo_marca.cursor()
    cursor.execute("SELECT marcasc FROM marcas_table")
    marca_db = cursor.fetchall()
    banco_combo_marca.close()
    # print(marca_db)

    for marca in marca_db:
        
        marca_db_formatada = str(marca).replace("('", "").replace("',)", "")
        tela_inicial.comboBox_marca.addItems([str(marca_db_formatada)])

def combo_nome():
    banco_combo_nome = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    cursor = banco_combo_nome.cursor()
    cursor.execute("SELECT nomesc FROM nomes_table")
    nome_db = cursor.fetchall()
    banco_combo_nome.close()
    # print(nome_db)

    for nome in nome_db:
        
        nome_db_formatada = str(nome).replace("('", "").replace("',)", "")
        tela_inicial.comboBox_nome.addItems([str(nome_db_formatada)])

def combo_categoria():
    banco_combo_categoria = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    cursor = banco_combo_categoria.cursor()
    cursor.execute("SELECT categoriasc FROM categorias_table")
    categoria_db = cursor.fetchall()
    banco_combo_categoria.close()
    # print(categoria_db)

    for categoria in categoria_db:
        
        categoria_db_formatada = str(categoria).replace("('", "").replace("',)", "")
        tela_inicial.comboBox_categoria.addItems([str(categoria_db_formatada)])        

def escolhe_data_validade():
    tela_calendario.show()
    tela_calendario.label.setText("")

def seleciona_data_validade():
    global data_formatada

    data = str(tela_calendario.calendarWidget.selectedDate())
    data_formatada = data[19:30].replace(", ", "-").replace(")", "")
    tela_calendario.label.setText("Data selecionada: " + data_formatada)

def confirma_data_validade():
    tela_inicial.label_validade.setText(data_formatada)
    tela_calendario.close()

def insere_confirmar():

    adc_alimento_marca = tela_inicial.comboBox_marca.currentText()
    adc_alimento_nome = tela_inicial.comboBox_nome.currentText()
    adc_alimento_categoria = tela_inicial.comboBox_categoria.currentText()
    adc_alimento_qntd = tela_inicial.comboBox_qntd.currentText()
    adc_alimento_validade = tela_inicial.label_validade.text()

    banco_adc_marca = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    comando_SQL_marca = "INSERT INTO alimentos (marca,nome,categoria,quantidade,validade) VALUES (%s,%s,%s,%s,%s)"
    valor_marca = [(str(adc_alimento_marca))]
    valor_marca = (str(adc_alimento_marca),str(adc_alimento_nome),str(adc_alimento_categoria),str(adc_alimento_qntd),str(adc_alimento_validade))
    cursor = banco_adc_marca.cursor()
    cursor.execute(comando_SQL_marca, valor_marca)
    banco_adc_marca.commit()
    banco_adc_marca.close()

    tela_inicial.label_7.setText("Alimento inserido com sucesso!")
    atualizar_db()

app=QtWidgets.QApplication([])
tela_inicial=uic.loadUi(r"tela_principal.ui")
tela_tabela=uic.loadUi(r"tela_tabela.ui")
tela_adc_marca=uic.loadUi(r"tela_adc_marca.ui")
tela_adc_nome=uic.loadUi(r"tela_adc_nome.ui")
tela_adc_categoria=uic.loadUi(r"tela_adc_categoria.ui")
tela_calendario=uic.loadUi(r"tela_calendario.ui")
tela_imagem=uic.loadUi(r"teste_imagem.ui")

tela_inicial.pushButton_marca.clicked.connect(escolhe_adc_marca)
tela_inicial.pushButton_nome.clicked.connect(escolhe_adc_nome)
tela_inicial.pushButton_categoria.clicked.connect(escolhe_adc_categoria)
tela_inicial.pushButton_confirmar.clicked.connect(insere_confirmar)

tela_inicial.comboBox_qntd.addItems(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"])
tela_inicial.pushButton_validade.clicked.connect(escolhe_data_validade)

tela_tabela.pushButton_inserir.clicked.connect(escolhe_inserir)

tela_adc_marca.pushButton.clicked.connect(adc_marca)
tela_adc_nome.pushButton.clicked.connect(adc_nome)
tela_adc_categoria.pushButton.clicked.connect(adc_categoria)

tela_calendario.calendarWidget.selectionChanged.connect(seleciona_data_validade)
tela_calendario.pushButton.clicked.connect(confirma_data_validade)

def cria_tabelas():

    # Abre o Banco de Dados e Cria Tabela
    banco_create_table = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    cursor = banco_create_table.cursor()
    cursor.execute("CREATE TABLE if not exists alimentos (id INT NOT NULL AUTO_INCREMENT,  marca VARCHAR(110) NOT NULL,  nome VARCHAR(45) NOT NULL,  categoria VARCHAR(45) NOT NULL,	quantidade INT NULL,  validade DATE NULL,  PRIMARY KEY (id))DEFAULT CHARACTER SET = utf8mb4;")
    banco_create_table.commit()
    banco_create_table.close()

    banco_create_marcas = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    cursor = banco_create_marcas.cursor()
    cursor.execute("CREATE TABLE if not exists marcas_table (id INT NOT NULL AUTO_INCREMENT,  marcasc VARCHAR(110) NOT NULL,  PRIMARY KEY (id))DEFAULT CHARACTER SET = utf8mb4;")
    banco_create_marcas.commit()
    banco_create_marcas.close()

    banco_create_nomes = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    cursor = banco_create_nomes.cursor()
    cursor.execute("CREATE TABLE if not exists nomes_table (id INT NOT NULL AUTO_INCREMENT,  nomesc VARCHAR(110) NOT NULL,  PRIMARY KEY (id))DEFAULT CHARACTER SET = utf8mb4;")
    banco_create_nomes.commit()
    banco_create_nomes.close()

    banco_create_categorias = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    cursor = banco_create_categorias.cursor()
    cursor.execute("CREATE TABLE if not exists categorias_table (id INT NOT NULL AUTO_INCREMENT,  categoriasc VARCHAR(110) NOT NULL,  PRIMARY KEY (id))DEFAULT CHARACTER SET = utf8mb4;")
    banco_create_categorias.commit()
    banco_create_categorias.close()    

def atualizar_db():

    banco_combo_categoria = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz")
    cursor = banco_combo_categoria.cursor()
    cursor.execute("SELECT categoriasc FROM categorias_table")
    categoria_db = cursor.fetchall()
    banco_combo_categoria.close()

    banco_atualizar_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="rivz") 
    cursor = banco_atualizar_db.cursor()
    cursor.execute("SELECT * FROM alimentos")
    dados_lidos = cursor.fetchall()
    # Coloca os dados na tabela da interface
    tela_tabela.tableWidget.setRowCount(len(dados_lidos))
    tela_tabela.tableWidget.setColumnCount(6)
    for i in range(0, len(dados_lidos)):
        for j in range(0,6):
            tela_tabela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

atualizar_db()
cria_tabelas()
combo_marca()
combo_nome()
combo_categoria()
tela_inicial.label_validade.setText("")
tela_tabela.show()
tela_imagem.show()
app.exec()