print("Login Facebook")
nama = ["Fyan", "Hendra"]
email = ["fyanramadhan1@gmail.com", "hendrausman2@gmail.com"]
password = ["fyan123","hendra123"]
email_kamu = input("Masukkan Email anda : ")
password_kamu = input("masukkan password : ")
if email_kamu == email[0] and password_kamu == password[0]:
    print("Selamat Datang" , nama[0], "anda telah login ke facebook")
elif email_kamu == email[1] and password_kamu == password[1]:
    print("Selamat Datang", nama[1], "anda telah login ke facebook")
else:
    print("Maaf, Anda tidak bisa login")