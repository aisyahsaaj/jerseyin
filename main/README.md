====== Tugas Individu 2 ======
1) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: 
a. Membuat Proyek Django Baru
Pertama-tama, saya membuat proyek Django baru dengan menjalankan perintah django-admin startproject nama_proyek di terminal. Saya memilih nama yang deskriptif untuk proyek ini yang mencerminkan tujuan aplikasi. Setelah proyek berhasil dibuat, saya masuk ke direktori proyek dan memverifikasi bahwa struktur dasar Django telah terbentuk dengan benar, termasuk file manage.py dan folder proyek utama.

b. Membuat Aplikasi Main
Dalam direktori proyek, saya menjalankan perintah python manage.py startapp main untuk membuat aplikasi baru bernama 'main'. Saya kemudian menambahkan aplikasi ini ke dalam INSTALLED_APPS di file settings.py proyek agar Django mengenali aplikasi main sebagai bagian dari proyek.

c. Routing pada Proyek
Untuk melakukan routing, saya memodifikasi file urls.py pada level proyek. Saya mengimpor fungsi include dari django.urls dan menambahkan path yang mengarahkan URL kosong ('') ke aplikasi main menggunakan include('main.urls'). Ini memastikan bahwa ketika pengguna mengakses root URL, request akan diteruskan ke aplikasi main.

d. Membuat Model Product
Di file models.py aplikasi main, saya mendefinisikan model Product dengan semua atribut yang diperlukan. 

e. Membuat View dan Template
Saya membuat fungsi di views.py yang merender template HTML. Fungsi ini mengambil data dari model Product (jika ada) dan mengirimkannya ke template melalui context. Saya membuat direktori templates dan file HTML yang menampilkan nama aplikasi, data pribadi (nama dan kelas), serta daftar produk yang diambil dari database.

f. Routing pada Aplikasi Main
Saya membuat file urls.py di aplikasi main dan mendefinisikan path yang mengarahkan URL kosong ke fungsi view yang telah dibuat. Ini melengkapi routing dari level proyek ke level aplikasi.

g. Deployment ke PWS
Setelah semua tahap selesai, saya menyimpan perubahan ke GitHub dan memicu deployment otomatis ke PWS dengan menjalankan perintah git add ., git commit -m "pesan commit", dan git push origin main. Setelah itu, saya memeriksa repository GitHub untuk memastikan kode sudah terupdate dan memantau log deployment di dashboard PWS untuk memverifikasi bahwa aplikasi telah terdeploy dengan sukses tanpa error.

2) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
terdapat pada -> images/baganFlowchart


3) Jelaskan peran settings.py dalam proyek Django!
Jawab : 
Dalam proyek Django, file settings.py berperan sebagai pusat konfigurasi yang mengatur jalannya seluruh aplikasi dalam satu proyek. Di dalamnya terdapat berbagai pengaturan penting, seperti informasi dasar proyek (misalnya SECRET_KEY, DEBUG, dan ALLOWED_HOSTS), daftar aplikasi yang digunakan melalui INSTALLED_APPS, serta konfigurasi database yang menentukan bagaimana Django berinteraksi dengan penyimpanan data. File ini juga mengatur lokasi templatenya.

4) Bagaimana cara kerja migrasi database di Django?
Jawab:
Migrasi database di Django adalah proses yang memastikan struktur database selalu sesuai dengan model Python yang dibuat dalam aplikasi. Ketika developer menambahkan atau mengubah model pada file models.py, Django tidak langsung mengubah database, melainkan membuat file migrasi menggunakan perintah makemigrations. File migrasi ini berisi instruksi dalam bentuk Python yang menggambarkan perubahan yang harus dilakukan pada database, seperti membuat tabel baru atau menambahkan kolom. Setelah itu, perintah migrate dijalankan untuk menerapkan instruksi tersebut ke database sehingga perubahan model tercermin dalam struktur tabel. Riwayat migrasi ini disimpan pada tabel khusus django_migrations, sehingga Django dapat melacak migrasi mana yang sudah diterapkan dan memungkinkan rollback atau pengaturan versi jika diperlukan. Dengan sistem ini, developer tidak perlu menulis query SQL secara manual, karena Django sudah mengelolanya secara otomatis.

5) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab:
Menurut saya, Django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena framework ini sudah menyediakan banyak fitur bawaan yang lengkap sehingga pemula tidak perlu membangun semuanya dari nol. Django memiliki struktur proyek yang jelas dan teratur, sehingga mahasiswa atau developer baru bisa memahami bagaimana komponen aplikasi saling terhubung, mulai dari model (database), view (logika), hingga template (antarmuka pengguna). Selain itu, Django menggunakan bahasa Python yang relatif mudah dipelajari dan sintaksnya sederhana.

6) Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawab:
Menurut saya, tutorial yang diberikan cenderung dirancang agar mahasiswa dapat langsung menyalin kode tanpa benar-benar memahami maksud dari implementasinya. Meskipun sudah ada penjelasan per baris kode, tetap saja sulit bagi mahasiswa untuk sekaligus mengerjakan dan memahami konsep di baliknya. Akan lebih baik jika tutorial disusun dalam bentuk semi-challenge, sehingga mahasiswa terdorong untuk menulis sendiri dan sekaligus memahami maksud dari kode tersebut. Di sisi lain, asisten dosen sudah cukup membantu saya dalam mengerjakan tutorial. Penjelasan yang diberikan juga sudah cukup lengkap dan mudah dipahami.


====== TUGAS INDIVIDU 3 ======
1) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
jawab: 
Dalam pengimplementasian sebuah platform, kita memerlukan data delivery karena platform modern pada hakikatnya adalah kumpulan dari berbagai komponen atau "stack" yang terpisah, seperti frontend, backend, dan database, yang harus bekerja sama secara kohesif. Tanpa aliran data, tiap komponen tidak dapat saling sinkron. Data delivery berfungsi sebagai jembatan yang menghubungkan seluruh stack, sehingga data dari sumber (server atau basis data) dapat sampai ke pengguna akhir melalui antarmuka aplikasi, atau diteruskan ke sistem lain yang membutuhkannya. Format seperti HTML, XML, dan JSON membantu agar data bisa ditransfer dan dipahami dengan standar yang sama, sehingga aplikasi berbeda tetap bisa berkomunikasi.

2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
jawab: 
Menurut saya, JSON lebih baik dibandingkan XML. JSON lebih mudah dibaca oleh manusia dan mesin karena tidak menggunakan tag seperti XML, selain itu JSON cenderung menghasilkan ukuran file yang lebih kecil, sehingga transfer data lebih cepat dan efisien. JSON juga lebih aman dalam penguraian data dibanding XML, yang rentan terhadap beberapa risiko seperti injeksi entitas eksternal (XXE). Mungkin itu juga yang membuat JSON lebih populer karena dalam pengiriman data dalam aplikasi modern JSON lebih ringan, cepat, dan mudah digunakan dibanding XML yang lebih berat dan kompleks. Namun, XML masih digunakan ketika diperlukan struktur data yang sangat terperinci dan validasi yang kuat.

3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
jawab:
fungsi dari method is_valid() adalah untuk memvalidasi semua data yang ada di dalam form Django. Method ini akan melakukan serangkaian pengecekan untuk memastikan bahwa data yang diinput oleh user memenuhi semua aturan yang telah ditentukan untuk setiap field di dalam form tersebut.
Cara kerjanya dimulai dari membersihkan data dengan mengubah data mentah yang berasal dari request (biasanya string) ke dalam tipe data Python yang sesuai. Selanjutnya Django menjalankan semua validator bawaan dan kustom pada setiap field. Jika ada data yang tidak valid, Django akan mengumpulkan semua error tersebut dan menyimpannya di dalam atribut form.errors. Jika semua data valid, is_valid() akan mengembalikan True. Jika ada satu saja yang salah, akan mengembalikan False. Jadi alasan kita sangat membutuhkan method ini adalah untuk menjamin integritas dan keamanan data yang masuk ke dalam aplikasi dan database kita.

4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
jawab:
CSRF token diperlukan saat membuat form di Django untuk melindungi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah serangan di mana penyerang memanfaatkan sesi login pengguna yang sudah terautentikasi untuk melakukan aksi tanpa sepengetahuan pengguna, misalnya mengirim permintaan berbahaya melalui form palsu yang dibuat di situs lain. Fungsi CSRF token adalah untuk memberikan token unik dan acak yang disisipkan ke dalam form sebagai hidden input. Token ini kemudian diverifikasi oleh server saat form dikirim untuk memastikan permintaan berasal dari pengguna yang sah, bukan dari sumber eksternal yang berbahaya. Jika token tidak ada atau tidak cocok, Django akan menolak permintaan tersebut dengan error 403.
Jika CSRF token tidak ditambahkan pada form Django, maka aplikasi rentan terhadap serangan CSRF. Penyerang bisa membuat form palsu di situs lain yang ketika dikirim akan memicu aksi di aplikasi Django menggunakan sesi login korban, misalnya mengubah data, melakukan transaksi, atau aksi berbahaya lainnya tanpa izin pengguna.

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
jawab:
Langkah pertama yang saya lakukan adalah masuk ke direktori project menggunakan perintah cd + path, lalu mengaktifkan virtual environment. Setelah itu saya memastikan konfigurasi TEMPLATES di settings.py sudah benar agar Django dapat membaca file HTML dari folder templates. Saya kemudian membuat folder main/templates/ dan menambahkan base.html sebagai template utama. Selanjutnya saya membuat forms.py yang berisi ProductForm berbasis ModelForm untuk menerima input produk sesuai field yang ada di models.py. Pada views.py, saya menambahkan fungsi show_main untuk menampilkan daftar produk, create_product untuk menambahkan produk baru, dan show_product untuk menampilkan detail produk sekaligus memanggil method increment_views agar jumlah view bertambah. Semua fungsi ini kemudian saya daftarkan di urls.py dengan path yang sesuai. Untuk mendukung tampilan, saya membuat tiga file HTML: main.html untuk daftar produk dengan tombol Add dan Detail, create_product.html untuk form input produk yang dilindungi csrf_token, serta product_detail.html untuk menampilkan detail tiap produk. Setelah komponen HTML berjalan, saya menambahkan fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id di views.py dengan bantuan HttpResponse dan serializers agar data bisa di-deliver dalam format XML maupun JSON, baik untuk seluruh objek maupun berdasarkan ID tertentu. Fungsi-fungsi ini juga saya daftarkan pada urls.py. Untuk menguji hasilnya, saya menjalankan server dengan python manage.py runserver lalu mengakses endpoint di localhost dan juga menggunakan Postman untuk memastikan data dapat ditampilkan sesuai format. Terakhir, saya melakukan dokumentasi hasil pengujian di Postman sebelum melakukan add-commit-push ke GitHub dan PWS.

6) Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
jawab:
Menurut saya tutorial 2 lebih mudah untuk dipahami sekaligus diimplementasikan, karena dirancang agar kami ikut aktif menuliskan kode secara langsung, contohnya saat membuat fungsi baru JSON dan XML. Selain itu, asdos juga cukup membantu saya ketika mengalami kendala dalam mengerjakan tutorial sehingga proses belajar terasa lebih lancar.

bukti screenshot ada di dalam folder images

====== TUGAS INDIVIDU 4 ======
1) Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
jawab:
AuthenticationForm adalah form bawaan Django yang disediakan oleh modul django.contrib.auth.forms. Form ini digunakan untuk autentikasi pengguna (login) dengan cara memverifikasi username dan password terhadap data yang ada di database.
Secara default, AuthenticationForm berisi dua field utama, yaitu username dan password.
Saat dipanggil di view, form ini akan memvalidasi input (apakah user ada, apakah password benar), lalu menghasilkan objek User jika autentikasi berhasil, atau menyediakan error message jika login gagal. 
kelebihannya kita tidak perlu membuat form login dari nol, karena sudah built-indan siap pakai (sudah ada validasi dasar juga). selain itu ini juga sudah terintegrasi dengan sistem auth django, jadi langsung terhubung dengan backend autentikasi Django. namun disisi lain, form ini memiliki keterbatasan pada field yang digunakan (secara default hanya mendukung login dengan username). selain itu tampilannya juga sederhana, sehingga perlu CSS/Bootstrap/dsb untuk settingan tampilan yang lebih advanced.

2) Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?
jawab:
Autentikasi dan otorisasi adalah dua konsep yang berbeda namun saling melengkapi dalam keamanan aplikasi. Autentikasi adalah proses memverifikasi identitas pengguna, misalnya melalui username dan password, atau metode lain seperti login via Google. Sementara itu, otorisasi adalah proses menentukan apa yang boleh dilakukan oleh pengguna setelah identitasnya terverifikasi, misalnya apakah seorang pengguna hanya bisa membaca data atau juga dapat menghapusnya.
Django mengimplementasikan autentikasi melalui sistem bawaan django.contrib.auth, yang menyediakan form, view, dan fungsi seperti authenticate(), login(), dan logout() untuk menangani login serta manajemen sesi pengguna. Untuk otorisasi, Django menyediakan sistem permission dan group, di mana setiap model otomatis memiliki izin dasar (add, change, delete, view) dan developer dapat menambahkan izin khusus sesuai kebutuhan. terdapat juga decorator seperti @login_required untuk memastikan hanya pengguna yang sudah login yang bisa mengakses halaman tersebut.  

3) Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
jawab: 
a) session:
menyimpan data di sisi server sementara browser hanya menyimpan session ID, biasanya melalui cookie bernama sessionid. Hal ini membuat sessions lebih aman, fleksibel dalam menyimpan data berukuran besar, dan mudah dikontrol oleh server, misalnya untuk mengatur masa berlaku atau memaksa logout. Kekurangannya, sessions membebani server karena harus mengelola banyak data user secara bersamaan, serta tetap membutuhkan cookie atau mekanisme lain untuk menghubungkan request dengan session yang benar.
b) cookies:
disimpan di sisi client (browser) sehingga sederhana digunakan, dapat bertahan meskipun browser ditutup, dan bisa diakses langsung oleh JavaScript, sehingga cocok untuk menyimpan preferensi ringan seperti bahasa atau tema. Namun, cookies memiliki ukuran terbatas, selalu terkirim di setiap request sehingga menambah beban jaringan, serta lebih rentan terhadap manipulasi atau pencurian data jika tidak diamankan.

4) Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
jawab:
secara default tidak sepenuhnya aman. Cookies bisa dicuri lewat serangan XSS (Cross-Site Scripting) jika attacker berhasil menyisipkan script berbahaya yang membaca cookie. Selain itu, cookies dapat dimanipulasi pengguna karena tersimpan di sisi client, sehingga data sensitif tidak boleh langsung disimpan di dalamnya. Risiko lain adalah session hijacking atau pencurian cookie session melalui serangan MITM (Man-in-the-Middle) jika cookie dikirim lewat koneksi yang tidak dienkripsi.
Untuk mengurangi risiko ini, Django menerapkan beberapa mekanisme pengamanan pada cookies secara default. Misalnya, Django menyimpan data sensitif (seperti informasi login) di server-side session, bukan di cookie langsung — cookie hanya berisi session ID acak. Django juga menyediakan opsi konfigurasi keamanan, seperti SESSION_COOKIE_HTTPONLY=True (mencegah akses JavaScript ke cookie), SESSION_COOKIE_SECURE=True (cookie hanya dikirim melalui HTTPS), dan SESSION_COOKIE_SAMESITE='Lax' atau 'Strict' (mencegah pengiriman cookie lintas situs yang bisa dimanfaatkan dalam serangan CSRF). 

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
jawab:
Seperti biasa, saya membuka terminal pada direktori proyek dan mengaktifkan virtual environment. Setelah itu, saya mulai mengimplementasikan fungsi registrasi, login, dan logout agar pengguna dapat mengakses aplikasi sesuai dengan status autentikasinya. Pada file views.py, saya menambahkan fungsi register menggunakan UserCreationForm untuk membuat akun baru. Kemudian saya menambahkan fungsi login_user menggunakan AuthenticationForm untuk memvalidasi kredensial pengguna dan menyimpan sesi login, termasuk menyimpan cookie last_login untuk mencatat waktu login terakhir. Fungsi logout_user juga saya buat untuk menghapus sesi dan cookie tersebut, sehingga pengguna harus login kembali untuk mengakses halaman utama.
Setelah mekanisme autentikasi selesai, saya membuat dua akun pengguna berbeda pada lokal. Masing-masing akun saya gunakan untuk membuat tiga dummy data melalui model yang sudah ada, sehingga total terdapat enam data yang terdistribusi berdasarkan pemilik akun.
Agar setiap data terhubung dengan pemiliknya, saya menghubungkan model Product dengan model User menggunakan ForeignKey. Dengan demikian, setiap product hanya bisa dimiliki oleh satu user, dan halaman utama hanya menampilkan data sesuai dengan akun yang sedang login.
Pada halaman utama, saya juga menambahkan informasi detail pengguna yang sedang login, seperti username, dan menampilkan cookie last_login yang tersimpan sebelumnya. Hal ini memastikan pengguna dapat melihat kapan terakhir kali mereka login, sekaligus membuat pengalaman pengguna lebih personal.
Setelah semua fitur berjalan dengan baik, saya menyimpan perubahan menggunakan Git (git add, git commit) lalu melakukan push ke GitHub dan PWS.

Bukti akun pengguna dan dummy data masing2 ada di dalam folder images.