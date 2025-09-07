# Data Understanding - Dataset Iris

## 1. Gambaran Umum Dataset

Dataset Iris terdiri dari **150 baris data** dengan **5 kolom** yang merepresentasikan pengukuran morfologi bunga iris dari 3 spesies berbeda.

## 2. Deskripsi Variabel dan Tipe Data

| Variabel | Tipe Data | Deskripsi | Satuan | Contoh Nilai |
|----------|-----------|-----------|--------|--------------|
| **sepal_length** | Numerical (Float) | Panjang sepal bunga iris | cm | 5.1, 4.9, 7.0 |
| **sepal_width** | Numerical (Float) | Lebar sepal bunga iris | cm | 3.5, 3.0, 3.2 |
| **petal_length** | Numerical (Float) | Panjang petal bunga iris | cm | 1.4, 4.7, 6.0 |
| **petal_width** | Numerical (Float) | Lebar petal bunga iris | cm | 0.2, 1.4, 2.5 |
| **species** | Categorical (String) | Spesies bunga iris | - | Iris-setosa, Iris-versicolor, Iris-virginica |

## 3. Analisis Tipe Data Detail

### 3.1 Variabel Numerik (4 variabel)
- **Tipe**: Continuous numerical data (Float)
- **Skala**: Ratio scale (memiliki nilai nol absolut)
- **Operasi Matematika**: Dapat dilakukan operasi aritmatika penuh
- **Visualisasi**: Histogram, boxplot, scatterplot

### 3.2 Variabel Kategorikal (1 variabel)
- **Tipe**: Nominal categorical data
- **Jumlah Kategori**: 3 kelas
- **Encoding**: String literals
- **Visualisasi**: Bar chart, pie chart

## 4. Distribusi Data

![Distribusi Species Iris](https://raw.githubusercontent.com/Haritss28/PSD/website/myfirstbook/images/distribusi_spesies.png)

*Gambar 1: Distribusi Pada Setiap Kelas*

### 4.1 Distribusi Kelas (Target Variable)
- **Iris-setosa**: 50 sampel (33.33%)
- **Iris-versicolor**: 50 sampel (33.33%)
- **Iris-virginica**: 50 sampel (33.33%)
- **Status**: Balanced dataset (distribusi seimbang)

## 5. Kualitas Data

### 5.1 Missing Values
- **Status**: Tidak ada missing values (100% complete)
- **Implikasi**: Tidak perlu data cleaning untuk missing values

### 5.2 Data Consistency
- **Format**: Konsisten untuk semua observasi
- **Decimal Places**: Konsisten dengan 1 decimal place
- **Naming Convention**: Konsisten dengan format "Iris-species"

## 6. Karakteristik Data untuk Machine Learning

### 6.1 Feature Variables (X)
- **Jumlah**: 4 variabel numerik
- **Skala**: Berbeda-beda (perlu normalisasi/standardisasi)
- **Korelasi**: Kemungkinan ada korelasi antar features

### 6.2 Target Variable (y)
- **Tipe**: Multi-class classification (3 kelas)
- **Balance**: Perfectly balanced
- **Encoding**: Perlu label encoding untuk algoritma ML

---
