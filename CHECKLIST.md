# ✅ Checklist de Configuração

## 📋 Antes de Começar

- [ ] Python 3.8+ instalado
- [ ] Acesso ao Supabase (https://ewgkfpbbdylakbxtndnh.supabase.co)

## 🔧 Configuração do Banco de Dados

### Passo 1: Acessar o Supabase
1. [ ] Acesse https://ewgkfpbbdylakbxtndnh.supabase.co
2. [ ] Faça login na sua conta

### Passo 2: Criar as Tabelas
1. [ ] Clique em **SQL Editor** no menu lateral
2. [ ] Clique em **New Query**
3. [ ] Abra o arquivo `setup_supabase.sql` deste projeto
4. [ ] Copie TODO o conteúdo do arquivo
5. [ ] Cole no SQL Editor do Supabase
6. [ ] Clique em **Run** (ou pressione Ctrl+Enter)
7. [ ] Verifique se apareceu "Success. No rows returned"

### Passo 3: Verificar as Tabelas
1. [ ] Clique em **Table Editor** no menu lateral
2. [ ] Você deve ver duas tabelas:
   - `escalas_sexta`
   - `feriados`

## 💻 Configuração Local

### Passo 1: Instalar Dependências
```bash
pip install -r requirements.txt
```
- [ ] Comando executado com sucesso

### Passo 2: Verificar Arquivo .env
- [ ] O arquivo `.env` existe na raiz do projeto
- [ ] Contém as três variáveis:
  - `SUPABASE_URL`
  - `SUPABASE_KEY`
  - `ADMIN_PASSWORD`

## 🚀 Testar a Aplicação

### Teste 1: Tela Administrativa
```bash
streamlit run admin.py
```
- [ ] Aplicação abriu no navegador
- [ ] Tela de login apareceu
- [ ] Login funcionou com email e senha corretos
- [ ] Consegue adicionar uma escala de teste
- [ ] Consegue adicionar um feriado de teste

### Teste 2: Tela Pública
```bash
streamlit run public.py
```
- [ ] Aplicação abriu no navegador
- [ ] Dados cadastrados aparecem na tela
- [ ] Não há tela de login (acesso público)

## 🎯 Emails Autorizados

Verifique se estes emails estão configurados:
- [ ] alinesantiago@bemol.com.br
- [ ] fabriciomacedo@bemol.com.br
- [ ] antonioguedes@bemol.com.br
- [ ] carolinacosta@bemol.com.br

## 🔐 Senha Padrão

- [ ] Senha: `Bemol@2026`

## 📝 Próximos Passos

Após completar todos os itens acima:
- [ ] Testar todas as funcionalidades (inserir, editar, deletar)
- [ ] Verificar se os dados aparecem na tela pública
- [ ] Preparar para deploy no Streamlit Cloud (opcional)

## 🆘 Problemas Comuns

### Erro: "No module named 'supabase'"
**Solução:** Execute `pip install -r requirements.txt`

### Erro: "SUPABASE_KEY não configurada"
**Solução:** Verifique se o arquivo `.env` existe e contém a chave

### Erro ao fazer login
**Solução:** Verifique se o email está na lista de autorizados e a senha está correta

### Tabelas não aparecem no Supabase
**Solução:** Execute novamente o script SQL no SQL Editor

## ✅ Configuração Completa!

Se todos os itens estão marcados, seu sistema está pronto para uso! 🎉
