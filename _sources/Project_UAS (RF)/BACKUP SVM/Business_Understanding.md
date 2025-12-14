# **Business Understanding (Klasifikasi Time Series - Dataset BME)**
## **1. Latar Belakang**
Klasifikasi time series merupakan salah satu permasalahan penting dalam bidang machine learning dan data mining. Berbeda dengan klasifikasi data tabular biasa, data time series memiliki karakteristik khusus yaitu adanya urutan waktu (temporal order) yang harus dipertimbangkan dalam proses analisis. Kemampuan untuk mengklasifikasikan pola time series secara akurat memiliki aplikasi luas di berbagai bidang seperti pengenalan aktivitas manusia, diagnosis medis berdasarkan sinyal EKG, hingga prediksi kondisi mesin industri.

Dataset BME (Begin, Middle, End) merupakan salah satu benchmark dataset yang digunakan untuk menguji performa algoritma klasifikasi time series. Dataset ini terdiri dari sinyal-sinyal temporal yang memiliki pola khas berupa tonjolan (bump) yang muncul di posisi berbeda: awal (Begin), tengah (Middle), atau akhir (End) dari rangkaian waktu. Meskipun terlihat sederhana, dataset BME menjadi tantangan tersendiri karena perbedaan antar kelas hanya terletak pada posisi temporal dari pola tersebut, bukan pada bentuk polanya.

Dengan memanfaatkan algoritma Support Vector Machine (SVM) dengan kernel linear, analisis ini bertujuan untuk membangun model klasifikasi yang mampu mengenali dan membedakan ketiga kelas tersebut secara akurat. SVM Linear dipilih karena kemampuannya dalam menemukan hyperplane optimal yang memisahkan kelas-kelas berbeda dalam ruang fitur berdimensi tinggi, serta sifatnya yang robust terhadap overfitting terutama pada data dengan dimensi tinggi seperti time series.

## **2. Business Problem**
Dalam konteks klasifikasi time series, tantangan utama yang dihadapi adalah bagaimana menangkap informasi temporal yang tersimpan dalam urutan data. Metode klasifikasi konvensional yang mengabaikan urutan waktu seringkali gagal memberikan hasil optimal pada data time series. Adapun permasalahan spesifik yang ingin dijawab dalam proyek ini meliputi:

- Bagaimana membangun model klasifikasi menggunakan SVM Linear yang mampu mengenali perbedaan posisi pola (awal, tengah, akhir) dalam rangkaian time series?
- Apakah pendekatan SVM Linear cukup efektif untuk menangani karakteristik dataset BME yang membedakan kelas berdasarkan posisi temporal?
- Bagaimana mengoptimalkan parameter SVM Linear agar menghasilkan performa klasifikasi yang maksimal?

## **3. Tujuan Analisis**
Proyek ini bertujuan untuk membangun sistem klasifikasi time series pada dataset BME menggunakan algoritma Support Vector Machine (SVM) dengan kernel linear. Adapun tujuan utamanya meliputi:

- Membangun model klasifikasi time series menggunakan SVM Linear yang mampu membedakan tiga kelas pada dataset BME (Begin, Middle, End) berdasarkan posisi pola temporal dalam rangkaian data.
- Melakukan tuning hyperparameter SVM Linear, khususnya parameter regularisasi (C), untuk mendapatkan konfigurasi model yang optimal.
- Mengevaluasi performa model menggunakan metrik evaluasi seperti Accuracy, Precision, Recall, dan F1-Score untuk memastikan model dapat mengklasifikasikan ketiga kelas secara seimbang.
- Menganalisis hasil klasifikasi melalui confusion matrix untuk mengidentifikasi pola kesalahan prediksi dan memahami kekuatan serta kelemahan model SVM Linear pada dataset BME.

## **4. Manfaat Proyek**
Hasil analisis ini diharapkan memberikan manfaat edukatif dan praktis bagi berbagai pihak, antara lain:

- Menjadi referensi pembelajaran dalam memahami penerapan algoritma SVM Linear untuk permasalahan klasifikasi time series serta bagaimana melakukan evaluasi model secara komprehensif.
- Memberikan insight mengenai efektivitas SVM Linear sebagai baseline model untuk klasifikasi time series, termasuk kelebihan dan keterbatasannya dibanding metode lain.
- Hasil proyek ini dapat menjadi pembanding (baseline) untuk pengembangan model klasifikasi time series yang lebih kompleks seperti SVM dengan kernel RBF, atau pendekatan deep learning.

## **5. Ruang Lingkup Proyek**
Ruang lingkup proyek ini meliputi:

- Penggunaan dataset BME yang merupakan bagian dari UEA/UCR Time Series Classification Archive.
- Dataset terdiri dari rangkaian time series dengan panjang tertentu yang terbagi ke dalam tiga kelas: Begin, Middle, dan End.
- Model yang digunakan adalah Support Vector Machine (SVM) dengan kernel linear.
Tahapan proyek meliputi:

1. Eksplorasi data (EDA) untuk memahami struktur serta distribusi kelas pada dataset BME.
2. Visualisasi sampel data dari setiap kelas untuk mengidentifikasi pola karakteristik masing-masing kelas.
3. Preprocessing data termasuk normalisasi atau standarisasi menggunakan StandardScaler agar sesuai dengan karakteristik algoritma SVM.
4. Dataset BME terdiri dari file TRAIN.arff dan TEST.arff sebagaimana disediakan oleh UEA/UCR Time Series Classification Archive.
   Pada penelitian ini, file TRAIN.arff digunakan sepenuhnya sebagai data latih. Sementara itu, file TEST.arff dibagi menjadi dua bagian, yaitu:
    - sebagian kecil data (±8 sampel) digunakan sebagai data uji untuk evaluasi model, dan
    - sisanya digunakan sebagai data baru (unseen data) dalam proses deployment aplikasi.
5. Pelatihan model SVM Linear dengan melakukan tuning hyperparameter C (regularization parameter).
6. Evaluasi performa model berdasarkan Accuracy, Precision, Recall, F1-Score, dan analisis Confusion Matrix.
