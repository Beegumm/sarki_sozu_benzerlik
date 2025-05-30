import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

plt.rcParams.update({
    "font.size": 12,
    "figure.figsize": (10, 6),
    "axes.titlesize": 16,
    "axes.labelsize": 14
})

def plot_zipf(file_path, title, output_path):
    df = pd.read_csv(file_path)
    all_words = " ".join(df["text"]).split()
    freq = Counter(all_words)
    freq_sorted = sorted(freq.values(), reverse=True)
    ranks = range(1, len(freq_sorted)+1)

    plt.figure()
    plt.loglog(ranks, freq_sorted, marker='o', linestyle='-', color='darkblue', markersize=3)
    plt.title(title)
    plt.xlabel("Kelime Sırası (log)")
    plt.ylabel("Frekans (log)")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"✅ Zipf grafiği kaydedildi: {output_path}")

if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    plot_zipf("data/processed/lemmatized.csv", "Zipf Grafiği (Lemmatized)", "outputs/zipf_lemmatized.png")
    plot_zipf("data/processed/stemmed.csv", "Zipf Grafiği (Stemmed)", "outputs/zipf_stemmed.png")