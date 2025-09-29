from fastapi import FastAPI, HTTPException 
from app.database import livros_db, get_proximo_id, get_livros_count, get_livros_disponiveis
from typing import List, Dict, Any


app = FastAPI(
title="Sistema Biblioteca API",
description = "Api de gerenciamento de biblioteca",
version="1.0.0"
)

@app.get("/")
async def root():
    return {"message":"Bem-vindo ao Sistema Bibliote API"}

@app.get("/health")
async def health_check():
    return {"status":"Api rodando normalmente!"}

@app.get("/info")
async def info():
    """informações sobre estado da biblioteca"""
    return  {
        "total_livros":get_livros_count(),
        "livros_disponiveis": len(get_livros_disponiveis()),
        "status":"operacional"
                 
    }                    
            
@app.get("/livros", response_model =List[Dict[str, Any]])
async def listar_livros():
    """Lista de Livros cadastrados"""
    return list(livros_db.values())

@app.get("/livros/{livros_id}")
async def buscar_livro(livro_id:int):
    """Busca livro especifico pelo ID"""
    livro = livros_db.get(livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail = "Livro não encontrado")    
    
    return livro 

@app.get("/livros/disponiveis")
async def listar_livros_disponiveis():
    """Retorna Livros que tem disponibilidade"""
    return get_livros_disponiveis()