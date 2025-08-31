# Proyek Akhir: Analisis Attrition Karyawan Perusahaan Edutech

## Business Understanding

**Latar Belakang**
Jaya Jaya Maju adalah perusahaan multinasional di bidang Edutech yang berdiri sejak tahun 2000 dengan lebih dari 1.000 karyawan tersebar di seluruh Indonesia.
Meskipun perusahaan sudah berkembang pesat, tingkat **attrition rate** (rasio karyawan keluar terhadap total karyawan) perusahaan cukup tinggi, mencapai **>10%**.
Tingginya attrition rate berpotensi meningkatkan biaya perekrutan, pelatihan, dan mengganggu produktivitas perusahaan.
Untuk itu, manajemen HR ingin memahami faktor-faktor yang memengaruhi keputusan karyawan untuk keluar dan mengembangkan strategi retensi yang tepat.

---

## Permasalahan Bisnis

Manajer departemen HR meminta bantuan untuk:

1. Mengidentifikasi faktor-faktor utama yang memengaruhi tingginya attrition rate.
2. Menganalisis data karyawan secara menyeluruh guna memahami pola dan tren terkait turnover.
3. Mengembangkan model prediksi attrition untuk membantu HR mengantisipasi potensi karyawan keluar.
4. Membuat business dashboard interaktif untuk memonitor dan memvisualisasikan faktor-faktor attrition secara real-time, sehingga dapat mendukung pengambilan keputusan berbasis data.

---

## Cakupan Proyek

1. **Data Preprocessing & Feature Engineering**

   * Membersihkan data, menangani missing values, encoding fitur kategorikal, dan scaling.
2. **Exploratory Data Analysis (EDA)**

   * Visualisasi dan analisis statistik untuk menemukan pola dan insight.
3. **Model Machine Learning**

   * Membangun model klasifikasi untuk memprediksi attrition karyawan.
4. **Evaluasi Model**

   * Menggunakan metrik evaluasi seperti Confusion Matrix, Classification Report, dan ROC-AUC.
5. **Dashboard Interaktif**

   * Membuat aplikasi analisis berbasis **Streamlit** untuk memudahkan eksplorasi data dan insight.

---

## Persiapan

### 🔗 Dataset

* **Sumber Data**: [Employee Data - Dicoding](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)
* **Jumlah Data**: 1.470 karyawan dengan tingkat attrition **12.18%** (179 karyawan keluar).

---

### 🛠️ Tech Stack

* **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
* **Streamlit** (Pembuatan Dashboard)
* **Joblib** (Model Serialization)
* **GitHub** (Version Control)

---

### ⚙️ Persiapan & Setup Proyek

Pastikan Anda mengikuti langkah-langkah berikut agar proyek dapat dijalankan dengan baik:

#### 1. Clone Repository

```bash
git clone https://github.com/Nauviii/Data-Science-HR-Analytics.git
cd Data-Science-HR-Analytics
```

#### 2. Membuat dan Mengaktifkan Virtual Environment

Agar lingkungan pengembangan terisolasi dan stabil, buat virtual environment (venv):

* **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

* **macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Menjalankan Dashboard

```bash
streamlit run app.py
```

---

## Business Dashboard

🔗 Akses Dashboard: [HR Analytics Dashboard](https://hr-analytics-app.streamlit.app/)

Dashboard ini adalah aplikasi interaktif berbasis Streamlit yang membantu stakeholder menganalisis tingkat attrition. Dashboard mencakup:

1. **EDA (Exploratory Data Analysis)** – Visualisasi distribusi data dan korelasi antar fitur.
2. **Model Results** – Hasil prediksi attrition dengan metrik evaluasi.
3. **Insights & Recommendations** – Temuan utama dan rekomendasi actionable.

---

## 📌 Conclusion

Proyek ini berhasil membangun **end-to-end pipeline data science** untuk menganalisis dan memprediksi attrition karyawan di perusahaan Jaya Jaya Maju. Analisis dilakukan dengan pendekatan **Exploratory Data Analysis (EDA)**, pemodelan machine learning, serta pengembangan **dashboard interaktif** berbasis Streamlit yang dapat digunakan manajemen untuk memonitor faktor-faktor attrition secara real-time.

Berdasarkan analisis data terhadap **1.470 karyawan dengan tingkat attrition 12,18%**, ditemukan bahwa attrition dipengaruhi oleh kombinasi faktor lingkungan kerja, demografi, pengalaman kerja, dan kompensasi.

### 🔍 Faktor-Faktor Utama Penyebab Attrition

1. **Kepuasan Kerja dan Lingkungan Rendah**
2. **Usia Muda (Early Career Stage)**
3. **Tekanan Kerja Tinggi di Divisi R\&D**
4. **Masa Kerja Singkat dan Transisi Manajemen**
5. **Pendapatan Relatif Rendah**

### 👤 Karakteristik Karyawan yang Rentan Attrition

* Usia muda dan berada di tahap awal karier.
* Masa kerja relatif singkat (0–5 tahun).
* Berada di divisi dengan tingkat tekanan kerja tinggi.
* Tingkat kepuasan kerja dan lingkungan rendah.
* Kompensasi di bawah rata-rata perusahaan.

### 📈 Jawaban Pertanyaan Bisnis

* **Faktor utama penyebab attrition:** Rendahnya kepuasan kerja, usia muda, masa kerja singkat, tekanan kerja tinggi, dan kompensasi rendah.
* **Profil karyawan dengan risiko tinggi:** Karyawan baru dengan gaji rendah, kepuasan kerja rendah, dan bekerja di divisi dengan beban tinggi.
* **Tindakan untuk mengurangi attrition:** Peningkatan engagement, penyesuaian kompensasi, dukungan karyawan baru, dan optimasi manajemen divisi.

---

## Rekomendasi Strategis

1. **Peningkatan Kepuasan Kerja & Lingkungan**

   * Rutin melakukan employee engagement survey.
   * Program kesejahteraan dan komunikasi terbuka.
2. **Program Retensi Karyawan Muda**

   * Mentorship, pelatihan soft skill, dan rotasi kerja.
3. **Optimasi Manajemen R\&D**

   * Evaluasi beban kerja, pemberian reward untuk inovasi.
4. **Dukungan Transisi Manajemen**

   * Onboarding manager baru & sesi check-in rutin.
5. **Perbaikan Kompensasi & Benefit**

   * Benchmarking gaji dan penawaran benefit non-finansial.
