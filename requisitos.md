# Engenharia de Requisitos – Sistema BiblioTech

Este documento apresenta o levantamento e a documentação dos requisitos do sistema **BiblioTech**, um sistema de gestão para bibliotecas comunitárias, conforme descrição fornecida pelo cliente.

---

## Requisitos Funcionais

| ID    | Descrição                                                                 | Prioridade |
|------|----------------------------------------------------------------------------|------------|
| RF01 | O sistema deve permitir que o bibliotecário cadastre livros no acervo.     | Alta       |
| RF02 | O sistema deve permitir informar título, autor, ISBN, categoria e quantidade de exemplares do livro. | Alta |
| RF03 | O sistema deve permitir o cadastro de leitores com nome, CPF, e-mail e telefone. | Alta |
| RF04 | O sistema deve permitir registrar empréstimos de livros para leitores cadastrados. | Alta |
| RF05 | O sistema deve registrar a data do empréstimo automaticamente.             | Média      |
| RF06 | O sistema deve calcular automaticamente a data prevista de devolução (14 dias após o empréstimo). | Média |
| RF07 | O sistema deve permitir a devolução de livros emprestados.                 | Alta       |
| RF08 | O sistema deve permitir a renovação de empréstimos, desde que não existam reservas para o livro. | Média |
| RF09 | O sistema deve permitir que leitores façam reservas quando não houver exemplares disponíveis. | Média |
| RF10 | O sistema deve notificar o leitor por e-mail quando um livro reservado estiver disponível. | Baixa |

---

## Requisitos Não-Funcionais

| ID    | Categoria     | Descrição                                                                 | Métrica |
|------|---------------|----------------------------------------------------------------------------|--------|
| RNF01 | Desempenho    | O sistema deve registrar um empréstimo em até 2 segundos.                  | ≤ 2s   |
| RNF02 | Segurança     | O sistema deve proteger os dados pessoais dos leitores.                   | CPF e e-mail armazenados com acesso restrito |
| RNF03 | Disponibilidade | O sistema deve estar disponível durante o horário de funcionamento da biblioteca. | ≥ 99% do horário |
| RNF04 | Usabilidade   | O sistema deve possuir interface simples e intuitiva para bibliotecários. | Treinamento ≤ 1h |
| RNF05 | Confiabilidade| O sistema não deve permitir perda de dados em caso de falhas inesperadas. | Backup diário |

---

## Regras de Negócio

| ID   | Descrição |
|------|-----------|
| RN01 | O prazo padrão de empréstimo de livros é de 14 dias. |
| RN02 | O valor da multa por atraso é de R$ 2,00 por dia. |
| RN03 | Um empréstimo só pode ser renovado se não houver reservas para o livro. |
| RN04 | Um leitor só pode reservar um livro se não houver exemplares disponíveis. |
| RN05 | A notificação de reserva é enviada ao primeiro leitor da fila de reservas. |

---

## User Stories

### US01
Como **bibliotecário**  
Quero **cadastrar livros no acervo**  
Para **organizar e controlar os livros disponíveis na biblioteca**

**Critérios de Aceitação:**
- [ ] O sistema permite informar todos os dados obrigatórios do livro
- [ ] O sistema impede cadastro sem ISBN

**Story Points:** 3

---

### US02
Como **bibliotecário**  
Quero **cadastrar leitores**  
Para **permitir o controle de empréstimos e reservas**

**Critérios de Aceitação:**
- [ ] O CPF do leitor deve ser único
- [ ] O e-mail deve ser válido

**Story Points:** 2

---

### US03
Como **bibliotecário**  
Quero **registrar empréstimos de livros**  
Para **controlar a retirada de exemplares**

**Critérios de Aceitação:**
- [ ] O sistema verifica se há exemplares disponíveis
- [ ] A data de devolução é calculada automaticamente

**Story Points:** 3

---

### US04
Como **leitor**  
Quero **reservar um livro indisponível**  
Para **garantir meu atendimento quando ele for devolvido**

**Critérios de Aceitação:**
- [ ] A reserva só é permitida se não houver exemplares
- [ ] A reserva entra em uma fila ordenada

**Story Points:** 2

---

### US05
Como **bibliotecário**  
Quero **registrar a devolução de livros**  
Para **liberar exemplares para outros leitores**

**Critérios de Aceitação:**
- [ ] O sistema calcula multa automaticamente em caso de atraso
- [ ] O sistema verifica reservas pendentes

**Story Points:** 3

---

### US06
Como **leitor**  
Quero **receber notificações sobre livros reservados**  
Para **saber quando posso retirar o livro**

**Critérios de Aceitação:**
- [ ] O sistema envia e-mail na devolução do livro
- [ ] Apenas o primeiro da fila é notificado

**Story Points:** 2
