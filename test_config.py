import streamlit as st
import os

st.title("🛠️ Diagnóstico de Configuração")

st.write("Verificando variáveis de ambiente e secrets...")

# 1. Verificar st.secrets
st.subheader("1. Streamlit Secrets (st.secrets)")
try:
    if hasattr(st, 'secrets'):
        st.success("✅ st.secrets está disponível")
        
        # Listar chaves (sem mostrar valores)
        keys = list(st.secrets.keys())
        st.write(f"Chaves encontradas: {keys}")
        
        if "SUPABASE_KEY" in st.secrets:
            st.success("✅ SUPABASE_KEY encontrada em secrets")
            key_val = st.secrets["SUPABASE_KEY"]
            st.write(f"Começa com: {key_val[:10]}...")
            st.write(f"Tamanho: {len(key_val)}")
        else:
            st.error("❌ SUPABASE_KEY NÃO encontrada em secrets")
            
    else:
        st.error("❌ st.secrets NÃO está disponível")
except Exception as e:
    st.error(f"Erro ao acessar secrets: {e}")

# 2. Verificar Environment Variables
st.subheader("2. Variáveis de Ambiente (os.environ)")
if "SUPABASE_KEY" in os.environ:
    st.success("✅ SUPABASE_KEY encontrada em environment")
else:
    st.warning("⚠️ SUPABASE_KEY não encontrada em environment (Normal no Streamlit Cloud)")

# 3. Teste do módulo config.py
st.subheader("3. Teste do módulo config.py")
try:
    import config
    st.write(f"SUPABASE_URL do config: {config.SUPABASE_URL}")
    
    if config.SUPABASE_KEY:
        st.success("✅ Config.py carregou a chave com sucesso!")
        st.write(f"Tamanho da chave: {len(config.SUPABASE_KEY)}")
    else:
        st.error("❌ Config.py retornou chave vazia")
except Exception as e:
    st.error(f"Erro ao importar config: {e}")
