# HR Analytics: Employee Attrition Clustering Dashboard

Project ini membahas **HR Analytics** dengan fokus pada **attrition (tingkat keluar-masuk karyawan)**.  
Pendekatan yang digunakan adalah **Machine Learning - KMeans Clustering**, lalu divisualisasikan melalui **dashboard interaktif** untuk mendapatkan insight yang lebih mudah dipahami.

## 🚀 Cara Menjalankan Dashboard


```bash
https://hr-analytics-app.streamlit.app/
```

## 📊 Alur Analisis

1. Eksplorasi Data
    - Dilakukan melalui notebook.ipynb
    - Meliputi preprocessing, EDA, dan feature engineering

2. Clustering dengan KMeans
    - Model KMeans dilatih untuk membagi karyawan ke dalam beberapa cluster berdasarkan atribut yang relevan dengan attrition.

    - File model:

       1. model_summary.joblib → ringkasan clustering, digunakan di dashboard

       2. kmeans_model.joblib → model KMeans asli, bisa digunakan untuk prediksi tambahan

3. Dashboard
    - app.py menggunakan model hasil clustering untuk menampilkan insight, visualisasi, dan analisis interaktif.

## 📌 Insight Utama
  - Segmentasi karyawan berdasarkan risiko attrition
  - Faktor-faktor yang memengaruhi tingkat attrition
  - Distribusi cluster untuk mendukung keputusan HR

## 📦 Requirements

Dependencies utama dapat dilihat di requirements.txt

🙌 Kontributor

Project ini dikerjakan oleh:

  - Fikri Kurnia (@Nauviii)

## 📄 Lisensi

Project ini dibuat untuk kebutuhan submission Dicoding dan hanya digunakan untuk tujuan pembelajaran.
