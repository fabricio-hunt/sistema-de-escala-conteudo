# Guia de Instalacao Rapida

## Passo 1: Configurar o Supabase

1. Acesse o Supabase
2. Va para **SQL Editor**
3. Copie e cole o conteudo do arquivo `setup_supabase.sql`
4. Execute o script para criar as tabelas

## Passo 2: Instalar Dependencias

```bash
# Ativar ambiente virtual (se ainda nao estiver ativo)
python -m venv venv
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Passo 3: Executar a Aplicacao

### Tela Administrativa
```bash
streamlit run admin.py
```

### Tela Publica
```bash
streamlit run public.py
```

## Credenciais de Acesso (Admin)

**Emails autorizados:**
Verifique a lista em `config.py`

**Senha:**
Verifique a senha configurada no seu arquivo `.env`

## Notas Importantes

- O arquivo `.env` deve ser configurado com as credenciais
- O `.gitignore` protege suas credenciais
- Execute primeiro o script SQL no Supabase antes de rodar a aplicacao
- A tela publica nao requer login
- Apenas administradores podem inserir, atualizar ou deletar dados
