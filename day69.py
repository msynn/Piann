class Segitiga :
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def get_luas(self):
        return self.alas * self.tinggi / 2

segitiga1 = Segitiga(10, 5)
segitiga2 = Segitiga(5, 10)

print('Luas Segitiga 1:', segitiga1.get_luas())
print('Luas Segitiga 2:', segitiga2.get_luas())