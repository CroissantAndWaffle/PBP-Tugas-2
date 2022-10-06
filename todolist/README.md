## Link Heroku
- https://tombomb.herokuapp.com/
- https://tombomb.herokuapp.com/todolist

# Tugas 5
## Inline, Internal, dan External CSS
#### Inline
Menambahkan tag style pada setiap tag html yang ingin di *Styling*. Implementasi sangat susah.

kelebihan:
- Cepat untuk insert CSS, bagus untuk testing.
- Tidak harus membuat dokumen external.

kekurangan:
- Memakan banyak waktu
- Akan mempengaruhi download time dan ukuran page.


#### Internal CSS
Menambahkan tag style pada section head. 

kelebihan:
- Kode sama seperti external CSS, namun tidak perlu membuat file terpisah.

kekurangan:
- Menambahkan waktu loading dan ukuran page


#### Internal CSS
Menambahkan tag style pada section head. 

kelebihan:
- Kode dan ukuran file HTML menjadi lebih bersih dan ukuran file menjadi lebih kecil
- Dapat menggunakan satu file .css yang sama untuk banyak pages.

kekurangan:
- Kadang tidak ter-render sampai file external css ter-load.
- Meng-upload dan me-link banyak file css akan meningkatkan download time pada site.


## Tag HTML5
- Doctype : Menentukan tipe dokumen.
- html : menginformasikan ke website bahwa dokumen berbentuk html.
- head : untuk element element seperti document title, character set, styles, links, scripts.
- body : untuk diisi dengan konten dari dokumen html.
- script : untuk js
- h1-h6 : untuk heading
- nav : untuk navigasi
- style : untuk css


## CSS selector
- #id : Tanda # digunakan untuk select id 
- .class : Tanda . digunakan untuk select class
- elemnt : Tanpa menggunakan tanda pada awal selector

## Implementasi
Mengimplementasikan bootstrap agar mudah dalam mengkustomisasi website yang dibuat pada todolist. Membuat file css pada folder static dan menggunakan implementasi external css agar mudah dalam menerapkan *Styling*. Mengubah warna dan layout agar website lebih enak dipandang. Mengimplementasikan Navbar responsif dengan menggunakan bootstrap pada seluruh dokumen html. Memodifikasi setiap formulir agar enak dilihat. mengimplementasikan card pada todolist dan hover sesuai tugas.

## Refrensi
- https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css
- https://www.w3docs.com/snippets/html/html5-page-structure.html
- https://www.w3schools.com/css/css_selectors.asp



# Tugas 4
## Kegunaan csrf_token
csrf token berguna untuk mencegah serangan *Cross-Site Request Forgery*. csrf adalah sebuah serangan yang membuat seorang user yang sudah terautentikasi pada suatu web melakukan suatu aksi yang diinginkan oleh penyerang. csrf dilakukan dengan link, csrf token akan mencegah hal ini dengan membuat token yang sangat panjang yang hampir tidak mungkin untuk ditebak. Dengan begini, penyerang bukan hanya harus membuat user menggunakan web yang dibuat, melainkan juga harus menebak token yang dibuat oleh csrf token.

## form.as_table
form.as_table akan me-*render* form sebagai *table cells* yang akan dibungkus dengan tag <tr> saat html dieksekusi. Untuk membuat form secara manual gunakan tag <td> dan <tr> pada tiap judul form (jika ada) dan form yang ada dengan begini anda dapat menghasilkan tabel secara manual.

## Alur data
Data yang disubmit oleh user akan disimpan dalam database django sesuai id masing-masing user untuk membedakan antara user satu dan yang lainnya. Saat ingin ditampilkan data akan difilter sesuai dengan id yang tadi tergantung usernya sehingga membedakan satu user dengan yang lain. Setelah di filter data akan ditampilkan pada HTML.

## Implementasi
Buat models sesuai ketentuan soal. Tambahkan fungsi baru pada views seperti register, login, logout, serta fungsi untuk membuat task baru. Jangan lupa modifikasi fungsi yang menampilkan /todolist agar menampilkan sesuai user yang mengakses dan tambahkan keharusan untuk login sebelum membuka data. Buatlah file HTML dari setiap fungsi yang memerlukan tampilan pada web dengan mengimplementasikan form pada HTML. Tambahkan juga fungsi logout untuk dapat mengganti account. Routing semua link ke urls.

## Refrensi
- https://owasp.org/www-community/attacks/csrf
- https://www.geeksforgeeks.org/form-as_table-render-django-forms-as-table/