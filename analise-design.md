# Análise de Design – Classe GerenciadorEmprestimo

Este documento apresenta a análise de design da classe `GerenciadorEmprestimo`, fornecida na versão inicial do sistema BiblioTech. A análise considera princípios de Engenharia de Software, com foco em SOLID, coesão, acoplamento e possibilidades de refatoração.

---

## Violação dos Princípios SOLID

### SRP – Single Responsibility Principle
O princípio da responsabilidade única é claramente violado. A classe `GerenciadorEmprestimo` possui múltiplas responsabilidades, tais como:
- Acesso direto ao banco de dados
- Lógica de negócio de empréstimos e reservas
- Envio de e-mails de notificação
- Geração de arquivos PDF
- Cálculo e registro de multas

Essa concentração de responsabilidades faz com que a classe tenha várias razões para mudar, indo contra o SRP.

---

### OCP – Open/Closed Principle
A classe não está aberta para extensão e está fortemente fechada para modificação. Qualquer mudança no mecanismo de notificação (ex: outro tipo de mensagem), persistência ou geração de relatórios exige modificação direta do código da classe principal.

Não há uso de abstrações que permitam estender funcionalidades sem alterar o código existente.

---

### DIP – Dependency Inversion Principle
A classe depende diretamente de implementações concretas, como:
- Biblioteca SQLite (`sqlite3`)
- Serviço SMTP para envio de e-mails
- Biblioteca de geração de PDF

Essas dependências diretas dificultam testes, reutilização e manutenção, violando o princípio de inversão de dependência.

---

## Problemas de Coesão e Acoplamento

### Baixa Coesão
A classe apresenta baixa coesão, pois suas funções não estão relacionadas a uma única finalidade. Ela mistura regras de negócio, persistência de dados, comunicação externa e geração de documentos.

Classes com baixa coesão tendem a ser mais difíceis de entender, testar e evoluir.

---

### Alto Acoplamento
O alto acoplamento é evidenciado pelo uso direto de:
- SQL embutido nos métodos
- Criação direta de conexões com banco de dados
- Instanciação direta de serviços externos

Isso torna a classe fortemente dependente de detalhes de implementação, dificultando mudanças futuras.

---

## Sugestões de Refatoração

Para melhorar a qualidade do código e alinhar o sistema aos princípios de Engenharia de Software, recomenda-se:

- Separar responsabilidades em classes distintas, aplicando o SRP:
  - Repositórios para acesso a dados
  - Serviços para notificação, geração de relatórios e cálculo de multas
- Introduzir interfaces e abstrações para permitir extensibilidade (OCP)
- Aplicar injeção de dependências, reduzindo o acoplamento (DIP)
- Criar uma classe orquestradora responsável apenas por coordenar o fluxo do empréstimo

Com essas mudanças, o sistema se torna mais modular, legível, testável e manutenível.

---

## Conclusão

A análise evidencia que, apesar de funcional, a versão original da classe `GerenciadorEmprestimo` apresenta problemas significativos de design. A aplicação dos princípios SOLID e conceitos de baixo acoplamento e alta coesão é essencial para melhorar a qualidade do software, justificando a refatoração proposta na próxima etapa da prática.

