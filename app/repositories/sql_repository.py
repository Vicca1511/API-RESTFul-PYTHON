from typing import List , Optional
from sqlalchemy.orm import Session
from app.schemas import Livro, LivroCreate , LivroUpdate
from app.interfaces.repository import LivroRepository
from app.models import LivroDB


class SQLLivroRepository(LivroRepository):
    """
    Implementação SQL do repositório de livros usando SQLAlchemy.
    Esta classe implementa a interface LivroRepository para
    operações com banco de dados real.
    """
    def __init__(self, db: Session):
        """
        Inicializa o repositório com uma sessão do banco.
        
        Args:
            db (Session): Sessão do SQLAlchemy
        """
        self.db = db

    def listar_todos(self) -> List[Livro]:
        """Implementação SQL: retorna todos os livros"""
        livros_db = self.db.query(LivroDB).all()
        return [Livro.model_validate(livro) for livro in livros_db ]
    
    def buscar_por_id(self, livro_id: int ) -> Optional[Livro]:
        """Implementação SQL: busca livro por ID"""
        livro_db = self.db.query(LivroDB).filter(LivroDB.id == livro_id).first()
        return Livro.model_validate(livro_db) if livro_db else None
    
    def criar(self, livro: LivroCreate) -> Livro:
        livro_db = LivroDB(livro.model_dump())

        self.db.add(livro_db)
        self.db.commit()
        self.db.refresh(livro_db)
        
        return Livro.model_validate(livro_db)
    
    def atualizar(self, livro_id: int, livro_update:LivroUpdate ) -> Optional[Livro]:
        """Implementação SQL: atualiza livro existente"""
        livro_db = self.db.query(LivroDB).filter(LivroDB.id == livro_id).first()

        if not livro_db:
            return None
        
        update_data = livro_update.model_dump(exclude_unset=True)
        for campo, valor in update_data.items():
            setattr(livro_db, campo, valor)


        self.db.commit()
        self.db.refresh(livro_db)
        return Livro.model_validate(livro_db)
    
    def deletar(self, livro_id: int) -> bool:
        """Implementação SQL: remove livro"""
        livro_db = self.db.query(LivroDB).filter(LivroDB.id == livro_id).first()
        if not livro_db:
            return False
        
        self.db.delete(livro_db)
        self.db.commit()
        return True
        
            
        