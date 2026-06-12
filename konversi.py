import os
import pandas as pd
import json

# Memastikan folder 'data' sudah terbentuk
os.makedirs("data", exist_ok=True)

CSV_PATH = os.path.join("data", "indonesia_mtsamples.csv")
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"Silakan taruh file indonesia_mtsamples.csv di dalam folder 'data' terlebih dahulu!")

print("Membaca dan memproses dataset CSV...")
# Membaca dataset dengan delimeter titik koma (;) sesuai dengan struktur data asli
df = pd.read_csv(CSV_PATH, sep=";", engine='python', encoding='utf-8-sig')
df.columns = df.columns.str.strip().str.lower()

# Membersihkan baris kosong pada teks kalimat panjang transkripsi
df = df.dropna(subset=['transcription_id']).reset_index(drop=True)

# Mengubah data ke dalam bentuk List of Dictionary untuk format JSON
data_list = []
for idx, row in df.iterrows():
    data_list.append({
        "id": idx,
        "specialty": str(row['medical_specialty_id']),
        "sample_name": str(row['sample_name_id']),
        "description": str(row['description_id']),
        "transcription": str(row['transcription_id']),
        "keywords": str(row['keywords_id']) if 'keywords_id' in df.columns and pd.notna(row['keywords_id']) else '-'
    })

# Menyimpan file ke dalam folder data
JSON_PATH = os.path.join("data", "dataset_medis.json")
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(data_list, f, indent=4, ensure_ascii=False)

print(f"Sukses! Berkas '{JSON_PATH}' berhasil diekstraksi.")