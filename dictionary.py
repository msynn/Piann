data = [{"nama" : "Fyan ramadhan", "umur": "19", "Jurusan": "Teknik Informatika"},
        {"nama" : "Fahri", "umur": "20", "Jurusan": "Teknik Informatika"}]

print("nama\t\t: ",data[0]["nama"])
print("umur\t\t: ",data[0]["umur"])
print("Jurusan\t\t: ",data[0]["Jurusan"])
print("nama\t\t: ",data[1]["nama"])
print("umur\t\t: ",data[1]["umur"])
print("Jurusan\t\t: ",data[1]["Jurusan"])

print("\n\n\n\n\n\n\n")

data2 = [["Fyan Ramadhan", "19", "Teknik Informatika"],
         ["Fahri", "20", "Teknik Informatika"]]

for mahasiswa in data2 :
        print("nama\t\t: ",mahasiswa[0])
        print("umur\t\t: ",mahasiswa[1])
        print("Jurusan\t\t: ",mahasiswa[2])
        print("")
