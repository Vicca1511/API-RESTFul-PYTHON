from typing import List , Optional
from sqlalchemy.orm import Session
from app.schemas import Livro, LivroCreate , LivroUpdate
from app.interfaces.repository import LivroRepository
from app.models import LivroDB


class ''