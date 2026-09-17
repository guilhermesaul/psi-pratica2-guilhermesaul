from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Autor(Base):
    __tablename__ = "autores"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    pais: Mapped[str] = mapped_column(String(100))

    livros: Mapped[List["Livro"]] = relationship(back_populates="autor")


class Livro(Base):
    __tablename__ = "livros"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))
    ano: Mapped[int]
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    
    autor: Mapped["Autor"] = relationship(back_populates="livros")