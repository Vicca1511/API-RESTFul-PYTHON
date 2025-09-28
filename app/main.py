from fastapi import FastAPI

app= FastAPI(
    title="Sistema Biblioteca API",
    description="API para gerenciamento de uma biblioteca ",
    version="1.0.0"
)

@app.get("/home")
async def root():
    return {"message":"Bem-vindo a API da Biblioteca"}

@app.get("/health")
async def health_check():
    return{"status":"API rodando normalmente!"}