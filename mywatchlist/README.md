Tautan untuk tugas ini: 
- [mywatchlist](https://tugas2-pbp-afiq.herokuapp.com/mywatchlist)
- [mywatchlist/html](https://tugas2-pbp-afiq.herokuapp.com/mywatchlist/html)
- [mywatchlist/xml](https://tugas2-pbp-afiq.herokuapp.com/mywatchlist/xml)
- [mywatchlist/json](https://tugas2-pbp-afiq.herokuapp.com/mywatchlist/json)

## Perbedaan antara JSON, XML, dan HTML
- JSON (JavaScript Object Notation) adalah suatu *text format* yang *lightweight* untuk menyimpan dan *transporting* data. JSON ditulis dalam notasi object JavaScript dan bersifat *self-describing* sehingga orang yang membacanya secara intuitif dapat mengerti maksudnya. JSON dibangun dengan dasar 2 struktur, yaitu suatu koleksi dari pasangan *name/value* serta suatu *ordered list* dari *values*. 
- XML (eXtensible Markup Language) adalah suatu *markup language* untuk menyimpan dan transportasi data. XML didesain untuk mampu menyimpan data secara ringkas dan mudah diatur. Perbedaan JSON dan XML adalah JSON mengandung *tags* awal dan akhir sedangkan XML tidak, JSON *support* array sedangkan XML tidak, dan JSON lebih mudah dibaca dibanding XML. 
- HTML (HyperText Markup Language) adalah suatu *markup language* untuk menampilkan sesuatu di *browser*. Artinya, kegunaan utama HTML adalah untuk membuat / menyusun tampilan yang ada di browser yang akan dilihat *client*. Walaupun sama-sama *markup language*, terdapat perbedaan mendasar antara HTML dan XML, di mana HTML digunakan untuk menampilkan sesuatu di *browser*, sedangkan XML adalah untuk penyimpanan dan transpor data. 

## Pentingnya data delivery dalam pengimplementasian sebuah *platform*
*Data delivery* penting dalam suatu *platform* sebab untuk mengakses data dari *database* serta melakukan *handling* pertukaran data antara client dan *server* kita tentu memerlukan *data delivery* yang bisa dilakukan dalam bentuk JSON, XML, dan HTML. 

## Pengimplementasian Tugas 3
1. Membuat aplikasi baru bernama `mywatchlist` menggunakan perintah `python manage.py startapp mywatchlist` serta mengaktivan *virtual environment*.
2. Menambahkan *path* `mywatchlist` sehingga http://localhost:8000/mywatchlist dapat diakses dengan cara masuk ke folder `project_django` > `urls.py` lalu pada bagian `urlspatterns` tambahkan `path("mywatchlist/", include("mywatchlist.urls"))`. Kita perlu daftarkan juga aplikasi kita ke `INSTALLED_APPS` pada bagian `settings.py`.
3. Membuat model di `models.py` sesuai dengan spesifikasi yang diminta pada tugas lalu melakukan migrasi.
4. Menambahkan data ke `initial_mywatchlist_data.json` kemudian memasukkan data tersebut ke *database* lokal Django.
5. Membuat file HTML pada folder templates untuk menampilkan data-data yang sudah di-*load* tadi dan tidak lupa juga melakukan *routing*. 
6. Melakukan *deployment* (tidak perlu dilakukan lagi sebab pada minggu-minggu sebelumnya kita sudah men-*deploy*). Kita hanya perlu melakukan `git add`, `commit`, dan `push` pada *repository*. Setelah itu kita perlu sedikit melakukan konfigurasi di Heroku yaitu pada bagian *more*, pilih *run a console* > ketik `bash`. Setelah itu pada terminal yang terbuka tuliskan perintah `python manage.py loaddata initial_watchlist_data.json` untuk me-*load* data.
7. Melakukan *unit test* dengan menambahkan potongan kode berikut pada `tests.py`:
```
class Test(TestCase):
    def test_html(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_mywatchlist"))
        self.assertEquals(response.status_code, 200)

    def test_json(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code, 200)

    def test_xml(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code, 200)
```
kemudian menjalankan perintah untuk melakukan *unit test*.
## Postman
![](https://i.ibb.co/jzf1pZQ/postman-html.png)
![](https://i.ibb.co/vQFhfnv/postman-json.png)
![](https://i.ibb.co/52ZcMxG/postman-xml.png)
