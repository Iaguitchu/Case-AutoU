import os
from flask import Flask
from models import db, EmailTable
from config import Config
from blueprints.page import page

app = Flask(__name__, static_url_path='', static_folder='static')
app.config.from_object(Config)
app.register_blueprint(page)
db.init_app(app)



with app.app_context():
    # garante que a pasta existe
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    db.create_all()
    if not EmailTable.query.first():
        email_teste = EmailTable(
            email="teste@autou.com",
            assunto="Primeiro email",
            mensagem="Este é um email de teste salvo direto no banco.",
            classificacao="Produtivo",
            resposta_sugerida="Obrigado pelo seu email. Entraremos em contato em breve.",
            excluidos = " "
        )
        db.session.add(email_teste)
        db.session.commit()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)