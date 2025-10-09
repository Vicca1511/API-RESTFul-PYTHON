from pydantic import BaseModel, ConfigDict
from typing import Optional


class CategoriaLivro(str, Enum):
    FICCAO = "ficcao"
    TECNICO = "tecnico"
    CIENTIFICO = "cientifico"
    BIOGRAFIA = "biografia"
    HISTORIA = "historia"


class LivroBase(BaseModel):
    titulo: str
    autor: str
    categoria: str
    ano_publicacao: int
    isbn: str
    disponivel: bool = True

class LivroCreate(LivroBase):
    pass

class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    categoria: Optional[str] = None
    ano_publicacao: Optional[int] = None
    isbn: Optional[str] = None
    disponivel: Optional[bool] = None

class Livro(LivroBase):
    id: int 
    model_config = ConfigDict(from_attributes=True)