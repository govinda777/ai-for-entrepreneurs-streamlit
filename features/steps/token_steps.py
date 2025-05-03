from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@given('que o usuário tem tokens suficientes')
def step_impl(context):
    token_balance = context.wait.until(
        EC.presence_of_element_located((By.ID, "token-balance"))
    )
    balance = float(token_balance.text.split()[0])
    assert balance > 0

@then('o saldo atual de tokens deve ser exibido corretamente')
def step_impl(context):
    token_balance = context.wait.until(
        EC.presence_of_element_located((By.ID, "token-balance"))
    )
    assert token_balance.is_displayed()
    assert len(token_balance.text) > 0

@then('o custo do relatório deve ser debitado do saldo')
def step_impl(context):
    # Obter saldo inicial
    initial_balance = context.wait.until(
        EC.presence_of_element_located((By.ID, "token-balance"))
    )
    initial_amount = float(initial_balance.text.split()[0])
    
    # Obter custo do relatório
    report_cost = context.wait.until(
        EC.presence_of_element_located((By.ID, "report-cost"))
    )
    cost = float(report_cost.text.split()[0])
    
    # Verificar saldo final
    final_balance = context.wait.until(
        EC.presence_of_element_located((By.ID, "token-balance"))
    )
    final_amount = float(final_balance.text.split()[0])
    
    assert final_amount == initial_amount - cost 