import os

class Config:
    # Banco de dados
    SQLALCHEMY_DATABASE_URI = "sqlite:///meu_banco.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False #evita overhead de sinalização de mudanças no ORM

    # uploads
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB
    ALLOWED_EXT = {"pdf", "txt"}

    # Chave API OpenAI
    OPENAI_API_KEY = os.environ.get("OPENAI_KEY")