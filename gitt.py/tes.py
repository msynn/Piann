nama_depan = input("Masukkan nama depan : ")
nama_belakang = input("Masukkan nama belakang : ")
nama_lengkap = nama_depan + nama_belakang
kelas = int(input("Anda kelas berapa : "))
angkatan = int(input("Angkatan tahun berapa anda : "))
tahun_lahir = int(input("Masukkan tahun lahir : "))
asal = input("Masukkan daerah asal : ")
usia_masuk_PT = 2021 - angkatan

print('''Nama saya {} lahir pada tahun {}.
saya merupakan mahasiswa angkatan {} kelas {}
saya berusia {} Tahun ketika mulai berkuliah.
saya berasal dari {}''' .format(nama_lengkap, tahun_lahir, angkatan, kelas, usia_masuk_PT, asal))