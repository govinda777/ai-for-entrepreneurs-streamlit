from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    # Configurar o driver do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar em modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)

def after_all(context):
    # Fechar o driver após todos os testes
    context.driver.quit()

def before_scenario(context, scenario):
    # Limpar cookies antes de cada cenário
    context.driver.delete_all_cookies()

def after_scenario(context, scenario):
    # Capturar screenshot em caso de falha
    if scenario.status == "failed":
        context.driver.save_screenshot(f"failed_{scenario.name}.png") 