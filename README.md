# Sistema de Escala Conteudo BOL

Sistema de gerenciamento de escalas de sexta-feira e feriados para a equipe de conteudo da BEMOL.

## Arquitetura

O projeto segue o padrao MVC (Model-View-Controller):

```
sistema-de-escala-conteudo-bol/
├── models/
│   └── database.py          # Camada de acesso ao banco (Databricks)
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
DATABRICKS_SERVER_HOSTNAME=adb-926216925051160.0.azuredatabricks.net
DATABRICKS_HTTP_PATH=sql/protocolv1/o/926216925051160/0325-154030-toes330
DATABRICKS_TOKEN=seu_personal_access_token_aqui
ADMIN_PASSWORD=sua_senha_segura
```

### 5. Configure o Databricks

Para inicializar as tabelas `escalas_sexta` e `feriados` no Databricks, certifique-se de que configurou as variáveis no arquivo `.env` e, em seguida, execute o script de inicialização do banco:

```bash
python setup_database.py
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
- 🧹 **Limpeza automatica** de escalas e feriados com data passada ao acessar o painel

### Tela Publica (Visualizacao)

```bash
streamlit run public.py
```

**Funcionalidades:**
- Visualizacao de todas as escalas de sexta-feira
- Visualizacao de todos os feriados
- 📅 **Ordenacao por data ascendente** — a data mais proxima (recente) sempre aparece no topo da tabela
- 🔴 **Destaque visual** — a primeira linha (proxima data) e destacada em vermelho claro para facil identificacao
- 🧹 **Limpeza automatica** — entradas com data passada sao deletadas automaticamente ao carregar a pagina
- Sem necessidade de login
- Interface limpa e responsiva

## Deploy no Streamlit Cloud

1. Faca push do codigo para o GitHub
2. Acesse share.streamlit.io
3. Conecte seu repositorio
4. Configure os Secrets no Streamlit Cloud:
   ```toml
   DATABRICKS_SERVER_HOSTNAME = "adb-926216925051160.0.azuredatabricks.net"
   DATABRICKS_HTTP_PATH = "sql/protocolv1/o/926216925051160/0325-154030-toes330"
   DATABRICKS_TOKEN = "seu_personal_access_token_aqui"
   ADMIN_PASSWORD = "sua_senha_segura"
   ```
5. Deploy automatico!

## Tecnologias

- Python 3.x
- Streamlit - Framework web
- Databricks - Cloud Data Platform
- python-dotenv - Gerenciamento de variaveis de ambiente
- pandas - Manipulacao de dados

## Licenca

Propriedade de BEMOL S.A.
