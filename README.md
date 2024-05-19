
# Nofijak

![logo](./assets/icon.png)

Sebuah aplikasi untuk memudahkan menonton film

## Daftar Isi

- [Deskripsi Singkat](#deskripsi-singkat)
- [Cara menjalankan Aplikasi](#cara-menjalankan-aplikasi)
- [Daftar Modul](#daftar-modul)
- [Daftar Tabel Basisdata](#daftar-tabel-basisdata)

## Deskripsi Singkat

Aplikasi ini dirancang untuk penggemar film dan serial yang sering menonton konten secara bajakan dan mengalami kesulitan melacak progress menonton mereka. Aplikasi ini ringan, berjalan secara lokal tanpa memerlukan koneksi internet, menghemat storage perangkat dan kuota internet. Fitur utamanya mencakup pelacakan progress menonton, di mana pengguna dapat menandai film atau serial sebagai ongoing dan melanjutkan dari titik terakhir yang ditonton. Pengguna juga dapat menyimpan manual menit yang telah ditonton untuk memastikan progress tidak hilang. Selain itu, terdapat fitur watchlist untuk menambahkan konten yang ingin ditonton di masa mendatang, lengkap dengan sinopsis, gambar, dan genre. Pengguna dapat memberikan rating setelah menyelesaikan menonton, serta mengurutkan dan memfilter konten berdasarkan rating dan genre untuk menemukan preferensi mereka dengan mudah. Fitur tambahan memungkinkan pengguna menghapus film dari watchlist dan menghentikan tanda ongoing untuk menjaga daftar tetap terorganisir dan up-to-date. Aplikasi ini bertujuan memberikan pengalaman menonton yang lebih teratur, terorganisir, dan menyenangkan.

## Cara menjalankan Aplikasi 

### Prasyarat
pastikan anda mempunyai python versi 3.7 atau yang lebih baru

(download python disini jika anda belum punya python)

```
https://www.python.org/downloads/
```

### menjalankan aplikasi

clone repository ini 
```
git clone https://gitlab.informatika.org/alandmprtma/if2250-2024-k03-g06-nofijak.git
```

Install dependencies
```
pip install -r requirements.txt
```

pastikan anda berada pada root directory 

```
...\if2250-2024-k03-g06-nofijak>
```

ubah directory ke src
```
cd src
```
Jalankan program menggunakan flet
```
flet run nofijak.py
```

## Daftar Modul

- [Modul 1 : Modul Halaman All / Watchlist / Ongoing / Completed](#modul-1--modul-halaman-all--watchlist--ongoing--completed)
- [Modul 2 : Modul Halaman Informasi Film/Series](#modul-2--modul-halaman-informasi-filmseries)
- [Pembagian Tugas](#pembagian-tugas)

### Modul 1 : Modul Halaman All / Watchlist / Ongoing / Completed

Modul ini berisi halaman utama untuk aplikasi Nofijak

![Gambar All Entries Main Page](tests/All%20entries%20main%20page.png)
![Gambar Watchlist Main Page](tests/watchlist%20main%20page.png)
![Gambar Ongoing Main Page](tests/ongoing%20main%20page.png)
![Gambar Completed Main Page](tests/completed%20main%20page.png)

### Modul 2 : Modul Halaman Informasi Film/Series

Modul ini berisi halaman mengenai informasi film atau series

![Gambar Information Film](tests/Information%20Film.png)
![Gambar Information Series](tests/Information%20Series.png)
![Gambar Add Movies](tests/add%20Movies.png)
![Gambar Edit Movies](tests/edit%20Movies.png)
![Gambar Add Series](tests/add%20Series.png)
![Gambar Edit Series](tests/edit%20Series.png)

### Pembagian Tugas

| Tugas | Nama  | NIM |
|-------|-------|-----|
| All Entries                                           | Aland Mulia Pratama | 13522124 |
| Watchlists, Ongoing, Completed, Informasi film/series | Muhammad Rasheed Qais Tandjung | 13522158 | 
| Tambah film/series                                    | Muhammad Dzaki Arta    | 13522149 |
| Edit Informasi film/series                            | Rizqika Mulia Pratama | 13522126 | 
| Database Aplikasi                                     | Ikhwan Al Hakim | 13522147 | 


## Daftar Tabel Basisdata

1. [Tabel dan Atribut](#tabel-dan-atribut)
    - [Tabel 1: finished_movies](#tabel-1-finished_movies)
    - [Tabel 2: finished_series](#tabel-2-finished_series)
    - [Tabel 3: movies](#tabel-3-movies)
    - [Tabel 4: ongoing_movies](#tabel-4-ongoing_movies)
    - [Tabel 5: ongoing_series](#tabel-5-ongoing_series)
    - [Tabel 6: review_movies](#tabel-6-review_movies)
    - [Tabel 7: review_series](#tabel-7-review_series)
    - [Tabel 8: series](#tabel-8-series)
    - [Tabel 9: watchlist_movies](#tabel-9-watchlist_movies)
    - [Tabel 10: watchlist_series](#tabel-10-watchlist_series)
2. [Hubungan Antar Tabel](#hubungan-antar-tabel)
3. [Catatan](#catatan)

## Tabel dan Atribut

### Tabel 1: finished_movies

Tabel ini berisi data film yang sudah di tonton 

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
| movies_id     | INT           | Primary Key, Auto Increment          |
| finished_date | date          | Tanggal selesai menonton	       |

### Tabel 2: finished_series

Tabel ini berisi data series yang sudah ditonton

| Atribut       | Tipe Data     | Keterangan               |
|---------------|---------------|-------------------------------|
| series_id     | INT           | Foreign Key			|
| finished_date | date          | Tanggal selesai menonton	|

### Tabel 3: movies

Tabel ini berisi seluruh data film

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
| movies_id     | INT           | Primary Key, Auto Increment          |
| name          | VARCHAR(255)  | Nama film                            |
| duration      | INT		| durasi film                          |
| release_year  | INT 		| Tahun film dirilis                   |
| genre         | VARCHAR(255)  | genre dari film                      |
| synopsis	| VARCHAR(255)  | berisi synopsis dari film            |

### Tabel 4: ongoing_movies

Tabel ini berisi data film yang sedang ditonton 

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
|movies_id	| INT		| Foreign Key untuk movies_id		|
| watched_duration | INT 	| berisi durasi film 			|

### Tabel 5: ongoing_series

Table ini berisi data series yang sedang ditonton 

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
| series_id 	| INT		| Foreign Key untuk series_id		|
| season_progress | INT 	| berisi season terakhir yang sedang ditonton |
| episode_progress | INT 	| berisi episode terakhir yang sedang ditonton |
| watched_duration | INT 	| beriis durasi episode series yang terakhir ditonton | 

### Tabel 6: review_movies

Tabel in berisi data review film 

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
| movies_id 	| INT		| Foreign Key ke movies_id		|
| rating	| INT 		| berisi rating film nilai dari 1 sampai 10 |

### Tabel 7: review_series

Table ini berisi data review series

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
| series_id 	| INT 		| Foreign Key ke series_id	|
| rating 	| INT 		| berisi rating film nilai dari 1 sampai 10 |
| review 	| text		| berisi review dari pengguna 	|

### Tabel 8: series

Tabel ini berisi seluruh data series

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
| series_id 	| INT 		| Primary Key Auto Increment		|
| name		| VARCHAR(100)	| Berisi nama dari series		|
| duration 	| INT 		| Berisi durasi dari series	|
| release_year  | INT		| Berisi tahun rilis dari series	|
| genre 	| VARCHAR(30)   | Berisi genre dari series		|
| synopsis 	| text 		| Berisi dari  synopsis series 		|
| season 	| INT 		| berisi banyak season dari series	|
| episode 	| INT 		| Berisi banyak episode dari series |

### Tabel 9: watchlist_movies

Tabel ini berisi data watchlist film

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
| movies_id 	| INT 		| Foreign Key ke movies_id pada table movies |

### Tabel 10: watchlist_series

Tabel ini berisi data watchlist series

| Atribut       | Tipe Data     | Keterangan                           |
|---------------|---------------|--------------------------------------|
| series_id 	| INT 		| Foreign Key series_id pada table series |

## Hubungan Antar Tabel

- **finished_movies.movies_id** berhubungan dengan **movies.movies_id**
- **finished_series.series_id** berhubungan dengan **series.series_id**
- **ongoing_movies.movies_id** berhubungan dengan **movies.movies_id**
- **ongoing_series.series_id** berhubungan dengan **series.series_id**
- **review_movies.movies_id** berhubungan dengan **movies.movies_id**
- **review_series.series_id** berhubungan dengan **series.series_id**
- **watchlist_movies.movies_id** berhubungan dengan **movies.movies_id**
- **watchlist_series.series_id** berhubungan dengan **series.series_id**

---