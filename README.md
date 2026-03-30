# Proyek Akhir: Menyelesaikan Permasalahan Risiko Dropout

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

## Persiapan

Sumber data yang digunakan pada proyek ini berasal dari dataset performa mahasiswa yang disediakan oleh Dicoding.

Sumber data:  
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Proyek ini dijalankan menggunakan **Python 3.12.7**.

### Menyiapkan Environment Proyek

Pada proyek ini, environment disarankan dipisahkan menggunakan virtual environment agar dependency yang digunakan tidak bertabrakan dengan proyek lain.

#### Opsi 1: Menggunakan Virtual Environment (venv)

Buat virtual environment dengan perintah berikut:

```bash
python -m venv venv
```

Aktifkan virtual environment:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Install seluruh library yang dibutuhkan dari file `requirements.txt`:

```bash
pip install -r requirements.txt
```

Apabila ingin menjalankan notebook secara lokal, gunakan perintah berikut:

```bash
jupyter notebook
```

#### Opsi 2: Menggunakan Conda

Buat environment baru:

```bash
conda create --name student-dropout python=3.12.7
```

Aktifkan environment:

```bash
conda activate student-dropout
```

Install dependency proyek:

```bash
pip install -r requirements.txt
```

Apabila ingin menjalankan notebook secara lokal, gunakan perintah berikut:

```bash
jupyter notebook
```

## Menjalankan Sistem Prediksi Dropout Mahasiswa

Model machine learning yang telah dibangun disimpan dalam file **`student_dropout_brf_model.pkl`** dan digunakan pada aplikasi berbasis **Streamlit** yang terdapat pada file **`prediction.py`**.

File **`prediction.py`** berfungsi sebagai antarmuka prediksi, sedangkan file **`student_dropout_brf_model.pkl`** berisi model **Balanced Random Forest (Calibrated)** yang telah dilatih sebelumnya. Aplikasi ini digunakan untuk membantu memprediksi kemungkinan seorang mahasiswa mengalami dropout berdasarkan beberapa variabel utama yang paling relevan.

Model dilatih menggunakan data dengan status akhir **Dropout** dan **Graduate**. Data dengan status **Enrolled** tidak digunakan pada tahap training, tetapi digunakan pada tahap implementasi untuk melakukan scoring risiko dropout sebagai bagian dari **early warning system**.

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
2. Memeriksa konsistensi fitur input dengan fitur yang digunakan model
3. Menerima input data mahasiswa melalui form Streamlit
4. Menghitung probabilitas risiko dropout
5. Menghasilkan:
   - `Dropout Risk Score`
   - `Graduate Probability`
   - `Risk Category`
   - `Predicted Outcome`
   - `Recommended Intervention`

### Menjalankan Aplikasi Secara Lokal

Untuk menjalankan aplikasi prediksi, gunakan perintah berikut:

```bash
streamlit run prediction.py
```

Link Streamlit:  
https://student-dropout-zfbucn53jbmmj6wfjyhbfa.streamlit.app/

## 📊 Business Dashboard

Business dashboard dibuat untuk membantu institusi memantau kondisi dropout mahasiswa secara lebih cepat, terstruktur, dan mudah dipahami. Dashboard ini berfungsi sebagai alat monitoring serta pendukung pengambilan keputusan berbasis data.

Dashboard dibagi ke dalam beberapa tab utama berikut:

---

### 🔹 Tab 1 — Gambaran Umum Status Mahasiswa

Tab ini menampilkan distribusi mahasiswa berdasarkan status **Dropout**, **Enrolled**, dan **Graduate**, baik dalam bentuk jumlah maupun persentase.

**Insight utama:**
- Memberikan gambaran kondisi umum mahasiswa
- Menunjukkan tingkat dropout secara keseluruhan
- Menjadi indikator awal apakah dropout merupakan masalah signifikan

---

### 🔹 Tab 2 — Analisis Faktor-Faktor Dropout

Tab ini menampilkan faktor-faktor utama yang berkaitan dengan dropout, terutama dari sisi akademik dan administratif.

**Variabel yang dianalisis:**
- Jumlah mata kuliah lulus semester 1 dan 2  
- Nilai semester 1 dan 2  
- Status pembayaran biaya kuliah  
- Program studi (**course**)  

**Insight utama:**
- Performa akademik (terutama semester 2) sangat berpengaruh terhadap dropout  
- Faktor finansial menjadi salah satu penyebab utama  
- Risiko dropout berbeda pada tiap program studi  

---

### 🔹 Tab 3 — Course dengan Risiko Dropout Tertinggi

Tab ini menampilkan program studi dengan tingkat dropout tertinggi berdasarkan **dropout rate**.

**Insight utama:**
- Risiko dropout tidak merata di semua program studi  
- Beberapa course memiliki tingkat risiko jauh lebih tinggi  
- Membantu institusi menentukan prioritas evaluasi program studi  

---

### 🔹 Tab 4 — Variabel Prioritas untuk Monitoring

Tab ini menampilkan lima indikator utama yang perlu dipantau secara rutin oleh institusi:

- `CU2_Approved_Group`  
- `Tuition_fees_up_to_date`  
- `Course`  
- `CU2_Grade_Group`  
- `CU1_Approved_Group`  

**Insight utama:**
- Fokus pada variabel paling berpengaruh  
- Membantu monitoring lebih efisien  
- Memudahkan identifikasi mahasiswa berisiko tinggi  

---

### 🔹 Tab 5 — Early Warning Mahasiswa Enrolled

Tab ini menampilkan hasil prediksi model machine learning untuk mendeteksi risiko dropout lebih dini, khususnya pada mahasiswa yang masih **enrolled**.

**Informasi yang ditampilkan:**
- Distribusi kategori risiko (**Low Risk, Medium Risk, High Risk**)  
- Jumlah mahasiswa **High Risk**  
- Course dengan jumlah mahasiswa High Risk terbanyak  
- Rekomendasi intervensi  

**Insight utama:**
- Mengidentifikasi mahasiswa berisiko sebelum dropout terjadi  
- Membantu menentukan prioritas intervensi  
- Mendukung pengambilan keputusan berbasis data  

---

## 🎯 Kesimpulan Dashboard

Dashboard ini memungkinkan institusi untuk:
- Memahami kondisi dropout secara menyeluruh  
- Mengidentifikasi faktor utama penyebab dropout  
- Menentukan program studi dengan risiko tinggi  
- Memantau variabel penting secara terfokus  
- Mengimplementasikan sistem **early warning** berbasis machine learning  
**Akses Dashboard Metabase**  
Email: `root@mail.com`  
Password: `root123`  
Nama dashboard: `dashboard_final_proyek_dicoding`

## Conclusion

Berdasarkan hasil analisis dan dashboard yang telah dibuat, institusi memiliki 4.424 mahasiswa, yang terdiri dari 2.209 mahasiswa berstatus **Graduate**, 1.421 mahasiswa berstatus **Dropout**, dan 794 mahasiswa berstatus **Enrolled**. Hasil ini menunjukkan bahwa dropout merupakan isu yang cukup signifikan dan perlu mendapat perhatian serius.

Faktor yang paling berkaitan dengan dropout adalah jumlah mata kuliah yang lulus pada semester 2, status pembayaran biaya kuliah, **course**, nilai semester 2, dan jumlah mata kuliah lulus pada semester 1. Mahasiswa yang tidak lulus mata kuliah pada semester 2 menunjukkan dropout rate yang sangat tinggi, demikian juga mahasiswa yang pembayaran biaya kuliahnya tidak up to date.

Dari sisi program studi, beberapa **course** memiliki dropout rate yang jauh lebih tinggi dibanding course lainnya, seperti **Biofuel Production Technologies**, **Equinculture**, **Informatics Engineering**, **Management (evening attendance)**, dan **Basic Education**. Hal ini menunjukkan bahwa risiko dropout tidak tersebar merata, tetapi terkonsentrasi pada kelompok tertentu.

Hasil modeling menunjukkan bahwa model **Balanced Random Forest** memiliki performa yang sangat baik untuk memprediksi risiko dropout mahasiswa. Adapun hasil evaluasi model adalah sebagai berikut:

- **Accuracy:** 0.8333
- **Precision:** 0.7209
- **Recall:** 0.9366
- **F1-Score:** 0.8147
- **ROC-AUC:** 0.9606
- **PR-AUC:** 0.9554
- **Balanced Accuracy:** 0.8518

Nilai **ROC-AUC** dan **PR-AUC** yang tinggi menunjukkan bahwa model memiliki kemampuan yang sangat baik dalam membedakan mahasiswa yang berpotensi dropout dan graduate. Nilai **recall** yang tinggi menunjukkan bahwa model sangat sensitif dalam mendeteksi mahasiswa yang berisiko dropout, sehingga sesuai digunakan sebagai sistem **early warning**.

Model tidak menggunakan threshold default 0.5, tetapi menggunakan threshold optimal sebesar **0.1479** yang diperoleh dari optimasi **F2-score**. Pendekatan ini dipilih agar model lebih fokus dalam meningkatkan recall sehingga lebih banyak mahasiswa berisiko dropout dapat dideteksi lebih awal, meskipun terdapat trade-off pada precision.

Berdasarkan hasil **feature importance**, faktor yang paling berpengaruh terhadap risiko dropout adalah **jumlah mata kuliah yang lulus pada semester 2** (`Curricular_units_2nd_sem_approved`) dengan kontribusi sebesar **53,90%**. Faktor ini menjadi penentu paling dominan dibandingkan variabel lainnya. Selanjutnya, faktor yang juga memiliki pengaruh cukup besar adalah **program studi** (`Course`) sebesar **12,61%**, **status pembayaran biaya kuliah** (`Tuition_fees_up_to_date`) sebesar **11,24%**, **nilai semester 2** (`Curricular_units_2nd_sem_grade`) sebesar **6,65%**, dan **jumlah mata kuliah lulus semester 1** (`Curricular_units_1st_sem_approved`) sebesar **6,14%**.
Temuan ini menunjukkan bahwa faktor akademik dan finansial merupakan penentu utama risiko dropout. Mahasiswa dengan jumlah mata kuliah lulus yang rendah, nilai akademik yang rendah, serta status pembayaran yang tidak lancar memiliki kemungkinan dropout yang lebih tinggi dibandingkan mahasiswa lainnya.

Secara keseluruhan, proyek ini menunjukkan bahwa kombinasi antara exploratory data analysis, dashboard monitoring, dan model prediksi dropout dapat membantu institusi memahami sumber risiko dropout, memantau kelompok mahasiswa yang paling rentan, serta mendukung keputusan intervensi secara lebih objektif, cepat, dan tepat sasaran.

## Rekomendasi Action Items

1. **Perkuat monitoring akademik sejak semester awal**  
   Mahasiswa dengan jumlah mata kuliah lulus yang rendah dan nilai semester yang rendah menunjukkan risiko dropout yang sangat tinggi. Institusi perlu memperkuat monitoring akademik sejak semester awal melalui tutoring, remedial, dan pendampingan belajar.

2. **Prioritaskan intervensi pada mahasiswa dengan masalah pembayaran**  
   Mahasiswa yang biaya kuliahnya tidak up to date memiliki dropout rate sangat tinggi. Oleh karena itu, institusi perlu memprioritaskan intervensi finansial dan administrasi pada kelompok ini.

3. **Fokuskan perhatian pada course dengan dropout rate tertinggi**  
   Program studi dengan dropout rate tinggi perlu mendapatkan perhatian khusus melalui evaluasi kurikulum, pendampingan akademik, serta monitoring mahasiswa yang lebih intensif.

4. **Gunakan dashboard sebagai alat monitoring rutin**  
   Dashboard yang telah dibuat perlu digunakan secara berkala oleh institusi untuk memantau perubahan risiko dropout, terutama pada variabel-variabel prioritas.

5. **Gunakan hasil model sebagai early warning system**  
   Model prediksi dropout yang telah dibangun dapat digunakan sebagai sistem peringatan dini untuk memprioritaskan mahasiswa high risk agar mendapatkan intervensi lebih cepat sebelum benar-benar dropout.