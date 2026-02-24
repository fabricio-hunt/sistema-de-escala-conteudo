"""
View da Tela de Administração
"""
import streamlit as st
import pandas as pd
from datetime import date
from models.database import Database
from controllers.auth import AuthController
import config


class AdminView:
    """Tela de administração para gerenciar escalas e feriados"""
    
    def __init__(self, db: Database):
        self.db = db
    
    def render_login(self):
        """Renderiza a tela de login"""
        st.title(f"{config.APP_ICON} {config.APP_TITLE}")
        st.subheader("🔐 Área Administrativa")
        
        with st.form("login_form"):
            email = st.text_input("Email", placeholder="seu.email@bemol.com.br")
            password = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar", use_container_width=True)
            
            if submit:
                if AuthController.login(email, password):
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("Email ou senha inválidos!")
    
    def render_admin_panel(self):
        """Renderiza o painel administrativo"""
        st.title(f"{config.APP_ICON} {config.APP_TITLE}")
        
        # Header com informações do usuário
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("⚙️ Painel Administrativo")
        with col2:
            if st.button("🚪 Sair", use_container_width=True):
                AuthController.logout()
                st.rerun()
        
        st.info(f"👤 Logado como: **{AuthController.get_current_user()}**")
        
        # Tabs para diferentes seções
        tab1, tab2 = st.tabs(["📅 Escalas de Sexta-feira", "🎉 Feriados"])
        
        with tab1:
            self._render_escalas_section()
        
        with tab2:
            self._render_feriados_section()
    
    def _render_escalas_section(self):
        """Renderiza a seção de escalas de sexta-feira"""
        st.markdown("### Gerenciar Escalas de Sexta-feira")
        
        # Formulário para adicionar/editar
        with st.expander("➕ Adicionar Nova Escala", expanded=False):
            with st.form("add_escala_form"):
                nome = st.text_input("Nome do Colaborador")
                data = st.date_input("Data da Sexta-feira", value=date.today())
                submit = st.form_submit_button("Adicionar Escala", use_container_width=True)
                
                if submit:
                    if nome.strip():
                        if self.db.add_escala(nome, str(data)):
                            st.success("✅ Escala adicionada com sucesso!")
                            st.rerun()
                        else:
                            st.error("❌ Erro ao adicionar escala")
                    else:
                        st.warning("⚠️ Preencha o nome do colaborador")
        
        # Lista de escalas existentes
        st.markdown("#### 📋 Escalas Cadastradas")
        escalas = self.db.get_all_escalas()
        
        if escalas:
            for escala in escalas:
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 2, 1, 1])
                    
                    with col1:
                        st.text(f"👤 {escala['nome']}")
                    with col2:
                        st.text(f"📅 {escala['data']}")
                    with col3:
                        if st.button("✏️", key=f"edit_escala_{escala['id']}", help="Editar"):
                            st.session_state[f"editing_escala_{escala['id']}"] = True
                            st.rerun()
                    with col4:
                        if st.button("🗑️", key=f"del_escala_{escala['id']}", help="Deletar"):
                            if self.db.delete_escala(escala['id']):
                                st.success("Escala deletada!")
                                st.rerun()
                    
                    # Formulário de edição inline
                    if st.session_state.get(f"editing_escala_{escala['id']}", False):
                        with st.form(f"edit_form_escala_{escala['id']}"):
                            new_nome = st.text_input("Nome", value=escala['nome'])
                            new_data = st.date_input("Data", value=pd.to_datetime(escala['data']).date())
                            col_save, col_cancel = st.columns(2)
                            
                            with col_save:
                                save = st.form_submit_button("💾 Salvar", use_container_width=True)
                            with col_cancel:
                                cancel = st.form_submit_button("❌ Cancelar", use_container_width=True)
                            
                            if save:
                                if self.db.update_escala(escala['id'], new_nome, str(new_data)):
                                    st.session_state[f"editing_escala_{escala['id']}"] = False
                                    st.success("Atualizado!")
                                    st.rerun()
                            
                            if cancel:
                                st.session_state[f"editing_escala_{escala['id']}"] = False
                                st.rerun()
                    
                    st.divider()
        else:
            st.info("Nenhuma escala cadastrada ainda.")
    
    def _render_feriados_section(self):
        """Renderiza a seção de feriados"""
        st.markdown("### Gerenciar Feriados")
        
        # Formulário para adicionar
        with st.expander("➕ Adicionar Novo Feriado", expanded=False):
            with st.form("add_feriado_form"):
                nome_colaborador = st.text_input("Nome do Colaborador")
                nome_feriado = st.text_input("Nome do Feriado")
                data = st.date_input("Data do Feriado", value=date.today())
                time = st.selectbox("Time", config.TIMES)
                submit = st.form_submit_button("Adicionar Feriado", use_container_width=True)
                
                if submit:
                    if nome_colaborador.strip() and nome_feriado.strip():
                        if self.db.add_feriado(nome_colaborador, nome_feriado, str(data), time):
                            st.success("✅ Feriado adicionado com sucesso!")
                            st.rerun()
                        else:
                            st.error("❌ Erro ao adicionar feriado")
                    else:
                        st.warning("⚠️ Preencha todos os campos obrigatórios")
        
        # Lista de feriados existentes
        st.markdown("#### 📋 Feriados Cadastrados")
        feriados = self.db.get_all_feriados()
        
        if feriados:
            for feriado in feriados:
                with st.container():
                    col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 1, 1, 1])
                    
                    with col1:
                        st.text(f"👤 {feriado['nome_colaborador']}")
                    with col2:
                        st.text(f"🎉 {feriado['nome_feriado']}")
                    with col3:
                        st.text(f"📅 {feriado['data']}")
                    with col4:
                        st.text(f"👥 {feriado['time']}")
                    with col5:
                        if st.button("✏️", key=f"edit_feriado_{feriado['id']}", help="Editar"):
                            st.session_state[f"editing_feriado_{feriado['id']}"] = True
                            st.rerun()
                    with col6:
                        if st.button("🗑️", key=f"del_feriado_{feriado['id']}", help="Deletar"):
                            if self.db.delete_feriado(feriado['id']):
                                st.success("Feriado deletado!")
                                st.rerun()
                    
                    # Formulário de edição inline
                    if st.session_state.get(f"editing_feriado_{feriado['id']}", False):
                        with st.form(f"edit_form_feriado_{feriado['id']}"):
                            new_nome_colaborador = st.text_input("Colaborador", value=feriado['nome_colaborador'])
                            new_nome_feriado = st.text_input("Feriado", value=feriado['nome_feriado'])
                            new_data = st.date_input("Data", value=pd.to_datetime(feriado['data']).date())
                            new_time = st.selectbox("Time", config.TIMES, 
                                                   index=config.TIMES.index(feriado['time']) if feriado['time'] in config.TIMES else 0)
                            
                            col_save, col_cancel = st.columns(2)
                            
                            with col_save:
                                save = st.form_submit_button("💾 Salvar", use_container_width=True)
                            with col_cancel:
                                cancel = st.form_submit_button("❌ Cancelar", use_container_width=True)
                            
                            if save:
                                if self.db.update_feriado(feriado['id'], new_nome_colaborador, 
                                                         new_nome_feriado, str(new_data), new_time):
                                    st.session_state[f"editing_feriado_{feriado['id']}"] = False
                                    st.success("Atualizado!")
                                    st.rerun()
                            
                            if cancel:
                                st.session_state[f"editing_feriado_{feriado['id']}"] = False
                                st.rerun()
                    
                    st.divider()
        else:
            st.info("Nenhum feriado cadastrado ainda.")
