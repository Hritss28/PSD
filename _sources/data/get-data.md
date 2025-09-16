# Get Data

## Sumber Data
Data Iris didapatkan dari dua database berbeda untuk mendemonstrasikan integrasi data multi-sumber:

### Database MySQL
Menyimpan data karakteristik sepal bunga iris:
- `sepal_length` - Panjang sepal (cm)
- `sepal_width` - Lebar sepal (cm)

### Database PostgreSQL  
Menyimpan data karakteristik petal dan klasifikasi spesies:
- `petal_length` - Panjang petal (cm)
- `petal_width` - Lebar petal (cm)
- `species` - Jenis spesies iris (setosa, versicolor, virginica)

## Ekstraksi Data

### 1. Mengambil Data dari MySQL
Code Python untuk mengambil data sepal dari MySQL ke Power BI:

```python
import mysql.connector as myconnector
import pandas as pd

# Koneksi ke database MySQL
conn = myconnector.connect(
    database="iris_db",
    host="localhost",
    user="root",
    password="",
    port=3306
)

# Query data sepal
sepal = pd.read_sql("SELECT * FROM iris_table", conn)

# Tutup koneksi
conn.close()
```

### 2. Mengambil Data dari PostgreSQL
Code Python untuk mengambil data petal dan spesies dari PostgreSQL ke Power BI:

```python
import pandas as pd
import psycopg2 as pgconnector

# Koneksi ke database PostgreSQL
conn = pgconnector.connect(
    "dbname=iris_db host=localhost user=postgres password=zanra2401 port=2005"
)

# Query data petal dan spesies
petal_species = pd.read_sql("SELECT * FROM iris_table", conn)

# Tutup koneksi
conn.close()
```

## Integrasi Data di Power BI

Setelah kedua dataset berhasil diambil dari masing-masing database, data kemudian diintegrasikan di Power BI melalui proses **merge/join** berdasarkan key yang sama (biasanya ID atau index row).

### Hasil Akhir
Dataset terintegrasi yang berisi:
- `sepal_length` (dari MySQL)
- `sepal_width` (dari MySQL)  
- `petal_length` (dari PostgreSQL)
- `petal_width` (dari PostgreSQL)
- `species` (dari PostgreSQL)

Dataset lengkap ini kemudian siap digunakan untuk analisis dan visualisasi dalam Power BI dashboard.

![Dataset Iris Marge](../images/dateset_marge.png)