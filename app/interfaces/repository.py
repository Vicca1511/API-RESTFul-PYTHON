from abc import ABC , abstractmethod
from typing import List , Optional
from app.schemas import Livro , LivroCreate , LivroUpdate

class LivroRepository(ABC):
    """Interface para operações de persistência de livros"""

    @abstractmethod
    def listar_todos(self) -> List[Livro]:
        """Retorna todos os livros"""
        pass

    @abstractmethod
    def buscar_por_id(self, livro_id: int ) -> Optional[Livro]:
        """Busca um livro pelo ID. Retorna None se não encontrado"""
        pass

    @abstractmethod
    def criar(self , livro: LivroCreate) -> Livro:
        """Cria um novo livro. Retorna o livro criado com ID"""
        pass

    @abstractmethod
    def atualizar(self , livro: LivroUpdate) -> Optional[Livro]:
        """Atualiza um livro existente. Retorna None se não encontrado"""
        pass

    @abstractmethod
    def deletar(self , livro_id: int) -> bool:
        """Remove um livro. Retorna True se removeu, False se não encontrado"""
        pass    