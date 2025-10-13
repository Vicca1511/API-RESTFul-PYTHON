from typing import List, Optional , Dict
from app.schemas import Livro , LivroCreate , LivroUpdate
from app.interfaces.repository import LivroRepository

class MemoryLivroRepository(LivroRepository):
    """
    Implementação em memória do repositório de livros.
    
    Esta classe implementa a interface LivroRepository usando
    um dicionário em memória para armazenamento.
    
    Características:
    - Estado por instância (cada instância tem seus próprios dados)
    - Ideal para desenvolvimento e testes
    - Fácil migração para banco real depois
    """
    def __init__(self):
        # Estado interno da instância (não global!)
        self._livros:Dict[ int , dict] = {}
        self._contador_id = 1

        # Popular com dados iniciais para demonstração
        self._popular_dados_iniciais()

    def _popular_dados_iniciais():
        dados_iniciais = [
            {
                "titulo": "Dom Casmurro",
                "autor": "Machado de Assis", 
                "categoria": "ficcao",
                "ano_publicacao": 1899,
                "isbn": "978-8535932042",
                "disponivel": True
            },
            {
                "titulo": "O Senhor dos Anéis",
                "autor": "J.R.R. Tolkien",
                "categoria": "ficcao", 
                "ano_publicacao": 1954,
                "isbn": "978-8533613379",
                "disponivel": True
            }
        ]

        # Adicionar cada livro com ID único
        for livro_data in dados_iniciais:
            self._livros[self._contador_id] = {
                "id": self._contador_id, 
                **livro_data
            }
            self._contador_id += 1


    def listar_todos(self) -> List[Livro]:
        """Implementação concreta: retorna todos os livros"""
        # Converter cada dicionário para objeto Livro
        return [Livro.model_validate(livro) for livro in self._livros.values()]
    
    def buscar_por_id(self, livro_id: int) -> Optional[Livro]:
        """Implementação concreta: busca livro por ID"""
        livro_data = self._livros.get(livro_id)

        if livro_data:
            return Livro.model_validate(livro_data)
        return None
    
    def criar(self, livro: LivroCreate) -> Livro:
        """Implementação concreta: cria novo livro"""
        livro_data = livro.model_dump()
        livro_data['id'] = self._contador_id
        
         # Armazenar no dicionário interno
        self._livros[self._contador_id] = livro_data        

        # Criar objeto Livro para retorno (Pydantic v2)
        livro_criado = Livro.model_validate(livro_data)

        # Incrementar contador para próximo ID
        self._contador_id += 1

        return livro_criado
    
    def atualizar(self,livro_id : int , livro: LivroUpdate) -> Optional[Livro]:
        """Implementação concreta: atualiza livro existente"""
        # Verificar se livro existe
        if livro_id not in self._livros:
            return None
        
        livro_existente = self._livros[livro_id]
        
        # Obter apenas campos que foram fornecidos no update (Pydantic v2)
        update_data = livro.model_dump(exclude_unset=True)

        # Aplicar atualizações
        for campo, valor in update_data.items():
            livro_existente[campo] = valor

       # Retornar livro atualizado (Pydantic v2)
        return Livro.model_validate(livro_existente)

    def deletar(self, livro_id: int) -> bool:
        """Implementação concreta: remove livro"""
        if livro_id in self._livros:
            del self._livros[livro_id]
            return True
        return False     
