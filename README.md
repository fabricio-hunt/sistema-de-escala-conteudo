# Sistema de Escala Conteudo BOL

Sistema de gerenciamento de escalas de sexta-feira e feriados para a equipe de conteudo da BEMOL.

## Arquitetura

O projeto segue o padrao MVC (Model-View-Controller):

```
sistema-de-escala-conteudo-bol/
├── models/
│   └── database.py          # Camada de acesso ao banco (Supabase)
├── views/
│   ├── admin_view.py        # Interface administrativa
│   └── public_view.py       # Interface publica
├── controllers/
│   └── auth.py              # Controle de autenticacao
├── admin.py                 # Aplicacao Streamlit (Admin)
├── public.py                # Aplicacao Streamlit (Publico)
├── config.py                # Configuracoes centralizadas
├── requirements.txt         # Dependencias Python
├── .env                     # Variaveis de ambiente (NAO COMMITAR)
└── .env.example             # Template de variaveis
```

## Seguranca

- Credenciais armazenadas em variaveis de ambiente (.env)
- .gitignore configurado para proteger dados sensiveis
- Autenticacao obrigatoria para area administrativa
- Lista restrita de emails autorizados
- Separacao clara entre tela publica e administrativa

## Instalacao

### 1. Clone o repositorio

```bash
cd "c:\Users\fabricio.barauna\OneDrive - BEMOL S A\Documentos\sistema-de-escala-conteudo-bol"
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instale as dependencias

```bash
pip install -r requirements.txt
```

### 4. Configure as variaveis de ambiente

Crie um arquivo .env baseado no .env.example:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_anonima_do_supabase
ADMIN_PASSWORD=sua_senha_segura
```

### 5. Configure o Supabase

Crie as seguintes tabelas no Supabase:

#### Tabela: escalas_sexta
```sql
CREATE TABLE escalas_sexta (
  id BIGSERIAL PRIMARY KEY,
  nome TEXT NOT NULL,
  data DATE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Tabela: feriados
```sql
CREATE TABLE feriados (
  id BIGSERIAL PRIMARY KEY,
  nome_colaborador TEXT NOT NULL,
  nome_feriado TEXT NOT NULL,
  data DATE NOT NULL,
  time TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Uso

### Tela Administrativa (Admin)

```bash
streamlit run admin.py
```

**Credenciais de acesso:**
- Emails autorizados (configurados em config.py)
- Senha: (configurada no arquivo .env)

**Funcionalidades:**
- Login seguro
- Adicionar escalas de sexta-feira
- Editar escalas existentes
- Deletar escalas
- Adicionar feriados
- Editar feriados
- Deletar feriados

### Tela Publica (Visualizacao)

```bash
streamlit run public.py
```

**Funcionalidades:**
- Visualizacao de todas as escalas de sexta-feira
- Visualizacao de todos os feriados
- Sem necessidade de login
- Interface limpa e responsiva

## Deploy no Streamlit Cloud

1. Faca push do codigo para o GitHub
2. Acesse share.streamlit.io
3. Conecte seu repositorio
4. Configure os Secrets no Streamlit Cloud:
   ```toml
   SUPABASE_URL = "sua_url_do_supabase"
   SUPABASE_KEY = "sua_chave_anonima_do_supabase"
   ADMIN_PASSWORD = "sua_senha_segura"
   ```
5. Deploy automatico!

## Tecnologias

- Python 3.x
- Streamlit - Framework web
- Supabase - Banco de dados PostgreSQL
- python-dotenv - Gerenciamento de variaveis de ambiente
- pandas - Manipulacao de dados

## Licenca

Propriedade de BEMOL S.A.
