# Most-Streamed-Spotify-Songs-2023

## Proyek Analisis Data: Most Streamed Spotify Songs 2023
Proyek ini bertujuan untuk menganalisis data streaming lagu di Spotify sepanjang tahun 2023. Dengan memanfaatkan dataset dari https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data, saya melakukan beberapa analisis untuk mengidentifikasi tren dan pola yang mungkin berguna bagi penggemar musik, artis, dan industri musik. Analisis ini mencakup identifikasi lagu dan artis dengan jumlah streaming terbanyak, pengaruh bulan terhadap jumlah streaming, serta dampak kolaborasi terhadap popularitas lagu.

Dataset yang digunakan dalam proyek ini berisi informasi mengenai lagu-lagu paling banyak di-streaming di Spotify sepanjang tahun 2023. Data mencakup informasi seperti nama lagu, nama artis, jumlah streaming, dan bulan rilis.

### Langkah-Langkah Analisis
1. Membersihkan Data
   - Menghapus kolom yang tidak diperlukan untuk analisis lebih lanjut.
   - Mengubah tipe data kolom streams menjadi integer untuk memudahkan perhitungan.
   - Menambahkan kolom baru streams_in_million yang merepresentasikan jumlah streaming dalam jutaan.
   - Melakukan pemetaan dari nomor bulan ke nama bulan untuk memudahkan visualisasi.
  
2. Top 10 Lagu dengan Streams Terbanyak
Saya mengelompokkan data berdasarkan nama lagu (track_name) dan menghitung total jumlah streaming. Data ini kemudian diurutkan untuk mendapatkan 10 lagu dengan jumlah streaming terbanyak.

3. Top 10 Artis dengan Streams Terbanyak
Analisis serupa dilakukan pada artis, di mana data dikelompokkan berdasarkan nama artis (artist(s)_name) dan total jumlah streaming dihitung. Saya mengidentifikasi 10 artis dengan jumlah streaming terbanyak.

4. Pengaruh Kolaborasi terhadap Jumlah Streams
Untuk menganalisis dampak kolaborasi terhadap popularitas lagu, saya menyaring data untuk mendapatkan informasi mengenai jumlah artis yang terlibat dalam setiap lagu dan jumlah streamingnya.

5. Pengaruh Bulan terhadap Jumlah Streams
Saya menganalisis bagaimana bulan rilis mempengaruhi jumlah streaming dengan mengelompokkan data berdasarkan bulan rilis dan menghitung total jumlah streaming setiap bulan.

### Visualisasi Data
Saya menggunakan berbagai alat visualisasi seperti Matplotlib, Seaborn, dan Plotly untuk membuat grafik yang menggambarkan temuan utama dari analisis ini. Beberapa visualisasi yang dibuat meliputi:
- Bar chart untuk 10 lagu dengan jumlah streaming terbanyak.
- Bar chart untuk 10 artis dengan jumlah streaming terbanyak.
- Scatter plot untuk melihat pengaruh kolaborasi terhadap jumlah streaming.
- Line chart untuk menggambarkan tren jumlah streaming berdasarkan bulan rilis.

### Teknologi yang Digunakan
- Python untuk analisis data dan scripting.
- Pandas untuk manipulasi dan analisis data.
- Plotly untuk visualisasi interaktif.
- Matplotlib dan Seaborn untuk visualisasi statis.

### Kesimpulan
Proyek ini memberikan wawasan mendalam tentang tren dan pola dalam data streaming Spotify selama tahun 2023. Dengan analisis ini, kita dapat lebih memahami faktor-faktor yang mempengaruhi popularitas lagu dan artis, serta bagaimana kolaborasi dan waktu rilis dapat mempengaruhi jumlah streaming. Proyek ini merupakan contoh bagaimana data musik dapat dianalisis untuk mendapatkan wawasan yang berharga, dan saya berharap dapat memberikan kontribusi positif bagi penelitian dan strategi dalam industri musik.
