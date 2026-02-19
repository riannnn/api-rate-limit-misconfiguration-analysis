# api-rate-limit-misconfiguration-analysis
Security analysis of API rate limiting misconfiguration validated via Burp Suite, cURL automation, and Python scripting.

This project aims to analyze the rate limiting implementation of an API endpoint and identify potential configuration errors that could lead to API misuse.

Tests are performed both manually and automatically to ensure that the system actually executes requests on the backend.

📌 Ikhtisar

Proyek ini bertujuan untuk menganalisis pembatasan laju implementasi pada sebuah API titik akhir dan mengidentifikasi potensi kesalahan konfigurasi yang dapat menyebabkan penyalahgunaan API.

Pengujian dilakukan secara manual dan otomatis untuk memastikan apakah sistem benar-benar menerapkan permintaan di sisi backend.

🎯 Tujuan Proyek

Memahami cara kerja rate limiting pada API

Menguji efektivitas permintaan perdagangan

Mengidentifikasi potensi penyalahgunaan API

Memberikan rekomendasi perbaikan keamanan

🛠 Metodologi Pengujian

1️⃣ Manual Pengujian (cURL)

Mengirimkan permintaan berulang dalam waktu singkat

Server respons mengamati

Memeriksa apakah muncul HTTP 429 (Terlalu Banyak Permintaan)

Hasil:
Server tetap merespons 200 OK tanpa bergerak.

2️⃣ Pengujian Otomatis (Skrip Python)

Membuat skrip menggunakan permintaan perpustakaan

Mengirim ±50 permintaan secara cepat

Mencatat kode status dari setiap respon

Hasil:
Tidak ditemukan HTTP 429 atau mekanisme pembatasan backend.

📊 Temuan

Sistem menampilkan batas kecepatan informasi

Tidak terdapat penegakan di sisi backend

Semua permintaan tetap diproses tanpa transaksi

Tidak muncul HTTP 429 (Terlalu Banyak Permintaan)

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Security](https://img.shields.io/badge/Security-Research-red) ![OWASP](https://img.shields.io/badge/OWASP-Aware-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Focus](https://img.shields.io/badge/Focus-API%20Security-critical)
