import os
import json
import numpy as np
from flask import Flask, request, render_template
from rank_bm25 import BM25Okapi

# KONFIGURASI KHUSUS: Menggabungkan folder static ke folder templates
app = Flask(__name__, template_folder='templates', static_folder='templates')

# =========================================================================
# PROSES 1: MEMBACA DATABASE DARI FOLDER DATA (MEMENUHI INDIKATOR 2)
# =========================================================================
JSON_PATH = os.path.join("data", "dataset_medis.json")
if not os.path.exists(JSON_PATH):
    raise FileNotFoundError(f"Berkas database {JSON_PATH} tidak ditemukan! Jalankan 'python konversi.py' terlebih dahulu.")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    dataset = json.load(f)


# =========================================================================
# PROSES 2: PROSES TOKENSASI & INDEKSING ALGORITMA BM25 OKAPI
# =========================================================================
print("Mengindeks korpus dokumen medis menggunakan BM25 Okapi...")

def tokenize_indonesia(text):
    """Fungsi tokenisasi untuk membersihkan tanda baca dan memecah teks menjadi kata kecil"""
    cleaned = str(text).lower().replace(",", "").replace(".", "").replace('"', "").replace(";", "")
    return cleaned.split()

# Mengekstrak field transkripsi (kalimat panjang) dari database JSON
corpus_texts = [doc['transcription'] for doc in dataset]

# Memproses pemecahan kata (bag-of-words) untuk seluruh dokumen rekam medis
tokenized_corpus = [tokenize_indonesia(text) for text in corpus_texts]
bm25 = BM25Okapi(tokenized_corpus)

# PROSES 3: ROUTING & LOGIKA UTAMA SEARCH ENGINE BM25
@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query = ""
    
    if request.method == 'POST':
        query = request.form.get('query', '')
        
        if query.strip() != "":
            # Tokenisasi kata kunci pencarian dari user
            tokenized_query = tokenize_indonesia(query)
            
            # Hitung skor relevansi menggunakan rumus statistik BM25 Okapi
            bm25_scores = bm25.get_scores(tokenized_query)
            
            # Lakukan perangkingan (Re-ranking) dan ambil Top 5 dokumen teratas
            top_indices = np.argsort(bm25_scores)[::-1][:5]
            
            for idx in top_indices:
                score = bm25_scores[idx]
                
                # Hanya tampilkan hasil jika kata kunci cocok/relevan (Skor matematika > 0)
                if score > 0:
                    results.append({
                        "specialty": dataset[idx]['specialty'],
                        "sample_name": dataset[idx]['sample_name'],
                        "description": dataset[idx]['description'],
                        "transcription": dataset[idx]['transcription'],
                        "keywords": dataset[idx]['keywords'],
                        "score": round(float(score), 4) # MEMUNCULKAN NILAI KESAMAAN (MEMENUHI INDIKATOR 4)
                    })
                    
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)



