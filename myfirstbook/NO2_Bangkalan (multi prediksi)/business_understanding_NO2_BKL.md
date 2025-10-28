# Business Understanding (Kadar NO₂ di Kabupaten Bangkalan)

## 1. Latar Belakang
Kualitas udara merupakan salah satu indikator penting dalam menentukan tingkat kesehatan lingkungan suatu wilayah. Salah satu parameter utama yang berperan dalam menilai kualitas udara adalah konsentrasi nitrogen dioksida (NO₂). Gas ini umumnya dihasilkan dari aktivitas pembakaran bahan bakar fosil seperti kendaraan bermotor, industri, dan pembangkit listrik. Paparan NO₂ dalam jangka panjang dapat menimbulkan gangguan pernapasan serta memperburuk kondisi penyakit paru-paru kronis.

Kabupaten Bangkalan, yang menjadi salah satu wilayah penyangga aktivitas di Pulau Madura dan dekat dengan kawasan industri serta jalur lalu lintas menuju Surabaya, berpotensi mengalami peningkatan kadar NO₂ akibat pertumbuhan transportasi dan aktivitas ekonomi. Oleh karena itu, diperlukan suatu sistem prediksi yang mampu memperkirakan kadar NO₂ secara akurat untuk membantu pemerintah daerah dan masyarakat dalam melakukan antisipasi terhadap pencemaran udara.

Dengan memanfaatkan data penginderaan jauh satelit Copernicus Sentinel-5P serta metode machine learning, khususnya K-Nearest Neighbors (KNN) Regression, analisis ini bertujuan untuk mengidentifikasi pola perubahan kadar NO₂ harian dan melakukan prediksi konsentrasi di hari-hari berikutnya.

## 2. Business Problem
Hingga saat ini, sebagian besar pemantauan kualitas udara masih dilakukan secara reaktif, yaitu setelah pencemaran terjadi. Padahal, kemampuan untuk melakukan prediksi kadar NO₂ secara harian akan sangat membantu dalam pengambilan keputusan yang lebih proaktif. Namun, tantangan yang dihadapi adalah:
- Bagaimana memanfaatkan data historis konsentrasi NO₂ untuk memprediksi kadar NO₂ pada hari berikutnya?
- Bagaimana memilih pendekatan model yang sederhana namun efektif untuk menghasilkan prediksi yang akurat dan mudah diimplementasikan?

## 3. Tujuan Analisis
Proyek ini bertujuan untuk membangun sistem prediksi konsentrasi NO₂ harian menggunakan pendekatan machine learning, khususnya algoritma K-Nearest Neighbors Regression (KNN Regression).
Adapun tujuan utamanya meliputi:

1. Membangun model prediksi konsentrasi NO₂ harian di Kabupaten Bangkalan menggunakan algoritma KNN Regression berdasarkan data historis dari 1 hingga 5 hari sebelumnya.
2. Mengevaluasi performa model dengan melihat metrik seperti Mean Squared Error (MSE), Mean Absolute Error (MAE), dan R² Score untuk menentukan jumlah lag hari optimal.
3. Mengidentifikasi pola temporal antara nilai NO₂ hari ini dengan nilai-nilai pada hari-hari sebelumnya guna memahami tingkat pengaruh waktu terhadap perubahan kualitas udara.

## 4. Manfaat Bisnis
Hasil analisis ini diharapkan memberikan manfaat strategis bagi berbagai pihak, antara lain:

- Pemerintah Daerah/Dinas Lingkungan Hidup (DLH): Mendukung proses pemantauan kualitas udara dengan sistem prediksi sederhana dan hemat sumber daya.
- Masyarakat: Mendapatkan informasi dini tentang potensi peningkatan polusi udara untuk mencegah dampak kesehatan.
- Peneliti/Akademisi : Menjadi contoh penerapan model regresi non-parametrik (KNN Regression) dalam bidang prediksi lingkungan berbasis data terbuka.

## 5. Ruang Lingkup Proyek
Ruang lingkup proyek ini meliputi:

- Pengambilan data konsentrasi NO₂ harian dari satelit Copernicus Sentinel-5P untuk wilayah administratif Kabupaten Bangkalan.
- Periode data yang digunakan mencakup sekitar sembilan bulan terakhir (01 Januari 2025 hingga 01 Oktober 2025).

Tahapan proyek meliputi:
1. Pengumpulan dan pembersihan data (penanganan missing values dengan interpolasi linear).
2. Transformasi data menjadi supervised learning dengan lag 1–5 hari.
3. Normalisasi data menggunakan StandardScaler.
4. Pelatihan model KNN Regression dengan berbagai nilai lag days.
5. Evaluasi performa model berdasarkan MSE, MAE, dan R².
6. Prediksi kadar NO₂ hari berikutnya menggunakan model terbaik.

Fokus penelitian ini terbatas pada hubungan waktu (lag NO₂), belum memasukkan faktor cuaca seperti suhu, kelembapan, dan kecepatan angin.

