"""
Configuração do Sistema de Escala Conteúdo BOL
Suporta tanto ambiente local (.env) quanto Streamlit Cloud (secrets)
"""
import os
import sys
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (ambiente local)
load_dotenv()

# Tenta importar streamlit para acessar secrets
try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False

def get_config(key: str, default: str = "") -> str:
    """
    Obtém configuração do Streamlit secrets ou variáveis de ambiente
    Prioridade: Streamlit secrets > .env > default
    """
    value = None
    
    # 1. Tenta pegar do Streamlit Secrets
    if HAS_STREAMLIT:
        try:
            # Verifica se secrets foi inicializado e contém a chave
            if hasattr(st, 'secrets') and key in st.secrets:
                value = st.secrets[key]
        except Exception:
            # Ignora erros de acesso a secrets (ex: fora do contexto do streamlit)
            pass
    
    # 2. Se não achou, tenta variáveis de ambiente (.env)
    if value is None:
        value = os.getenv(key)
        
    # 3. Se ainda não achou, usa o default
    if value is None:
        value = default
        
    return value

# Configurações do Supabase
SUPABASE_URL = get_config("SUPABASE_URL", "https://ewgkfpbbdylakbxtndnh.supabase.co")
SUPABASE_KEY = get_config("SUPABASE_KEY", "")

# Lista de emails de administradores autorizados
ADMIN_EMAILS = [
    "alinesantiago@bemol.com.br",
    "fabriciomacedo@bemol.com.br",
    "antonioguedes@bemol.com.br",
    "carolinacosta@bemol.com.br"
]

# Senha padrão (em produção, usar hash)
ADMIN_PASSWORD = get_config("ADMIN_PASSWORD", "Bemol@2026")

# Times disponíveis
TIMES = ["Cadastro", "SEO", "FrontEnd"]

# Configurações da aplicação
APP_TITLE = "Sistema de Escala Conteúdo BOL"
APP_ICON = "📅"
