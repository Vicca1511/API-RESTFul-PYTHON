from typing import Dict

livros_db: Dict( int, dict) = {}
contador_id = 1

#Dados para teste 

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
        "titulo": "Clean Code",
        "autor": "Robert C. Martin",
        "categoria": "tecnico",
        "ano_publicacao": 2008,
        "isbn": "978-0132350884",
        "disponivel": True
    }
]

# popular banco

for livro_data in dados_iniciais:
    livros_db[contador_id] = {"id":contador_id , **livro_data}
    contador_id += 1

def get_proximo_id() -> int:
    global contador_id
    id_atual = contador_id 
    contador_id += 1 
    return id_atual

def get_num_livros() -> int:
    return len(livros_db)

def livros_disponiveis() -> list:
    return [ livro for livro in livros_db.values() if livro.get('disponivel', True)]
