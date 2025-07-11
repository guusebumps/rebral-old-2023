from PyQt5 import  uic,QtWidgets
from colorama import Cursor
import mysql.connector
from reportlab.pdfgen import canvas
import pandas as pd
import xlwt
import openpyxl

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="professor"
)

def funcao_salvar():
    pagina_editar.close()

def funcao_excluir_linha():
    linha = pagina_lista.tableWidget.currentRow()
    pagina_lista.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM chamadas")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM chamadas WHERE id="+ str(valor_id))

def funcao_editar_linha():
    pagina_editar.show()
    linha = pagina_lista.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM chamadas")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM chamadas WHERE id="+ str(valor_id))
    chamada = cursor.fetchall()

    pagina_editar.lineEdit.setText(str(chamada[0][0]))
    pagina_editar.lineEdit_2.setText(str(chamada[0][1]))
    pagina_editar.lineEdit_3.setText(str(chamada[0][2]))
    pagina_editar.lineEdit_4.setText(str(chamada[0][3]))
    pagina_editar.lineEdit_5.setText(str(chamada[0][4]))
    pagina_editar.lineEdit_6.setText(str(chamada[0][5]))
    pagina_editar.lineEdit_7.setText(str(chamada[0][6]))
    pagina_editar.lineEdit_8.setText(str(chamada[0][7]))
    pagina_editar.lineEdit_9.setText(str(chamada[0][8]))
    pagina_editar.lineEdit_10.setText(str(chamada[0][9]))
    pagina_editar.lineEdit_11.setText(str(chamada[0][10]))
    pagina_editar.lineEdit_12.setText(str(chamada[0][11]))
    pagina_editar.lineEdit_13.setText(str(chamada[0][12]))
    print(chamada)

def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM chamadas"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("chamadas_cadastradas.pdf")
    pdf.setFont("Times-Bold", 12)

    pdf.drawString(110,750, "Q S O Nº.")
    pdf.drawString(210,750, "DATA")
    pdf.drawString(310,750, "PREFIXO")
    pdf.drawString(410,750, "HORA \nINÍCIO")
    pdf.drawString(510,750, "HORA \n FIM")
    pdf.drawString(610,750, "FREQ. \n ou \nFAIXA")
    pdf.drawString(710,750, "FONIA \n   ou \n  CW")
    pdf.drawString(810,750, "RST\nENV.")
    pdf.drawString(910,750, "RST \nREC.")
    pdf.drawString(1010,750, "Q S L \n ENV.")
    pdf.drawString(1110,750, "Q S L \n REC.")
    pdf.drawString(1210,750, "OUTRAS \nANOTAÇÕES")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(510,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(610,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(710,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(810,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(910,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(1010,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(1110,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(1210,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(1310,750 - y, str(dados_lidos[i][0]))
    
    pdf.save()
    print("PDF FOI GERADO COM SUCESSO")

def gerar_excel():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM chamadas"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    for i in range(len(dados_lidos)):
        d = {'Q S O \nNº.': [str(dados_lidos[i][1])], 
        'DATA': [str(dados_lidos[i][2])], 
        'PREFIXO': [str(dados_lidos[i][3])],
        'HORA \nINÍCIO': [str(dados_lidos[i][4])],
        'HORA \n FIM': [str(dados_lidos[i][5])],
        'FREQ. \n ou \nFAIXA': [str(dados_lidos[i][6])],
        'FONIA \n   ou \n  CW': [str(dados_lidos[i][7])],
        'RST\nENV.': [str(dados_lidos[i][8])],
        'RST \nREC.': [str(dados_lidos[i][9])],
        'Q S L \n ENV.': [str(dados_lidos[i][10])],
        'Q S L \n REC.': [str(dados_lidos[i][11])],
        'OUTRAS \nANOTAÇÕES': [str(dados_lidos[i][12])]
        }

    dados = pd.DataFrame(data= d)
    dados.to_excel('chamadas_cadastradas.xls', index= False)


def funcao_escolher_cadastrar():
    formulario.show()
    primeira_pagina.close()

def funcao_voltar_cadastrar():
    formulario.close()
    primeira_pagina.show()

def funcao_escolher_lista():
    pagina_lista.show()
    primeira_pagina.close()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM chamadas"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    pagina_lista.tableWidget.setRowCount(len(dados_lidos))
    pagina_lista.tableWidget.setColumnCount(12)

    for i in range(0, len(dados_lidos)):
        for j in range(0,12):
            pagina_lista.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def funcao_voltar_lista():
    pagina_lista.close()
    primeira_pagina.show()

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()
    linha7 = formulario.lineEdit_7.text()
    linha8 = formulario.lineEdit_8.text()
    linha9 = formulario.lineEdit_9.text()
    linha10 = formulario.lineEdit_10.text()
    linha11 = formulario.lineEdit_11.text()
    linha12 = formulario.lineEdit_12.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO chamadas (QSO,DIA,PREFIXO,HORA_INICIO,HORA_FIM,FREQ_ou_FAIXA,FONIA_ou_CW,RST_ENV,RST_REC,QSL_ENV,QSL_REC,OUTRAS_ANOTACOES) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1)),(str(linha2)),(str(linha3)),(str(linha4)),(str(linha5)),(str(linha6)),(str(linha7)),(str(linha8)),(str(linha9)),(str(linha10)),(str(linha11)),(str(linha12)),
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    formulario.lineEdit_7.setText("")
    formulario.lineEdit_8.setText("")
    formulario.lineEdit_9.setText("")
    formulario.lineEdit_10.setText("")
    formulario.lineEdit_11.setText("")
    formulario.lineEdit_12.setText("")




app=QtWidgets.QApplication([])
primeira_pagina=uic.loadUi(r"E:\VS Code\professor\professorexcel\pagesqt\first_page.ui")
formulario=uic.loadUi(r"E:\VS Code\professor\professorexcel\pagesqt\main_page.ui")
pagina_lista=uic.loadUi(r"E:\VS Code\professor\professorexcel\pagesqt\list_page.ui")
pagina_editar=uic.loadUi(r"E:\VS Code\professor\professorexcel\pagesqt\edit_page.ui")
primeira_pagina.pushButton_3.clicked.connect(funcao_escolher_cadastrar)
primeira_pagina.pushButton_4.clicked.connect(funcao_escolher_lista)
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(funcao_voltar_cadastrar)
pagina_lista.pushButton_2.clicked.connect(funcao_voltar_lista)
pagina_lista.pushButton_excel.clicked.connect(gerar_excel)
pagina_lista.pushButton_pdf.clicked.connect(gerar_pdf)
pagina_lista.pushButton_Excluir.clicked.connect(funcao_excluir_linha)
pagina_lista.pushButton_editar.clicked.connect(funcao_editar_linha)
pagina_editar.pushButton_salvar.clicked.connect(funcao_salvar)

primeira_pagina.show()
app.exec()