# Gerenciador-financeiro-com-GUI
Gerenciador de Finanças
Este projeto é um Gerenciador de Finanças desenvolvido com PySide6 e SQLite. Ele permite aos usuários registrar transações financeiras, calcular lucros e gastos, e visualizar um resumo das transações.

Requisitos 
Python 3.x,
PySide6,
SQLite,

![Captura de tela_2024-06-23_17-26-27](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/0dd1d04f-3713-4222-8066-d00c622c489b)

Funcionalidades :

  Conexão com Banco de Dados
  
A aplicação utiliza SQLite para armazenar os dados das transações.
Duas tabelas são criadas se não existirem: Transacoes e tabela_do_valor.
Registrar Transações

Lucro: Insira a descrição e o valor da receita e clique em "Calcular Lucro" para adicionar a transação de receita.

Gasto: Insira a descrição e o valor da despesa e clique em "Calcular Gasto" para adicionar a transação de despesa.

Excluir Transações
Selecione uma linha na tabela de transações e clique em "Remover" para excluir a transação selecionada.
Campos de Entrada

self.valor_input: Campo para entrada do valor da transação.
self.descricao_input: Campo para entrada da descrição da transação.
self.total: Campo de leitura que exibe o total das transações.

Erros e Validação
Logs de Erros: Uma caixa de mensagem de erro é exibida quando valores inválidos são inseridos ou quando campos obrigatórios estão vazios.

Quando o Usuario clica em adicionar e não há valores nos campos este erro e retornado :

![Erro_nada_inserido](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/51b217fd-ec59-452e-a51d-9ca393d0c170)

Quando o Usuario inserir letras ou caracteres inválidos será retornado este erro :
![erro_caracter_invalido](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/e63c984f-d5d7-4a6a-a7ef-697c6ea322f8)

Se o usuario clicar em remover uma linha e n tiver selecionado uma linha será retornado este erro :

![erro_selecione_remover](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/9f69bbd6-acad-4817-b6be-38ef1e21a18b)
