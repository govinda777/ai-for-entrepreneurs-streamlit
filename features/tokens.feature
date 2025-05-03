Feature: Gestão de Tokens
  Como um usuário autenticado
  Eu quero gerenciar meus tokens
  Para controlar meus gastos na plataforma

  Scenario: Verificar saldo de tokens
    Given que o usuário está autenticado
    When o usuário acessa o dashboard
    Then o saldo atual de tokens deve ser exibido corretamente

  Scenario: Consumo de tokens ao gerar relatório
    Given que o usuário tem tokens suficientes
    When o usuário gera um relatório
    Then o custo do relatório deve ser debitado do saldo 