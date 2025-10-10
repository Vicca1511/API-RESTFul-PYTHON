# correcao_categorias.py
import sqlite3

def corrigir_categorias():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    print('��� Corrigindo categorias no banco...')
    
    # Mapeamento de correções
    correcoes = [
        (1, 'ficcao'),           # Dom Casmurro
        (2, 'fantasia'),         # O Senhor dos Anéis  
        (3, 'ficcao')            # 1984 → Ficção Científica vira 'ficcao'
    ]
    
    for livro_id, nova_categoria in correcoes:
        cursor.execute(
            'UPDATE livros SET categoria = ? WHERE id = ?',
            (nova_categoria, livro_id)
        )
        print(f'✅ ID {livro_id}: categoria corrigida para \"{nova_categoria}\"')
    
    conn.commit()
    
    # Verificar
    print('\n��� Verificação final:')
    cursor.execute('SELECT id, titulo, categoria FROM livros ORDER BY id')
    for row in cursor.fetchall():
        print(f'   ID {row[0]}: {row[1]} → {row[2]}')
    
    conn.close()
    print('\n��� Categorias corrigidas com sucesso!')

if __name__ == '__main__':
    corrigir_categorias()
