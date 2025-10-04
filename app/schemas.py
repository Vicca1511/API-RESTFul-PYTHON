from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class CategoriaLivro(str, Enum):
    FICCAO = "ficcao"
    TECNICO = "tecnico"
    CIENTIFICO = "cientifico"
    BIOGRAFIA = "biografia"
    HISTORIA = "historia"

class LivroBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200, description="Título do livro")
    autor: str = Field(..., min_length=1, max_length=100, description="Autor do livro")
    categoria: CategoriaLivro = Field(..., description="Categoria do livro")
    ano_publicacao: int = Field(..., ge=1000, le=2024, description="Ano de publicação")
    isbn: Optional[str] = Field(None, max_length=20, description="ISBN do livro")
    disponivel: bool = Field(True, description="Disponibilidade do livro")  # Corrigido: disponivel

class LivroCreate(LivroBase):
    pass

class LivroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=200)
    autor: Optional[str] = Field(None, min_length=1, max_length=100)
    categoria: Optional[CategoriaLivro] = None
    ano_publicacao: Optional[int] = Field(None, ge=1000, le=2024)
    isbn: Optional[str] = Field(None, max_length=20)
    disponivel: Optional[bool] = None  # Corrigido: disponivel

class Livro(LivroBase):
    id: int = Field(..., description="ID único do livro")

    class Config:
        from_attributes = True