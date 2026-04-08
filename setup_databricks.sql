-- Script SQL para configurar as tabelas no Supabase
-- Execute este script no SQL Editor do Supabase

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

-- Função para atualizar automaticamente o campo updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para escalas_sexta
DROP TRIGGER IF EXISTS update_escalas_sexta_updated_at ON escalas_sexta;
CREATE TRIGGER update_escalas_sexta_updated_at
    BEFORE UPDATE ON escalas_sexta
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Trigger para feriados
DROP TRIGGER IF EXISTS update_feriados_updated_at ON feriados;
CREATE TRIGGER update_feriados_updated_at
    BEFORE UPDATE ON feriados
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Habilitar Row Level Security (RLS) para segurança adicional
ALTER TABLE escalas_sexta ENABLE ROW LEVEL SECURITY;
ALTER TABLE feriados ENABLE ROW LEVEL SECURITY;

-- Política para permitir leitura pública (para a tela de visualização)
CREATE POLICY "Permitir leitura pública de escalas_sexta"
    ON escalas_sexta FOR SELECT
    USING (true);

CREATE POLICY "Permitir leitura pública de feriados"
    ON feriados FOR SELECT
    USING (true);

-- Política para permitir todas as operações com a chave anon
-- (a autenticação será feita na aplicação)
CREATE POLICY "Permitir todas operações em escalas_sexta"
    ON escalas_sexta FOR ALL
    USING (true)
    WITH CHECK (true);

CREATE POLICY "Permitir todas operações em feriados"
    ON feriados FOR ALL
    USING (true)
    WITH CHECK (true);

-- Dados de exemplo (opcional - remova se não quiser dados iniciais)
INSERT INTO escalas_sexta (nome, data) VALUES
    ('João Silva', '2026-01-31'),
    ('Maria Santos', '2026-02-07')
ON CONFLICT DO NOTHING;

INSERT INTO feriados (nome_colaborador, nome_feriado, data, time) VALUES
    ('Pedro Oliveira', 'Carnaval', '2026-02-16', 'SEO'),
    ('Ana Costa', 'Sexta-feira Santa', '2026-04-03', 'FrontEnd')
ON CONFLICT DO NOTHING;
