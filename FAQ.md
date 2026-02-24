# ❓ FAQ - Perguntas Frequentes

## 🔐 Autenticação e Acesso

### Como faço login no sistema?
1. Acesse a tela administrativa (`admin.py`)
2. Digite seu email autorizado (@bemol.com.br)
3. Digite a senha: `Bemol@2026`
4. Clique em "Entrar"

### Esqueci minha senha, como recupero?
A senha padrão é `Bemol@2026` para todos os administradores. Se precisar alterá-la, entre em contato com o administrador do sistema.

### Meu email não está funcionando, o que faço?
Verifique se seu email está na lista de administradores autorizados:
- alinesantiago@bemol.com.br
- fabriciomacedo@bemol.com.br
- antonioguedes@bemol.com.br
- carolinacosta@bemol.com.br

Se seu email não está na lista, solicite ao administrador que adicione em `config.py`.

### A tela pública precisa de login?
**Não!** A tela pública (`public.py`) é acessível sem login. Qualquer pessoa pode visualizar as escalas e feriados.

---

## 📅 Gerenciamento de Escalas

### Como adiciono uma nova escala de sexta-feira?
1. Faça login na tela administrativa
2. Vá para a aba "Escalas de Sexta-feira"
3. Clique em "Adicionar Nova Escala"
4. Preencha o nome do colaborador e a data
5. Clique em "Adicionar Escala"

### Como edito uma escala existente?
1. Na lista de escalas, clique no botão ✏️ (editar)
2. Modifique os dados desejados
3. Clique em "Salvar"

### Como deleto uma escala?
1. Na lista de escalas, clique no botão 🗑️ (deletar)
2. A escala será removida imediatamente

### Posso adicionar múltiplas escalas para o mesmo dia?
Sim! Você pode adicionar quantas escalas quiser para a mesma data.

---

## 🎉 Gerenciamento de Feriados

### Como adiciono um novo feriado?
1. Faça login na tela administrativa
2. Vá para a aba "Feriados"
3. Clique em "Adicionar Novo Feriado"
4. Preencha:
   - Nome do colaborador
   - Nome do feriado
   - Data do feriado
   - Time (Cadastro/SEO/FrontEnd)
5. Clique em "Adicionar Feriado"

### Quais são os times disponíveis?
- **Cadastro**
- **SEO**
- **FrontEnd**

### Posso adicionar um time personalizado?
Sim! Para adicionar um novo time, edite o arquivo `config.py` e adicione o nome na lista `TIMES`.

---

## 🛠️ Problemas Técnicos

### Erro: "No module named 'streamlit'"
**Solução:** Instale as dependências:
```bash
pip install -r requirements.txt
```

### Erro: "SUPABASE_KEY não configurada"
**Solução:** 
1. Verifique se o arquivo `.env` existe
2. Certifique-se de que contém a linha `SUPABASE_KEY=...`
3. Reinicie a aplicação

### Erro: "ModuleNotFoundError: No module named 'supabase'"
**Solução:** Instale as dependências:
```bash
pip install -r requirements.txt
```

### A aplicação não abre no navegador
**Solução:**
1. Verifique se a porta 8501 está livre
2. Tente acessar manualmente: http://localhost:8501
3. Reinicie a aplicação

### Os dados não aparecem na tela pública
**Solução:**
1. Verifique se as tabelas foram criadas no Supabase
2. Execute o script `setup_supabase.sql`
3. Verifique se há dados cadastrados na tela administrativa

---

## 🗄️ Banco de Dados

### Como crio as tabelas no Supabase?
1. Acesse https://ewgkfpbbdylakbxtndnh.supabase.co
2. Vá para **SQL Editor**
3. Copie o conteúdo de `setup_supabase.sql`
4. Cole e execute no SQL Editor

### Como verifico se as tabelas foram criadas?
1. No Supabase, vá para **Table Editor**
2. Você deve ver:
   - `escalas_sexta`
   - `feriados`

### Posso deletar dados diretamente no Supabase?
Sim, mas é recomendado usar a interface administrativa para manter o controle.

### Como faço backup dos dados?
No Supabase:
1. Vá para **Table Editor**
2. Selecione a tabela
3. Clique em **Export** → **CSV**

---

## 🚀 Deploy e Produção

### Como coloco o sistema online?
Siga o guia completo em `DEPLOY.md`. Resumo:
1. Faça push para o GitHub
2. Conecte no Streamlit Cloud
3. Configure os secrets
4. Deploy automático!

### Quanto custa hospedar?
- **Streamlit Cloud:** Gratuito
- **Supabase:** Plano gratuito disponível
- **Total:** R$ 0,00 (usando planos gratuitos)

### Posso usar um domínio personalizado?
Sim! O Streamlit Cloud permite configurar domínios personalizados no plano pago.

### Como atualizo o sistema em produção?
```bash
git add .
git commit -m "Descrição da atualização"
git push
```
O Streamlit Cloud fará deploy automático!

---

## 👥 Gerenciamento de Usuários

### Como adiciono um novo administrador?
1. Abra o arquivo `config.py`
2. Adicione o email na lista `ADMIN_EMAILS`
3. Salve e reinicie a aplicação

### Como removo um administrador?
1. Abra o arquivo `config.py`
2. Remova o email da lista `ADMIN_EMAILS`
3. Salve e reinicie a aplicação

### Como altero a senha padrão?
1. Abra o arquivo `.env`
2. Modifique a linha `ADMIN_PASSWORD=...`
3. Salve e reinicie a aplicação

---

## 📊 Visualização de Dados

### Os dados são atualizados em tempo real?
Sim! Sempre que você adiciona, edita ou deleta um registro, a tela é atualizada automaticamente.

### Posso exportar os dados?
Atualmente não há função de exportação na interface, mas você pode:
1. Acessar o Supabase
2. Ir para Table Editor
3. Exportar como CSV

### Posso filtrar os dados?
A funcionalidade de filtro não está implementada na versão atual, mas pode ser adicionada facilmente.

---

## 🔧 Personalização

### Como altero as cores do sistema?
Edite o arquivo `.streamlit/config.toml` e modifique as cores em `[theme]`.

### Como adiciono novos campos?
1. Adicione a coluna no Supabase (SQL Editor)
2. Atualize `models/database.py`
3. Atualize as views em `views/`

### Posso adicionar notificações por email?
Sim! Você precisará integrar um serviço de email (como SendGrid) e adicionar a lógica no código.

---

## 📱 Uso Mobile

### O sistema funciona no celular?
Sim! O Streamlit é responsivo e funciona em dispositivos móveis.

### Há um aplicativo mobile?
Não há app nativo, mas você pode acessar via navegador mobile.

---

## 🆘 Suporte

### Onde encontro mais documentação?
- `README.md` - Documentação completa
- `INSTALACAO.md` - Guia de instalação
- `ARQUITETURA.md` - Detalhes técnicos
- `DEPLOY.md` - Guia de deploy
- `CHECKLIST.md` - Checklist de configuração

### Como reporto um bug?
Entre em contato com o administrador do sistema ou crie uma issue no repositório GitHub.

### Posso contribuir com melhorias?
Sim! Faça um fork do repositório, implemente as melhorias e envie um pull request.

---

## 💡 Dicas e Truques

### Como faço para testar sem afetar os dados reais?
1. Crie um projeto separado no Supabase para testes
2. Configure um arquivo `.env.test` com as credenciais de teste
3. Use esse ambiente para testes

### Posso ter múltiplas instâncias rodando?
Sim! Cada instância pode rodar em uma porta diferente:
```bash
streamlit run admin.py --server.port 8501
streamlit run public.py --server.port 8502
```

### Como acelero o carregamento?
- Use índices no banco de dados (já configurados)
- Limite a quantidade de dados exibidos
- Use cache do Streamlit (@st.cache_data)

---

**Não encontrou sua pergunta?**  
Entre em contato com o administrador do sistema ou consulte a documentação completa.

---

**Sistema de Escala Conteúdo BOL**  
*BEMOL S.A. - 2026*
