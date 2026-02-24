# Script para criar as tabelas no Supabase via Python
# Execute este script se preferir criar as tabelas via código ao invés do SQL Editor

from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = "https://ewgkfpbbdylakbxtndnh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV3Z2tmcGJiZHlsYWtieHRuZG5oIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk1MzQ4NzMsImV4cCI6MjA4NTExMDg3M30.uZqfX4i3_H4_F-hkNrJBG9p8W7RTvYDbobf1VVB9WZY"

def setup_database():
    """Configura as tabelas no Supabase"""
    
    print("🔧 Configurando banco de dados no Supabase...")
    
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # SQL para criar as tabelas
    sql_commands = """
    -- Tabela de Escalas de Sexta-feira
    CREATE TABLE IF NOT EXISTS escalas_sexta (
      id BIGSERIAL PRIMARY KEY,
      nome TEXT NOT NULL,
      data DATE NOT NULL,
      created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
      updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

    -- Índice para melhorar performance de busca por data
    CREATE INDEX IF NOT EXISTS idx_escalas_sexta_data ON escalas_sexta(data DESC);

    -- Tabela de Feriados
    CREATE TABLE IF NOT EXISTS feriados (
      id BIGSERIAL PRIMARY KEY,
      nome_colaborador TEXT NOT NULL,
      nome_feriado TEXT NOT NULL,
      data DATE NOT NULL,
      time TEXT NOT NULL CHECK (time IN ('Cadastro', 'SEO', 'FrontEnd')),
      created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
      updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

    -- Índice para melhorar performance de busca por data
    CREATE INDEX IF NOT EXISTS idx_feriados_data ON feriados(data DESC);

    -- Índice para busca por time
    CREATE INDEX IF NOT EXISTS idx_feriados_time ON feriados(time);
    """
    
    print("\n⚠️  ATENÇÃO:")
    print("Este script requer acesso ao SQL Editor do Supabase.")
    print("\nPara configurar o banco de dados:")
    print("1. Acesse: https://ewgkfpbbdylakbxtndnh.supabase.co")
    print("2. Vá para 'SQL Editor'")
    print("3. Copie e cole o conteúdo do arquivo 'setup_supabase.sql'")
    print("4. Execute o script")
    print("\n✅ Após executar o SQL, você poderá usar o sistema normalmente!")

if __name__ == "__main__":
    setup_database()
