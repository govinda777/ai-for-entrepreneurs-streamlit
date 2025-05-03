Feature: Geração de Relatórios
  Como um usuário autenticado
  Eu quero gerar relatórios personalizados
  Para obter insights sobre meu negócio

  Scenario: Visualizar tipos de relatório disponíveis
    Given que o usuário está autenticado
    When o usuário acessa o dashboard
    Then todos os tipos de relatório devem ser exibidos
    And o custo em tokens deve ser visível para cada relatório

  Scenario: Selecionar um relatório
    Given que o usuário está autenticado
    When o usuário seleciona um tipo de relatório
    Then o formulário correspondente deve ser exibido

  Scenario: Preencher formulário válido
    Given que o usuário selecionou um relatório
    When o usuário preenche todos os campos obrigatórios
    And clica em "Gerar Relatório"
    Then o processamento deve iniciar
    And o relatório deve ser gerado com sucesso

  Scenario: Tentar gerar relatório com formulário incompleto
    Given que o usuário selecionou um relatório
    When o usuário deixa campos obrigatórios em branco
    And clica em "Gerar Relatório"
    Then uma mensagem de erro deve ser exibida

  Scenario: Visualizar relatório gerado
    Given que um relatório foi gerado com sucesso
    When o usuário acessa o dashboard
    Then o relatório deve aparecer na lista de relatórios recentes
    And o usuário deve poder visualizar os detalhes do relatório 