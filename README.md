# MajTod

Automation script bot for Maj*r

The English version of the Readme is available at [README_EN.md](README_EN.md)

# Daftar Isi

- [MajTod](#majtod)
- [Daftar Isi](#daftar-isi)
- [Pendaftaran](#pendaftaran)
- [Fitur](#fitur)
- [Dukung saya](#dukung-saya)
- [Cara Penggunaan](#cara-penggunaan)
  - [Opsi Command Line / Argument Command Line](#opsi-command-line--argument-command-line)
  - [Tentang Proxy](#tentang-proxy)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [Cara Melakukan Update](#cara-melakukan-update)
- [Kode Javascript untuk Mendapatkan Data di Aplikasi Telegram Desktop](#kode-javascript-untuk-mendapatkan-data-di-aplikasi-telegram-desktop)
- [Terima kasih](#terima-kasih)

# Pendaftaran

Ikuti tautan berikut untuk mendaftar : https://t.me/major/start?startapp=629438076

# Fitur

- [x] Presensi Harian
- [x] Otomatis Bermain Game
- [x] Otomatis Menyelesaikan Task (tidak semua)
- [x] Mendukung pemakaian proxy
- [x] Penggunaan User-Agent acak
- [x] Laporan total saldo semua

# Dukung saya

Jika anda suka dengan hasil pekerjaan saya anda bisa mendukung saya melakui tautan dibawah

- [Indonesia] https://s.id/nusanqr (QRIS)
- [Indonesia] https://trakteer.id/fawwazthoerif/tip
- [Global] https://sociabuzz.com/fawwazthoerif/tribe
- Jika anda ingin mengirim dalam bentuk lain, anda bisa menghubungi saya melalui telegram.

# Cara Penggunaan

## Opsi Command Line / Argument Command Line

Script / program ini juga mendukung beberapa argument parameter yang bisa dipakai, berikut adalah penjelasan argument 

`--data` / `-D` bisa digunakan ketika anda mempunyai nama file yang berbeda untuk menyimpan data akun. Secara bawaan nama file yang digunakan oleh script / program ini untuk menyimpan data akun adalah `data.txt`, semisal anda mempunyai file bernama `query.txt` sebagai file yang menyimpan data akun maka tinggal jalankan `bot.py` dengan menambahkan argumetn `--data` / `-D`. Contoh `python bot.py --data query.txt`

`--proxy` / `-P` bisa digunakan ketika anda mempunyai nama file yang berbeda untuk menyimpan list proxy. Nama file yang digunakan oleh script / program ini untuk menyimpan daftar proxy adalah `proxies.txt`, semisal anda mempunyai file bernama `prox.txt` sebagai file yang menyimpan daftar proxy, anda hanya tinggal menambahkan argument parameter `--proxy` / `-P` untuk dapat menggunakan file proxy anda. Contoh `python bot.py --proxy prox.txt`

`--worker` / `-W` argument ini berfungsi untuk melakukan kustomisasi jumlah thread / worker yang digunakan ketika script bot ini berjalan. Secara bawaan script / software ini jumlah worker nya adalah (total core cpu / 2), semisal cpu anda memiliki core 6 maka jumlah worker yang digunakan adalah 3. Anda bisa melakukan kustomisasi untuk jumlah worker ini menggunakan argument ini. Contohnya anda ingin membuat jumlah worker nya menjadi 100 maka jalankan `bot.py` dengan argument seperti ini `python bot.py --worker 100`. Dan jika anda tidak suka menggunakan worker / thread / multiprocessing maka anda bisa melakukan kustomisasi worker menjadi 1, contoh `python bot.py --worker 1`.

`--action` / `-A` argument ini berfungsi untuk langsung masuk ke kemu yang dituju, misal dalam script bot ini ada 5 menu jika anda tidak ingin melakukan input secara manual anda bisa menggunakan argument ini untuk langsung masuk ke menu yang dituju. Contoh : `python bot.py --action 5` dalalm contoh tersebut berarti anda akan langsung masuk ke menu nomor 5. Argument ini berguna jika kalian menggunakan docker / pm2 untuk menjalankan script bot di proses background.

## Tentang Proxy

Daftar di Website Berikut untuk Mendapatkan Proxy Gratis : [Here](https://www.webshare.io/?referral_code=dwj0m9cdi4mp)

Website dengan harga proxy termurah $1/GB [Here](https://dataimpulse.com/?aff=48082)

Anda bisa menambahkan daftar proxy di file `proxies.txt` dan format proxynya seprti berikut :

Jika terdapat autentikasi :

Format : 

```
protocol://user:password@hostname:port
```

Contoh :

```
http://admin:admin@69.69.69.69:6969
```

Jika tidak ada autentikasi :

Format :

```
protocol://hostname:port
```

Contoh :

```
```

Contoh :

```
http://69.69.69.69:6969
```

Tolong diperhatikan dengan saksama apakah proxy yang anda gunakan itu harus menggunakan autentikasi atau tidak, karena banyak orang yang DM saya bertanya cara penggunaan proxy.

Berikut cara penggunaan dibeberapa operasi sistem

## Windows

1. Pastikan komputer anda sudah terinstall python dan git, jika belum anda bisa menginstallnya terlebih dahulu

    Saran versi python adalah 3.10

    Unduh python : [https://python.org](https://python.org)

    Unduh Git : [https://git-scm.com](https://git-scm.com/)

2. Buka Terminal / CMD

3. Kloning repository ini
   ```shell
   git clone https://github.com/akasakaid/majtod.git
   ```

4. Masuk ke folder majtod
   ```shell
   cd majtod
   ```

5. Install library yang dibutuhkan
   ```shell
   python -m pip install -r requiremens.txt
   ```

6. Edit/ ubah file `data.txt`, isi file `data.txt` dengan data akun kalian. Kalian bisa mendapatkan data akun kalian dengan cara menggunakan kode javascript yang telah saya sediakan dibawah.
   
7. Jalankan/ eksekusi file utama 
   ```shell
   python bot.py
   ```

## Linux

1. Pastikan komputer anda sudah terinstall python dan git, jika belum anda bisa menginstallnya terlebih dahulu

    Perintah linux untuk melakukan installasi python dan git

    ```shell
    sudo apt install python3 python3-venv python3-pip git -y
    ```

2. Kloning repository ini
   ```shell
   git clone https://github.com/akasakaid/majtod.git
   ```

3. Masuk ke folder majtod
   ```shell
   cd majtod
   ```

4. Buat virtual environment dan mengaktifkannya.
   
   ```shell
   python3 -m venv env && source env/bin/activate
   ```

5. Install library yang dibutuhkan
   ```shell
   python -m pip install -r requiremens.txt
   ```

6. Edit/ ubah file `data.txt`, isi file `data.txt` dengan data akun kalian. Kalian bisa mendapatkan data akun kalian dengan cara menggunakan kode javascript yang telah saya sediakan dibawah.
   
7. Jalankan/ eksekusi file utama 
   ```shell
   python bot.py
   ```

## Termux

1. Pastikan di aplikasi termux anda sudah terinstall python dan git, jika belum anda bisa menginstallnya terlebih dahulu
   
   ```shell
   pkg update -y && pkg upgrade -y && pkg install python git -y
   ```

2. Kloning repository ini
   ```shell
   git clone https://github.com/akasakaid/majtod.git
   ```

3. Masuk ke folder majtod
   ```shell
   cd majtod
   ```

4. Install library yang dibutuhkan
   ```shell
   python -m pip install -r requiremens.txt
   ```

5. Edit/ ubah file `data.txt`, isi file `data.txt` dengan data akun kalian. Kalian bisa mendapatkan data akun kalian dengan cara menggunakan kode javascript yang telah saya sediakan dibawah.
   
6. Jalankan/ eksekusi file utama 
   ```shell
   python bot.py
   ```

# Cara Melakukan Update

Hapus terlebih dahulu file `database.sqlite3`, anda bisa menggunakan peringah terminal dibawah (sesuaikan dengan sistem operasi yang anda gunakan)

Windows CMD / Windows Powershell

```shell
del database.sqlite3
```

Linux/Termux/Unix/MacOs

```shell
rm database.sqlite3
```

Anda bisa melakukan update hanya dengan perintah `git pull` jika anda memang dari awal sudah melakukan clone repository dengan git.
Jika anda tidak melakukan clone repository dengan git anda bisa melakukan update paksa dengan perintah dibawah (sesuaikan sistem operasi yang anda gunakan.).

Windows powershell : 
```shell
Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/bot.py -OutFile bot.py; Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/models.py -OutFile models.py; Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/requirements.txt -OutFile requirements.txt
```

Linux/Termux/Unix/Windows CMD/MacOS: 

```shell
curl https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/bot.py -o bot.py && curl https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/models.py -o models.py && curl https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/requirements.txt -o requirements.txt
```

# Kode Javascript untuk Mendapatkan Data di Aplikasi Telegram Desktop

Berikut beberapa kode javascript yang  bisa dicoba untuk mendapatkan data melalui aplikasi telegram desktop.

Setelah anda melakukan eksesusi kode coba melakukan paste jika tidak muncul maka coba kode javascript selainnya.

```javascript
copy(Telegram.WebApp.initData)
```

```javascript
copy(JSON.parse(sessionStorage.__telegram__initParams).tgWebAppData)
```

# Terima kasih