# 🏗️ Arquitetura do Sistema

## 📊 Visão Geral

```
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA DE ESCALA BOL                     │
└─────────────────────────────────────────────────────────────┘

┌──────────────────────┐              ┌──────────────────────┐
│   TELA 1: ADMIN      │              │   TELA 2: PÚBLICA    │
│   (admin.py)         │              │   (public.py)        │
│                      │              │                      │
│  🔐 Login Required   │              │  👁️ View Only        │
│  ✏️ CRUD Operations  │              │  📊 Data Display     │
└──────────────────────┘              └──────────────────────┘
         │                                      │
         │                                      │
         └──────────────┬───────────────────────┘
                        │
                        ▼
         ┌──────────────────────────┐
         │   MVC ARCHITECTURE       │
         └──────────────────────────┘
                        │
         ┌──────────────┼──────────────┐
         │              │              │
         ▼              ▼              ▼
    ┌────────┐    ┌─────────┐    ┌────────┐
    │ MODEL  │    │  VIEW   │    │CONTROL │
    │        │    │         │    │        │
    │database│    │admin_   │    │ auth   │
    │  .py   │    │view.py  │    │  .py   │
    │        │    │public_  │    │        │
    │        │    │view.py  │    │        │
    └────────┘    └─────────┘    └────────┘
         │
         │
         ▼
    ┌─────────────────────────────┐
    │      SUPABASE DATABASE      │
    │                             │
    │  📅 escalas_sexta           │
    │  🎉 feriados                │
    └─────────────────────────────┘
```

## 🔄 Fluxo de Dados

### Tela Administrativa (Admin)

```
1. Usuário acessa admin.py
   ↓
2. AuthController verifica credenciais
   ↓
3. Se autenticado → AdminView renderiza painel
   ↓
4. Usuário realiza operação (CRUD)
   ↓
5. Database.py comunica com Supabase
   ↓
6. Dados são salvos/atualizados/deletados
   ↓
7. Interface atualiza automaticamente
```

### Tela Pública

```
1. Usuário acessa public.py
   ↓
2. PublicView renderiza interface
   ↓
3. Database.py busca dados no Supabase
   ↓
4. Dados são exibidos em tabelas
```

## 📁 Estrutura de Arquivos

```
sistema-de-escala-conteudo-bol/
│
├── 📄 config.py                 # Configurações centralizadas
├── 📄 admin.py                  # App Streamlit (Admin)
├── 📄 public.py                 # App Streamlit (Público)
│
├── 📁 models/
│   ├── __init__.py
│   └── database.py              # Camada de acesso ao BD
│
├── 📁 controllers/
│   ├── __init__.py
│   └── auth.py                  # Controle de autenticação
│
├── 📁 views/
│   ├── __init__.py
│   ├── admin_view.py            # Interface administrativa
│   └── public_view.py           # Interface pública
│
├── 📄 .env                      # Variáveis de ambiente (SECRETO)
├── 📄 .env.example              # Template de variáveis
├── 📄 .gitignore                # Proteção de arquivos sensíveis
│
├── 📄 requirements.txt          # Dependências Python
├── 📄 setup_supabase.sql        # Script de criação de tabelas
├── 📄 setup_database.py         # Helper de configuração
│
├── 📄 iniciar.bat               # Launcher Windows
├── 📄 README.md                 # Documentação principal
├── 📄 INSTALACAO.md             # Guia de instalação
├── 📄 CHECKLIST.md              # Checklist de configuração
└── 📄 ARQUITETURA.md            # Este arquivo
```

## 🔐 Camadas de Segurança

```
┌─────────────────────────────────────────┐
│  1. Autenticação de Email               │
│     ✓ Lista restrita de emails          │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  2. Verificação de Senha                │
│     ✓ Senha única para todos admins     │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  3. Variáveis de Ambiente               │
│     ✓ Credenciais em .env               │
│     ✓ .gitignore protege .env           │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  4. Supabase RLS (Row Level Security)   │
│     ✓ Políticas de acesso configuradas  │
└─────────────────────────────────────────┘
```

## 🗄️ Modelo de Dados

### Tabela: escalas_sexta

| Campo      | Tipo      | Descrição                    |
|------------|-----------|------------------------------|
| id         | BIGSERIAL | Chave primária (auto)        |
| nome       | TEXT      | Nome do colaborador          |
| data       | DATE      | Data da sexta-feira          |
| created_at | TIMESTAMP | Data de criação              |
| updated_at | TIMESTAMP | Data de atualização          |

### Tabela: feriados

| Campo            | Tipo      | Descrição                    |
|------------------|-----------|------------------------------|
| id               | BIGSERIAL | Chave primária (auto)        |
| nome_colaborador | TEXT      | Nome do colaborador          |
| nome_feriado     | TEXT      | Nome do feriado              |
| data             | DATE      | Data do feriado              |
| time             | TEXT      | Cadastro/SEO/FrontEnd        |
| created_at       | TIMESTAMP | Data de criação              |
| updated_at       | TIMESTAMP | Data de atualização          |

## 🎨 Padrão MVC Aplicado

### Model (models/database.py)
- Responsável por toda comunicação com Supabase
- Métodos CRUD para escalas e feriados
- Tratamento de erros de banco de dados

### View (views/)
- **admin_view.py**: Interface administrativa com formulários
- **public_view.py**: Interface pública somente leitura
- Renderização de componentes Streamlit

### Controller (controllers/auth.py)
- Gerenciamento de autenticação
- Verificação de permissões
- Controle de sessão

## 🚀 Deploy

### Opção 1: Local
```bash
streamlit run admin.py    # Porta 8501
streamlit run public.py   # Porta 8502
```

### Opção 2: Streamlit Cloud
1. Push para GitHub
2. Conectar no share.streamlit.io
3. Configurar secrets
4. Deploy automático

## 📊 Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal
- **Streamlit**: Framework web
- **Supabase**: Backend as a Service (PostgreSQL)
- **python-dotenv**: Gerenciamento de variáveis
- **pandas**: Manipulação de dados

## 🔄 Ciclo de Vida de uma Operação

```
Usuário → Interface (View) → Controller → Model → Supabase
                                                      ↓
Usuário ← Interface (View) ← Controller ← Model ← Resposta
```

---

**Desenvolvido para BEMOL S.A.**
*Sistema de Escala Conteúdo BOL*
