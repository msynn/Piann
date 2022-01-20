print("Daftar kota")
kota = [
    "Kendari", "Palopo", "Mamuju tengah", "Majene", "Mamuju",
    "Pasang Kayu", "Palu", "Makassar", "Manado"
]

for i in kota :
    print(i)

kotaYangDicari = input("Apa kota yang anda cari : ")
for i, kota in enumerate(kota):
    if kota.lower() == kotaYangDicari.lower():
        print('Kota yang anda cari berada pada indeks', i)
        break
else :
    print('Maaf, Kota yang anda cari tidak ada!')