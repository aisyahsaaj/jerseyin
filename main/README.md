Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: 
1. Membuat Proyek Django Baru
Pertama-tama, saya membuat proyek Django baru dengan menjalankan perintah django-admin startproject nama_proyek di terminal. Saya memilih nama yang deskriptif untuk proyek ini yang mencerminkan tujuan aplikasi. Setelah proyek berhasil dibuat, saya masuk ke direktori proyek dan memverifikasi bahwa struktur dasar Django telah terbentuk dengan benar, termasuk file manage.py dan folder proyek utama.

2. Membuat Aplikasi Main
Dalam direktori proyek, saya menjalankan perintah python manage.py startapp main untuk membuat aplikasi baru bernama 'main'. Saya kemudian menambahkan aplikasi ini ke dalam INSTALLED_APPS di file settings.py proyek agar Django mengenali aplikasi main sebagai bagian dari proyek.

3. Routing pada Proyek
Untuk melakukan routing, saya memodifikasi file urls.py pada level proyek. Saya mengimpor fungsi include dari django.urls dan menambahkan path yang mengarahkan URL kosong ('') ke aplikasi main menggunakan include('main.urls'). Ini memastikan bahwa ketika pengguna mengakses root URL, request akan diteruskan ke aplikasi main.

4. Membuat Model Product
Di file models.py aplikasi main, saya mendefinisikan model Product dengan semua atribut yang diperlukan. 

5. Membuat View dan Template
Saya membuat fungsi di views.py yang merender template HTML. Fungsi ini mengambil data dari model Product (jika ada) dan mengirimkannya ke template melalui context. Saya membuat direktori templates dan file HTML yang menampilkan nama aplikasi, data pribadi (nama dan kelas), serta daftar produk yang diambil dari database.

6. Routing pada Aplikasi Main
Saya membuat file urls.py di aplikasi main dan mendefinisikan path yang mengarahkan URL kosong ke fungsi view yang telah dibuat. Ini melengkapi routing dari level proyek ke level aplikasi.

7. Deployment ke PWS
Setelah semua tahap selesai, saya menyimpan perubahan ke GitHub dan memicu deployment otomatis ke PWS dengan menjalankan perintah git add ., git commit -m "pesan commit", dan git push origin main. Setelah itu, saya memeriksa repository GitHub untuk memastikan kode sudah terupdate dan memantau log deployment di dashboard PWS untuk memverifikasi bahwa aplikasi telah terdeploy dengan sukses tanpa error.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
terdapat pada -> images/baganFlowchart


Jelaskan peran settings.py dalam proyek Django!
Jawab : 
Dalam proyek Django, file settings.py berperan sebagai pusat konfigurasi yang mengatur jalannya seluruh aplikasi dalam satu proyek. Di dalamnya terdapat berbagai pengaturan penting, seperti informasi dasar proyek (misalnya SECRET_KEY, DEBUG, dan ALLOWED_HOSTS), daftar aplikasi yang digunakan melalui INSTALLED_APPS, serta konfigurasi database yang menentukan bagaimana Django berinteraksi dengan penyimpanan data. File ini juga mengatur lokasi templatenya.

Bagaimana cara kerja migrasi database di Django?
Jawab:
Migrasi database di Django adalah proses yang memastikan struktur database selalu sesuai dengan model Python yang dibuat dalam aplikasi. Ketika developer menambahkan atau mengubah model pada file models.py, Django tidak langsung mengubah database, melainkan membuat file migrasi menggunakan perintah makemigrations. File migrasi ini berisi instruksi dalam bentuk Python yang menggambarkan perubahan yang harus dilakukan pada database, seperti membuat tabel baru atau menambahkan kolom. Setelah itu, perintah migrate dijalankan untuk menerapkan instruksi tersebut ke database sehingga perubahan model tercermin dalam struktur tabel. Riwayat migrasi ini disimpan pada tabel khusus django_migrations, sehingga Django dapat melacak migrasi mana yang sudah diterapkan dan memungkinkan rollback atau pengaturan versi jika diperlukan. Dengan sistem ini, developer tidak perlu menulis query SQL secara manual, karena Django sudah mengelolanya secara otomatis.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab:
Menurut saya, Django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena framework ini sudah menyediakan banyak fitur bawaan yang lengkap sehingga pemula tidak perlu membangun semuanya dari nol. Django memiliki struktur proyek yang jelas dan teratur, sehingga mahasiswa atau developer baru bisa memahami bagaimana komponen aplikasi saling terhubung, mulai dari model (database), view (logika), hingga template (antarmuka pengguna). Selain itu, Django menggunakan bahasa Python yang relatif mudah dipelajari dan sintaksnya sederhana.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawab:
Menurut saya, tutorial yang diberikan cenderung dirancang agar mahasiswa dapat langsung menyalin kode tanpa benar-benar memahami maksud dari implementasinya. Meskipun sudah ada penjelasan per baris kode, tetap saja sulit bagi mahasiswa untuk sekaligus mengerjakan dan memahami konsep di baliknya. Akan lebih baik jika tutorial disusun dalam bentuk semi-challenge, sehingga mahasiswa terdorong untuk menulis sendiri dan sekaligus memahami maksud dari kode tersebut. Di sisi lain, asisten dosen sudah cukup membantu saya dalam mengerjakan tutorial. Penjelasan yang diberikan juga sudah cukup lengkap dan mudah dipahami.