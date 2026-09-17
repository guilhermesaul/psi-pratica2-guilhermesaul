# Onde estão os modelos ORM no seu projeto?
Estão no arquivo models.py. As classes Autor e Livro herdam de Base (configurada em database.py), permitindo ao SQLAlchemy transformá-las em tabelas no SQLite.

# Qual classe representa o lado "um" e qual representa o lado "muitos" no relacionamento?
Autor é o lado "um" (um autor tem vários livros, indicado pela lista em livros). Livro é o lado "muitos" (vários livros pertencem a um único autor, indicado pelo atributo singular autor).

# Para que serve o ForeignKey em Livro.autor_id?
Garante a integridade dos dados. Ele obriga que o valor de autor_id na tabela de livros exista de fato na coluna id da tabela de autores.

# O que acontece se você esquecer o session.commit() após inserir os dados?
Os dados não são salvos no banco. O session.add_all() apenas deixa as informações na memória. Sem o commit(), ocorre um rollback automático ao fechar a sessão e a inserção é descartada.