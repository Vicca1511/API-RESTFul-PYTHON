from fastapi import FastAPI, HTTPException, status , Depends
from sqlalchemy.orm import Session
from app.schemas import Livro, LivroCreate, LivroUpdate
from app.crud import crud_livros
from app.models import get_db
from typing import List

app = FastAPI(
    title="Sistema Biblioteca API",
    description="API para gerenciamento de biblioteca",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Bem Vindo a API da Biblioteca!"}

@app.get("/health")
async def health_check():
    return {"message": "API rodando normalmente."}

@app.get("/info")
async def info(db: Session = Depends(get_db)):
    """Informações sobre o estado da biblioteca"""
    livros = crud_livros.listar_livros(db)
    disponiveis = [livro for livro in livros if livro.disponivel]
    return {
        "total_livros": len(livros),
        "livros_disponiveis": len(disponiveis),
        "status": "operacional"
    }

# --- ENDPOINTS CRUD PARA LIVROS ---

@app.get("/livros/disponiveis", response_model=List[Livro])
async def listar_livros_disponiveis(db: Session = Depends(get_db)):
    """Lista apenas livros disponíveis"""
    livros = crud_livros.listar_livros(db)
    return [livro for livro in livros if livro.disponivel]    

@app.get("/livros", response_model=List[Livro])
async def listar_livros(db: Session = Depends(get_db)):
    """Lista todos os livros cadastrados"""
    return crud_livros.listar_livros(db)

@app.get("/livros/{livro_id}", response_model=Livro)
async def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    """Busca um livro específico pelo ID"""
    livro = crud_livros.buscar_livro(db, livro_id)
    if not livro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado."
        )
    return livro

@app.post("/livros", response_model=Livro, status_code=status.HTTP_201_CREATED)
async def criar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    """Cria um novo livro"""
    return crud_livros.criar_livro(db, livro)

@app.put("/livros/{livro_id}", response_model=Livro)
async def atualizar_livro(livro_id: int, livro_update: LivroUpdate, db: Session = Depends(get_db)):
    """Atualiza um livro existente"""
    livro_atualizado = crud_livros.atualizar_livro(db , livro_id, livro_update)  # ✅ Corrigido
    if not livro_atualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Livro não encontrado."
        )
    return livro_atualizado

@app.delete("/livros/{livro_id}")  # ✅ Corrigido
async def deletar_livro(livro_id: int, db: Session = Depends(get_db)):  # ✅ Corrigido
    """Remove um livro do sistema"""
    if not crud_livros.deletar_livro(db, livro_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado."
        )
    return {"message": "Livro excluído com sucesso!"}