## Gerenciador-financeiro-com-GUI
Gerenciador de Finanças
Este projeto é um Gerenciador de Finanças desenvolvido com PySide6 e SQLite. Ele permite aos usuários registrar transações financeiras, calcular lucros e gastos, e visualizar um todas as transações.

## Tecnologias usadas
-**Pyside6**-
-**Python2.12.3**-
-**SQLite**-

![Captura de tela_2024-06-23_17-26-27](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/0dd1d04f-3713-4222-8066-d00c622c489b)
![Captura de tela_2024-06-23_17-32-33](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/3966ada7-3893-4b4a-86e2-5ee177fea92f)

 ## Conexão com Banco de Dados

Caso seja a primeira vez do usuario executando o programa, sera criado automaticamente 
as tabelas do SQLite, e todos os registros da aplicação serão salvos localmente 

## Funcionalidades 

`Botão Lucro`   : Após inserir a descrição e o valor, este botão irá adicionar uma transação positiva que ira somar com o total

`Botão Gasto`   : Após inserir a descrição e o valor, este botão irá adicionar uma transação negativa que ira subtrair o total 

`Botão Excluir` : Este botão exclui as transações da linha selecionada, e remove automaticamente do total e do Banco de Dados

## Logs de Erros 
Uma caixa de mensagem de erro é exibida quando valores inválidos são inseridos ou quando campos obrigatórios estão vazios.

Quando o Usuario clica em adicionar e não há valores nos campos este erro e retornado :

![Erro_nada_inserido](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/51b217fd-ec59-452e-a51d-9ca393d0c170)

Quando o Usuario inserir letras ou caracteres inválidos será retornado este erro :
![erro_caracter_invalido](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/e63c984f-d5d7-4a6a-a7ef-697c6ea322f8)

Se o usuario clicar em remover uma linha e n tiver selecionado uma linha será retornado este erro :

![erro_selecione_remover](https://github.com/Brayandev0/Gerenciador-financeiro-com-GUI/assets/84828739/9f69bbd6-acad-4817-b6be-38ef1e21a18b)
