import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Interface
class IRepositorio(ABC):
    @abstractmethod
    def buscar(self, id):
        pass

    @abstractmethod
    def salvar(self, entidade):
        pass


# Repositórios
class RepositorioLivro(IRepositorio):
    def __init__(self, db_path):
        self.db_path = db_path

    def buscar(self, isbn):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros WHERE isbn = ?", (isbn,))
        livro = cursor.fetchone()
        conn.close()
        return livro

    def atualizar_disponibilidade(self, isbn):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE livros 
            SET exemplares_disponiveis = exemplares_disponiveis - 1
            WHERE isbn = ?
        """, (isbn,))
        conn.commit()
        conn.close()

    def salvar(self, entidade):
        pass


class RepositorioLeitor(IRepositorio):
    def __init__(self, db_path):
        self.db_path = db_path

    def buscar(self, cpf):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leitores WHERE cpf = ?", (cpf,))
        leitor = cursor.fetchone()
        conn.close()
        return leitor

    def salvar(self, entidade):
        pass


class RepositorioEmprestimo(IRepositorio):
    def __init__(self, db_path):
        self.db_path = db_path

    def salvar(self, dados):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO emprestimos (livro_isbn, leitor_cpf, data_emprestimo, data_devolucao_prevista)
            VALUES (?, ?, ?, ?)
        """, dados)

        conn.commit()
        emprestimo_id = cursor.lastrowid
        conn.close()
        return emprestimo_id

    def buscar(self, id):
        pass


# Serviços
class ServicoNotificacao:
    def enviar(self, mensagem):
        print("Notificação enviada:", mensagem)


class ServicoRelatorio:
    def gerar(self, dados):
        print("Relatório gerado:", dados)


class CalculadoraMulta:
    def calcular(self, data_prevista):
        hoje = datetime.now()
        if hoje > data_prevista:
            dias = (hoje - data_prevista).days
            return dias * 2.0
        return 0


# Classe principal
class GerenciadorEmprestimo:
    def __init__(
        self,
        repo_livro,
        repo_leitor,
        repo_emprestimo,
        servico_notificacao,
        servico_relatorio,
        calculadora_multa
    ):
        self.repo_livro = repo_livro
        self.repo_leitor = repo_leitor
        self.repo_emprestimo = repo_emprestimo
        self.servico_notificacao = servico_notificacao
        self.servico_relatorio = servico_relatorio
        self.calculadora_multa = calculadora_multa

    def realizar_emprestimo(self, livro_isbn, leitor_cpf):
        livro = self.repo_livro.buscar(livro_isbn)
        if not livro:
            return False, "Livro não encontrado"

        leitor = self.repo_leitor.buscar(leitor_cpf)
        if not leitor:
            return False, "Leitor não encontrado"

        exemplares = livro[4]

        if exemplares > 0:
            data_emprestimo = datetime.now().strftime('%Y-%m-%d')
            data_devolucao = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

            emprestimo_id = self.repo_emprestimo.salvar(
                (livro_isbn, leitor_cpf, data_emprestimo, data_devolucao)
            )

            self.repo_livro.atualizar_disponibilidade(livro_isbn)

            self.servico_notificacao.enviar("Empréstimo realizado")
            self.servico_relatorio.gerar(f"Comprovante {emprestimo_id}")

            return True, "Empréstimo realizado com sucesso"

        else:
            return False, "Livro indisponível"
