# Dokumentasi Preprocessing Data dengan KNIME (Projek Pra UTS)

## Deskripsi Umum
Dokumen ini menjelaskan langkah-langkah preprocessing data yang dilakukan menggunakan KNIME Analytics Platform. Workflow ini mencakup proses import data, eksplorasi data, analisis statistik, deteksi outlier, penanganan missing values dengan SMOTE, dan balancing data.

---

## Langkah-Langkah Preprocessing

### 1. Koneksi dan Import Data

#### 1.1 PostgreSQL Connector
- **Node**: PostgreSQL Connector
- **Fungsi**: Membuat koneksi ke database PostgreSQL
- **Konfigurasi**:
  - Hostname dan port database
  - Username dan password
  - Nama database
- **Status**: ✅ Terkoneksi
  ![PostgreSQL Connector](./images_knime/postgresqlconnector.png)

#### 1.2 DB Table Selector
- **Node**: DB Table Selector
- **Fungsi**: Memilih tabel dari database yang akan digunakan untuk analisis
- **Output**: Referensi tabel yang dipilih
![DB Table Selector](./images_knime/DBTableSelector.png)

#### 1.3 DB Reader
- **Node**: DB Reader
- **Fungsi**: Membaca seluruh data dari tabel yang dipilih
- **Output**: Dataset lengkap dalam format tabel KNIME

---

### 2. Eksplorasi Data Awal

#### 2.1 Table View - Melihat Isi Dataset
- **Node**: Table View
- **Fungsi**: Menampilkan isi dataset Ecoli
- **Tujuan**: Memeriksa struktur data, kolom, dan isi data mentah
- **Output**: "Melihat Isi Dataset Ecoli"
![Table View](./images_knime/TableView.png)

#### 2.2 Bar Chart - Distribusi Class Original
- **Node**: Bar Chart
- **Fungsi**: Visualisasi distribusi kelas pada data original
- **Tujuan**: Mengidentifikasi ketidakseimbangan kelas (class imbalance)
- **Output**: "Distribusi Class (Original)"
![Distribusi Class Original](./images_knime/KonfigurasiDistribusiClassOriginal.png)
![Distribusi Class Original](./images_knime/DistribusiClassOriginal.png)

#### 2.3 Statistics - Cek Statistic
- **Node**: Statistics
- **Fungsi**: Menghitung statistik deskriptif dari dataset original
- **Metrik**: Mean, median, standard deviation, min, max, quartiles
- **Tujuan**: Memahami karakteristik data sebelum preprocessing
- **Output**: "Cek statistic"
![Statistics Node](./images_knime/StatisticsKonfigurasi.png)
![Statistics Node](./images_knime/StatisticsNode.png)

#### 2.4 Bar Chart - Distribusi Missing Value (Original)
- **Node**: Bar Chart
- **Fungsi**: Visualisasi distribusi missing value
- **Tujuan**: Mengidentifikasi kolom dengan missing value
- **Output**: "Distribusi Missing Value (tidak ada missing value)"
![Distribusi Missing Value](./images_knime/KonfigurasiDistribusiMissingValue.png)
![Distribusi Missing Value](./images_knime/DistribusiMissingValue.png)


---

### 3. Deteksi dan Handling Outlier

#### 3.1 Numeric Outliers dan Handling Outlier
- **Node**: Numeric Outliers
- **Fungsi**: Mendeteksi dan menandai outlier pada kolom numerik, serta menhandling Outlier
- **Metode**: IQR (Interquartile Range) Method
- **Tujuan**: Mengidentifikasi data yang tidak normal
- **Output**: "Deteksi Outlier dan Menangani Outlier"
![Deteksi dan Handling Outlier](./images_knime/DeteksidanHandlingOutlier.png)

#### 3.2 Bar Chart - Distribusi Deteksi Outlier
- **Node**: Bar Chart
- **Fungsi**: Visualisasi jumlah dan distribusi outlier yang terdeteksi
- **Tujuan**: Melihat seberapa banyak outlier per kolom
- **Output**: "Distribusi Deteksi Outlier"
![Distribusi Outlier](./images_knime/KonfigurasiDistribusiOutlier.png)
![Distribusi Outlier](./images_knime/DistribusiOutlier.png)

---

### 4. Balancing Data dengan SMOTE (Tahap 1)

#### 4.1 SMOTE
- **Node**: SMOTE (Synthetic Minority Over-sampling Technique)
- **Fungsi**: Melakukan oversampling pada kelas minoritas
- **Tujuan**: Menyeimbangkan distribusi kelas
- **Metode**: Membuat data sintetis menggunakan K-Nearest Neighbors
- **Output**: "Balancing Data Menggunakan Smote"
![SMOTE Node](./images_knime/KonfigurasiSMOTENode.png)
![SMOTE Node](./images_knime/SMOTENode.png)

#### 4.2 Statistics - Cek Statistic Setelah Smote
- **Node**: Statistics
- **Fungsi**: Menghitung statistik deskriptif setelah SMOTE
- **Tujuan**: Melihat perubahan statistik setelah balancing
- **Output**: "Cek statistic Setelah Smote"
![Statistic Setelah Smote](./images_knime/StatisticSetelahSmote.png)

---

### 5. Penanganan Missing Value Setelah SMOTE

#### 5.1 Bar Chart - Distribusi Missing Value Setelah SMOTE
- **Node**: Bar Chart
- **Fungsi**: Visualisasi missing value yang muncul setelah proses SMOTE
- **Tujuan**: Mengidentifikasi missing value yang terbentuk
- **Output**: "Distribusi Missing Value Setelah Smote (terdapat Missing Value)"
![Distribusi Missing Value Setelah SMOTE](./images_knime/KonfigurasiDistribusiMissingValueSetelahSMOTE.png)
![Distribusi Missing Value Setelah SMOTE](./images_knime/DistribusiMissingValueSetelahSMOTE.png)

#### 5.2 Missing Value Node
- **Node**: Missing Value
- **Fungsi**: Menangani missing value dengan berbagai metode
- **Metode yang digunakan**: 
  - Median imputation untuk numerik
- **Tujuan**: Membersihkan missing value setelah SMOTE
- **Output**: "Penangan Missing Value setela smote"
![Missing Value Node](./images_knime/MissingValueNode.png)

---

### 6. Verifikasi dan Analisis Akhir

#### 6.1 Statistics - Cek Statistik Setelah Penanganan Missing Value
- **Node**: Statistics
- **Fungsi**: Menghitung statistik final setelah penanganan missing value
- **Tujuan**: Memastikan data sudah bersih dan siap digunakan
- **Output**: "Cek Statistik setelah Penanganan Missing Value"
![Cek Statistik Setelah Penanganan Missing Value](./images_knime/CekStatistikSetelahPenangananMissingValue.png)

#### 6.2 Bar Chart - Distribusi Missing Value Final
- **Node**: Bar Chart
- **Fungsi**: Visualisasi untuk memastikan tidak ada missing value
- **Tujuan**: Verifikasi bahwa missing value sudah tertangani
- **Output**: "Distribusi Missing Value Setelah Penanganan Missing Value (Tidak ada Missing Value)"
![Distribusi Missing Value Final](./images_knime/KonfigurasiDistribusiMissingValueFinal.png)
![Distribusi Missing Value Final](./images_knime/DistribusiDistribusiMissingValueFinal.png)

#### 6.3 Table View - Hasil Setelah Di Balancing
- **Node**: Table View
- **Fungsi**: Menampilkan dataset final setelah semua preprocessing
- **Tujuan**: Review data final sebelum export
- **Output**: "Hasil Setelah Di Balancing"
![Table View Hasil Setelah Di Balancing](./images_knime/HasilSetelahDiBalancing.png)


#### 6.4 Bar Chart - Distribusi Kelas Setelah Balancing
- **Node**: Bar Chart
- **Fungsi**: Visualisasi distribusi kelas final
- **Tujuan**: Memastikan kelas sudah seimbang
- **Output**: "Dristibusi Kelas setelah balancing"
![Distribusi Kelas Setelah Balancing](./images_knime/KonfigurasiDistribusiKelasSetelahBalancing.png)
![Distribusi Kelas Setelah Balancing](./images_knime/DistribusiKelasSetelahBalancing.png)

---

### 7. Export Data

#### 7.1 CSV Writer
- **Node**: CSV Writer
- **Fungsi**: Mengekspor hasil preprocessing ke file CSV
- **Konfigurasi**: 
  - Path dan nama file output
  - Column delimiter
  - Header inclusion
- **Output**: "Convert Ke CSV Hasil setelah balancing"
![Export Data](./images_knime/CSVWriter.png)

---

## Workflow Summary

![Export Data](./images_knime/workflow.png)
```
PostgreSQL Connector → DB Table Selector → DB Reader → 
├── Table View (Melihat Isi Dataset Ecoli)
├── Bar Chart (Distribusi Class Original)
├── Statistics (Cek statistic)
└── Numeric Outliers (Deteksi Outlier) → 
    ├── Bar Chart (Distribusi Deteksi Outlier)
    └── SMOTE (Balancing Data) → 
        ├── Bar Chart (Distribusi Missing Value Original)
        ├── Statistics (Cek statistic Setelah Smote)
        └── Bar Chart (Distribusi Missing Value Setelah Smote) →
            └── Missing Value (Penanganan Missing Value) →
                ├── Statistics (Cek Statistik setelah Penanganan Missing Value)
                ├── Bar Chart (Distribusi Missing Value Final)
                ├── Table View (Hasil Setelah Di Balancing)
                ├── Bar Chart (Distribusi Kelas setelah balancing)
                └── CSV Writer (Export)
```

---

## Alur Proses Preprocessing

### Fase 1: Import dan Eksplorasi
1. Koneksi ke PostgreSQL database
2. Membaca data dari tabel Ecoli
3. Visualisasi distribusi kelas original
4. Analisis statistik deskriptif

### Fase 2: Deteksi Outlier
5. Deteksi outlier menggunakan metode IQR
6. Visualisasi distribusi outlier
7. Penanganan outlier (removal atau treatment)

### Fase 3: Balancing Data
8. Penerapan SMOTE untuk balancing kelas
9. Cek missing value pada data original
10. Analisis statistik setelah SMOTE

### Fase 4: Penanganan Missing Value
11. Identifikasi missing value yang muncul setelah SMOTE
12. Penanganan missing value dengan metode imputation
13. Verifikasi tidak ada missing value tersisa

### Fase 5: Verifikasi dan Export
14. Analisis statistik final
15. Verifikasi distribusi kelas sudah seimbang
16. Review data final
17. Export ke format CSV

---

## Temuan dan Hasil

### Temuan Preprocessing:

1. **Missing Values**: 
   - Data original: Tidak ada missing value
   - Setelah SMOTE: Terdapat missing value
   - Setelah penanganan: Berhasil dibersihkan

2. **Class Imbalance**: 
   - Terdapat ketidakseimbangan kelas pada data original
   - Berhasil diseimbangkan menggunakan SMOTE

3. **Outliers**: 
   - Terdeteksi outlier pada beberapa fitur numerik
   - Ditangani pada tahap preprocessing

4. **Statistik Data**:
   - Statistik berubah setelah SMOTE (karena penambahan data sintetis)
   - Statistik stabil setelah penanganan missing value
---

## Kesimpulan

Preprocessing data telah dilakukan dengan langkah-langkah sistematis dan komprehensif meliputi:

1. ✅ Import data dari PostgreSQL
2. ✅ Eksplorasi dan analisis statistik awal
3. ✅ Deteksi dan penanganan outlier
4. ✅ Balancing data menggunakan SMOTE
5. ✅ Penanganan missing value yang muncul setelah SMOTE
6. ✅ Verifikasi kualitas data final
7. ✅ Export hasil ke CSV

**Data siap untuk tahap selanjutnya**: Modeling, Machine Learning, atau Data Mining.
