# Guia de Deploy no Streamlit Cloud

## Pre-requisitos

- [ ] Conta no GitHub
- [ ] Conta no Streamlit Cloud (https://share.streamlit.io)
- [ ] Banco de dados Supabase configurado

## Passo a Passo

### 1. Preparar o Repositorio GitHub

#### 1.1 Criar repositorio no GitHub
1. Acesse https://github.com
2. Clique em **New Repository**
3. Nome: `sistema-escala-bol`
4. Visibilidade: **Private** (recomendado)
5. Clique em **Create repository**

#### 1.2 Fazer push do codigo
```bash
cd "c:\Users\fabricio.barauna\OneDrive - BEMOL S A\Documentos\sistema-de-escala-conteudo-bol"

# Inicializar git (se ainda nao foi feito)
git init

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit - Sistema de Escala BOL"

# Adicionar remote (substitua SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/sistema-escala-bol.git

# Push para o GitHub
git push -u origin main
```

**IMPORTANTE:** O arquivo `.env` NAO sera enviado (esta no .gitignore)

### 2. Configurar Streamlit Cloud

#### 2.1 Acessar Streamlit Cloud
1. Acesse https://share.streamlit.io
2. Faca login com sua conta GitHub
3. Clique em **New app**

#### 2.2 Configurar App Administrativo

**Configuracoes:**
- Repository: `SEU_USUARIO/sistema-escala-bol`
- Branch: `main`
- Main file path: `admin.py`
- App URL: `escala-bol-admin` (ou outro nome)

#### 2.3 Configurar Secrets

Clique em **Advanced settings** -> **Secrets**

Cole o seguinte conteudo (substitua pelos seus dados do .env):

```toml
SUPABASE_URL = "sua_url_do_supabase"
SUPABASE_KEY = "sua_chave_anonima_do_supabase"
ADMIN_PASSWORD = "sua_senha_segura"
```

#### 2.4 Deploy
1. Clique em **Deploy!**
2. Aguarde o build
3. Sua app estara disponivel em: `https://escala-bol-admin.streamlit.app`

### 3. Configurar App Publico

Repita o processo acima, mas com as seguintes diferencas:

**Configuracoes:**
- Repository: `SEU_USUARIO/sistema-escala-bol`
- Branch: `main`
- Main file path: `public.py`
- App URL: `escala-bol-publico`

**Secrets:** (mesmos do app admin)

### 4. Atualizar config.py para Streamlit Cloud

Crie um arquivo `.streamlit/secrets.toml` no repositorio (opcional, apenas para desenvolvimento local se nao usar .env):

```bash
mkdir .streamlit
```

Adicione ao `.gitignore` se criar localmente:
```
.streamlit/secrets.toml
```

O `config.py` ja esta configurado para ler do Streamlit secrets.

## URLs Finais

Apos o deploy, voce tera:

- **Admin:** https://escala-bol-admin.streamlit.app
- **Publico:** https://escala-bol-publico.streamlit.app

## Atualizacoes

Para atualizar a aplicacao:

```bash
# Fazer alteracoes no codigo
git add .
git commit -m "Descricao da alteracao"
git push

# O Streamlit Cloud fara deploy automatico!
```

## Seguranca

### Boas Praticas Implementadas

1. **Secrets no Streamlit Cloud**: Credenciais nao ficam no codigo
2. **Repositorio Privado**: Codigo nao e publico
3. **`.gitignore`**: Arquivo `.env` nunca e commitado
4. **Autenticacao**: Apenas admins acessam area administrativa

### Importante

- Nunca commite o arquivo `.env`
- Mantenha o repositorio privado
- Nao compartilhe as URLs publicamente (especialmente a admin)
- Considere adicionar autenticacao adicional se necessario

## Troubleshooting

### Erro: "ModuleNotFoundError"
**Solucao:** Verifique se `requirements.txt` esta correto

### Erro: "SUPABASE_KEY nao configurada"
**Solucao:** Verifique os Secrets no Streamlit Cloud

### App nao atualiza apos push
**Solucao:** 
1. Acesse o dashboard do Streamlit Cloud
2. Clique em **Reboot app**

### Erro de conexao com Supabase
**Solucao:** Verifique se as tabelas foram criadas corretamente

## Monitoramento

No Streamlit Cloud voce pode:
- Ver logs em tempo real
- Monitorar uso de recursos
- Reiniciar a aplicacao
- Ver metricas de acesso

## Custos

- **Streamlit Cloud:** Gratuito para apps publicos
- **Supabase:** Plano gratuito disponivel
- **GitHub:** Gratuito para repositorios privados

## Pronto!

Seu sistema esta no ar e acessivel de qualquer lugar!

---

**Desenvolvido para BEMOL S.A.**
