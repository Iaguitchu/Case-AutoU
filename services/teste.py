import nltk
#nltk.download('stopwords')
#nltk.download('punkt_tab')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize


# rodar antes:  python -m spacy download pt_core_news_sm
import spacy


stop_words = set(stopwords.words('portuguese'))


def remover_stopwords(texto:str):
    tokens = word_tokenize(texto)
    tokens_filtrados = []
    for palavra in tokens:
        if palavra.lower() not in stop_words:
            tokens_filtrados.append(palavra)
    return ' '.join(tokens_filtrados)



nlp = spacy.load("pt_core_news_sm")

def processar_lemma(texto: str) -> str:
    doc = nlp(texto)
    lemmas = []  

    for tok in doc:
        #tok.is_space → espaços/brancos || tok.is_punct → pontuação || tok.is_stop → stopwords (ex.: “de”, “a”, “o”, “que”, “não”*)
        if not (tok.is_space or tok.is_punct or tok.is_stop): 
            lemma = tok.lemma_
            lemmas.append(lemma)
    return " ".join(lemmas)

print(processar_lemma(remover_stopwords(''' Protocolo #482913
 De: cliente@empresa.com.br
 Para: suporte@suaaplicacao.com
 Assunto: Solicitação de atualização 
Olá, time de suporte,
 Poderiam, por favor, me informar o status da requisição vinculada ao protocolo #482913? Preciso
 da confirmação de que o acesso ao módulo de relatórios foi liberado para o usuário João Martins
 (CPF 123.456.789-00) ainda hoje.
 Segue em anexo o PDF com o termo de aceite assinado pelo cliente. Caso falte alguma informação
 ou documento complementar, me avisem para que eu possa providenciar.
 Obrigado e fico no aguardo do retorno com os próximos passos e prazos.
 Atenciosamente,
 Carla Souza
 Analista de Operações 
Tel: (11) 99999-9999
 Empresa X''')))