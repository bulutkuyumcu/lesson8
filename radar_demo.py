# Hız sınırı
# Aracın Hızı
# Ceza Bedeli
# Kademeli ceza bedeli hesaplaması

# hız = yol/zaman

yol = int(input("KM giriniz : "))
zaman = float(input("Yol süresi giriniz : (saat) "))
hiz = yol/zaman
hizSiniri = 130
asimOrani = 0

# 150 - 130 = 20
# 130   20
# 100   X
# (100*20) / 130 = X

if hiz > hizSiniri:
    asimOrani = (100*(hiz-hizSiniri)) / hizSiniri

print("{} km mesafeyi {} sürede alan aracın ortalama hızı {} aşım oranı %{}".format(yol,zaman,hiz,asimOrani))

kademe1 = 427
kademe2 = 888
kademe3 = 1823

if asimOrani <10:
    print("Ceza yemediniz. Aşım oranınız : {}".format(asimOrani))
elif asimOrani > 10 and asimOrani <= 30:
    print("Ceza yediniz. Ceza tutarı: {} Aşım oranınız : {}".format(kademe1,asimOrani))
elif asimOrani >30 and asimOrani <= 50:
    print("Ceza yediniz. Ceza tutarı: {} Aşım oranınız : {}".format(kademe2,asimOrani))
else:
    print("Ceza yediniz. Ceza tutarı: {} Aşım oranınız : {}".format(kademe3,asimOrani))
