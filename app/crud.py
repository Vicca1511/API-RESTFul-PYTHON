from typing import List, Optional
from app.schemas import Livro, LivroCreate, LivroUpdate
from app.interfaces.repository import LivroRepository

class CRUDLivros:
    """
    Camada de lógica de negócio para operações com livros.
    
    Esta classe NÃO sabe como os dados são armazenados - ela apenas
    orquestra as operações delegando para o repositório injetado.
    
    Agora funciona com QUALQUER repositório que implemente LivroRepository:
    - SQLivroRepository (banco real)
    - MemoryLivroRepository (memória - para testes)
    - Qualquer outra implementação futura
    """
    def __init__(self, repository: LivroRepository):
        """
        Inicializa o CRUD com um repositório injetado.
        
        Args:
            repository (LivroRepository): Implementação do repositório
        """
        self.repository = repository

    def listar_livros(self) -> List[Livro]:
        """
        Lista todos os livros cadastrados.
        
        Returns:
            List[Livro]: Lista de todos os livros
        """
        return self.repository.listar_todos()    
    
    def buscar_livro(self , livro_id: int) -> Optional[Livro]:
        """
        Busca um livro específico pelo ID.
        
        Args:
            livro_id (int): ID do livro a ser buscado
            
        Returns:
            Optional[Livro]: O livro encontrado ou None se não existir
        """
        return self.repository.buscar_por_id(livro_id)
    
    def criar_livro(self , livro: LivroCreate) -> Livro:
        """
        Cria um novo livro no sistema.
        
        Args:
            livro (LivroCreate): Dados do livro a ser criado
            
        Returns:
            Livro: O livro criado com ID atribuído
        """
        return self.repository.criar(livro)
    
    def atualizar_livro(self, livro_id: int, livro_update: LivroUpdate) -> Optional[Livro]:
        """
        Atualiza um livro existente.
        
        Args:
            livro_id (int): ID do livro a ser atualizado
            livro_update (LivroUpdate): Dados parciais para atualização
            
        Returns:
            Optional[Livro]: O livro atualizado ou None se não encontrado
        """
        return self.repository.atualizar(livro_id, livro_update)
    
    def deletar_livro(self, livro_id: int) -> bool:
        """
        Remove um livro do sistema.
        
        Args:
            livro_id (int): ID do livro a ser removido
            
        Returns:
            bool: True se foi removido, False se não encontrado
        """
        return self.repository.deletar(livro_id)