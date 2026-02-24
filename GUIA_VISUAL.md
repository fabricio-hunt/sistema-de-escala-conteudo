# 🎨 Guia Visual de Uso - Sistema de Escala Conteúdo BOL

## 📱 Visão Geral das Telas

O sistema possui **duas aplicações independentes**:

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  🔐 TELA 1: ADMINISTRATIVA (admin.py)                       │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  📧 Email: _____________________________             │  │
│  │  🔒 Senha: _____________________________             │  │
│  │                                                       │  │
│  │              [ ENTRAR ]                               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  Após login:                                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  📅 Escalas de Sexta-feira | 🎉 Feriados             │  │
│  │  ─────────────────────────────────────────────────   │  │
│  │                                                       │  │
│  │  ➕ Adicionar Nova Escala                            │  │
│  │                                                       │  │
│  │  📋 Lista de Escalas:                                │  │
│  │  👤 João Silva    📅 31/01/2026    ✏️  🗑️          │  │
│  │  👤 Maria Santos  📅 07/02/2026    ✏️  🗑️          │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  👁️ TELA 2: PÚBLICA (public.py)                            │
│                                                              │
│  📊 Sistema de Escala Conteúdo BOL                          │
│                                                              │
│  📅 Escalas de Sexta-feira                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Nome              │ Data da Sexta-feira              │  │
│  │ João Silva        │ 31/01/2026                       │  │
│  │ Maria Santos      │ 07/02/2026                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  🎉 Feriados                                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Colaborador │ Feriado  │ Data       │ Time          │  │
│  │ Pedro       │ Carnaval │ 16/02/2026 │ SEO           │  │
│  │ Ana         │ Páscoa   │ 03/04/2026 │ FrontEnd      │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔐 Fluxo de Login (Tela Administrativa)

```
┌─────────────┐
│   INÍCIO    │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│  Acessar admin.py       │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│  Tela de Login          │
│  ┌───────────────────┐  │
│  │ Email: _______    │  │
│  │ Senha: _______    │  │
│  │   [ ENTRAR ]      │  │
│  └───────────────────┘  │
└──────┬──────────────────┘
       │
       ▼
    ┌──────┐
    │Email │
    │válido?│
    └┬────┬┘
     │    │
   NÃO  SIM
     │    │
     │    ▼
     │  ┌──────┐
     │  │Senha │
     │  │correta?│
     │  └┬────┬┘
     │   │    │
     │  NÃO  SIM
     │   │    │
     ▼   ▼    ▼
   ┌─────────────────┐
   │ ❌ Erro de      │
   │    Login        │
   └─────────────────┘
              │
              ▼
        ┌──────────────────┐
        │ ✅ Login OK      │
        │                  │
        │ Painel Admin     │
        └──────────────────┘
```

---

## ➕ Adicionar Escala de Sexta-feira

```
1️⃣ Fazer Login
   ↓
2️⃣ Clicar na aba "📅 Escalas de Sexta-feira"
   ↓
3️⃣ Clicar em "➕ Adicionar Nova Escala"
   ↓
4️⃣ Preencher o formulário:
   ┌─────────────────────────────────┐
   │ Nome do Colaborador:            │
   │ [________________]              │
   │                                 │
   │ Data da Sexta-feira:            │
   │ [📅 31/01/2026]                 │
   │                                 │
   │     [ Adicionar Escala ]        │
   └─────────────────────────────────┘
   ↓
5️⃣ Clicar em "Adicionar Escala"
   ↓
6️⃣ ✅ Escala adicionada com sucesso!
```

---

## ✏️ Editar Escala Existente

```
1️⃣ Localizar a escala na lista
   ┌─────────────────────────────────────────┐
   │ 👤 João Silva  📅 31/01/2026  ✏️  🗑️  │
   └─────────────────────────────────────────┘
   ↓
2️⃣ Clicar no botão ✏️ (Editar)
   ↓
3️⃣ Formulário de edição aparece:
   ┌─────────────────────────────────┐
   │ Nome: [João Silva]              │
   │ Data: [📅 31/01/2026]           │
   │                                 │
   │  [ 💾 Salvar ]  [ ❌ Cancelar ] │
   └─────────────────────────────────┘
   ↓
4️⃣ Modificar os dados
   ↓
5️⃣ Clicar em "💾 Salvar"
   ↓
6️⃣ ✅ Escala atualizada!
```

---

## 🗑️ Deletar Escala

```
1️⃣ Localizar a escala na lista
   ┌─────────────────────────────────────────┐
   │ 👤 João Silva  📅 31/01/2026  ✏️  🗑️  │
   └─────────────────────────────────────────┘
   ↓
2️⃣ Clicar no botão 🗑️ (Deletar)
   ↓
3️⃣ ✅ Escala deletada imediatamente!
   (Sem confirmação - cuidado!)
```

---

## 🎉 Adicionar Feriado

```
1️⃣ Fazer Login
   ↓
2️⃣ Clicar na aba "🎉 Feriados"
   ↓
3️⃣ Clicar em "➕ Adicionar Novo Feriado"
   ↓
4️⃣ Preencher o formulário:
   ┌─────────────────────────────────┐
   │ Nome do Colaborador:            │
   │ [________________]              │
   │                                 │
   │ Nome do Feriado:                │
   │ [________________]              │
   │                                 │
   │ Data do Feriado:                │
   │ [📅 16/02/2026]                 │
   │                                 │
   │ Time:                           │
   │ [▼ Cadastro ▼]                  │
   │    SEO                          │
   │    FrontEnd                     │
   │                                 │
   │     [ Adicionar Feriado ]       │
   └─────────────────────────────────┘
   ↓
5️⃣ Clicar em "Adicionar Feriado"
   ↓
6️⃣ ✅ Feriado adicionado com sucesso!
```

---

## 👁️ Visualizar Dados (Tela Pública)

```
1️⃣ Executar public.py
   ↓
2️⃣ Tela abre automaticamente no navegador
   ↓
3️⃣ Dados são exibidos em tabelas:
   
   📅 ESCALAS DE SEXTA-FEIRA
   ┌────────────────────────────────┐
   │ Nome          │ Data           │
   ├───────────────┼────────────────┤
   │ João Silva    │ 31/01/2026     │
   │ Maria Santos  │ 07/02/2026     │
   └────────────────────────────────┘
   
   🎉 FERIADOS
   ┌─────────────────────────────────────────────────┐
   │ Colaborador │ Feriado  │ Data       │ Time     │
   ├─────────────┼──────────┼────────────┼──────────┤
   │ Pedro       │ Carnaval │ 16/02/2026 │ SEO      │
   │ Ana         │ Páscoa   │ 03/04/2026 │ FrontEnd │
   └─────────────────────────────────────────────────┘
```

---

## 🔄 Fluxo Completo de Uso

```
┌──────────────────────────────────────────────────────┐
│                                                       │
│  ADMINISTRADOR                    USUÁRIO PÚBLICO    │
│                                                       │
│  1. Acessa admin.py              1. Acessa public.py │
│     ↓                                ↓               │
│  2. Faz login                     2. Vê os dados     │
│     ↓                                                 │
│  3. Adiciona/Edita/Deleta                            │
│     ↓                                                 │
│  4. Dados salvos no Supabase                         │
│     ↓                                ↓               │
│  5. ← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─                │
│     Dados aparecem automaticamente                   │
│     na tela pública                                  │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

## 🎨 Elementos da Interface

### Ícones Utilizados

| Ícone | Significado |
|-------|-------------|
| 📅 | Escalas de Sexta-feira |
| 🎉 | Feriados |
| 👤 | Colaborador/Usuário |
| 🔐 | Login/Autenticação |
| ➕ | Adicionar novo item |
| ✏️ | Editar item |
| 🗑️ | Deletar item |
| 💾 | Salvar alterações |
| ❌ | Cancelar operação |
| ✅ | Sucesso |
| ⚠️ | Aviso |
| 🚪 | Sair/Logout |

### Cores do Sistema

- **Primária:** Laranja (#FF6B35) - BEMOL
- **Secundária:** Azul - Confiança
- **Fundo:** Branco/Cinza claro
- **Texto:** Cinza escuro

---

## 📱 Responsividade

O sistema se adapta a diferentes tamanhos de tela:

```
┌─────────────────────────────────────┐
│  💻 DESKTOP (> 1024px)              │
│  ┌───────────────────────────────┐  │
│  │  Layout completo              │  │
│  │  Tabelas largas               │  │
│  │  Múltiplas colunas            │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘

┌──────────────────────┐
│  📱 MOBILE           │
│  ┌────────────────┐  │
│  │  Layout        │  │
│  │  compacto      │  │
│  │  Tabelas       │  │
│  │  empilhadas    │  │
│  └────────────────┘  │
└──────────────────────┘
```

---

## ⌨️ Atalhos de Teclado (Streamlit)

- **Ctrl + R** - Recarregar aplicação
- **Ctrl + K** - Abrir menu de comandos
- **Esc** - Fechar modais

---

## 🎯 Dicas de Uso

### ✅ Boas Práticas

1. **Sempre faça logout** após usar a tela administrativa
2. **Verifique os dados** antes de deletar
3. **Use datas no formato correto** (DD/MM/AAAA)
4. **Mantenha nomes consistentes** para facilitar busca

### ⚠️ Cuidados

1. **Não há confirmação ao deletar** - cuidado ao clicar em 🗑️
2. **Não compartilhe a senha** com pessoas não autorizadas
3. **Não deixe a sessão aberta** em computadores compartilhados

---

## 🔄 Atualizações em Tempo Real

```
Administrador adiciona escala
         ↓
    Salva no Supabase
         ↓
    Tela pública atualiza
         ↓
    Usuários veem imediatamente
```

**Nota:** Pode ser necessário recarregar a página pública para ver atualizações.

---

## 🎉 Pronto para Usar!

Agora você conhece todas as funcionalidades do sistema!

**Próximos passos:**
1. ✅ Configure o sistema (veja CHECKLIST.md)
2. 🧪 Teste todas as funcionalidades
3. 📊 Comece a usar no dia a dia
4. 🚀 (Opcional) Faça deploy online

---

**Sistema de Escala Conteúdo BOL**  
*BEMOL S.A. - 2026*
