import subprocess

print("🔹 1. Şarkı sözleri indiriliyor...")
subprocess.run(["python", "scripts/fetch_lyrics.py"])

print("🔹 2. Ön işleme başlıyor...")
subprocess.run(["python", "scripts/preprocess.py"])

print("🔹 3. Zipf grafikleri oluşturuluyor...")
subprocess.run(["python", "scripts/zipf_plotter.py"])

print("🔹 4. Word2Vec modelleri eğitiliyor...")
subprocess.run(["python", "scripts/train_w2v.py"])

print("🔹 5. Cosine similarity hesaplanıyor...")
subprocess.run(["python", "scripts/compare.py"])

print("✅ Tüm işlemler başarıyla tamamlandı.")