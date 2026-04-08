## Requisitos Funcionais

| ID | Descrição | Prioridade |
|----|-----------|------------|
| RF01 | O sistema deve permitir cadastrar livros com título, autor, ISBN, categoria e quantidade | Alta |
| RF02 | O sistema deve permitir atualizar dados dos livros | Média |
| RF03 | O sistema deve permitir cadastrar leitores com nome, CPF, email e telefone | Alta |
| RF04 | O sistema deve permitir consultar livros disponíveis | Alta |
| RF05 | O sistema deve permitir registrar empréstimos de livros | Alta |
| RF06 | O sistema deve calcular automaticamente a data de devolução | Alta |
| RF07 | O sistema deve permitir registrar reservas quando não houver exemplares | Alta |
| RF08 | O sistema deve notificar o leitor por email quando o livro estiver disponível | Média |
| RF09 | O sistema deve permitir renovação de empréstimos | Média |
| RF10 | O sistema deve calcular multa por atraso na devolução | Alta |

## Requisitos Não-Funcionais

| ID | Categoria | Descrição | Métrica |
|----|-----------|-----------|---------|
| RNF01 | Desempenho | O sistema deve responder consultas em até 2 segundos | Tempo de resposta |
| RNF02 | Segurança | Os dados dos usuários devem ser protegidos | Criptografia de dados |
| RNF03 | Usabilidade | Interface deve ser simples e intuitiva | Teste com usuários |
| RNF04 | Disponibilidade | O sistema deve estar disponível 99% do tempo | SLA |
| RNF05 | Confiabilidade | O sistema não deve perder dados | Backup diário |

## Regras de Negócio

| ID | Descrição |
|----|-----------|
| RN01 | O prazo de empréstimo é de 14 dias |
| RN02 | Multa de R$ 2,00 por dia de atraso |
| RN03 | Não é possível renovar empréstimos com reservas ativas |
| RN04 | Reserva só é permitida se não houver exemplares disponíveis |
| RN05 | O primeiro da fila de reserva tem prioridade |

## User Stories

### US01
Como bibliotecário  
Quero cadastrar livros  
Para manter o acervo atualizado  

Critérios de Aceitação:
- [ ] Deve permitir inserir título, autor, ISBN
- [ ] Deve salvar no sistema corretamente  

Story Points: 3  

---

### US02
Como leitor  
Quero me cadastrar  
Para poder pegar livros emprestados  

Critérios de Aceitação:
- [ ] Deve cadastrar CPF único
- [ ] Deve validar email  

Story Points: 2  

---

### US03
Como bibliotecário  
Quero registrar empréstimos  
Para controlar os livros  

Critérios de Aceitação:
- [ ] Deve verificar disponibilidade
- [ ] Deve registrar datas automaticamente  

Story Points: 5  

---

### US04
Como leitor  
Quero reservar livros  
Para garantir acesso quando disponível  

Critérios de Aceitação:
- [ ] Deve entrar em fila
- [ ] Deve receber notificação  

Story Points: 3  

---

### US05
Como sistema  
Quero calcular multas  
Para penalizar atrasos  

Critérios de Aceitação:
- [ ] Deve calcular R$2 por dia
- [ ] Deve registrar no sistema  

Story Points: 4  

---

### US06
Como bibliotecário  
Quero renovar empréstimos  
Para dar mais prazo ao leitor  

Critérios de Aceitação:
- [ ] Não permitir se houver reserva
- [ ] Atualizar nova data  

Story Points: 3  
