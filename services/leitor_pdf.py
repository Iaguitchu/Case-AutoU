import PyPDF2

def extracao_texto_pdf(caminho_arquivo: str):
    #Abrir e ler o arquivo PDF
    with open(caminho_arquivo, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        texto = ""
        for pagina in leitor_pdf.pages:
            texto += pagina.extract_text() + "\n"
    return texto

def extracao_texto_txt(caminho_arquivo: str):
    with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as arquivo_txt:
        texto = arquivo_txt.read()
    return texto