## Link Heroku
- https://tombomb.herokuapp.com/
- https://tombomb.herokuapp.com/katalog

## Bagan Django
![Flowcharts](https://user-images.githubusercontent.com/112454640/190055568-c12a6e4e-5eef-4262-97fe-f596811c2d84.svg)
- URLs
urls.py bertugas untuk mengalihkan permintaan dari HTTP kepada view yang sesuai dengan url yang diminta.
- View
views.py akan menerima permintaan dari HTTP dan akan mengembalikan respon sesuai permintaan dari HTTP tersebut. views.py juga mengakses model dan template untuk memenuhi permintaan HTTP.
- Models
models.py akan menyediakan suatu mekanisme untuk mengelola dan meminta query dalam suatu database
- Template
Template yang biasanya merupakan file HTML (tidak harus) akan membuat struktur atau layout yang akan merepresentasikan konten yang ingin ditampilkan.

## Manfaat Virtual Environment
- Dapat mengakomodasi banyak versi dari python. Jadi saat implementasi dengan python dapat memiliki versi python yang berbeda-beda dimana mereka semua tidak akan bercampur satu sama lain.
- Dapat mengakomodasi versi django yang berbeda-beda, terutama saat bekerja secara berkelompok tentu lebih baik menggunakan versi django yang sama agar tidak banyak error dan lebih mudah saat proses debugging. Dengan adanya virtual environment kita tak perlu untuk downgrade django untuk menyamai versi yang dimiliki oleh teman sekelompok.

## Langkah Implementasi
1. Membuat fungsi pada views.py yang berisi data yang ingin ditampilkan dengan mengimport data dari model.
2. Membuat routing pada urls.py dengan mengimport fungsi dari views.py.
3. Memetakan data yang sudah ada, pada file HTML dengan syntax {{}}.
4. Membuat migrasi dan loaddata agar dapat dicoba pada server local terlebih dahulu sebelum di deploy.
5. Mendeploy ke heroku melalui github.

## Refrensi
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction
- https://www.parallels.com/blogs/ras/virtual-machine/#:~:text=Portability.,%2C%20making%20them%20hardware%2Dindependent.