import PyPDF2

def extracao_texto_pdf(caminho_arquivo: str):
   # Abrir e ler o arquivo PDF em modo binário (rb = read binary)
    with open(caminho_arquivo, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf) # cria um objeto leitor para o PDF

        texto = ""
        for pagina in leitor_pdf.pages:
            texto += pagina.extract_text() + "\n" #\n separa as páginas
    return texto

def extracao_texto_txt(caminho_arquivo: str):
    with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as arquivo_txt: # errors="ignore" ignora caracteres que não podem ser lidos
        texto = arquivo_txt.read()
    return texto