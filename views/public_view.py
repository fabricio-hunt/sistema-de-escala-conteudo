"""
View da Tela Pública (Visualização)
"""
import streamlit as st
import pandas as pd
from models.database import Database
import config


def _render_html_table_escalas(df: pd.DataFrame):
    """Renderiza tabela HTML de escalas com a primeira linha destacada em vermelho claro"""
    html = """
    <style>
        .escala-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 14px;
            margin-bottom: 20px;
        }
        .escala-table th {
            background-color: #f0f2f6;
            color: #31333F;
            padding: 12px 16px;
            text-align: left;
            border-bottom: 2px solid #ddd;
            font-weight: 600;
        }
        .escala-table td {
            padding: 10px 16px;
            border-bottom: 1px solid #eee;
        }
        .escala-table tr:hover {
            background-color: #f8f9fa;
        }
        .escala-table .highlight-row {
            background-color: #FFCDD2 !important;
            font-weight: bold;
        }
        .escala-table .highlight-row td {
            color: #B71C1C;
        }
    </style>
    <table class="escala-table">
        <thead>
            <tr>
                <th>Nome do Colaborador</th>
                <th>Data da Sexta-feira</th>
            </tr>
        </thead>
        <tbody>
    """
    for i, row in df.iterrows():
        row_class = 'highlight-row' if i == 0 else ''
        html += f"""
            <tr class="{row_class}">
                <td>{row['nome']}</td>
                <td>{row['data_formatada']}</td>
            </tr>
        """
    html += """
        </tbody>
    </table>
    """
    return html


def _render_html_table_feriados(df: pd.DataFrame):
    """Renderiza tabela HTML de feriados com a primeira linha destacada em vermelho claro"""
    html = """
    <style>
        .feriado-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 14px;
            margin-bottom: 20px;
        }
        .feriado-table th {
            background-color: #f0f2f6;
            color: #31333F;
            padding: 12px 16px;
            text-align: left;
            border-bottom: 2px solid #ddd;
            font-weight: 600;
        }
        .feriado-table td {
            padding: 10px 16px;
            border-bottom: 1px solid #eee;
        }
        .feriado-table tr:hover {
            background-color: #f8f9fa;
        }
        .feriado-table .highlight-row {
            background-color: #FFCDD2 !important;
            font-weight: bold;
        }
        .feriado-table .highlight-row td {
            color: #B71C1C;
        }
    </style>
    <table class="feriado-table">
        <thead>
            <tr>
                <th>Nome do Colaborador</th>
                <th>Nome do Feriado</th>
                <th>Data do Feriado</th>
                <th>Time</th>
            </tr>
        </thead>
        <tbody>
    """
    for i, row in df.iterrows():
        row_class = 'highlight-row' if i == 0 else ''
        html += f"""
            <tr class="{row_class}">
                <td>{row['nome_colaborador']}</td>
                <td>{row['nome_feriado']}</td>
                <td>{row['data_formatada']}</td>
                <td>{row['time']}</td>
            </tr>
        """
    html += """
        </tbody>
    </table>
    """
    return html


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
                <div style='width: 18px; height: 18px; background-color: #FFCDD2; border: 1px solid #E57373; border-radius: 3px;'></div>
                <span style='font-size: 0.9em; color: #555;'>🔴 Próxima data na escala (destaque)</span>
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
            df_escalas['data_dt'] = pd.to_datetime(df_escalas['data'])
            df_escalas = df_escalas.sort_values('data_dt', ascending=True).reset_index(drop=True)
            df_escalas['data_formatada'] = df_escalas['data_dt'].dt.strftime('%d/%m/%Y')
            
            # Renderizar tabela HTML com destaque
            html_table = _render_html_table_escalas(df_escalas)
            st.markdown(html_table, unsafe_allow_html=True)
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
            
            # Renderizar tabela HTML com destaque
            html_table_f = _render_html_table_feriados(df_feriados)
            st.markdown(html_table_f, unsafe_allow_html=True)
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
