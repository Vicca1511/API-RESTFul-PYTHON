from sqlalchemy.orm import Session
from app.models import LivroDB
import logging


# Dados iniciais para teste
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
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "categoria": "Ficção Científica",
        "ano_publicacao": 1949,
        "isbn": "978-0451524935",
        "disponivel": False
    }

]

# Popular banco com dados iniciais

def popular_banco_inicial(db: Session):
    """Popula o banco com dados iniciais se estiver vazio"""
    quantidade_livros = db.query(LivroDB).count()

    if quantidade_livros == 0 :
        print("🎯 Populando banco com dados iniciais...")

        for livro_data in dados_iniciais:
            livro = LivroDB(**livro_data)
            db.add(livro)

        db.commit()
        print(f"✅ {len(dados_iniciais)} livros adicionados ao banco!")
    else:
        print(f"📚 Banco já contém {quantidade_livros} livros. Pulando população inicial.")          
