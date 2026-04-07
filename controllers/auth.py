"""
Controlador de Autenticação
"""
import streamlit as st
import config


class AuthController:
    """Gerencia autenticação de administradores"""
    
    @staticmethod
    def is_admin_email(email: str) -> bool:
        """Verifica se o email está na lista de administradores"""
        return email.lower() in [e.lower() for e in config.ADMIN_EMAILS]
    
    @staticmethod
    def verify_password(password: str) -> bool:
        """Verifica se a senha está correta usando bcrypt hash"""
        import bcrypt
        try:
            return bcrypt.checkpw(
                password.encode('utf-8'), 
                config.ADMIN_PASSWORD_HASH.encode('utf-8')
            )
        except Exception as e:
            print(f"Erro de verificação bcrypt: {e}")
            return False
    
    @staticmethod
    def login(email: str, password: str) -> bool:
        """Realiza o login do administrador"""
        if AuthController.is_admin_email(email) and AuthController.verify_password(password):
            st.session_state.authenticated = True
            st.session_state.admin_email = email
            return True
        return False
    
    @staticmethod
    def logout():
        """Realiza o logout"""
        st.session_state.authenticated = False
        st.session_state.admin_email = None
    
    @staticmethod
    def is_authenticated() -> bool:
        """Verifica se há um usuário autenticado"""
        return st.session_state.get("authenticated", False)
    
    @staticmethod
    def get_current_user() -> str:
        """Retorna o email do usuário autenticado"""
        return st.session_state.get("admin_email", "")
