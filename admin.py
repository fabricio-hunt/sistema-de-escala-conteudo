"""
Aplicação Streamlit - Tela de Administração
"""
import streamlit as st

# Configuração da página DEVE ser o primeiro comando Streamlit executado
st.set_page_config(
    page_title="Sistema de Escala - Admin",
    page_icon="📅",
    layout="wide"
)

from models.database import Database
from views.admin_view import AdminView
from controllers.auth import AuthController
import config

# CSS customizado
st.markdown("""
<style>
    .stButton>button {
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    div[data-testid="stExpander"] {
        border-radius: 10px;
        border: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)


def main():
    """Função principal da aplicação admin"""
    try:
        # Inicializa o banco de dados
        db = Database()
        
        # Inicializa a view
        admin_view = AdminView(db)
        
        # Verifica autenticação
        if not AuthController.is_authenticated():
            admin_view.render_login()
        else:
            admin_view.render_admin_panel()
    
    except ValueError as e:
        st.error(f"❌ Erro de configuração: {e}")
        st.info("💡 Certifique-se de criar um arquivo `.env` com as credenciais do Supabase.")
    except Exception as e:
        st.error(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()
