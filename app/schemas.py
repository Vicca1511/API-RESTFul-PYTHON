from pydantic import BaseModel
from typing import Optional
from enum import Enum

class CategoriaLivro(str, Enum):
    FICCAO = "ficcao"
    TECNICO = "tecnico"
    CIENTIFICO = "cientifico"
    BIOGRAFIA = "biografia"
    HISTORIA = "historia"

class LivroBase(BaseModel):
    titulo:str
    autor:str
    categoria:CategoriaLivro
    ano_publicacao: int
    isbn:Optional[str] = None
    disponivel: bool = True

class LivroCreate(LivroBase):
    pass

class LivroUpdate(BaseModel):
    titulo:str = None
    autor:str = None
    categoria:CategoriaLivro = None
    ano_publicacao: int = None
    isbn:Optional[str] = None
    disponivel: bool = None

class Livro(LivroBase):
    id:int

    class Config:
        from_attributes = True    
