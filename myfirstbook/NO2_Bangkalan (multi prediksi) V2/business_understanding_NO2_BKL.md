# Business Understanding (Kadar NO₂ di Kabupaten Bangkalan)

## 1. Latar Belakang
Kualitas udara merupakan salah satu indikator penting dalam menentukan tingkat kesehatan lingkungan suatu wilayah. Salah satu parameter utama yang berperan dalam menilai kualitas udara adalah konsentrasi nitrogen dioksida (NO₂). Gas ini umumnya dihasilkan dari aktivitas pembakaran bahan bakar fosil seperti kendaraan bermotor, industri, dan pembangkit listrik. Paparan NO₂ dalam jangka panjang dapat menimbulkan gangguan pernapasan serta memperburuk kondisi penyakit paru-paru kronis.

Kabupaten Bangkalan, yang menjadi salah satu wilayah penyangga aktivitas di Pulau Madura dan dekat dengan kawasan industri serta jalur lalu lintas menuju Surabaya, berpotensi mengalami peningkatan kadar NO₂ akibat pertumbuhan transportasi dan aktivitas ekonomi. Oleh karena itu, diperlukan suatu sistem prediksi yang mampu memperkirakan kadar NO₂ secara akurat untuk membantu pemerintah daerah dan masyarakat dalam melakukan antisipasi terhadap pencemaran udara.

Jika sebelumnya sistem prediksi hanya berfokus pada perkiraan satu hari ke depan, maka dalam penelitian ini dilakukan pengembangan model untuk memprediksi kadar NO₂ hingga tiga hari ke depan (multi-step forecasting). Pendekatan ini memberikan kemampuan yang lebih luas dalam memperkirakan tren jangka pendek kualitas udara, sehingga langkah mitigasi dapat dilakukan lebih dini. Dengan memanfaatkan data penginderaan jauh satelit Copernicus Sentinel-5P serta metode machine learning, khususnya K-Nearest Neighbors (KNN) Regression, analisis ini bertujuan untuk mengidentifikasi pola perubahan kadar NO₂ harian dan melakukan prediksi berjangka beberapa hari ke depan secara lebih adaptif dan akurat.

## 2. Business Problem
Hingga saat ini, sebagian besar pemantauan kualitas udara masih dilakukan secara reaktif, yaitu setelah pencemaran terjadi. Padahal, kemampuan untuk melakukan prediksi kadar NO₂ secara berjangka (lebih dari satu hari) akan sangat membantu dalam pengambilan keputusan yang lebih proaktif. Namun, tantangan yang dihadapi adalah:
- Bagaimana memanfaatkan data historis konsentrasi NO₂ untuk memprediksi kadar NO₂ hingga tiga hari ke depan?
- Bagaimana menentukan model dan konfigurasi lag yang paling optimal agar hasil prediksi multi-step tetap akurat dan stabil?

## 3. Tujuan Analisis
Proyek ini bertujuan untuk membangun sistem prediksi konsentrasi NO₂ harian menggunakan pendekatan machine learning, khususnya algoritma K-Nearest Neighbors Regression (KNN Regression).
Adapun tujuan utamanya meliputi:

1. Membangun model prediksi konsentrasi NO₂ di Kabupaten Bangkalan yang mampu memperkirakan nilai hingga tiga hari ke depan berdasarkan data historis (multi-step forecasting).
2. Mengevaluasi performa model KNN Regression untuk masing-masing horizon prediksi (hari ke-1, ke-2, dan ke-3) menggunakan metrik seperti Mean Squared Error (MSE), Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), dan R² Score.
3. Mengidentifikasi pengaruh nilai lag terhadap kemampuan model dalam memprediksi kadar NO₂ berjangka beberapa hari, guna memahami seberapa jauh data historis dapat memberikan informasi yang relevan terhadap kondisi masa depan.

## 4. Manfaat Bisnis
Hasil analisis ini diharapkan memberikan manfaat strategis bagi berbagai pihak, antara lain:

- Pemerintah Daerah/Dinas Lingkungan Hidup (DLH): Mendukung proses pemantauan kualitas udara dengan sistem prediksi multi-hari yang membantu perencanaan mitigasi lebih awal.
- Masyarakat: Mendapatkan informasi lebih awal mengenai potensi peningkatan polusi udara dalam beberapa hari mendatang untuk mempersiapkan langkah pencegahan kesehatan.
- Peneliti/Akademisi : Menjadi contoh penerapan model regresi non-parametrik (KNN Regression) dalam skenario multi-step forecasting berbasis data satelit terbuka.

## 5. Ruang Lingkup Proyek
Ruang lingkup proyek ini meliputi:

- Pengambilan data konsentrasi NO₂ harian dari satelit Copernicus Sentinel-5P untuk wilayah administratif Kabupaten Bangkalan.
- Periode data yang digunakan mencakup sekitar sembilan bulan terakhir (01 Januari 2025 hingga 01 Oktober 2025).

Tahapan proyek meliputi:
1. Pengumpulan dan pembersihan data (penanganan missing values dengan interpolasi linear).
2. Transformasi data menjadi supervised learning dengan lag 1–5 hari.
3. Normalisasi data menggunakan StandardScaler.
4. Pelatihan model KNN Regression untuk melakukan prediksi hingga tiga hari ke depan (multi-output regression).
5. Evaluasi performa model berdasarkan MSE, MAE, MAPE, dan R² untuk setiap horizon prediksi.
6. Visualisasi hasil berupa perbandingan antara nilai aktual dan prediksi untuk masing-masing horizon (t+1, t+2, t+3).

Fokus penelitian ini terbatas pada hubungan waktu (lag NO₂), belum memasukkan faktor cuaca seperti suhu, kelembapan, dan kecepatan angin.



