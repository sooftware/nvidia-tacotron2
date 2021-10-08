import re
import unicodedata

CHOSUNGS = "".join([chr(_) for _ in range(0x1100, 0x1113)])
JOONGSUNGS = "".join([chr(_) for _ in range(0x1161, 0x1176)])
JONGSUNGS = "".join([chr(_) for _ in range(0x11A8, 0x11C3)])
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIALS = " ?!"

ALL_VOCABS = "".join([
    CHOSUNGS,
    JOONGSUNGS,
    JONGSUNGS,
    ALPHABETS,
    NUMBERS,
    SPECIALS
])
VOCAB_DICT = {
    "_": 0,
    "~": 1,
}

for idx, v in enumerate(ALL_VOCABS):
    VOCAB_DICT[v] = idx + 2


def normalize(text):
    text = unicodedata.normalize('NFKD', text)
    text = text.upper()
    text = text.replace('%', unicodedata.normalize('NFKD', '퍼센트'))
    regex = unicodedata.normalize('NFKD', r"[^ \u11A8-\u11FF\u1100-\u115E\u1161-\u11A70-9A-Z?!]")
    text = re.sub(regex, '', text)
    text = re.sub(' +', ' ', text)
    text = text.strip()
    return text


def tokenize(text, encoding: bool = True):
    tokens = list()

    for t in text:
        if encoding:
            tokens.append(VOCAB_DICT[t])
        else:
            tokens.append(t)

    if encoding:
        tokens.append(VOCAB_DICT['~'])
    else:
        tokens.append('~')

    return tokens


def text_to_sequence(text):
    text = normalize(text)
    tokens = tokenize(text, encoding=True)
    return tokens
