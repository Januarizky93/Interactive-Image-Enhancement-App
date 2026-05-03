# Evaluasi Transformasi Intensitas dan Analisis Histogram untuk Peningkatan Kualitas Citra Digital

## Ringkasan
Repositori ini berisi aplikasi interaktif berbasis Python untuk mengevaluasi metode peningkatan kualitas citra digital pada domain spasial. Fokus utama penelitian mencakup integrasi transformasi intensitas dan metode berbasis histogram dalam satu antarmuka eksperimen yang dapat digunakan untuk analisis visual dan statistik sederhana.

Aplikasi mengimplementasikan:
- Image Negative
- Power-Law (Gamma Correction)
- Gray Level Slicing
- Histogram Equalization
- Histogram Matching
- Contrast Limited Adaptive Histogram Equalization (CLAHE)

## Latar Belakang Ilmiah
Citra digital sering mengalami degradasi kualitas akibat kontras rendah, pencahayaan tidak merata, dan keterbatasan sensor. Untuk meningkatkan keterbacaan informasi visual sebelum tahap analisis lanjutan, digunakan teknik image enhancement yang bekerja pada nilai intensitas piksel.

Pendekatan pada proyek ini menggabungkan:
- Transformasi intensitas untuk mengatur kecerahan, menonjolkan rentang keabuan tertentu, dan mempertegas struktur visual.
- Analisis histogram untuk memahami dan memperbaiki distribusi intensitas secara global maupun lokal.

## Tujuan Penelitian
- Mengevaluasi efektivitas metode transformasi intensitas pada citra grayscale.
- Menganalisis perubahan distribusi intensitas citra sebelum dan sesudah enhancement.
- Membandingkan karakteristik metode pada kondisi citra kontras rendah dan pencahayaan tidak merata.
- Menyediakan media eksplorasi interaktif berbasis Python untuk pembelajaran dan eksperimen.

## Metodologi Singkat
1. Pemilihan data citra dari dataset terbuka.
2. Preprocessing: konversi ke grayscale, normalisasi ukuran (umumnya 512x512), dan standarisasi data piksel.
3. Penerapan metode enhancement secara terpisah.
4. Evaluasi berbasis:
   - Perbandingan visual citra asli vs citra hasil.
   - Analisis histogram sebelum dan sesudah pemrosesan.
   - Statistik sederhana: mean dan entropy.

## Hasil Utama (Intisari)
- Histogram Equalization efektif meningkatkan kontras global, tetapi pada kondisi tertentu dapat menurunkan detail lokal akibat over-enhancement.
- CLAHE memberikan peningkatan kontras yang lebih adaptif dan stabil pada area lokal, terutama saat pencahayaan tidak merata.
- Power-Law (gamma correction) fleksibel untuk penyesuaian kecerahan, dengan performa sangat dipengaruhi pemilihan parameter gamma.
- Tidak ada satu metode yang unggul mutlak untuk semua citra; pemilihan metode bergantung pada karakteristik citra awal.

## Struktur Repositori
- `APLIKASI EVALUASI TRANSFORMASI INTENSITAS DAN ANALISIS HISTOGRAM DALAM PENINGKATAN KUALIRTAS CITRA DIGITAL.py` : aplikasi utama berbasis Tkinter.
- `DataSet/` : folder data citra untuk pengujian.
- Berkas PDF dan DOCX : naskah ilmiah yang menjadi acuan penelitian.
- Berkas gambar JPEG/PNG : dokumentasi visual hasil eksperimen.

## Kebutuhan Sistem
- Python 3.9+
- pip

Dependensi Python:
- numpy
- opencv-python
- matplotlib
- pillow
- scipy

## Instalasi
```bash
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install numpy opencv-python matplotlib pillow scipy
```

## Menjalankan Aplikasi
```bash
python "APLIKASI EVALUASI TRANSFORMASI INTENSITAS DAN ANALISIS HISTOGRAM DALAM PENINGKATAN KUALIRTAS CITRA DIGITAL.py"
```

## Alur Penggunaan
1. Klik Open Image untuk memuat citra uji.
2. Opsional: klik Open Reference Image untuk kebutuhan Histogram Matching.
3. Atur gamma melalui slider jika menggunakan Power-Law.
4. Pilih metode enhancement dari panel kanan.
5. Amati hasil citra, histogram, dan statistik (mean, entropy) pada tampilan aplikasi.

## Kontribusi (Novelty)
- Integrasi beberapa metode enhancement ke dalam satu aplikasi interaktif terpadu.
- Evaluasi komparatif dengan kombinasi analisis visual dan distribusi histogram.
- Dukungan eksplorasi parameter secara real-time untuk kebutuhan riset dan pembelajaran.

## Keterbatasan
- Evaluasi statistik masih sederhana (mean dan entropy), belum mencakup metrik objektif lanjutan seperti PSNR/SSIM.
- Fokus utama pada citra grayscale.
- Evaluasi kuantitatif lintas dataset dapat diperluas lebih lanjut.

## Pengembangan Lanjutan
- Menambahkan metrik evaluasi objektif (PSNR, SSIM, NIQE).
- Menambahkan pipeline batch processing dan logging eksperimen.
- Menambahkan ekspor hasil evaluasi ke format CSV.
- Menambah dukungan antarmuka web (misalnya Streamlit) untuk akses yang lebih luas.

## Sitasi
Jika repositori ini digunakan sebagai referensi akademik, mohon cantumkan sitasi terhadap penulis dan judul penelitian:

Adhitya Januarizky Hadi Putra. Evaluasi Transformasi Intensitas dan Analisis Histogram dalam Peningkatan Kualitas Citra Digital Berbasis Aplikasi Interaktif.

## Lisensi
Silakan tambahkan lisensi yang sesuai (misalnya MIT License) sebelum publikasi final repositori.
