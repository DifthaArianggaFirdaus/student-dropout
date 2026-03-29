# Proyek Akhir: Menyelesaikan Permasalahan Resiko Dropout

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik dalam mencetak lulusan. Namun demikian, institusi ini masih menghadapi permasalahan penting, yaitu tingginya jumlah mahasiswa yang tidak menyelesaikan pendidikannya atau mengalami dropout.

Tingginya angka dropout menjadi isu yang serius karena dapat berdampak pada menurunnya tingkat kelulusan, efektivitas layanan akademik, serta citra institusi secara keseluruhan. Selain itu, dropout juga menunjukkan bahwa terdapat mahasiswa yang tidak mampu mempertahankan keberlanjutan studinya, baik karena faktor akademik, administratif, maupun kondisi personal tertentu. Oleh karena itu, Jaya Jaya Institut membutuhkan pendekatan berbasis data untuk memahami pola dropout mahasiswa dan mendeteksi sedini mungkin mahasiswa yang berisiko tinggi agar dapat diberikan bimbingan atau intervensi yang sesuai.

Melalui proyek ini, dilakukan analisis data mahasiswa untuk mengidentifikasi distribusi status mahasiswa, menemukan faktor-faktor yang paling berkaitan dengan dropout, mengetahui program studi yang memiliki risiko dropout tertinggi, membangun model prediksi risiko dropout, serta menyusun dashboard bisnis yang dapat membantu institusi dalam melakukan monitoring dan pengambilan keputusan secara lebih terstruktur.

### Permasalahan Bisnis

1. Berapa jumlah dan persentase mahasiswa berdasarkan status **Dropout**, **Enrolled**, dan **Graduate** selama periode analisis?

2. Faktor-faktor apa yang paling berkaitan dengan status dropout mahasiswa selama periode analisis?

3. Program studi atau **course** mana yang paling berisiko mengalami dropout, dan berapa besar dropout rate-nya selama periode analisis?

4. Variabel utama apa saja yang wajib dipantau institusi untuk menekan risiko dropout selama periode analisis?

5. Bagaimana pendekatan berbasis data dapat membantu institusi dalam mendeteksi mahasiswa berisiko dropout lebih dini dan menentukan intervensi yang tepat?

### Cakupan Proyek

- Melakukan data understanding dan data preprocessing.
- Melakukan exploratory data analysis untuk memahami pola dropout mahasiswa.
- Melakukan feature engineering untuk memperkaya informasi prediktif.
- Membangun model machine learning untuk prediksi risiko dropout mahasiswa.
- Mengelompokkan mahasiswa ke dalam kategori risiko dropout.
- Menyusun dashboard bisnis untuk monitoring kondisi mahasiswa.
- Menyusun rekomendasi intervensi berbasis data untuk membantu institusi menekan risiko dropout.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:

```
pip install -r requirements.txt


## Menjalankan Sistem Prediksi Dropout Mahasiswa

Model machine learning yang telah dibangun disimpan dalam file **`student_dropout_brf_model.pkl`** dan digunakan pada aplikasi lokal berbasis **Streamlit** yang terdapat pada file **`app.py`**.

File `prediction.py` berfungsi sebagai antarmuka prediksi, sedangkan file `student_dropout_brf_model.pkl` berisi model **Balanced Random Forest** yang telah dilatih sebelumnya. Aplikasi ini digunakan untuk membantu memprediksi kemungkinan seorang mahasiswa mengalami dropout berdasarkan beberapa variabel utama yang paling relevan.

### Variabel Input Model
Model prediksi pada `prediction.py` menggunakan variabel berikut:

- `Curricular_units_2nd_sem_approved`
- `Curricular_units_2nd_sem_grade`
- `Curricular_units_1st_sem_approved`
- `Curricular_units_1st_sem_grade`
- `Tuition_fees_up_to_date`
- `Debtor`
- `Scholarship_holder`
- `Age_at_enrollment`
- `Application_mode`
- `Course`

### Cara Kerja Aplikasi
Aplikasi Streamlit pada file `prediction.py` bekerja dengan langkah berikut:

1. Memuat model dari file **`student_dropout_brf_model.pkl`**
2. Menerima input data mahasiswa melalui form Streamlit
3. Membentuk data input sesuai struktur fitur model
4. Menghasilkan:
   - prediksi dropout
   - skor risiko dropout
   - kategori risiko (`Low Risk`, `Medium Risk`, `High Risk`)
   - rekomendasi intervensi

### Menjalankan Aplikasi Secara Lokal
Untuk menjalankan aplikasi prediksi, gunakan perintah berikut:

```bash
streamlit run prediction.py

link Streamlit : https://student-dropout-as6ygb2danvpy8dtmxrctg.streamlit.app/


## Business Dashboard

Business dashboard dibuat untuk membantu institusi memantau kondisi dropout mahasiswa secara lebih cepat, terstruktur, dan mudah dipahami. Dashboard ini dirancang sebagai alat monitoring dan pendukung pengambilan keputusan berbasis data.

Dashboard dibagi ke dalam beberapa tab utama.

Tab 1 — Gambaran Umum Status Mahasiswa
Tab ini menampilkan distribusi mahasiswa berdasarkan status Dropout, Enrolled, dan Graduate, baik dalam bentuk jumlah maupun persentase. Tab ini membantu institusi memahami kondisi umum mahasiswa selama periode analisis.

Tab 2 — Faktor-Faktor Utama yang Berkaitan dengan Dropout
Tab ini menampilkan faktor-faktor utama yang berkaitan dengan dropout, terutama pada aspek akademik dan administratif, seperti:
- jumlah mata kuliah yang lulus pada semester 1 dan 2,
- nilai semester 1 dan 2,
- status pembayaran biaya kuliah.
Tab ini membantu institusi mengidentifikasi variabel yang paling berkontribusi terhadap risiko dropout.

Tab 3 — Course dengan Risiko Dropout Tertinggi
Tab ini menampilkan program studi atau course dengan dropout rate tertinggi. Visualisasi ini membantu institusi memahami bahwa risiko dropout tidak tersebar merata, tetapi lebih terkonsentrasi pada beberapa program studi tertentu.

Tab 4 — Variabel Prioritas untuk Monitoring
Tab ini menampilkan lima indikator utama yang wajib dipantau institusi, yaitu:
- CU2_Approved_Group
- Tuition_fees_up_to_date
- Course
- CU2_Grade_Group
- CU1_Approved_Group
Tab ini membantu institusi memfokuskan perhatian pada kelompok mahasiswa yang paling rentan mengalami dropout.

Tab 5 — Early Warning Mahasiswa Enrolled
Tab ini menampilkan hasil pendekatan berbasis data melalui model prediksi dropout. Pada tab ini ditampilkan:
- distribusi kategori risiko mahasiswa enrolled
- jumlah mahasiswa high risk
- course dengan jumlah high risk enrolled terbanyak
- distribusi rekomendasi intervensi
Tab ini membantu institusi menentukan prioritas intervensi secara lebih objektif dan terarah.

**Akses Dashboard Metabase**  
Email: `root@mail.com`  
Password: `root123`
nama : dashboard_final_proyek_dicoding


## Conclusion

Berdasarkan hasil analisis dan dashboard yang telah dibuat, institusi memiliki 4.424 mahasiswa, yang terdiri dari 2.209 mahasiswa berstatus Graduate, 1.421 mahasiswa berstatus Dropout, dan 794 mahasiswa berstatus Enrolled. Hasil ini menunjukkan bahwa dropout merupakan isu yang cukup signifikan dan perlu mendapat perhatian serius.

Faktor yang paling berkaitan dengan dropout adalah jumlah mata kuliah yang lulus pada semester 2, status pembayaran biaya kuliah, course, nilai semester 2, dan jumlah mata kuliah lulus pada semester 1. Mahasiswa yang tidak lulus mata kuliah pada semester 2 menunjukkan dropout rate yang sangat tinggi, demikian juga mahasiswa yang pembayaran biaya kuliahnya tidak up to date.

Dari sisi program studi, beberapa course memiliki dropout rate yang jauh lebih tinggi dibanding course lainnya, seperti Biofuel Production Technologies, Equinculture, Informatics Engineering, Management (evening attendance), dan Basic Education. Hal ini menunjukkan bahwa risiko dropout tidak tersebar merata, tetapi terkonsentrasi pada kelompok tertentu.

Hasil modeling juga menunjukkan bahwa pendekatan berbasis data dapat membantu institusi mendeteksi mahasiswa berisiko lebih dini. Model prediksi mampu mengelompokkan mahasiswa ke dalam kategori Low Risk, Medium Risk, dan High Risk. Pada mahasiswa yang masih enrolled, terdapat kelompok high risk yang perlu diprioritaskan untuk intervensi lebih awal.

Secara keseluruhan, proyek ini menunjukkan bahwa kombinasi antara exploratory data analysis, dashboard monitoring, dan model prediksi dropout dapat membantu institusi memahami sumber risiko dropout, memantau kelompok mahasiswa yang paling rentan, serta mendukung keputusan intervensi secara lebih objektif, cepat, dan tepat sasaran.

### Rekomendasi Action Items (Optional)

## Rekomendasi Action Items

1. Perkuat monitoring akademik sejak semester awal

Mahasiswa dengan jumlah mata kuliah lulus yang rendah dan nilai semester yang rendah menunjukkan risiko dropout yang sangat tinggi. Institusi perlu memperkuat monitoring akademik sejak semester awal melalui tutoring, remedial, dan pendampingan belajar.

2. Prioritaskan intervensi pada mahasiswa dengan masalah pembayaran

Mahasiswa yang biaya kuliahnya tidak up to date memiliki dropout rate sangat tinggi. Oleh karena itu, institusi perlu memprioritaskan intervensi finansial dan administrasi pada kelompok ini.

3. Fokuskan perhatian pada course dengan dropout rate tertinggi

Program studi dengan dropout rate tinggi perlu mendapatkan perhatian khusus melalui evaluasi kurikulum, pendampingan akademik, serta monitoring mahasiswa yang lebih intensif.

4. Gunakan dashboard sebagai alat monitoring rutin

Dashboard yang telah dibuat perlu digunakan secara berkala oleh institusi untuk memantau perubahan risiko dropout, terutama pada variabel-variabel prioritas.

5. Gunakan hasil model sebagai early warning system

Model prediksi dropout yang telah dibangun dapat digunakan sebagai sistem peringatan dini untuk memprioritaskan mahasiswa high risk agar mendapatkan intervensi lebih cepat sebelum benar-benar dropout.



