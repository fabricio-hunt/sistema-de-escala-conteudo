"""
View da Tela Pública (Visualização)
"""
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from models.database import Database
import config


def _build_escalas_html(df: pd.DataFrame) -> str:
    """Constrói HTML da tabela de escalas com destaque na primeira linha"""
    rows_html = ""
    for i, row in df.iterrows():
        if i == 0:
            rows_html += f"""
            <tr style="background-color: #FFCDD2; font-weight: bold;">
                <td style="color: #B71C1C;">{row['nome']}</td>
                <td style="color: #B71C1C;">{row['data_formatada']}</td>
            </tr>"""
        else:
            rows_html += f"""
            <tr>
                <td>{row['nome']}</td>
                <td>{row['data_formatada']}</td>
            </tr>"""

    height = 48 + len(df) * 45 + 10
    html = f"""
    <div style="font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, sans-serif; font-size: 14px;">
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background-color: #f0f2f6;">
                    <th style="padding: 12px 16px; text-align: left; border-bottom: 2px solid #ddd; color: #31333F; font-weight: 600;">Nome do Colaborador</th>
                    <th style="padding: 12px 16px; text-align: left; border-bottom: 2px solid #ddd; color: #31333F; font-weight: 600;">Data da Sexta-feira</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    <style>
        table td {{ padding: 10px 16px; border-bottom: 1px solid #eee; }}
        table tr:hover {{ background-color: #f8f9fa; }}
    </style>
    """
    return html, height


def _build_feriados_html(df: pd.DataFrame) -> str:
    """Constrói HTML da tabela de feriados com destaque na primeira linha"""
    rows_html = ""
    for i, row in df.iterrows():
        if i == 0:
            rows_html += f"""
            <tr style="background-color: #FFCDD2; font-weight: bold;">
                <td style="color: #B71C1C;">{row['nome_colaborador']}</td>
                <td style="color: #B71C1C;">{row['nome_feriado']}</td>
                <td style="color: #B71C1C;">{row['data_formatada']}</td>
                <td style="color: #B71C1C;">{row['time']}</td>
            </tr>"""
        else:
            rows_html += f"""
            <tr>
                <td>{row['nome_colaborador']}</td>
                <td>{row['nome_feriado']}</td>
                <td>{row['data_formatada']}</td>
                <td>{row['time']}</td>
            </tr>"""

    height = 48 + len(df) * 45 + 10
    html = f"""
    <div style="font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, sans-serif; font-size: 14px;">
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background-color: #f0f2f6;">
                    <th style="padding: 12px 16px; text-align: left; border-bottom: 2px solid #ddd; color: #31333F; font-weight: 600;">Nome do Colaborador</th>
                    <th style="padding: 12px 16px; text-align: left; border-bottom: 2px solid #ddd; color: #31333F; font-weight: 600;">Nome do Feriado</th>
                    <th style="padding: 12px 16px; text-align: left; border-bottom: 2px solid #ddd; color: #31333F; font-weight: 600;">Data do Feriado</th>
                    <th style="padding: 12px 16px; text-align: left; border-bottom: 2px solid #ddd; color: #31333F; font-weight: 600;">Time</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    <style>
        table td {{ padding: 10px 16px; border-bottom: 1px solid #eee; }}
        table tr:hover {{ background-color: #f8f9fa; }}
    </style>
    """
    return html, height


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
        
        # Seção de Escalas de Sexta-feira
        st.markdown("---")
        st.subheader("📅 Escalas de Sexta-feira")
        
        escalas = self.db.get_all_escalas()
        
        if escalas:
            df_escalas = pd.DataFrame(escalas)
            
            # Ordenar por data ascendente (mais próxima primeiro)
            df_escalas['data_dt'] = pd.to_datetime(df_escalas['data'])
            df_escalas = df_escalas.sort_values('data_dt', ascending=True).reset_index(drop=True)
            df_escalas['data_formatada'] = df_escalas['data_dt'].dt.strftime('%d/%m/%Y')
            
            html, height = _build_escalas_html(df_escalas)
            components.html(html, height=height, scrolling=False)
        else:
            st.info("📭 Nenhuma escala cadastrada no momento.")
        
        # Seção de Feriados
        st.markdown("---")
        st.subheader("🎉 Feriados")
        
        feriados = self.db.get_all_feriados()
        
        if feriados:
            df_feriados = pd.DataFrame(feriados)
            
            # Ordenar por data ascendente (mais próxima primeiro)
            df_feriados['data_dt'] = pd.to_datetime(df_feriados['data'])
            df_feriados = df_feriados.sort_values('data_dt', ascending=True).reset_index(drop=True)
            df_feriados['data_formatada'] = df_feriados['data_dt'].dt.strftime('%d/%m/%Y')
            
            html_f, height_f = _build_feriados_html(df_feriados)
            components.html(html_f, height=height_f, scrolling=False)
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
