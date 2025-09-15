# Preprocessing 

## Remove Data Outlier

### Remove Data Outlier Hasil dari Metode ABOD
```python

import pandas as pd
from pycaret.anomaly import * 
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("IRIS.csv")
data = data.drop(columns=["species"])

# setup data PyCaret
s = setup(data)

# membuat model dari metode
abod = create_model('abod') 
results = assign_model(abod)

# menghapus data outlier
cleaned_data = results[results["Anomaly"] == 0].copy()

print("Data asli: ", results.shape)
print("Data setelah hapus outlier: ", cleaned_data.shape)

# buat file csv baru
cleaned_data.to_csv("iris_abod_cleaned.csv", index=False)

fig, axes = plt.subplots(1, 2, figsize=(14,6))

# Sebelum dihapus data outlier
axes[0].scatter(
    results['petal_length'], results['petal_width'],
    c=results['Anomaly'], cmap='coolwarm', edgecolor='k'
)
axes[0].set_title("Sebelum Hapus Outlier (adob)")
axes[0].set_xlabel("Petal Length")
axes[0].set_ylabel("Petal Width")

# Sesudah dihapus data outlier
axes[1].scatter(
    cleaned_data['petal_length'], cleaned_data['petal_width'],
    c='blue', edgecolor='k'
)
axes[1].set_title("Sesudah Hapus Outlier (abod)")
axes[1].set_xlabel("Petal Length")
axes[1].set_ylabel("Petal Width")

handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Normal',
               markerfacecolor='blue', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Outlier',
               markerfacecolor='red', markersize=8)
]
plt.legend(handles=handles)

plt.tight_layout()
plt.show()
```

#### Hasil Preprocessing dengan ABOD

Setelah dilakukan deteksi outlier menggunakan metode *ABOD (Angle-Based Outlier Detection)*, data dibersihkan dengan cara menghapus baris yang teridentifikasi sebagai outlier.

- *Jumlah data asli* : 150 baris  
- *Jumlah data setelah hapus outlier* : 142 baris  
- *Jumlah data yang terdeteksi sebagai outlier* : 8 baris  

Jadi, sekitar *5,33% data* dianggap sebagai outlier dan dihapus dari dataset.  

![Petal Length](/images/prep_abod.png)

---

### Remove Data Outlier Hasil dari Metode KNN
```python

import pandas as pd
from pycaret.anomaly import * 
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("IRIS.csv")
data = data.drop(columns=["species"])

# setup data PyCaret
s = setup(data)

# membuat model dari metode
knn = create_model('knn') 
results = assign_model(knn)

# menghapus data outlier
cleaned_data = results[results["Anomaly"] == 0].copy()

print("Data asli: ", results.shape)
print("Data setelah hapus outlier: ", cleaned_data.shape)

# buat file csv baru
cleaned_data.to_csv("iris_abod_cleaned.csv", index=False)

fig, axes = plt.subplots(1, 2, figsize=(14,6))

# Sebelum dihapus data outlier
axes[0].scatter(
    results['petal_length'], results['petal_width'],
    c=results['Anomaly'], cmap='coolwarm', edgecolor='k'
)
axes[0].set_title("Sebelum Hapus Outlier (KNN)")
axes[0].set_xlabel("Petal Length")
axes[0].set_ylabel("Petal Width")

# Sesudah dihapus data outlier
axes[1].scatter(
    cleaned_data['petal_length'], cleaned_data['petal_width'],
    c='blue', edgecolor='k'
)
axes[1].set_title("Sesudah Hapus Outlier (KNN)")
axes[1].set_xlabel("Petal Length")
axes[1].set_ylabel("Petal Width")

handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Normal',
               markerfacecolor='blue', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Outlier',
               markerfacecolor='red', markersize=8)
]
plt.legend(handles=handles)

plt.tight_layout()
plt.show()
```


#### Hasil Preprocessing dengan KNN

Setelah dilakukan deteksi outlier menggunakan metode *KNN (k-Nearest Neighbors Detector)*, data dibersihkan dengan cara menghapus baris yang teridentifikasi sebagai outlier.

- *Jumlah data asli* : 150 baris  
- *Jumlah data setelah hapus outlier* : 142 baris  
- *Jumlah data yang terdeteksi sebagai outlier* : 8 baris  

Jadi, sekitar *5,33% data* dianggap sebagai outlier dan dihapus dari dataset.  

![Petal Length](/images/prep_knn.png)

---

### Remove Data Outlier Hasil dari Metode LOF

```python

import pandas as pd
from pycaret.anomaly import * 
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("IRIS.csv")
data = data.drop(columns=["species"])

# setup data PyCaret
s = setup(data)

# membuat model dari metode
lof = create_model('lof') 
results = assign_model(lof)

# menghapus data outlier
cleaned_data = results[results["Anomaly"] == 0].copy()

print("Data asli: ", results.shape)
print("Data setelah hapus outlier: ", cleaned_data.shape)

# buat file csv baru
cleaned_data.to_csv("iris_abod_cleaned.csv", index=False)

fig, axes = plt.subplots(1, 2, figsize=(14,6))

# Sebelum dihapus data outlier
axes[0].scatter(
    results['petal_length'], results['petal_width'],
    c=results['Anomaly'], cmap='coolwarm', edgecolor='k'
)
axes[0].set_title("Sebelum Hapus Outlier (LOF)")
axes[0].set_xlabel("Petal Length")
axes[0].set_ylabel("Petal Width")

# Sesudah dihapus data outlier
axes[1].scatter(
    cleaned_data['petal_length'], cleaned_data['petal_width'],
    c='blue', edgecolor='k'
)
axes[1].set_title("Sesudah Hapus Outlier (LOF)")
axes[1].set_xlabel("Petal Length")
axes[1].set_ylabel("Petal Width")

handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Normal',
               markerfacecolor='blue', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Outlier',
               markerfacecolor='red', markersize=8)
]
plt.legend(handles=handles)

plt.tight_layout()
plt.show()
```


#### Hasil Preprocessing dengan LOF

Setelah dilakukan deteksi outlier menggunakan metode *LOF (Local Outlier Factor)*, data dibersihkan dengan cara menghapus baris yang teridentifikasi sebagai outlier.

- *Jumlah data asli* : 150 baris  
- *Jumlah data setelah hapus outlier* : 142 baris  
- *Jumlah data yang terdeteksi sebagai outlier* : 8 baris  

Jadi, sekitar *5,33% data* dianggap sebagai outlier dan dihapus dari dataset.  

![Petal Length](/images/prep_lof.png)

---