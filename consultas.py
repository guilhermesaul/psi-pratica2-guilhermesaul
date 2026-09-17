from sqlalchemy import select
from models import Autor, Livro

def listar_livros(session):
    stmt = select(Livro)
    livros = session.scalars(stmt).all()
    for livro in livros:
        print(f"Livro: {livro.titulo} | Autor: {livro.autor.nome}")

def livros_por_autor(session, nome_autor):
    stmt = select(Livro).join(Livro.autor).where(Autor.nome == nome_autor)
    livros = session.scalars(stmt).all()
    for livro in livros:
        print(f"- {livro.titulo} ({livro.ano})")

def buscar_livros(session, trecho):
    stmt = select(Livro).where(Livro.titulo.ilike(f"%{trecho}%"))
    livros = session.scalars(stmt).all()
    for livro in livros:
        print(f"Encontrado: {livro.titulo} (Autor: {livro.autor.nome})")

def listar_autores_com_quantidade(session):
    stmt = select(Autor)
    autores = session.scalars(stmt).all()
    for autor in autores:
        print(f"Autor: {autor.nome} | Quantidade de livros: {len(autor.livros)}")

def detalhes_livro(session, titulo):
    stmt = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalars(stmt).first()
    
    if livro:
        print(f"Título: {livro.titulo}")
        print(f"Ano: {livro.ano}")
        print(f"Autor: {livro.autor.nome}")
        print(f"País do Autor: {livro.autor.pais}")
    else:
        print("Livro não encontrado.")