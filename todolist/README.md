Tautan tugas 4 ada [di sini](https://tugas2-pbp-afiq.herokuapp.com/todolist/).

## Kegunaaan `{% csrf_token %}` pada elemen `<form>`
CSRF adalah singkatan dari *Cross Site Request Forgery*, semacam *attack* yang memaksa pengguna *end user* untuk melakukan tindakan yang tidak diinginkan pada aplikasi web di mana mereka sudah terautentikasi di aplikasi web tersebut. Contoh kasusnya adalah apabila seorang *developer* membuat penghapusan akun suatu aplikasi tertentu dapat dilakukan melalui GET (seharusnya POST), maka bisa jadi ada orang mengirim sesuatu di aplikasi web kita (asumsi: aplikasi tersebut punya beberapa mekanisme untuk meninggalkan *feedback*) seperti ini:
```
Anda ingin kaya raya. Lihat gambar keren ini!
<img src='http://tugas2-pbp-afiq.herokuapp.com/ingin_kaya_raya_tapi_isinya_buat_ngapus_akun"/>
```
dengan setiap orang/akun yang mengklik gambar di atas, maka akun mereka akan terhapus. Apabila misalnya *malicious attack* ini dilakukan via POST dan bukan GET, bisa saja seseorang membuat *form* yang meminta data-data akun mereka lalu melakukan peretasan.

Apabila kita menggunakan CSRF token, hal semacam ini tidak mungkin terjadi.

## Apakah kita dapat membuat elemen `<form>` secara manual?
Bisa. Kita dapat membuat *form* secara manual melalui HTML dengan memanfaatkan atribut dari `<input>`. Konteks atribut dalam tugas ini adalah atribut `name`. *Value* dari `name` ini bisa diakses menggunakan `request.POST[name]`. Dengan demikian, masukan dari *user* pada *form* yang kita punya dapat diperoleh tanpa menggunakan *generator*.

## Proses alur data dari submisi yang dilakukan oleh pengguna melalui `HTML` *form*
Saat pengguna men-*submit* *task* pada *form* di halaman `create_task`, data akan dikirimkan via *request* POST dan diterima di fungsi `create_task` yang sudah dibuat di *views.py*. Di fungsi tersebut masukan dari *user* diproses dan ditmapung di variabel penampung lalu setelah itu disimpan di *database* menggunakan method `save()`.

## Implementasi pada *checklist*
Pertama, buat app Django baru dengan perintah `startapp` kemudian tambahkan aplikasi **todolist** ini ke INSTALLED_APPS di `settings.py`. Buat model di `models.py` sesuai dengan spesifikasi yang diminta soal lalu lakukan migrasi. 

Kedua, membuat halaman login, registrasi, dan logout sesuai yang ada di perintah lab 3. Lalu dibuat juga halaman create_task yang berisi form yang bersesuaian dengan fungsi create_task yang menerima argumen request dan id di `views.py`. Buat routing di `urls.py` untuk mengarahkan halaman-halaman tadi ke tautan yang sesuai.

Terakhir, melakukan add, commit, dan push ke GitHub kemudian membuat dua `user` dan tiga *dummy data* di kedua user tersebut. 
