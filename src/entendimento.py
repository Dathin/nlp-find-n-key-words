from nltk import tokenize
from typing import List


def _dividir_em_frases(texto: str) -> List[str]:
    return tokenize.sent_tokenize(texto, language="portuguese")