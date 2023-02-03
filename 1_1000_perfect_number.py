def mukemmel_mi(deger):
    toplam=0
    for i in range(1,deger):
        if deger%i==0:
            toplam+=i
    if toplam == deger:
        return True

print("""
    **** MÜKO SAYI ARAMA PROGRAMI ****
--Arama Yapmak İstediğiniz Aralığı Belirleyiniz--
    --Çıkış Yapmak için "Q" ya basınız--
""")
while True:
    sayı_b=input("Başlangıç Değerini Giriniz: ")
    if sayı_b.lower()=="q" :
        print("Program Sonlandırılıyor...")
        break
    sayı_s=input("Bitiş Değerinizi Giriniz: ")
    if sayı_s.lower() == "q":
        print("Program Sonlandırılıyor...")
        break
    else:
        muk_sayılar=[]
        sayı_b=int(sayı_b)
        sayı_s=int(sayı_s)
        for deger in range(sayı_b,sayı_s+1):
            if mukemmel_mi(deger)==True:
                muk_sayılar.append(deger)
        print("Seçtiğiniz Aralıktaki Mükemmel Sayılar:", muk_sayılar)




