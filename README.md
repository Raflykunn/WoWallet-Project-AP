# WoWallet by AP-06

## Deskripsi Singkat

**WoWallet** adalah aplikasi berbasis Python (CLI) yang dirancang untuk membantu pengelolaan kasir digital sederhana. Aplikasi ini menyediakan fitur login berbasis peran (Admin dan Kasir), manajemen produk, transaksi penjualan, laporan harian, serta dashboard profit.

Dikembangkan oleh Kelompok AP-06 dari kelas Bisnis, WoWallet bertujuan untuk memberikan solusi efisien dan praktis dalam pengelolaan usaha kecil hingga menengah.

## Tujuan

Proyek WoWallet bertujuan untuk mempermudah pengguna, baik admin maupun kasir, dalam mencatat transaksi penjualan secara cepat, akurat, dan efisien. Aplikasi ini juga dirancang untuk membantu pengelolaan stok produk dan harga melalui sistem CRUD sederhana yang mudah digunakan. Selain itu, WoWallet menampilkan laporan harian serta dashboard keuntungan yang berfungsi untuk memantau performa bisnis secara menyeluruh. Tidak hanya itu, sistem ini juga dilengkapi dengan fitur peringatan (alert) yang memberikan notifikasi ketika stok produk menipis dan mendeteksi produk dengan profit terkecil, sehingga pengambilan keputusan dapat dilakukan dengan lebih cepat dan tepat.

## Fitur Utama

1. **Inisialisasi Aplikasi dan Utilitas Umum**  
   Bertanggung jawab untuk menyiapkan file data awal dan menyediakan fungsi-fungsi utilitas dasar seperti membaca/menulis JSON dan mendapatkan waktu saat ini.

2. **Otentikasi Pengguna**  
   Menangani proses login pengguna (Admin/Kasir).

3. **Manajemen Produk**  
   Memungkinkan Admin untuk menambah, melihat, mengedit, menghapus produk, dan mengelola stok.

4. **Manajemen Transaksi Penjualan**  
   Menangani proses penjualan produk, termasuk mengurangi stok dan mencatat transaksi.

5. **Laporan dan Dashboard**  
   Menyediakan berbagai laporan dan ringkasan data seperti total profit, transaksi hari ini, produk terlaris, dan produk stok menipis.

6. **Antarmuka Menu**  
   Menampilkan menu yang berbeda untuk Admin dan Kasir, serta mengarahkan ke fungsi-fungsi yang sesuai.

7. **Program Utama**  
   Titik masuk utama aplikasi, bertanggung jawab untuk inisialisasi dan mengelola alur login dan pemilihan menu.

## Persyaratan

Untuk menjalankan aplikasi ini, pastikan perangkat Anda memenuhi persyaratan berikut:

- **Python**: Versi terbaru saat ini adalah Python 3.14. Aplikasi ini kompatibel dengan Python 3.x terbaru. Namun, disarankan menggunakan versi Python yang sedang Anda gunakan jika sudah terinstal (minimal Python 3.8 untuk kompatibilitas penuh).
- **Git**: Untuk cloning repository.
- **Visual Studio Code (VSCode)**: Direkomendasikan sebagai editor kode untuk development dan debugging aplikasi ini. Anda dapat mengunduh versi terbaru dari situs resmi Microsoft.

## Cara Menjalankan Program

Untuk menjalankan proyek WoWallet, ikuti langkah-langkah berikut:

1. Pastikan Python dan Git sudah terinstal di perangkat Anda.

2. Clone repository dengan perintah:

   ```
   git clone https://github.com/Raflykunn/WoWallet-Project-AP.git
   ```

3. Masuk ke direktori proyek:

   ```
   cd WoWallet-Project-AP
   ```

4. Jalankan program utama:

   ```
   python main.py
   ```

5. Program akan menampilkan menu utama di terminal. Pilih jenis login sesuai peran pengguna:

   - **Admin**: Untuk mengelola produk, stok, dan melihat laporan penjualan.
   - **Kasir**: Untuk mencatat transaksi penjualan harian.

6. Masukkan username dan password sesuai peran:

   - **Admin**  
     Username: admin  
     Password: adminpass
   - **Kasir**  
     Username: kasir  
     Password: kasirpass

7. Setelah berhasil login, Anda dapat langsung menggunakan fitur WoWallet sesuai peran masing-masing.

## Teknologi yang Digunakan

- **Python 3**: Bahasa pemrograman utama.
- **JSON**: Digunakan untuk menyimpan data pengguna, produk, dan transaksi.

## Kontributor / Tim

1. **Ilham Kurniawan** – Asisten Lab AP-06
2. **Muh. Rafly Nurramadhan (H071251079)** – Kontributor
3. **Syarief Rahmatullah (H071251067)** – Kontributor
4. **Afdhol As Syamardi (H071251049)** – Kontributor
5. **Siti Fatimah Hatta (H071251013)** – Kontributor
6. **Thoriq Muharram (H071251035)** – Kontributor
7. **Muhammad Aiman Amil (H071251071)** - Kontributor
8. **St. Asma Ashikah Hasnawing (H071251003)** - Kontributor

Terima kasih telah menggunakan WoWallet! Jika ada saran atau isu, silakan buka issue di repository GitHub.
