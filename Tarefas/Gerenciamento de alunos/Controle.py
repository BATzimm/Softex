from PyQt5 import  uic,QtWidgets
import mysql.connector

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alunos"

)
 

# Função para excluir aluno
def excluir_aluno():
    linha = segunda_tela.tableWidget.currentRow()
    if linha >= 0:  # Verifica se uma linha foi selecionada
        matricula = segunda_tela.tableWidget.item(linha, 1).text()  # Assume que a matrícula está na coluna 1

        # Exclui o registro do banco de dados
        cursor = banco.cursor()
        comando_SQL = "DELETE FROM aluno WHERE matricula = %s"
        dados = (matricula,)
        cursor.execute(comando_SQL, dados)
        banco.commit()

        # Remove a linha da tabela
        segunda_tela.tableWidget.removeRow(linha)


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()
    linha7 = formulario.lineEdit_7.text()
    media = (int(linha4) + int(linha5) + int(linha6) + int(linha7)) / 4

    if formulario.pushButton.isChecked():
        formulario.lineEdit_8.setText("Aluno cadastrado com sucesso!")

    print("Nome:",linha1)
    print("Matrícula:",linha2)
    print("Curso:",linha3)
    print("Nota 1°B:",linha4)
    print("Nota 2°B:",linha5)
    print("Nota 3°B:",linha6)
    print("Nota 4°B:",linha7)
    print("Média:",media)

    #Inserir Dados

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO aluno (nome, matricula, curso, nota1, nota2, nota3, nota4, media) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6), str(linha7), str(media))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    #Limpar Campos

    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    formulario.lineEdit_7.setText("")

#Trás a tela de listagem de alunos
def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM aluno"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(8)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 8):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

#Menu Interativo
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(excluir_aluno)

formulario.show()
app.exec()

