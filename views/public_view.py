"""
View da Tela Pública (Visualização)
"""
import streamlit as st
import pandas as pd
from models.database import Database
import config


class PublicView:
    """Tela pública para visualização de escalas e feriados"""
    
    def __init__(self, db: Database):
        self.db = db
    
    def render(self):
        """Renderiza a tela pública"""
        st.set_page_config(
            page_title=config.APP_TITLE,
            page_icon=config.APP_ICON,
            layout="wide"
        )
        
        st.title(f"{config.APP_ICON} {config.APP_TITLE}")
        st.markdown("### 📊 Visualização de Escalas e Feriados")
        
        # Seção de Escalas de Sexta-feira
        st.markdown("---")
        st.subheader("📅 Escalas de Sexta-feira")
        
        escalas = self.db.get_all_escalas()
        
        if escalas:
            df_escalas = pd.DataFrame(escalas)
            df_escalas = df_escalas[['nome', 'data']].rename(columns={
                'nome': 'Nome do Colaborador',
                'data': 'Data da Sexta-feira'
            })
            
            # Formatar data
            df_escalas['Data da Sexta-feira'] = pd.to_datetime(df_escalas['Data da Sexta-feira']).dt.strftime('%d/%m/%Y')
            
            st.dataframe(
                df_escalas,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("📭 Nenhuma escala cadastrada no momento.")
        
        # Seção de Feriados
        st.markdown("---")
        st.subheader("🎉 Feriados")
        
        feriados = self.db.get_all_feriados()
        
        if feriados:
            df_feriados = pd.DataFrame(feriados)
            df_feriados = df_feriados[['nome_colaborador', 'nome_feriado', 'data', 'time']].rename(columns={
                'nome_colaborador': 'Nome do Colaborador',
                'nome_feriado': 'Nome do Feriado',
                'data': 'Data do Feriado',
                'time': 'Time'
            })
            
            # Formatar data
            df_feriados['Data do Feriado'] = pd.to_datetime(df_feriados['Data do Feriado']).dt.strftime('%d/%m/%Y')
            
            st.dataframe(
                df_feriados,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("📭 Nenhum feriado cadastrado no momento.")
        
        # Footer
        st.markdown("---")
        st.markdown(
            """
            <div style='text-align: center; color: #666; padding: 20px;'>
                <p>Sistema de Escala Conteúdo BOL - BEMOL S.A.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
