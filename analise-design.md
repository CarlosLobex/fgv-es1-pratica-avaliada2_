# Análise de Design - GerenciadorEmprestimo

## Princípios SOLID Violados

### 1. SRP (Single Responsibility Principle)
A classe GerenciadorEmprestimo possui múltiplas responsabilidades:
- Acesso ao banco de dados
- Regras de negócio de empréstimo
- Envio de email
- Geração de PDF

Isso viola o princípio de responsabilidade única.

---

### 2. OCP (Open/Closed Principle)
A classe não está aberta para extensão e fechada para modificação.

Exemplo:
- Para mudar envio de email ou PDF, é necessário alterar a classe diretamente.

---

### 3. DIP (Dependency Inversion Principle)
A classe depende diretamente de implementações concretas:
- sqlite3
- smtplib
- reportlab

Não utiliza abstrações/interfaces.

---

## Problemas de Coesão e Acoplamento

### Baixa Coesão
A classe mistura várias responsabilidades diferentes (persistência, negócio, notificação e relatório).

### Alto Acoplamento
A classe está fortemente acoplada a:
- Banco de dados SQLite
- Serviço de email SMTP
- Biblioteca de geração de PDF

Isso dificulta manutenção e testes.

---

## Sugestões de Refatoração

- Separar responsabilidades em classes específicas:
  - Repositórios para acesso ao banco
  - Serviço de notificação para envio de email
  - Serviço de relatório para geração de PDF
  - Classe para cálculo de multa

- Aplicar injeção de dependência (DIP)

- Criar interfaces para repositórios

- Reduzir acoplamento e aumentar coesão

- Centralizar regras de negócio na classe principal, delegando tarefas
