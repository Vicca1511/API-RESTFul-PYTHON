import sqlite3
import os

def visualizar_banco():
    if not os.path.exists('biblioteca.db'):
        print('Banco de Dados não encontrado')
        return
    
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    print("🔍 VISUALIZADOR DO BANCO SQLite")
    print("=" * 50)
    
    
    # Ver tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tabelas: ")
    for table in tables:
        print(f"  ✅ {table[0]}")

    # Ver estrutura da tabela livros  

    print(f"\n🏗️  ESTRUTURA da tabela 'livros':")
    cursor.execute("PRAGMA table_info(livros);")  
    columns = cursor.fetchall()
    for col in columns:
        print(f"  📍 {col[1]} ({col[2]})")

    # Ver dados        
    print(f"\n📚 DADOS em 'livros':")
    cursor.execute("SELECT * FROM livros;")
    livros = cursor.fetchall()

    if livros:
        for livro in livros:
            id, titulo, autor, categoria, ano, isbn, disponivel = livro
            status = "✅ Disponível" if disponivel else "❌ Indisponível"
            print(f"  ID {id}: '{titulo}'")
            print(f"      👤 {autor} | 📁 {categoria} | 🗓️  {ano}")
            print(f"      📖 {isbn} | {status}")
            print()
    else:
        print("  📭 Nenhum livro cadastrado")
    
    conn.close()

if __name__ == "__main__":
    visualizar_banco()