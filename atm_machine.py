print("""
*********************************
    ATM - HOŞGELDİNİZ SN. IŞIK
*********************************

İşlemler ;
1. Bakiye Sorgulama 
2. Para Yatırma
3. Para Çekme 

Çıkış Yapmak için "Q" ya basınız..
********************************** 
""")

tbakiye=1000
ubakiye=1000/19
ebakiye=1000/20.5

while True:
    işlem=input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz : ")

    if işlem.lower()=="q" :
        print("İşleminiz Sonlandırılmıştır...")
        break
    elif (işlem=="1"):
        print("""
        Bakiyeniz       : {:.2f} TL
                        : {:.2f} USD
                        : {:.2f} EURO
        """.format(tbakiye,ubakiye,ebakiye))
    elif işlem=="2" :
        döviz=str(input("Lütfen Yatırmak İstediğiniz Döviz Cinsini Belirtiniz : TL,USD,EURO:  "))
        if döviz.lower()=="tl" :
            miktar=float(input("Lütfen Yatırmak İstediğiniz Tutarı Giriniz :  "))
            tbakiye+=miktar
            ubakiye=tbakiye/19
            ebakiye=tbakiye/20.5
            print("""
            Yatırma İşlemini Başarıyla Tamamlanmıştır...
            Yeni Bakiyeniz :{:.2f} TL
            """.format(tbakiye))
        elif döviz.lower()=="usd" :
            miktar = float(input("Lütfen Yatırmak İstediğiniz Tutarı Giriniz :  "))
            ubakiye += miktar
            tbakiye = ubakiye * 19
            ebakiye = tbakiye / 20.5
            print("""
            Yatırma İşlemini Başarıyla Tamamlanmıştır...
            Yeni Bakiyeniz :{:.2f} USD
            """.format(ubakiye))

        elif döviz.lower()=="euro" :
            miktar = float(input("Lütfen Yatırmak İstediğiniz Tutarı Giriniz :  "))
            ebakiye += miktar
            tbakiye = ebakiye * 20.5
            ubakiye = tbakiye / 19
            print("""
            Yatırma İşlemini Başarıyla Tamamlanmıştır...
            Yeni Bakiyeniz :{:.2f} EURO
            """.format(ebakiye))
        else :
            print("Seçtiğiniz Döviz Cinsi İçin Hizmer Veremiyoruz..")

    elif işlem=="3":
        döviz = str(input("Lütfen Çekmek İstediğiniz Döviz Cinsini Belirtiniz : TL,USD,EURO  "))

        if döviz.lower() == "tl":
            miktar=float(input("Lütfen Çekmek İstediğiniz Tutarı Giriniz (TL) :  "))
            if (miktar-tbakiye) > 0 :
                print("""Belirttiğiniz Tutarı Babanızdan İsteyiniz..
                """)
                print("""Başka Bir Tutar Denemek İster Misiniz ? 
                """)
                yanıt=str(input("""Evet için "E" , Ana Menüye Dönmek İçin "H" ye Basınız.."""))
                if yanıt.lower() == "h" :
                    continue

                elif yanıt.lower() == "e" :
                    miktar = float(input("Lütfen Çekmek İstediğiniz Tutarı Giriniz (TL) :  "))
                    tbakiye-=miktar
                    ubakiye=tbakiye/19
                    ebakiye=tbakiye/20.5
                    print("""
                    Yatırma Çekme İşleminiz Başarıyla Tamamlanmıştır...
                    Yeni Bakiyeniz :{:.2f} TL
                    """.format(tbakiye))

        elif döviz.lower()== "usd" :
            miktar = float(input("Lütfen Çekmek İstediğiniz Tutarı Giriniz (USD) :"))
            if miktar - ubakiye > 0:
                print("Belirttiğiniz Tutarı Babanızdan İsteyiniz..")
                continue
            ubakiye -= miktar
            tbakiye = ubakiye * 19
            ebakiye = tbakiye / 20.5
            print("""
            Yatırma Çekme İşleminiz Başarıyla Tamamlanmıştır...
            Yeni Bakiyeniz :{:.2f} USD
            """.format(ubakiye))

        elif döviz.lower()=="euro":
            miktar = float(input("Lütfen Çekmek İstediğiniz Tutarı Giriniz (EURO) :"))
            if miktar - ebakiye > 0:
                print("Belirttiğiniz Tutarı Babanızdan İsteyiniz..")
                continue
            ebakiye -= miktar
            tbakiye = ebakiye * 20.5
            ubakiye = tbakiye / 19
            print("""
            Yatırma Çekme İşleminiz Başarıyla Tamamlanmıştır...
            Yeni Bakiyeniz :{:.2f} EURO
            """.format(ebakiye))
        else :
            print("Seçtiğiniz Döviz Cinsi İçin Hizmet Veremiyoruz..")
    else :
        print("Geçersiz İşlem, Lütfen Tekrar Deneyiniz...")