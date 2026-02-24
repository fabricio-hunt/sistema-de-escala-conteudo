"""
Aplicação Streamlit - Tela Pública (Visualização)
"""
import streamlit as st
from models.database import Database
from views.public_view import PublicView


def main():
    """Função principal da aplicação pública"""
    try:
        # Inicializa o banco de dados
        db = Database()
        
        # Inicializa e renderiza a view pública
        public_view = PublicView(db)
        public_view.render()
    
    except ValueError as e:
        st.error(f"❌ Erro de configuração: {e}")
        st.info("💡 Certifique-se de criar um arquivo `.env` com as credenciais do Supabase.")
    except Exception as e:
        st.error(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()
