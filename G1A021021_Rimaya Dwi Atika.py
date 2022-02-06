def pertama():
  print("=======================================")
  print("SELAMAT DATANG DI APLIKASI UNIVERSITAS BENGKULU")
  print("=======================================")
  
  def welcome():
    print("\nApakah Anda Ingin Melakukan Pendaftaran Ulang Mahasiswa Secara Online ? ")
    print("1.Ya" "\n2.Tidak")
    awal =input("\nPilihan Anda : ")
    if awal=="1" :
      print("\nSelamat Datang di Menu Pendaftaran Ulang Online Mahasiswa Baru ")
    elif awal=="2":
      print("Silahkan Daftar Ulang Secara Offline")
      quit()
    else:
      print("input yang anda masukkan salah")
      welcome()
  welcome()
  
  print('')
  Nama=input("Silahkan Masukkan Nama Anda:") 
  Tanda_pengenal=(input("Masukkan Nomor Pokok Mahasiswa Anda:"))
 
  
  print("\nPILIHAN FAKULTAS")
  pilihan_fakultas=["1.TEKNIK","2.MIPA","3.FKIP","4.KEDOKTERAN","5.HUKUM"]
  for menu1 in pilihan_fakultas:
    print(menu1,end="\n")

  def fakultas():
    Fakultas=int(input("\nMasukkan Angka Berdasarkan Fakultas Anda :"))
    if Fakultas==1:
      print("=======PROGRAM STUDI INFORMATIKA=======")
    elif Fakultas==1:
      print("\nSELAMAT ANDA SUDAH MEMILIH PROGRAM STUDI INFORMATIKA")
      print("Silahkan Lengkapi Persyaratan Anda")
    else:
      print("\nHanya Tersedia Untuk Fakultas Teknik dan Progran Studi Informatika")
      fakultas()
  fakultas()
  
  print('')
  print("PILIHAN KELAS:")
  pilihan_kelas=["1.A","2.B","3.C"]
  for menu2 in pilihan_kelas:
    print(menu2,end="\n")

  def kelas():
    Pilihan_Kelas=int(input("\nSilahkan Memasukkan Kelas Pada Prodi Informatika :"))
    if Pilihan_Kelas==1:
      print("=============================")
      print("Selamat Datang di Kelas A Informatika")
      print("Lengkapi Persyaratan Anda Secara Offline")
      print("=============================")
    elif Pilihan_Kelas==2:
      print("===============================")
      print("Selamat Datang di Kelas B Informatika")
      print("Lengkapi Persyaratan Anda Secara Offline")
      print("===============================")
    elif Pilihan_Kelas==3:
      print("===============================")
      print("Selamat Datang di Kelas C Informatika")
      print("Lengkapi Persyaratan Anda Secara Offline")
      print("===============================")
    else:
      print("Input yang anda masukkan salah")
      kelas()
  kelas()

  def last():
    print("")
    print("Silahkan Mengirimkan Persyaratan Secara langsung Ke UNIVERSITAS BENGKULU")
    print("1.Ya\n2.Tidak")
    Again =input("\nPilihan Anda : ")
    if Again=="1":
      print("\n=======TERIMA KASIH TELAH MELAKUKAN PENDAFTARAN ULANG SECARA ONLINE=======")
      quit()
    elif Again=="2":
      pertama()
      quit()
    else:
      print("input yang anda masukkan salah")
      last()
  last()

pertama()

#def adalah kumpulan perintah atau baris kode yang dikelompokkan menjadi satu kesatuan untuk kemudian bisa dipanggil atau digunakan berkali-kali
#print berfungsi untuk menampilakan kode yang kita tulis dengan hasil atau output nantinya
#int berfungsi untuk mengubah bilangan atau string bilangan ke bentuk bilangan bulat (integer)
#if adalah kondisi yang digunakan untuk mengeksekusi kode jika kondisi bernilai benar (true)
#elif merupakan percabangan dari if
#else yaitu kebalikannya dari if yaitu kode akan dieksekusi jika bernilai salah
#input untuk memasukkan berupa huruf atau angka, sesuai dengan kebutuhan yang diinginkan
#quit() berfungsi untuk keluar dari suatu program
#end berfungsi mengganti karakter terakhir bawaan yang dicetak di layar
