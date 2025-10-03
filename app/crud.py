from typing import List, Optional
from app.schemas import  Livro, LivroCreate, LivroUpdate
from app.database import livros_db, get_proximo_id

class CRUDLivros:
    @staticmethod
    def listar_livros():
        """Lista todos os livros"""
        return [Livro(**livro) for livro in livros_db.values()]
    
    @staticmethod
    def buscar_livro(livro_id: int)-> Optional[Livro]:

        """Busca livros por ID"""
        livro_data = livros_db.get(livro_id)
        if livro_data:
            return Livro(**livro_data)

        return None

    @staticmethod 
    def criar_livro(livro:LivroCreate) -> Livro:
        """Adiciona novos livros"""
        novo_id = get_proximo_id
        novo_livro = Livro(id=novo_id, **livro.model_dump())
        livros_db[novo_id] = novo_livro.model_dump()
        return novo_livro
    
    staticmethod
    def atualizar_livro(livro_id: int, livro_update: LivroUpdate) -> Optional[Livro]:
        """Atualiza um Livro existente!"""
        livro_existente = livros_db[livro_id]
        
        update_data = livro_update.model_dump(exclude_unset=True)
        for campo, valor in update_data.items:
            livro_existente[campo] = valor
        return Livro (**livro_existente)
    
    @staticmethod
    def deletar_livro(livro_id:int) -> bool:
        """Remove Livros"""
        if livro_id in livros_db:
            del livros_db[livro_id]
            return True
        
        return False
    

crud_livros = CRUDLivros()






        

