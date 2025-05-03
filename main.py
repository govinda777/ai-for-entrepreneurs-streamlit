import streamlit as st
import json
import time
from report_types import REPORT_TYPES

def initialize_session():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'wallet_address' not in st.session_state:
        st.session_state.wallet_address = None
    if 'xperience_tokens' not in st.session_state:
        st.session_state.xperience_tokens = 0
    if 'selected_report' not in st.session_state:
        st.session_state.selected_report = None
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    if 'reports' not in st.session_state:
        st.session_state.reports = []

def login_page():
    st.title("IA do Empreendedor")
    st.subheader("Conecte sua carteira digital")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Conectar Metamask"):
            # Simulate wallet connection
            st.session_state.authenticated = True
            st.session_state.wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
            st.session_state.xperience_tokens = 100
            st.rerun()
            
    with col2:
        if st.button("Conectar WalletConnect"):
            # Simulate wallet connection
            st.session_state.authenticated = True
            st.session_state.wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
            st.session_state.xperience_tokens = 100
            st.rerun()

def show_report_selection():
    st.title("Selecione o Relatório")
    
    for report in REPORT_TYPES:
        with st.expander(f"{report.name} - {report.cost} Token Xperience"):
            st.write(report.description)
            if st.button(f"Selecionar {report.name}"):
                st.session_state.selected_report = report
                st.rerun()

def show_report_form():
    report = st.session_state.selected_report
    st.title(f"Formulário: {report.name}")
    
    form_data = {}
    for field in report.fields:
        if field.type == "text":
            form_data[field.name] = st.text_input(field.description, key=field.name)
        elif field.type == "number":
            form_data[field.name] = st.number_input(field.description, key=field.name)
    
    if st.button("Gerar Relatório"):
        if all(form_data.values()):
            st.session_state.form_data = form_data
            process_report()
        else:
            st.error("Por favor, preencha todos os campos obrigatórios.")

def process_report():
    st.title("Processando Relatório")
    
    # Simulate processing
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)
    
    # Simulate token transaction
    st.session_state.xperience_tokens -= st.session_state.selected_report.cost
    
    # Generate report
    report = {
        "type": st.session_state.selected_report.name,
        "data": st.session_state.form_data,
        "timestamp": time.time(),
        "insights": generate_insights(st.session_state.form_data)
    }
    
    st.session_state.reports.append(report)
    st.session_state.selected_report = None
    st.session_state.form_data = {}
    st.rerun()

def generate_insights(form_data):
    # This would be replaced with actual AI analysis
    return {
        "summary": "Análise completa baseada nos dados fornecidos",
        "recommendations": [
            "Recomendação 1 baseada nos dados",
            "Recomendação 2 baseada nos dados",
            "Recomendação 3 baseada nos dados"
        ],
        "next_steps": [
            "Próximo passo 1",
            "Próximo passo 2",
            "Próximo passo 3"
        ]
    }

def show_report(report):
    st.title(f"Relatório: {report['type']}")
    
    st.header("Dados Fornecidos")
    for key, value in report['data'].items():
        st.write(f"**{key}**: {value}")
    
    st.header("Insights")
    st.write(report['insights']['summary'])
    
    st.header("Recomendações")
    for rec in report['insights']['recommendations']:
        st.write(f"- {rec}")
    
    st.header("Próximos Passos")
    for step in report['insights']['next_steps']:
        st.write(f"- {step}")
    
    if st.button("Voltar ao Dashboard"):
        st.session_state.selected_report = None
        st.rerun()

def dashboard():
    st.title("Dashboard Principal")
    
    st.sidebar.success(f"Conectado: {st.session_state.wallet_address[:6]}...{st.session_state.wallet_address[-4:]}")
    st.sidebar.info(f"Tokens Xperience: {st.session_state.xperience_tokens}")
    
    if st.session_state.selected_report is None:
        if st.session_state.reports:
            st.header("Relatórios Recentes")
            for report in reversed(st.session_state.reports):
                with st.expander(f"{report['type']} - {time.strftime('%Y-%m-%d %H:%M', time.localtime(report['timestamp']))}"):
                    if st.button("Visualizar", key=f"view_{report['timestamp']}"):
                        show_report(report)
        
        st.header("Novo Relatório")
        show_report_selection()
    else:
        if st.session_state.form_data:
            show_report(st.session_state.reports[-1])
        else:
            show_report_form()

def main():
    initialize_session()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        dashboard()

if __name__ == "__main__":
    main()
