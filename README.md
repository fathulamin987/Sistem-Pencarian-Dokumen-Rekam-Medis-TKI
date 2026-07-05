# Medical Transcriptions Search Engine

Aplikasi web untuk mencari dokumen rekam medis (Medical Transcriptions) berbahasa Indonesia menggunakan metode **Information Retrieval**. Sistem akan mencari, mengurutkan, dan menampilkan dokumen rekam medis yang paling relevan berdasarkan kata kunci yang dimasukkan pengguna.

sumber dataset : https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions


## Fitur Utama

- **Pencarian Rekam Medis**  
  Mencari dokumen rekam medis berbahasa Indonesia berdasarkan kata kunci dan mengurutkan hasil sesuai tingkat relevansinya.

- **Menggunakan Flask**  
  Aplikasi dibangun menggunakan framework Flask dengan penyimpanan data dalam format JSON.

- **Tampilan Sederhana**  
  Antarmuka dibuat sederhana dan mudah digunakan. Tata letak halaman akan menyesuaikan ketika proses pencarian dilakukan.

- **Highlight Kata Kunci**  
  Kata kunci yang ditemukan pada hasil pencarian akan diberi warna kuning sehingga lebih mudah dikenali.

- **Tampilkan/Sembunyikan Isi Dokumen**  
  Pengguna dapat membuka atau menutup isi transkripsi agar tampilan hasil pencarian tetap rapi.

---

## Struktur Direktori Proyek

```text
├── data/
│   ├── indonesia_mtsamples.csv   # Dataset hasil terjemahan
│   └── dataset_medis.json        # Dataset dalam format JSON
├── templates/
│   ├── index.html                # Halaman utama aplikasi
│   └── style.css                 # Tampilan antarmuka
├── app.py                        # Program utama dan proses pencarian
├── konversi.py                   # Konversi dataset CSV ke JSON
├── tarjemah_data.ipynb           # Notebook proses penerjemahan dataset
└── README.md                     # Dokumentasi proyek
```

---

## Alur Kerja Sistem

Sistem bekerja melalui tiga tahap utama sebelum aplikasi dapat digunakan.

### 1. Penerjemahan Dataset (`tarjemah_data.ipynb`)

- Dataset rekam medis asli diperoleh dari Kaggle (Medical Transcriptions / MTSamples).
- Sebanyak **500 data** dipilih sebagai sampel agar proses pencarian lebih cepat.
- Data diterjemahkan dari Bahasa Inggris ke Bahasa Indonesia menggunakan library penerjemah di Python.
- Hasil terjemahan disimpan dalam file:

```
data/indonesia_mtsamples.csv
```

---

### 2. Konversi Dataset ke JSON (`konversi.py`)

- Membaca file CSV hasil terjemahan.
- Menghapus data yang tidak memiliki isi transkripsi.
- Mengubah data ke dalam format JSON.
- Menyimpan hasilnya sebagai:

```
data/dataset_medis.json
```

File JSON ini digunakan sebagai sumber data oleh aplikasi.

---

### 3. Proses Pencarian (`app.py`)

Saat aplikasi dijalankan:

- Sistem membaca file `dataset_medis.json`.
- Kata kunci yang dimasukkan pengguna diubah menjadi huruf kecil dan dibersihkan dari tanda baca.
- Sistem menghitung tingkat kecocokan menggunakan algoritma **BM25 Okapi**.
- Dokumen diurutkan berdasarkan skor relevansi.
- Lima dokumen dengan skor tertinggi akan ditampilkan kepada pengguna.

---

## Cara Menjalankan Proyek

### 1. Persyaratan

Pastikan Python versi **3.8** atau lebih baru sudah terpasang pada komputer.

### 2. Install Library

Buka Terminal atau Command Prompt kemudian jalankan:

```bash
pip install flask rank-bm25 numpy pandas openpyxl
```

### 3. Menjalankan Aplikasi

#### Langkah 1

Pastikan file berikut sudah berada di dalam folder `data/`.

```
indonesia_mtsamples.csv
```

#### Langkah 2

Konversi dataset menjadi format JSON.

```bash
python konversi.py
```

Jika berhasil akan terbentuk file:

```
data/dataset_medis.json
```

#### Langkah 3

Jalankan aplikasi Flask.

```bash
python app.py
```

#### Langkah 4

Buka browser kemudian akses alamat berikut.

```
http://127.0.0.1:5000
```

---

## Dataset

Dataset yang digunakan berasal dari **Medical Transcriptions (MTSamples)** yang tersedia di Kaggle.

Untuk mempercepat proses pencarian dan pengujian aplikasi, hanya digunakan **500 data** sebagai sampel. Seluruh data telah diterjemahkan ke dalam Bahasa Indonesia sebelum digunakan pada sistem.

---

## Catatan

Proyek ini dibuat sebagai implementasi sistem temu kembali informasi (Information Retrieval) menggunakan algoritma **BM25 Okapi** pada dokumen rekam medis. Dataset yang digunakan merupakan data publik dari Kaggle dan hanya digunakan untuk keperluan pembelajaran serta penelitian.
