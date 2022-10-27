# Veri Tabanı #
dbUsername ="admin"
dbPassword = "123123"
# Veri Tabanı #

# Login Form #

username = input("Kullanıcı adı giriniz: ")
password = input("Şifrenizi giriniz: ")

if dbUsername == username:
    if dbPassword == password:
        print("Giriş Başarılı")
    else :
        print("Şifreniz Hatalı")
else:
        print("Hesap Bulunamadı")