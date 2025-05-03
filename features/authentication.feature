Feature: Autenticação de Usuário
  Como um usuário
  Eu quero me autenticar usando minha carteira digital
  Para acessar os recursos da aplicação

  Scenario: Conectar com Metamask
    Given que o usuário está na página inicial
    When o usuário clica no botão "Conectar Metamask"
    Then o usuário deve ser autenticado
    And o endereço da carteira deve ser exibido
    And o saldo de tokens deve ser exibido

  Scenario: Conectar com WalletConnect
    Given que o usuário está na página inicial
    When o usuário clica no botão "Conectar WalletConnect"
    Then o usuário deve ser autenticado
    And o endereço da carteira deve ser exibido
    And o saldo de tokens deve ser exibido 