from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmailTable(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    assunto = db.Column(db.String(255), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    classificacao = db.Column(db.String(50), nullable=False)
    resposta_sugerida = db.Column(db.Text, nullable=True) 
    anexo_pdf = db.Column(db.String(512), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
