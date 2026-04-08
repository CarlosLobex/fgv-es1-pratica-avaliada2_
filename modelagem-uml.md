# Modelagem UML – Sistema BiblioTech

Este documento apresenta a modelagem UML do sistema **BiblioTech**, com o objetivo de representar a estrutura e o comportamento do sistema, facilitando a comunicação entre os envolvidos no desenvolvimento.

---

## Diagrama de Classes

```mermaid
classDiagram
    class Livro {
        isbn: String
        titulo: String
        autor: String
        categoria: String
        +verificarDisponibilidade()
        +atualizarQuantidade()
    }

    class Exemplar {
        id: int
        status: String
        +marcarEmprestado()
        +marcarDisponivel()
    }

    class Leitor {
        cpf: String
        nome: String
        email: String
        telefone: String
        +reservarLivro()
        +consultarEmprestimos()
    }

    class Bibliotecario {
        id: int
        nome: String
        +cadastrarLivro()
        +registrarEmprestimo()
    }

    class Emprestimo {
        id: int
        dataEmprestimo: Date
        dataDevolucaoPrevista: Date
        dataDevolucao: Date
        +registrar()
        +finalizar()
    }

    class Reserva {
        id: int
        dataReserva: Date
        +registrar()
        +notificarLeitor()
    }

    class Multa {
        id: int
        valor: float
        paga: boolean
        +calcular()
        +registrarPagamento()
    }

    Livro "1" --> "many" Exemplar
    Leitor "1" --> "many" Emprestimo
    Livro "1" --> "many" Emprestimo
    Livro "1" --> "many" Reserva
    Leitor "1" --> "many" Reserva



    Emprestimo "1" --> "0..1" Multa
    Bibliotecario --> Emprestimo

## Diagrama de Sequência – Realizar Empréstimo de Livro

```mermaid
sequenceDiagram
    actor Bibliotecario
    participant Sistema
    participant Livro
    participant Leitor
    participant Emprestimo

    Bibliotecario ->> Sistema: solicitarEmpréstimo(livroISBN, leitorCPF)
    Sistema ->> Livro: verificarDisponibilidade()
    Livro -->> Sistema: disponível / indisponível

    Sistema ->> Leitor: verificarCadastro()
    Leitor -->> Sistema: leitor válido

    alt Livro disponível
        Sistema ->> Emprestimo: registrarEmpréstimo()
        Emprestimo -->> Sistema: empréstimo confirmado
        Sistema -->> Bibliotecario: empréstimo realizado com sucesso
    else Livro indisponível
        Sistema ->> Sistema: registrarReserva()
        Sistema -->> Bibliotecario: reserva criada
    end
``
