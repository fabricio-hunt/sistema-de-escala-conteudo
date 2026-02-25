"""
View da Tela Pública (Visualização)
"""
import streamlit as st
import pandas as pd
from models.database import Database
import config


def _highlight_first_row(df: pd.DataFrame) -> list:
    """Retorna estilos para destacar a primeira linha (próxima data) em verde"""
    styles = []
    for i in range(len(df)):
        if i == 0:
            styles.append(['background-color: #1B5E20; color: #FFFFFF; font-weight: bold'] * len(df.columns))
        else:
            styles.append([''] * len(df.columns))
    return styles


class PublicView:
    """Tela pública para visualização de escalas e feriados"""
    
    def __init__(self, db: Database):
        self.db = db
    
    def _cleanup_past_entries(self):
        """Remove automaticamente entradas com datas passadas"""
        escalas_removed = self.db.delete_past_escalas()
        feriados_removed = self.db.delete_past_feriados()
        
        if escalas_removed > 0 or feriados_removed > 0:
            msgs = []
            if escalas_removed > 0:
                msgs.append(f"{escalas_removed} escala(s)")
            if feriados_removed > 0:
                msgs.append(f"{feriados_removed} feriado(s)")
            st.toast(f"🧹 Limpeza automática: {' e '.join(msgs)} com data passada removido(s).", icon="✅")
    
    def render(self):
        """Renderiza a tela pública"""
        st.set_page_config(
            page_title=config.APP_TITLE,
            page_icon=config.APP_ICON,
            layout="wide"
        )
        
        # Limpeza automática de entradas com data passada
        self._cleanup_past_entries()
        
        st.title(f"{config.APP_ICON} {config.APP_TITLE}")
        st.markdown("### 📊 Visualização de Escalas e Feriados")
        
        # Sidebar com link para o painel administrativo
        with st.sidebar:
            st.markdown("### ⚙️ Administração")
            st.link_button(
                "🔐 Acessar Painel Administrativo",
                "https://sistema-de-escala-conteudo-85qz5pgzcl4n6gv5woxxx9.streamlit.app",
                use_container_width=True
            )
            st.markdown("---")
        
        # Legenda de cores
        st.markdown(
            """
            <div style='display: flex; align-items: center; gap: 10px; margin-bottom: 10px;'>
                <div style='width: 18px; height: 18px; background-color: #1B5E20; border-radius: 3px;'></div>
                <span style='font-size: 0.9em; color: #555;'>🟢 Próxima data na escala (destaque)</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Seção de Escalas de Sexta-feira
        st.markdown("---")
        st.subheader("📅 Escalas de Sexta-feira")
        
        escalas = self.db.get_all_escalas()
        
        if escalas:
            df_escalas = pd.DataFrame(escalas)
            
            # Ordenar por data ascendente (mais próxima primeiro)
            df_escalas['data'] = pd.to_datetime(df_escalas['data'])
            df_escalas = df_escalas.sort_values('data', ascending=True).reset_index(drop=True)
            
            df_display = df_escalas[['nome', 'data']].copy()
            df_display.columns = ['Nome do Colaborador', 'Data da Sexta-feira']
            df_display['Data da Sexta-feira'] = df_display['Data da Sexta-feira'].dt.strftime('%d/%m/%Y')
            
            # Aplicar estilo com destaque na primeira linha
            styled = df_display.style.apply(
                lambda x: _highlight_first_row(df_display)[x.name], axis=1
            )
            
            st.dataframe(
                styled,
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
            
            # Ordenar por data ascendente (mais próxima primeiro)
            df_feriados['data'] = pd.to_datetime(df_feriados['data'])
            df_feriados = df_feriados.sort_values('data', ascending=True).reset_index(drop=True)
            
            df_display_f = df_feriados[['nome_colaborador', 'nome_feriado', 'data', 'time']].copy()
            df_display_f.columns = ['Nome do Colaborador', 'Nome do Feriado', 'Data do Feriado', 'Time']
            df_display_f['Data do Feriado'] = df_display_f['Data do Feriado'].dt.strftime('%d/%m/%Y')
            
            # Aplicar estilo com destaque na primeira linha
            styled_f = df_display_f.style.apply(
                lambda x: _highlight_first_row(df_display_f)[x.name], axis=1
            )
            
            st.dataframe(
                styled_f,
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
