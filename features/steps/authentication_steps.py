from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que o usuário está na página inicial')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8501")
    context.wait = WebDriverWait(context.driver, 10)

@when('o usuário clica no botão "Conectar Metamask"')
def step_impl(context):
    connect_button = context.wait.until(
        EC.element_to_be_clickable((By.ID, "connect-metamask"))
    )
    connect_button.click()

@when('o usuário clica no botão "Conectar WalletConnect"')
def step_impl(context):
    connect_button = context.wait.until(
        EC.element_to_be_clickable((By.ID, "connect-walletconnect"))
    )
    connect_button.click()

@then('o usuário deve ser autenticado')
def step_impl(context):
    # Verificar se o elemento de autenticação bem-sucedida está presente
    auth_success = context.wait.until(
        EC.presence_of_element_located((By.ID, "auth-success"))
    )
    assert auth_success.is_displayed()

@then('o endereço da carteira deve ser exibido')
def step_impl(context):
    wallet_address = context.wait.until(
        EC.presence_of_element_located((By.ID, "wallet-address"))
    )
    assert wallet_address.is_displayed()
    assert len(wallet_address.text) > 0

@then('o saldo de tokens deve ser exibido')
def step_impl(context):
    token_balance = context.wait.until(
        EC.presence_of_element_located((By.ID, "token-balance"))
    )
    assert token_balance.is_displayed()
    assert len(token_balance.text) > 0 