from typing import Dict

# Banco de dados em memória para livros
livros_db: Dict[int, dict] = {}
contador_id = 1

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
    }
]

# Popular banco com dados iniciais
for livro_data in dados_iniciais:
    livros_db[contador_id] = {"id": contador_id, **livro_data}
    contador_id += 1

def get_proximo_id() -> int:
    global contador_id
    id_atual = contador_id
    contador_id += 1
    return id_atual

def get_livros_count() -> int:
    """Retorna o número total de livros"""
    return len(livros_db)

def get_livros_disponiveis() -> list:
    """Retorna lista de livros disponíveis"""
    return [livro for livro in livros_db.values() if livro.get('disponivel', True)]
