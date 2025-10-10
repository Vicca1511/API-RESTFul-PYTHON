print("=== TESTANDO IMPORTS ===")

try:
    from app.models import criar_tabelas, SessionLocal
    from app.database import popular_banco_inicial
    print("✅ Imports funcionam!")
    
    print("Criando tabelas...")
    criar_tabelas()
    
    print("Populando banco...")
    db = SessionLocal()
    popular_banco_inicial(db)
    db.close()
    
    print("✅ Banco criado com sucesso!")
    
except Exception as e:
    print(f"❌ Erro: {e}")