
import streamlit as st
import json

def initialize_session():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'wallet_address' not in st.session_state:
        st.session_state.wallet_address = None
    if 'xperience_tokens' not in st.session_state:
        st.session_state.xperience_tokens = 0

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

def dashboard():
    st.title("Dashboard Principal")
    
    st.sidebar.success(f"Conectado: {st.session_state.wallet_address[:6]}...{st.session_state.wallet_address[-4:]}")
    st.sidebar.info(f"Tokens Xperience: {st.session_state.xperience_tokens}")
    
    st.header("Relatórios Disponíveis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.card("Mapa do Seu Negócio", "1 Token")
    with col2:
        st.card("Relatório Xperience", "1 Token")
    with col3:
        st.card("Relatório SEO", "1 Token")

def main():
    initialize_session()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        dashboard()

if __name__ == "__main__":
    main()
