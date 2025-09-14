# blueprints/page.py
import os, uuid
from flask import Blueprint, render_template, request, jsonify, current_app, send_from_directory
from werkzeug.utils import secure_filename
from models import db, EmailTable
from services.leitor_pdf import extracao_texto_pdf

page = Blueprint('page', __name__)

def _ext_ok(nome_arquivo: str) -> bool:
    allowed = current_app.config.get("ALLOWED_EXT")
    return "." in nome_arquivo and nome_arquivo.rsplit(".", 1)[1].lower() in allowed # Divide a string da direita para a esquerda, no máximo 1 vez

@page.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":

        # Processando o formulário via POST
        email    = request.form.get("email")
        assunto  = request.form.get("assunto")
        mensagem = request.form.get("mensagem")

        arquivo = request.files.get("anexo")
        nome_arquivo = None

        if arquivo and arquivo.filename:
            if not _ext_ok(arquivo.filename):
                return jsonify(message="Extensão não permitida (use .pdf ou .txt)."), 400

            ext = arquivo.filename.rsplit(".", 1)[1].lower() # Pega a extensão do arquivo
            identificador = f"{uuid.uuid4().hex}.{ext}" # Gera um nome único para o arquivo e adiciona a extensão
            dest = os.path.join(current_app.config["UPLOAD_FOLDER"], identificador) # define o caminho completo
            arquivo.save(dest)
            extracao_texto_pdf(dest)
            nome_arquivo = identificador


        # classificar depois com IA
        classificacao = "Produtivo" if mensagem else "Improdutivo"

        row = EmailTable(
            email=email,
            assunto=assunto,
            mensagem=mensagem or "(sem corpo — apenas anexo)",
            classificacao=classificacao,
            anexo_pdf=nome_arquivo
        )
        db.session.add(row)
        db.session.commit()

        return jsonify(message="Email registrado com sucesso!")
    else:
        # meu lembrete para criar uma lista de emails para mostrar na página
        
        # emails = EmailTable.query.order_by(EmailTable.created_at.desc()).all()
        # return render_template("home.html", emails=emails)
        return render_template("home.html")


@page.route('/lista_email')
def lista_email():
    return render_template("lista_email.html")
