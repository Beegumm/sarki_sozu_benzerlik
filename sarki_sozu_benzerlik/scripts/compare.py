from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

model = Word2Vec.load("models/lemmatized/word2vec_lemmatized_cbow_win2_dim100.model")
df = pd.read_csv("data/processed/lemmatized.csv")
texts = df["text"].tolist()[:2]

def sentence_vector(sentence):
    vectors = [model.wv[word] for word in sentence.split() if word in model.wv]
    if not vectors:
        return np.zeros(model.vector_size)
    return np.mean(vectors, axis=0)

vec1 = sentence_vector(texts[0])
vec2 = sentence_vector(texts[1])
score = cosine_similarity([vec1], [vec2])[0][0]

with open("outputs/similarity_score.txt", "w", encoding="utf-8") as out:
    out.write(f"Cosine Benzerlik Skoru: {score:.4f}")
print(f"✅ Benzerlik skoru: {score:.4f}")