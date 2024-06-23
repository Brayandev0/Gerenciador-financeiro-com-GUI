# Importações necessárias
from financas import Ui_Form
import sys 
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtGui import QIcon

# Classe principal da aplicação
class minha_aplicacao(Ui_Form, QWidget):
    def __init__(self) -> None:
        super(minha_aplicacao, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("gerenciador-financeiro.ico"))  # Define o ícone da janela
        self.tabela_de_valores = "Transacoes"  # Nome da tabela de transações
        self.tabela_do_valor = "tabela_do_valor"  # Nome da tabela do valor total
        self.setWindowTitle("Gerenciador de finanças")  # Define o título da janela
        self.conecao()  # Conecta ao banco de dados
        self.testar_valor()  # Verifica e inicializa o valor total, se necessário
        self.total.setReadOnly(True)  # Define o campo total como somente leitura
        self.carregar_a_porra_toda()  # Carrega todos os dados na interface
        self.botao_lucro.clicked.connect(lambda: self.calcular_lucro())  # Conecta o botão de lucro à função calcular_lucro
        self.botao_gasto.clicked.connect(lambda: self.calcular_gasto())  # Conecta o botão de gasto à função calcular_gasto
        self.remover_botao.clicked.connect(lambda: self.deletar())  # Conecta o botão de remover à função deletar

    def testar_valor(self):
        # Verifica se há valor inicial na tabela do valor total
        self.cursor_sql.execute(f'SELECT Valor FROM {self.tabela_do_valor}')
        self.conection.commit()
        d = self.cursor_sql.fetchone()
        if d == None:
            # Insere um valor inicial de 0 se não houver valor na tabela
            self.cursor_sql.execute(f'INSERT INTO {self.tabela_do_valor} (Valor) VALUES (?)', (0,))
            self.conection.commit()

    def logs_de_erros(self, mensagem: str):
        # Exibe uma mensagem de erro
        tela_de_erro = QMessageBox()
        tela_de_erro.setWindowTitle("Tela de Erro")
        tela_de_erro.setIcon(QMessageBox.Icon.Critical)
        tela_de_erro.setText(mensagem)
        return tela_de_erro.exec()

    def conecao(self):
        # Conecta ao banco de dados SQLite
        self.conection = sqlite3.connect("transacoes_totais")
        self.cursor_sql = self.conection.cursor()

        # Cria a tabela de transações, se não existir
        self.cursor_sql.execute(
            'CREATE TABLE IF NOT EXISTS Transacoes ('
            'descricao TEXT,'
            'Valor REAL'
            ')'
        )

        # Cria a tabela do valor total, se não existir
        self.cursor_sql.execute(
            'CREATE TABLE IF NOT EXISTS tabela_do_valor ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'Valor REAL'
            ')'
        )
        self.conection.commit()

    def calcular_lucro(self):
        # Calcula e registra uma nova entrada de lucro
        if self.valor_input.text() and self.descricao_input.text():
            try:
                valor_recebido = float(self.valor_input.text())
                valor_total = float(self.total.text())
                conta = valor_recebido + self.consultar_valor()
                self.total.setText(str(conta))
                self.adicionar_a_coluna(self.descricao_input.text(), valor_recebido)
                self.atualizar_total(conta)
            except ValueError:
                return self.logs_de_erros("Você Inseriu um caracter invalído")
        else:
            return self.logs_de_erros("Você não colocou nenhum valor para inserir ")

    def calcular_gasto(self):
        # Calcula e registra uma nova entrada de gasto
        if self.descricao_input.text() and self.valor_input.text():
            try:
                valor_recebido = float(self.valor_input.text()) * -1
                valor_total = float(self.total.text())
                conta = self.consultar_valor() + valor_recebido
                self.total.setText(f"{conta:.2f}")
                self.adicionar_a_coluna(self.descricao_input.text(), valor_recebido)
                self.atualizar_total(conta)
            except ValueError:
                self.limpar()
                return self.logs_de_erros("Você Inseriu um Caracter  Invalído")
        else:
            return self.logs_de_erros("Você não colocou nenhum valor para inserir ")

    def adicionar_a_coluna(self, descricao, valor):
        # Adiciona uma nova transação à tabela
        self.cursor_sql.execute(f' SELECT COUNT(*) FROM {self.tabela_de_valores} WHERE descricao=?', (descricao,))
        resultado = self.cursor_sql.fetchone()
        posicao_linha = self.tableWidget.rowCount()
        self.tableWidget.insertRow(posicao_linha)
        item_descricao = QTableWidgetItem(descricao)
        item_valor = QTableWidgetItem(f"{valor:.2f}")
        self.tableWidget.setItem(posicao_linha, 0, item_descricao)
        self.tableWidget.setItem(posicao_linha, 1, item_valor)
        if resultado[0] == 0:
            self.cursor_sql.execute(f'INSERT INTO {self.tabela_de_valores} (descricao, Valor) VALUES (?, ?)', (descricao, valor))
        self.conection.commit()
        self.limpar()

    def deletar(self):
        # Remove uma transação selecionada da tabela
        linha_selecionada = self.tableWidget.selectedItems()
        if linha_selecionada:
            linha = linha_selecionada[0].row()
            self.descricao_escolhida = self.tableWidget.item(linha, 0).text()
            self.valor_escolhido = self.tableWidget.item(linha, 1).text()
            total_escolhido = float(self.valor_escolhido)
            total = self.consultar_valor()
            total = total - total_escolhido
            self.cursor_sql.execute(f'DELETE FROM {self.tabela_de_valores} WHERE descricao = ? AND Valor = ?', (self.descricao_escolhida, self.valor_escolhido))
            self.atualizar_total(total)
            self.total.setText(str(total))
            self.tableWidget.removeRow(linha)
            self.conection.commit()
        elif not linha_selecionada:
            return self.logs_de_erros("Selecione algum campo para remover")

    def limpar(self):
        # Limpa os campos de entrada de valor e descrição
        self.valor_input.setText("")
        self.descricao_input.setText("")

    def carregar_a_porra_toda(self):
        # Carrega todas as transações e o valor total da base de dados para a interface
        self.cursor_sql.execute(f' SELECT descricao, Valor FROM {self.tabela_de_valores}')
        total = self.cursor_sql.fetchall()
        for dados in total:
            descricao, valor = dados
            self.adicionar_a_coluna(descricao, valor)
            self.cursor_sql.execute(f'SELECT Valor FROM {self.tabela_do_valor}')
        valor_total = self.cursor_sql.fetchone()
        if valor_total is not None:
            valor_total = str(valor_total[0])
            self.total.setText(valor_total)

    def consultar_valor(self):
        # Consulta o valor total atual na base de dados
        self.cursor_sql.execute(f'SELECT Valor FROM {self.tabela_do_valor}')
        valor_total = self.cursor_sql.fetchone()
        if valor_total == None:
            return 0
        return float(valor_total[0])

    def atualizar_total(self, valor):
        # Atualiza o valor total na base de dados
        self.cursor_sql.execute(f'UPDATE {self.tabela_do_valor} SET Valor = ? WHERE id = 1 ', (valor,))
        self.conection.commit()

# Inicializa a aplicação
app = QApplication(sys.argv)
app.setStyle("Fusion")
app.setWindowIcon(QIcon("gerenciador-financeiro.ico"))
janela = minha_aplicacao()
janela.setFixedSize(900, 482)
janela.show()
app.exec()
