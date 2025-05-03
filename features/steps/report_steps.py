from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@given('que o usuário está autenticado')
def step_impl(context):
    # Verificar se o usuário está autenticado
    assert context.driver.find_element(By.ID, "auth-success").is_displayed()

@when('o usuário acessa o dashboard')
def step_impl(context):
    dashboard_link = context.wait.until(
        EC.element_to_be_clickable((By.ID, "dashboard-link"))
    )
    dashboard_link.click()

@then('todos os tipos de relatório devem ser exibidos')
def step_impl(context):
    report_types = context.wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "report-type"))
    )
    assert len(report_types) > 0

@then('o custo em tokens deve ser visível para cada relatório')
def step_impl(context):
    report_costs = context.driver.find_elements(By.CLASS_NAME, "report-cost")
    assert len(report_costs) > 0
    for cost in report_costs:
        assert cost.is_displayed()
        assert len(cost.text) > 0

@when('o usuário seleciona um tipo de relatório')
def step_impl(context):
    first_report = context.wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "report-type"))
    )
    first_report.click()

@then('o formulário correspondente deve ser exibido')
def step_impl(context):
    form = context.wait.until(
        EC.presence_of_element_located((By.ID, "report-form"))
    )
    assert form.is_displayed()

@given('que o usuário selecionou um relatório')
def step_impl(context):
    context.execute_steps('''
        When o usuário seleciona um tipo de relatório
        Then o formulário correspondente deve ser exibido
    ''')

@when('o usuário preenche todos os campos obrigatórios')
def step_impl(context):
    required_fields = context.driver.find_elements(By.CLASS_NAME, "required-field")
    for field in required_fields:
        field.send_keys("Teste")

@when('o usuário deixa campos obrigatórios em branco')
def step_impl(context):
    # Não preencher nenhum campo
    pass

@when('clica em "Gerar Relatório"')
def step_impl(context):
    generate_button = context.wait.until(
        EC.element_to_be_clickable((By.ID, "generate-report"))
    )
    generate_button.click()

@then('o processamento deve iniciar')
def step_impl(context):
    processing = context.wait.until(
        EC.presence_of_element_located((By.ID, "processing-indicator"))
    )
    assert processing.is_displayed()

@then('o relatório deve ser gerado com sucesso')
def step_impl(context):
    success_message = context.wait.until(
        EC.presence_of_element_located((By.ID, "report-success"))
    )
    assert success_message.is_displayed()

@then('uma mensagem de erro deve ser exibida')
def step_impl(context):
    error_message = context.wait.until(
        EC.presence_of_element_located((By.ID, "error-message"))
    )
    assert error_message.is_displayed()

@given('que um relatório foi gerado com sucesso')
def step_impl(context):
    context.execute_steps('''
        Given que o usuário selecionou um relatório
        When o usuário preenche todos os campos obrigatórios
        And clica em "Gerar Relatório"
        Then o processamento deve iniciar
        And o relatório deve ser gerado com sucesso
    ''')

@then('o relatório deve aparecer na lista de relatórios recentes')
def step_impl(context):
    recent_reports = context.wait.until(
        EC.presence_of_element_located((By.ID, "recent-reports"))
    )
    assert recent_reports.is_displayed()
    assert len(recent_reports.find_elements(By.CLASS_NAME, "report-item")) > 0

@then('o usuário deve poder visualizar os detalhes do relatório')
def step_impl(context):
    report_details = context.wait.until(
        EC.presence_of_element_located((By.ID, "report-details"))
    )
    assert report_details.is_displayed() 