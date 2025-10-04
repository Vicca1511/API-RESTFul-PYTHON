from fastapi import FastAPI , HTTPException , status
from app.schemas import Livro , LivroCreate , LivroUpdate
from app.crud import crud_livros
from typing import List

app = FastAPI(
    title= "Sistea Biclioteca API",
    description= " API para gerenciamento de biblioteca",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message":"Bem Vindo a API da Biblioteca!"}

@app.get("/health")
async def health_check():
    return {"message":"API rodando normalmente."}

@app.get("/info")
async def info():
        """Informações sobre o estado da biblioteca"""
        livros = crud_livros.listar_livros()
        disponiveis = [livro for livro in livros if livro.disponivel]
        return {
        "total_livros": len(livros),
        "livros_disponiveis": len(disponiveis),
        "status": "operacional"
    }


# --- ENDPOINTS CRUD PARA LIVROS ---

@app.get("/livros", response_model= List[Livro])
async def listar_livros():
     """Lista todos os livros cadastrados"""
     return crud_livros.listar_livros()

@app.get("/livros/{livro_id}", response_model= Livro)
async def buscar_livro(livro_id:int):
     """Busca um livro específico pelo ID"""
     livro = crud_livros.buscar_livro(livro_id)
     if not livro:
          raise HTTPException(
               status_code= status.HTTP_404_NOT_FOUND,
               detail= "Livro não encontrado"
          )
     return livro


     
    
