# Get Data

## 1. Sumber Data
Data Iris didapatkan dari dua database berbeda untuk mendemonstrasikan integrasi data multi-sumber:

### 1.1 Database MySQL
Menyimpan data karakteristik sepal bunga iris:
- `sepal_length` - Panjang sepal (cm)
- `sepal_width` - Lebar sepal (cm)

### 1.2 Database PostgreSQL  
Menyimpan data karakteristik petal dan klasifikasi spesies:
- `petal_length` - Panjang petal (cm)
- `petal_width` - Lebar petal (cm)
- `species` - Jenis spesies iris (setosa, versicolor, virginica)

## 2. Ekstraksi Data

### 2.1 Mengambil Data dari MySQL
Code Python untuk mengambil data sepal dari MySQL ke Power BI:

```python
import pandas as pd
from sqlalchemy import create_engine

# buat koneksi ke MySQL
engine = create_engine("mysql+pymysql://root:@localhost/iris_sepal")

# ambil data
df = pd.read_sql("SELECT * FROM iris_sepal", engine)
```

### 2.2 Mengambil Data dari PostgreSQL
Code Python untuk mengambil data petal dan spesies dari PostgreSQL ke Power BI:

```python
import pandas as pd
from sqlalchemy import create_engine

# konfigurasi koneksi PostgreSQL
user = "postgres"        
password = "28_Maret_2005"      
host = "localhost"       
port = "5432"           
database = "iris_petal"        

# buat koneksi
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# ambil data ke DataFrame
df = pd.read_sql("SELECT * FROM iris_petal", engine)
```

## Integrasi Data di Power BI

Setelah kedua dataset berhasil diambil dari masing-masing database, data kemudian diintegrasikan di Power BI melalui proses **merge/join** berdasarkan key yang sama (saya berdasarkan id).

### Hasil Akhir
Dataset terintegrasi yang berisi:
- `sepal_length` (dari MySQL)
- `sepal_width` (dari MySQL)  
- `petal_length` (dari PostgreSQL)
- `petal_width` (dari PostgreSQL)
- `species` (dari PostgreSQL)

![Dataset Iris Marge](../images/dateset_marge.png)