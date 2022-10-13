# Asynchronous programming dan Synchronous programming
Sinkronus: setiap ada request user akan menunggu respon dari server untuk menampilkan request. Harus melakukan refresh.
Asinkronus: Server akan mengirim data secara parsial sehingga tidak memerlukan refresh, Jadi saat menunggu request dijawab oleh server user tetap bisa menggunakan web.

# Event-Driven Programming
paradigma di mana entitas (objek, layanan, dan sebagainya) berkomunikasi secara tidak langsung dengan mengirimkan pesan satu sama lain melalui perantara. Pesan biasanya disimpan dalam antrian sebelum ditangani oleh konsumen.
Pada tugas ini ada button yang dapat dihandle dengan submit atau click.

# Asynchronous programming pada AJAX
Dalam ajax penerapan pemrograman asinkronus dapat memakai keyword async pada suatu function dan juga dapat menggunakan jquery.

# Implementasi
1. Membuat view yang mengembalikan data dalam bentuk json dengan url tertentu.
2. Mengambil json dengan ajax get pada js
3. Membuat modal yang akan digunakan untuk add task
4. Membuat path todolist/add dan mengarahkan post ke todolist/add
5. Memakai jquery untuk implementasi js agar dapat menjadi asinkronus

# Refrensi
- https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/#:~:text=Asynchronous%20programming%20is%20the%20multitasker,time%20in%20a%20rigid%20sequence.
- https://aiven.io/blog/introduction-to-event-based-programming