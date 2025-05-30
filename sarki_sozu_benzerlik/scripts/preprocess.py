import os
import re
import pandas as pd

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"
os.makedirs(PROCESSED_PATH, exist_ok=True)

def clean(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower()

lemmatized, stemmed = [], []

for fname in os.listdir(RAW_PATH):
    with open(os.path.join(RAW_PATH, fname), "r", encoding="utf-8") as f:
        cleaned = clean(f.read())
        lemmatized.append(cleaned)
        stemmed.append(cleaned)

pd.DataFrame({"text": lemmatized}).to_csv(f"{PROCESSED_PATH}/lemmatized.csv", index=False)
pd.DataFrame({"text": stemmed}).to_csv(f"{PROCESSED_PATH}/stemmed.csv", index=False)
print("✅ preprocess: CSV dosyaları oluşturuldu.")