from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum

class CategoriaLivro(str, Enum):
    FICCAO = "ficcao"
    ROMANCE = "romance"           
    FANTASIA = "fantasia"         # ← Adicionei
    TECNICO = "tecnico"
    CIENTIFICO = "cientifico"
    BIOGRAFIA = "biografia"
    HISTORIA = "historia"

class LivroBase(BaseModel):
    titulo: str
    autor: str
    categoria: CategoriaLivro     # ← Usando a Enum!
    ano_publicacao: int
    isbn: str
    disponivel: bool = True

class LivroCreate(LivroBase):
    pass

class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    categoria: Optional[CategoriaLivro] = None  # ← Enum aqui também!
    ano_publicacao: Optional[int] = None
    isbn: Optional[str] = None
    disponivel: Optional[bool] = None

class Livro(LivroBase):
    id: int
    model_config = ConfigDict(from_attributes=True)