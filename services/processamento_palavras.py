# rodar antes:  python -m spacy download pt_core_news_sm
import spacy
try:
    nlp = spacy.load("pt_core_news_sm")
except OSError:
    from spacy.cli import download
    download("pt_core_news_sm")
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