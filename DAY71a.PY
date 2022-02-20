nilai = {"A": 4, "A-": 3.75, "B": 3, "B-": 2.75, "C": 2, "C-": 1.75, "D": 1, "E": 0}
print('Selamat datang di kalkulator IPK')
print('Harap masukkan semua nilai huruf IPK anda, satu per baris')
print('Masukkan baris kosong untuk menandai akhir.')
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input('Masukkan nilai: ')
    grade = grade.upper()
    if grade == '':
        done = True
    elif grade not in nilai:
        print('Nilai tidak valid')
    else:
        num_courses += 1
        total_points += nilai[grade]
if num_courses > 0:
    print('IPK anda adalah', total_points / num_courses)
