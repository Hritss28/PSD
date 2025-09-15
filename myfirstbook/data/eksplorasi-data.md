# Eksplorasi Data

## 1. Statistik Deskriptif Dasar

### 1.2 Jumlah Setiap Kelas
![Distribusi Species Iris](../images/species_distribusi.png)

**Hasil**:
- Iris-setosa: 50 sampel (33.33%)
- Iris-versicolor: 50 sampel (33.33%)
- Iris-virginica: 50 sampel (33.33%)

**Insight**: Dataset perfectly balanced - tidak ada bias kelas, ideal untuk machine learning.

### 1.3 Min-Max Setiap Kolom
![Min_Max_kolom](../images/min_max_kolom.png)

**Hasil Analisis**:
- **sepal_length**: 4.3 - 7.9 cm (range: 3.6 cm)
- **sepal_width**: 2.0 - 4.4 cm (range: 2.4 cm)
- **petal_length**: 1.0 - 6.9 cm (range: 5.9 cm)
- **petal_width**: 0.1 - 2.5 cm (range: 2.4 cm)

**Insight**: Petal length memiliki variasi terbesar (5.9 cm), menunjukkan karakteristik yang paling beragam antar spesies.

### 1.5 Tabel Ringkasan Statistik Lengkap

| Statistik | sepal_length | sepal_width | petal_length | petal_width |
|-----------|--------------|-------------|--------------|-------------|
| **Mean/Rata-Rata** | 5.84 | 3.05 | 3.76 | 1.20 |
| **Median** | 5.80 | 3.00 | 4.35 | 1.30 |
| **Std Dev** | 0.83 | 0.43 | 1.76 | 0.76 |
| **Variance** | 0.69 | 0.19 | 3.10 | 0.58 |
| **Min** | 4.30 | 2.00 | 1.00 | 0.10 |
| **Max** | 7.90 | 4.40 | 6.90 | 2.50 |
| **Range** | 3.60 | 2.40 | 5.90 | 2.40 |

#### 1.5.1 Rata-rata Setiap Kolom

**Hasil Analisis**:
- **sepal_length**: ~5.84 cm 
- **sepal_width**: ~3.05 cm 
- **petal_length**: ~3.76 cm 
- **petal_width**: ~1.20 cm 

**Insight**: Sepal umumnya lebih besar dari petal, dengan width selalu lebih kecil dari length.

#### 1.5.2 Median Setiap Kolom

**Hasil Analisis**:
- **sepal_length**: ~5.80 cm (mendekati mean, distribusi simetris)
- **sepal_width**: ~3.00 cm (mendekati mean, distribusi normal)
- **petal_length**: ~4.35 cm (lebih besar dari mean, skew ke kiri)
- **petal_width**: ~1.30 cm (lebih besar dari mean, skew ke kiri)

**Insight**: Petal measurements cenderung skewed karena perbedaan besar antara Iris-setosa dengan spesies lainnya.

#### 1.5.3 Standard Deviasi Setiap Kolom

**Hasil Analisis**:
- **sepal_length**: ~0.83 cm (variabilitas sedang)
- **sepal_width**: ~0.43 cm (variabilitas rendah)
- **petal_length**: ~1.76 cm (variabilitas tinggi)
- **petal_width**: ~0.76 cm (variabilitas sedang-tinggi)

**Insight**: Petal length memiliki variabilitas tertinggi, mengkonfirmasi bahwa ini adalah feature yang paling diskriminatif.

#### 1.5.4 Variance Setiap Kolom

**Hasil Analisis**:
- **sepal_length**: ~0.69 cm² (variance sedang)
- **sepal_width**: ~0.19 cm² (variance rendah)
- **petal_length**: ~3.10 cm² (variance tertinggi)
- **petal_width**: ~0.58 cm² (variance sedang)

**Insight**: Variance menguatkan temuan bahwa petal length memiliki dispersi data terbesar antar spesies.

## 
### ABOD 

```python
import pandas as pd
from pycaret.anomaly import * 
import matplotlib.pyplot as plt

data = pd.read_csv("IRIS.csv")
data = data.drop(columns=["species"])

s = setup(data)

abod = create_model('abod', fraction=0.05) 
results = assign_model(abod)

results_sorted = results.sort_values(by="Anomaly", ascending=False)

# Ringkasan hasil outlier detection (tampilkan 10 baris pertama)
print("Ringkasan Hasil Outlier Detection (10 baris pertama):")
print(results_sorted[['sepal_length','sepal_width','petal_length','petal_width','Anomaly','Anomaly_Score']].head(10))

# Hitung jumlah outlier dan normal
outlier_count = results['Anomaly'].sum()
normal_count = len(results) - outlier_count
total_count = len(results)
outlier_percent = (outlier_count / total_count) * 100

print("\n Statistik Outlier:")
print(f"Total Data     : {total_count}")
print(f"Normal Data    : {normal_count}")
print(f"Outlier Data   : {outlier_count}")
print(f"Persentase Outlier : {outlier_percent:.2f}%")

# Visualisasi tabel ringkas (opsional, misalnya untuk notebook)
summary_df = pd.DataFrame({
    'Kategori': ['Normal', 'Outlier'],
    'Jumlah': [normal_count, outlier_count],
    'Persentase': [100 - outlier_percent, outlier_percent]
})
print("\n Ringkasan Jumlah Data:")
print(summary_df)


# Buat scatter plot dengan dua fitur utama
plt.figure(figsize=(8,6))
plt.scatter(
    results['petal_length'], results['petal_width'],
    c=results['Anomaly'], cmap='coolwarm', edgecolor='k'
)

# Tambahkan judul dan label
plt.title("Visualisasi Deteksi Outlier dengan ABOD")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

# Tambahkan legenda
handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Normal',
               markerfacecolor='blue', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Outlier',
               markerfacecolor='red', markersize=8)
]
plt.legend(handles=handles)

plt.show()
```

#### Ringkasan Hasil Outlier Detection (10 baris pertama) ABOD

| Index | Sepal Length | Sepal Width | Petal Length | Petal Width | Anomaly | Anomaly Score |
|-------|--------------|-------------|--------------|-------------|---------|---------------|
| 131   | 7.9          | 3.8         | 6.4          | 2.0         | 1       | -0.137417     |
| 62    | 6.0          | 2.2         | 4.0          | 1.0         | 1       | -0.289391     |
| 108   | 6.7          | 2.5         | 5.8          | 1.8         | 1       | -0.084224     |
| 106   | 4.9          | 2.5         | 4.5          | 1.7         | 1       | -0.050388     |
| 117   | 7.7          | 3.8         | 6.7          | 2.2         | 1       | -0.129286     |
| 100   | 6.3          | 3.3         | 6.0          | 2.5         | 1       | -0.364475     |
| 134   | 6.1          | 2.6         | 5.6          | 1.4         | 1       | -0.309969     |
| 41    | 4.5          | 2.3         | 1.3          | 0.3         | 1       | -0.088998     |
| 84    | 5.4          | 3.0         | 4.5          | 1.5         | 0       | -3.127326     |
| 97    | 6.2          | 2.9         | 4.3          | 1.3         | 0       | -29.977802    |

---

#### Statistik Outlier ABOD

- **Total Data**     : 150  
- **Normal Data**    : 142  
- **Outlier Data**   : 8  
- **Persentase Outlier** : 5.33%  

---

#### Ringkasan Jumlah Data ABOD

| Kategori | Jumlah | Persentase |
|----------|--------|------------|
| Normal   | 142    | 94.67%     |
| Outlier  | 8      | 5.33%      |

---

#### Visualisasi Outlier ABOD


![Petal Length](abod.png)

### KNN

```python
import pandas as pd
from pycaret.anomaly import * 
import matplotlib.pyplot as plt

data = pd.read_csv("IRIS.csv")
data = data.drop(columns=["species"])

s = setup(data)

knn = create_model('knn', fraction=0.05) 
results = assign_model(knn)

results_sorted = results.sort_values(by="Anomaly", ascending=False)

# Ringkasan hasil outlier detection (tampilkan 10 baris pertama)
print("Ringkasan Hasil Outlier Detection (10 baris pertama):")
print(results_sorted[['sepal_length','sepal_width','petal_length','petal_width','Anomaly','Anomaly_Score']].head(10))

# Hitung jumlah outlier dan normal
outlier_count = results['Anomaly'].sum()
normal_count = len(results) - outlier_count
total_count = len(results)
outlier_percent = (outlier_count / total_count) * 100

print("\n Statistik Outlier:")
print(f"Total Data     : {total_count}")
print(f"Normal Data    : {normal_count}")
print(f"Outlier Data   : {outlier_count}")
print(f"Persentase Outlier : {outlier_percent:.2f}%")

# Visualisasi tabel ringkas (opsional, misalnya untuk notebook)
summary_df = pd.DataFrame({
    'Kategori': ['Normal', 'Outlier'],
    'Jumlah': [normal_count, outlier_count],
    'Persentase': [100 - outlier_percent, outlier_percent]
})
print("\n Ringkasan Jumlah Data:")
print(summary_df)


# Buat scatter plot dengan dua fitur utama
plt.figure(figsize=(8,6))
plt.scatter(
    results['petal_length'], results['petal_width'],
    c=results['Anomaly'], cmap='coolwarm', edgecolor='k'
)

# Tambahkan judul dan label
plt.title("Visualisasi Deteksi Outlier dengan KNN")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

# Tambahkan legenda
handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Normal',
               markerfacecolor='blue', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Outlier',
               markerfacecolor='red', markersize=8)
]
plt.legend(handles=handles)

plt.show()

```

#### Ringkasan Hasil Outlier Detection dengan Metode ABOD (10 Baris Pertama)

| Index | Sepal Length | Sepal Width | Petal Length | Petal Width | Anomaly | Anomaly Score |
|-------|--------------|-------------|--------------|-------------|---------|---------------|
| 131   | 7.9          | 3.8         | 6.4          | 2.0         | 1       | 1.024695      |
| 57    | 4.9          | 2.4         | 3.3          | 1.0         | 1       | 0.787401      |
| 109   | 7.2          | 3.6         | 6.1          | 2.5         | 1       | 0.806226      |
| 106   | 4.9          | 2.5         | 4.5          | 1.7         | 1       | 0.883176      |
| 117   | 7.7          | 3.8         | 6.7          | 2.2         | 1       | 1.019804      |
| 118   | 7.7          | 2.6         | 6.9          | 2.3         | 1       | 0.964365      |
| 98    | 5.1          | 2.5         | 3.0          | 1.1         | 1       | 0.818535      |
| 41    | 4.5          | 2.3         | 1.3          | 0.3         | 1       | 0.793726      |
| 84    | 5.4          | 3.0         | 4.5          | 1.5         | 0       | 0.509902      |
| 82    | 5.8          | 2.7         | 3.9          | 1.2         | 0       | 0.346410      |

---

#### Statistik Outlier ABOD

- **Total Data**     : 150  
- **Normal Data**    : 142  
- **Outlier Data**   : 8  
- **Persentase Outlier** : 5.33%  

---

#### Ringkasan Jumlah Data ABOD

| Kategori | Jumlah | Persentase |
|----------|--------|------------|
| Normal   | 142    | 94.67%     |
| Outlier  | 8      | 5.33%      |

---

#### Visualisasi Outlier ABOD


![Petal Length](knn.png)

---

### LOF

```python

import pandas as pd
from pycaret.anomaly import * 
import matplotlib.pyplot as plt

data = pd.read_csv("IRIS.csv")
data = data.drop(columns=["species"])

s = setup(data)

lof = create_model('lof', fraction=0.05) 
results = assign_model(lof)

results_sorted = results.sort_values(by="Anomaly", ascending=False)

# Ringkasan hasil outlier detection (tampilkan 10 baris pertama)
print("Ringkasan Hasil Outlier Detection (10 baris pertama):")
print(results_sorted[['sepal_length','sepal_width','petal_length','petal_width','Anomaly','Anomaly_Score']].head(10))

# Hitung jumlah outlier dan normal
outlier_count = results['Anomaly'].sum()
normal_count = len(results) - outlier_count
total_count = len(results)
outlier_percent = (outlier_count / total_count) * 100

print("\n Statistik Outlier:")
print(f"Total Data     : {total_count}")
print(f"Normal Data    : {normal_count}")
print(f"Outlier Data   : {outlier_count}")
print(f"Persentase Outlier : {outlier_percent:.2f}%")

# Visualisasi tabel ringkas (opsional, misalnya untuk notebook)
summary_df = pd.DataFrame({
    'Kategori': ['Normal', 'Outlier'],
    'Jumlah': [normal_count, outlier_count],
    'Persentase': [100 - outlier_percent, outlier_percent]
})
print("\n Ringkasan Jumlah Data:")
print(summary_df)


# Buat scatter plot dengan dua fitur utama
plt.figure(figsize=(8,6))
plt.scatter(
    results['petal_length'], results['petal_width'],
    c=results['Anomaly'], cmap='coolwarm', edgecolor='k'
)

# Tambahkan judul dan label
plt.title("Visualisasi Deteksi Outlier dengan LOF")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

# Tambahkan legenda
handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Normal',
               markerfacecolor='blue', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Outlier',
               markerfacecolor='red', markersize=8)
]
plt.legend(handles=handles)

plt.show()

```

#### Ringkasan Hasil Outlier Detection dengan Metode LOF (10 Baris Pertama)

| Index | Sepal Length | Sepal Width | Petal Length | Petal Width | Anomaly | Anomaly Score |
|-------|--------------|-------------|--------------|-------------|---------|---------------|
| 122   | 7.7          | 2.8         | 6.7          | 2.0         | 1       | 1.491365      |
| 118   | 7.7          | 2.6         | 6.9          | 2.3         | 1       | 1.624653      |
| 41    | 4.5          | 2.3         | 1.3          | 0.3         | 1       | 1.777233      |
| 98    | 5.1          | 2.5         | 3.0          | 1.1         | 1       | 1.511868      |
| 15    | 5.7          | 4.4         | 1.5          | 0.4         | 1       | 1.653626      |
| 14    | 5.8          | 4.0         | 1.2          | 0.2         | 1       | 1.463125      |
| 131   | 7.9          | 3.8         | 6.4          | 2.0         | 1       | 1.547288      |
| 117   | 7.7          | 3.8         | 6.7          | 2.2         | 1       | 1.572990      |
| 106   | 4.9          | 2.5         | 4.5          | 1.7         | 0       | 1.374999      |
| 105   | 7.6          | 3.0         | 6.6          | 2.1         | 0       | 1.399554      |

---

#### Statistik Outlier ABOD

- **Total Data**     : 150  
- **Normal Data**    : 142  
- **Outlier Data**   : 8  
- **Persentase Outlier** : 5.33%  

---

#### Ringkasan Jumlah Data ABOD

| Kategori | Jumlah | Persentase |
|----------|--------|------------|
| Normal   | 142    | 94.67%     |
| Outlier  | 8      | 5.33%      |

---

#### Visualisasi Outlier ABOD


![Petal Length](lof.png)


