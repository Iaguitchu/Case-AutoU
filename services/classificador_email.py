import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

def classificador_email(text: str):
    prompt = (
        "Você é um classificador binário. "
        "Leia o conteúdo de um e-mail e responda **apenas** com uma palavra: "
        "'Produtivo' ou 'Improdutivo'.\n\n"
        "Definições:\n"
        "- Produtivo: requer ação ou resposta específica (suporte, atualização de caso, dúvida sobre sistema, envio de documentos).\n"
        "- Improdutivo: felicitações, agradecimentos simples ou mensagens sem ação imediata.\n\n"
        "Email:\n"
        f"{text}\n\n"
        "Responda somente com Produtivo ou Improdutivo."
    )
    chat = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=10,
    )

    resposta = (chat.choices[0].message.content or "").strip().lower() # Se mensg for None, usa string vazia
    if "improdutivo" in resposta:
        return "Improdutivo"
    elif "produtivo" in resposta:
        return "Produtivo"
    else:
        return "Indefinido, tente novamente"


def sugerir_resposta(texto_original: str, categoria: str) :
    prompt = (
        f"Categoria do email: {categoria}.\n"
        "Gere uma resposta curta (até 120 palavras), educada e objetiva em PT-BR, "
        "com próximos passos claros. Se for Produtivo, solicite dados/indique ação. "
        "Se for Improdutivo, agradeça e encerre.\n\n"
        f"Email:\n{texto_original}"
    )
    chat = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=220,
    )
    return (chat.choices[0].message.content or "").strip()
