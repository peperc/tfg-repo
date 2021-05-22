import os
import re
import time
from gensim.models import Word2Vec


def preprocessing(file: str):

    if not os.path.isfile(file):
        print('File not found')
        return

    try:
        f = open(file)
    except IOError:
        print('File not accesible')
        return

    content = f.read()
    # Eliminar comas
    content = re.sub(r'\,', '', content)
    # Sustituir caracteres que no sean del alfabeto o espacios por saltos de linea
    content = re.sub(r'[^a-zA-ZÀ-ÿ\u00f1\u00d1\n ]', '\n', content)
    # ELiminar uno o más espacios a principio o final de linea
    content = re.sub(r'^ +| +$', '', content, flags=re.MULTILINE)
    # Sustituir dos o más saltos de línea seguidos por uno solo
    content = re.sub(r'\n{2,}', '\n', content)
    texts = content.split('\n')

    stoplist = set(
        'el la los las se a o por para sin como su que al en de y del con un una sobre sus lo no cuando'.split())

    sentences = [[word for word in sentence.lower().split() if word not in stoplist]
                 for sentence in texts if len(sentence.split()) > 2]

    return sentences


control = time.time()
print('Preprocessing your corpus...')

sentences = preprocessing('corpus/constitucion')
print(f'Time taken : {(time.time() - control) / 60:.2f} mins\n')

control = time.time()
print('Preparing your model...')

model = Word2Vec(sentences=sentences, vector_size=300,
                 window=5, min_count=1, workers=4)
print(f'Time taken : {(time.time() - control) / 60:.2f} mins\n')

print(model.wv.most_similar(positive=['derechos']))