from sqlalchemy import create_engine , Column , Integer , String , Boolean , Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABE_URL = "sqlite:///./biblioteca.db"

engine = create_engine (
    SQLALCHEMY_DATABE_URL,
    connect_args= {"check_same_thread": False}  # O que faz ? Qual a necessidade e razão ?
) 

SessionLocal = sessionmaker( autocommit = False, autoflush = False , bind=engine)

Base = declarative_base()

class LivroDB(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index= True)
    titulo = Column(String(200),nullable=False)
    autor = Column(String(100), nullable= False)
    categoria = Column(String(50) , nullable = False)
    ano_publicacao = Column(Integer, nullable = False)
    isbn = Column(String(50) , unique=True , nullable= False)
    disponivel = Column(Boolean, default= True)


def criar_tabelas():
    Base.metadata.create_all(bind= engine) # perguntar mais sobre 
    print("Tabelas criadas/Validadas!")
   
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    


