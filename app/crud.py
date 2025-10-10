from typing import List, Optional
from sqlalchemy.orm import Session
from app.schemas import Livro, LivroCreate, LivroUpdate
from app.models import LivroDB

class CRUDLivros:
    @staticmethod
    def listar_livros(db:Session) -> List[Livro]:
        """Lista todos os livros do Banco"""
         # db.query(LivroDB) = SELECT * FROM livros
        livros_db = db.query(LivroDB).all()
        return [Livro.model_validate(livro) for livro in livros_db]
    
    @staticmethod
    def buscar_livro(db: Session, livro_id: int) -> Optional[Livro]:
        """Busca livros por ID"""
        livro_db = db.query(LivroDB).filter(LivroDB.id == livro_id).first()
        
        return Livro.model_validate(livro_db) if livro_db else None

    @staticmethod 
    def criar_livro(db: Session, livro:LivroCreate) -> Livro:
        """Adiciona novos livros"""
        livro_db = LivroDB(**livro.model_dump())

        db.add(livro_db)
        db.commit()
        db.refresh(livro_db)

        return Livro.model_validate(livro_db)
    
    @staticmethod
    def atualizar_livro(db: Session , livro_id: int, livro_update: LivroUpdate) -> Optional[Livro]:
        """Atualiza um Livro existente!"""
        livro_db = db.query(LivroDB).filter(LivroDB.id == livro_id).first()
        if not livro_db:
            return None
        
        update_data = livro_update.model_dump(exclude_unset=True)
        for campo, valor in update_data.items():
            setattr(livro_db, campo, valor)

        db.commit()
        db.refresh(livro_db)    
        return Livro.model_validate(livro_db)
    
    @staticmethod
    def deletar_livro(db: Session , livro_id: int) -> bool:
        """Remove Livros"""
        livro_db = db.query(LivroDB).filter(LivroDB.id == livro_id).first()
        if not livro_db:
            return False
        
        db.delete(livro_db)
        db.commit()
        return True

crud_livros = CRUDLivros()