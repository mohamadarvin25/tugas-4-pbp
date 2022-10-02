## Tautan Aplikasi

Tautan aplikasi Heroku tugas 2 PBP ini dapat dilihat [di sini](https://tugas2-pbp-afiq.herokuapp.com/katalog).

## Bagan dan Kaitan antara *urls*, *views*, *models*, dan berkas HTML 
![Bagan](https://i.ibb.co/Qr3vXR3/bagan-cara-kerja-django.png)

Pertama-tama, Ketika *user* me-*request* sesuatu maka *request* tersebut akan masuk ke server Django dan diproses di `urls.py` di mana di ***urls*** akan dibuat *routing* atau bisa dibilang bagaimana dari *request* tersebut dialihkan ke halaman yang mana yang ada di aplikasi kita. Nah aturan-aturan penanganan *routing* ini diatur di `urls.py`. 

Dari **urls**, permintaan diteruskan di `views.py` di mana di *file* ini terdapat fungsi Python yang mengambil *http request* dan mengembalikan *http response* seperti dokumen HTML. Di bagian ini pula apabila *request* memerlukan *database*, ***views*** dapat memproses hal tersebut dengan memanggil query ke `models.py` dan *database* akan mengembalikan hasil *query* ke ***views*** tadi. 

Setelah segala request diproses, hasilnya akan ditampilkan ke *user* di *browser* dalam bentuk HTML yang didefinisikan di folder *templates*. *Templates* mana yg digunakan tergantung bagaimana *routing* yang kita atur di bagian `urls.py`.

## ***Virtual Environment***

*Virtual environment* adalah “cara” untuk memiliki versi yang berbeda-beda dari Python (bahasa pemrograman yang dipakai Django) di komputer kita tanpa membuat semuanya “bentrok” satu sama lain, sebab ketika kita mengaktifkan *virtual environment* maka tiap versi dapat dianggap sebagai *development environment* dan kita dapat memiliki berbagai versi *environmen*t yang berbeda-beda dan modul-modul di Python terisolasi satu sama lain. 

Mengapa *virtual environment* penting dalam mengembangkan suatu aplikasi Django? Sebab apabila kita sedang mengerjakan suatu *project* yang misalnya menggunakan Django versi 1.5 secara lokal dalam komputer kita, sedangkan di komputer kita ter-*install* Django versi 1.9 untuk *project* lain. Akan sangat susah untuk berkontribusi karena bisa jadi ditemukan *error* karena penggunaan versi yang berbeda. `Virtualenv` meng-*handle* kemungkinan konflik ini dengan mengaktifkan *virtual development environment* terpisah yang tidak terkait satu sama lain. Dengan konsep yang sama, kita dapat memiliki *environment* yang memiliki versi Python yang berbeda!

Kita tetap dapat bisa membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment* tapi bisa jadi versi Django yang kita gunakan akan terpengaruh (bisa ada *error*, dsb) apabila kita mengubah kode kita di *project* lain yang secara langsung berpengaruh pada *project* Django kita.

## Mengimplementasikan Model-View-Template
Pertama kita buat dulu suatu aplikasi Django **katalog** dengan perintah `python manage.py startapp katalog`. Setelah itu pada variabel `INSTALLED_APPS` kita bisa mendaftarkan aplikasi yang kita buat barusan. Kemudian di `models.py` kita *import* class Model dan kita buat *class* CatalogItem lalu kita lakukan migrasi untuk menerapkan skema model yang telah dibuat ke dalam database pada Django lokal kita. Setelah menkonfigurasi model, kita buat fungsi di `views.py` pada folder **katalog**, misalnya bernama **show_katalog** yang mempunyai parameter *request* yang mengembalikan `render(request, ‘katalog.html’, context)`. `katalog.html` inilah yang akan kita tampilkan apabila *user* melakukan *request* ke *server* Django. Setelah itu kita perlu buat `katalog.html` yang kita taruh pada folder **templates** di dalam folder aplikasi **katalog**. Setelah itu kita perlu melakukan *routing* terhadap fungsi yang ada di `views.py` agar dokumen HTML dapat ditampilkan. Pada bagian variable `urlpatterns` kita masukkan fungsi kita tadi yang bernama `show_katalog`. Kita juga perlu daftarkan aplikasi katalog ke `urls.py` pada folder **project_django** dengan menambahkan kode `path('wishlist/', include(katalog.urls')),`.

Untuk melakukan pemetaan data *template*, kita perlu *import* models yang dibuat di `models.py` ke `views.py`, di mana kita akan menggunakan *class* yang kita definisikan sebelumnya untuk melakukan transaksi data dari *database*. Dalam hal ini, kita perlu menambahkan kode 
```from wishlist.models import CatalogItem
from django.shortcuts import render
``` 
Lalu jangan lupa di dalam fungsi `show_katalog` kita tambahkan kode
```
'list_barang': data_barang_katalog,
'nama': ‘Afiq Ilyasa Akmal’
```
yang berfungsi memanggil fungsi *query* ke model *databas* dan menyimpannya ke suatu variabee `list_barang`. Tambahkan parameter `context` dimana data pada variabel `context` akan dirender oleh Django yang bisa nantinya kita tampilkan di halaman HTML. Pada tahap ini, kita sudah melakukan pemetaan data ke dalam HTML. Selanjutnya kita bisa mengatur *file* dalam folder template tadi untuk menampilkan data yang kita punya. 

Setelah sampai tahap ini, kita sudah mengimplementasikan konsep MVT Django pada *repository* kita. Tahap terakhir adalah melakukan *deployment* ke Heroku.

Pertama kita buat app dulu di Heroku kemudian catat *key API* nya. Kemudian kita ke bagian **Settings** > **Secret** > **Actions** lalu kita buat 2 *repository secret* yaitu `HEROKU_API_KEY` yang berisi *key API* tadi dan `HEROKU_APP_NAME` yang berisi nama aplikasi Heroku yang kita buat. Kemudian pada Github kita ke bagian **Actions** > lalu jalankan ulang *workflow*. Setelah proses *running* pada *workflow* berhasil, aplikasi kita telah berhasil di-*deploy* ke Heroku.  
