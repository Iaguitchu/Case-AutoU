# blueprints/page.py
import os, uuid
from flask import Blueprint, render_template, request, jsonify, current_app, send_from_directory
from werkzeug.utils import secure_filename
from models import db, EmailTable
from services.leitor_pdf import extracao_texto_pdf, extracao_texto_txt
from services.classificador_email import classificador_email, sugerir_resposta
from services.processamento_palavras import  processar_lemma

page = Blueprint('page', __name__)

def _ext_ok(nome_arquivo: str):
    if "." not in nome_arquivo:
        return False
    extensao = ('pdf', 'txt')
    arquivo_tratado = nome_arquivo.rsplit(".", 1)[1].lower() # Divide a string da direita para a esquerda, no máximo 1 vez
    if arquivo_tratado in extensao:
        return True
    else:
        return False 

@page.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":

        # Processando o formulário via POST
        email    = request.form.get("email")
        assunto  = request.form.get("assunto")
        mensagem = request.form.get("mensagem")

        arquivo = request.files.get("anexo")
        nome_arquivo = None

        if mensagem is None or mensagem.strip() == "" and (arquivo is None or arquivo.filename == ""):
            resposta_sugerida = "Por favor, insira uma mensagem ou anexe um arquivo."
            classificacao = "Improdutivo"

        elif arquivo and arquivo.filename:
            if not _ext_ok(arquivo.filename):
                return jsonify(message="Extensão não permitida (use .pdf ou .txt)."), 400

            ext = arquivo.filename.rsplit(".", 1)[1].lower() # Pega a extensão do arquivo
            identificador = f"{uuid.uuid4().hex}.{ext}" # Gera um nome único para o arquivo e adiciona a extensão
            dest = os.path.join(current_app.config["UPLOAD_FOLDER"], identificador) # Define o caminho completo
            arquivo.save(dest)
            if ext == "txt":
                extracao = extracao_texto_txt(dest)
            elif ext == "pdf":
                extracao = extracao_texto_pdf(dest)
            else:
                extracao = ""
            nome_arquivo = identificador
            texto = (mensagem or "") + (extracao or "")
            classificacao = classificador_email(processar_lemma(texto))
            resposta_sugerida = sugerir_resposta(processar_lemma(texto) or "", classificacao)
        
        else:
            classificacao = classificador_email(processar_lemma(mensagem or ""))
            resposta_sugerida = sugerir_resposta(processar_lemma(mensagem) or "", classificacao)
        

        row = EmailTable(
            email=email,
            assunto=assunto,
            mensagem= mensagem or "",
            classificacao=classificacao,
            anexo_pdf=nome_arquivo,
            resposta_sugerida=resposta_sugerida
        )
        db.session.add(row)
        db.session.commit()

        return jsonify(message=f"Email registrado com sucesso! Classificação: {classificacao}"), 200
    else:
        
        
        emails = EmailTable.query.order_by(EmailTable.data_hora.desc()).all()

        return render_template("home.html", emails=emails)


@page.route('/lista_email')
def lista_email():
    return render_template("lista_email.html")
