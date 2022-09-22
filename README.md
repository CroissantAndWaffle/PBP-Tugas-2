## Link Heroku
- https://tombomb.herokuapp.com/
- https://tombomb.herokuapp.com/mywatchlist

## Perbedaan antara JSON, XML, dan HTML
JSON
- Berdasarkan bahasa JavaScript.
- Merupakan cara untuk merepresentasi objek-objek yang ada.
- Dapat menggunakan array.
- Lebih mudah dibaca dari XML.
- tidak memakai end tag.
- Hanya bisa memakai encoding UTF-8

XML
- Sebuah Extensible markup language yang merupakan turunan dari SGML.
- Menggunakan tag untuk merepresentasikan item.
- Dapat menggunakan namespaces.
- Memakai start dan end tag.
- Lebih aman dari JSON.
- Dapat menulis comment.
- Dapat memakai berbagai macam encoding.

HTML
- Merupakan markup language.
- Digunakan untuk display pada web browser.
- Elemen HTML adalah pembangun laman HTML.
- Mendeskripsikan struktur web page secara semantik.
- Menggunakan start tag dan end tag.
- Memiliki atribut yang menyediakan informasi tambahan dari sebuah tag.

## Data delivery dalam implementasi sebuah platform
Data delivery diperlukan agar server dapat merespon suatu request dengan data dan tampilan yang ingin ditampilkan oleh pemilik server. Data delivery terdiri dari banyak bentuk, contohnya HTML, CSS, JavaScript, dll.

## Langkah Implementasi
1. Membuat app baru dengan startapp, serta menambahkan mywatchlist dalam INSTALLED_APPS pada settings.py
2. Menambahkan path yang nantinya dapat diakses pada urls.py pada folder app mywatchlist dan urls.py pada folder project.
3. Membuat class pada models.py yang memiliki atribut sesuai soal.
4. Membuat file HTML untuk tampilan web.
5. Membuat file JSON berisi data untuk objek Mywatchlist dan mengirimkan data ke HTML.
6. Menambahkan fungsi pada views.py yang dapat menampilkan format HTML,XML,dan JSON.
7. Membuat routing pada urls.py untuk fungsi yang sudah dibuat pada views.py
8. Melakukan deployment ke Heroku

## Postman
HTML
![Screenshot (29)](https://user-images.githubusercontent.com/112454640/191654393-cc280721-0639-418c-a1b1-6f7cbd265351.png)

XML
![Screenshot (30)](https://user-images.githubusercontent.com/112454640/191654404-3af76f5f-5c10-4b5d-9455-1d0f971e349e.png)

JSON
![Screenshot (31)](https://user-images.githubusercontent.com/112454640/191654411-a6f181f8-37f9-4616-8c25-d52ee9959f8a.png)

## Refrensi
- https://www.geeksforgeeks.org/difference-between-json-and-xml/
- https://learning.postman.com/docs/getting-started/sending-the-first-request/