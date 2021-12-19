#Belajar NOT,OR,AND,XOR

#Contoh NOT
aku = True
kamu = not aku
print('Aku adalah =', aku)
print('---contoh NOT---')
print('kamu adalah', kamu)

#Contoh OR (Jika salah satu true maka akan true)
print('======OR=====')
aku = False
dia = False
kamu = aku or dia
print(aku, 'OR', dia, '=', kamu)
aku = False
dia = True
kamu = aku or dia
print(aku, 'OR', dia, '=', kamu)
aku = True
dia = False
kamu = aku or dia
print(aku, 'OR', dia, '=', kamu)
aku = True
dia = True
kamu = aku or dia
print(aku, 'OR', dia, '=', kamu)

# contoh AND (akan False jika salah tau False)
print('======AND=====')
aku = False
dia = False
kamu = aku and dia
print(aku, 'AND', dia, '=', kamu)
aku = False
dia = True
kamu = aku and dia
print(aku, 'AND', dia, '=', kamu)
aku = True
dia = False
kamu = aku and dia
print(aku, 'AND', dia, '=', kamu)
aku = True
dia = True
kamu = aku and dia
print(aku, 'AND', dia, '=', kamu)

# contoh XOR (akan true jika salah satu True, Sisanya False)
print('======XOR=====')
aku = False
dia = False
kamu = aku ^ dia
print(aku, 'XOR', dia, '=', kamu)
aku = False
dia = True
kamu = aku ^ dia
print(aku, 'XOR', dia, '=', kamu)
aku = True
dia = False
kamu = aku ^ dia
print(aku, 'XOR', dia, '=', kamu)
aku = True
dia = True
kamu = aku ^ dia
print(aku, 'XOR', dia, '=', kamu)