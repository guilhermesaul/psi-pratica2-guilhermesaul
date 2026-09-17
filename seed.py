from models import Autor, Livro

def popular_banco(session):
    if session.query(Autor).first():
        return

    autor1 = Autor(nome="George Orwell", pais="Reino Unido")
    autor2 = Autor(nome="Franz Kafka", pais="Império Austro-Húngaro")
    autor3 = Autor(nome="Fyodor Dostoevsky", pais="Rússia")
    autor4 = Autor(nome="Jorge Amado", pais="Brasil")
    livro1 = Livro(titulo="1984", ano=1949, autor=autor1)
    livro2 = Livro(titulo="A Revolução dos Bichos", ano=1945, autor=autor1)
    livro3 = Livro(titulo="A Metamorfose", ano=1915, autor=autor2)
    livro4 = Livro(titulo="O Processo", ano=1925, autor=autor2)
    livro5 = Livro(titulo="O Sonho de um Homem Ridículo", ano=1877, autor=autor3)
    livro6 = Livro(titulo="Crime e Castigo", ano=1866, autor=autor3)
    livro7 = Livro(titulo="Capitães da Areia", ano=1937, autor=autor4)

    session.add_all([
        autor1, autor2, autor3, autor4,
        livro1, livro2, livro3, livro4, livro5, livro6, livro7
    ])
    session.commit()