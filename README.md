## Link Heroku
- https://tombomb.herokuapp.com/
- https://tombomb.herokuapp.com/todolist

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