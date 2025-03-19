import time
import random
import keyboard

while True:
    print(" ")
    print("ULTİMATE MENU v4")
    print(" ")
    print("ALLAH PANEL = 1")
    print("HESAP MAKİNESİ = 2")
    print("YÜZDE HESAPLAMA = 3")
    print("VKİ HESAPLAMA = 4")
    print("TAŞ KAĞIT MAKAS = 5")
    print("CASİNO = 6")
    print("HAMZA PANEL = 7")
    print(" ")
    ultimate_secim = int(input("Seçiminiz: "))
    if ultimate_secim == 1:
        while True:
            kiyamet_sekilleri = ["Heryer kurudu.", "Uzaylılar istila etti", "Yeryüzü terse döndü",
                                 "Yecücle mecüc geldi.",
                                 "deccal allah oldu.","canboyun anasının amı patladı"]
            random_kiyamet = random.choice(kiyamet_sekilleri)
            gezegen_yok_sekil = ["Büyük bir yıldız patladı ve etrafdaki herşeyi yok etti,Bu gezegende dahil.",
                                 "Gezegenin 3 katı büyüklüğündeki bir meteor gezegene çarptı ve gezegen parçalara ayrıldı.",
                                 "uzaydan gelen bir ışın gezegeni ortadan 2 ye yardı",
                                 "Uzaydan gelen bir cisim bin atom değerinde sıkıştırılmış bir top göndererek gezegeni havaya uçurdu."]
            random_yok_et = random.choice(gezegen_yok_sekil)
            gezegen_yarat = ["Büyük kütleli bir yıldızın patlaması sonucunda oluşmuş gezegen.",
                             "2 Karadeliğin çarpışması sonucu zaman bükülerek gerçekleşmiş büyük ama çok büyük olmayan bir gezegen oluştu.",
                             "Birbirine yakın bir kaç kaya parçasının kıvrılarak gelen gaz akımları birbiri ile etkileşime giriyor, farklı gaz akımları kaya parçalarının bir araya gelerek yığılmasına neden oluyor, böylece bir gezegen oluştu."]
            random_gezegen = random.choice(gezegen_yarat)

            print(" ")
            print("Allah Kontrol Paneli v3.4 FOR YİGİT")
            print(" ")
            print("Aşağıdan işlem seçebilirsiniz.")
            print(" ")
            print("KUL YARATMA = 1")
            print("KUL ÖLDÜRME = 2")
            print("SEVAP VERME = 3")
            print("GÜNAH VERME = 4")
            print("CEHENNEM SICAKLIK AYARLAMA = 5")
            print("PEYGAMBER GÖNDERME = 6")
            print("KIYAMET = 7")
            print("GEZEGEN YARAT = 8")
            print("GEZEGEN YOK ET = 9")
            print("VAHİY GÖNDER = 10")
            print("DEPREM GÖNDER = 11")
            print("EŞYA YOLLA = 12")
            print("VİRÜS GÖNDER = 13")
            print("GÜNDEM YARAT = 14")
            print("ANA MENÜ = 15")
            print("Çıkış = 0")
            print(" ")

            secim = int(input("Seçiminiz= "))
            if secim == 1:
                secim1 = str(input("Kişilik özelliği nasıl olsun?: "))
                secim_2 = str(input("Kişinin saç ve göz rengini giriniz:: "))
                secim_1 = str(input("İsmi ne olsun(annesine fısılda): "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim1}, {secim_2} özelliklerine sahip, ismi {secim_1} olan bir kul yaratıldı.")
                print(" ")
                devam1 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam1 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break
                elif devam1 == "d":
                    continue
            elif secim == 2:
                secim2 = str(input("Kimi öldüreceksiniz?: "))
                secim_2 = str(input("Kulu nasıl öldürmek istersiniz?: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim2} isimli kişiyi öldürdünüz. ölüm sebebi: {secim_2}")
                print(" ")
                devam2 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam2 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break
                elif devam2 == "d":
                    continue
            elif secim == 3:
                secim3 = str(input("Kime sevap vereceksiniz?: "))
                sevap = str(input("Neden sevap vereceksiniz?: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim3} isimli kula şu sebepten ötürü sevap verildi: {sevap}")
                print(" ")
                devam3 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam3 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break
                elif devam3 == "d":
                    continue
            elif secim == 4:
                secim4 = str(input("Kime günah vereceksiniz?: "))
                gunah = str(input("Neden günah vereceksiniz?:"))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim4} isimli kula şu sebepten ötürü günah verildi: {gunah}")
                print(" ")
                devam4 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam4 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break
                elif devam4 == "d":
                    continue
            elif secim == 5:
                secim5 = int(input("Cehennem kaç derece olsun?: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile cehennemin sıcaklığı şu dereceye ayarlandı: {secim5}")
                print(" ")
                devam5 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam5 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break
                elif devam5 == "d":
                    continue
            elif secim == 6:
                secim6 = str(input("Peygamberin ismi ne olsun?: "))
                peygamber = str(input("Nerye gönderilsin?: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim6} isimli peygamber şu lokasyona gönderildi: {peygamber}")
                print(" ")
                devam6 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam6 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break
                elif devam6 == "d":
                    continue
            elif secim == 7:
                secim7 = str(input("Gerçekten kıyamet yapmak istiyormusunuz? (evet/hayır): ")).lower()
                if secim7 == "evet":
                    print("Gerçekleştiriliyor.. 3")
                    time.sleep(1)
                    print("Gerçekleştiriliyor.. 2")
                    time.sleep(1)
                    print("Gerçekleştiriliyor.. 1")
                    time.sleep(1)
                    print(random_kiyamet)
                    print(" ")
                    devam7 = str(input("Çıkmak için T devam etmek D: ")).lower()
                    if devam7 == "t":
                        print("Çıkılıyor.. 3")
                        time.sleep(1)
                        print("Çıkılıyor.. 2")
                        time.sleep(1)
                        print("Çıkılıyor.. 1")
                        time.sleep(1)
                        break
                elif secim7 == "hayır":
                    print("Vazgecildi.")
                    print(" ")
                    devam7 = str(input("Çıkmak için T devam etmek D: ")).lower()
                    if devam7 == "t":
                        print("Çıkılıyor.. 3")
                        time.sleep(1)
                        print("Çıkılıyor.. 2")
                        time.sleep(1)
                        print("Çıkılıyor.. 1")
                        time.sleep(1)
                        break
                    elif devam7 == "d":
                        continue

            elif secim == 8:
                secim8 = str(input("Gezegen ismi giriniz: "))
                secim_8 = input("Gezegen büyüklüğünü yazınız: ")
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(
                    f"Başarı ile {secim8} adında bir gezegen oluşturuldu. Büyüklük: {secim_8} oluşma süreci ise: {random_gezegen}")
                print(" ")
                devam8 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam8 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break

            elif secim == 9:
                secim9 = str(input("Yok etmek istediğiniz gezegenin ismi: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim9} gezegenini yok ettiniz. Sebep: {random_yok_et}")
                devam9 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam9 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break

            elif secim == 10:
                secim10 = str(input("Vahiy göndereceğiniz kişiyi seçin: "))
                secim_10 = str(input("Vahiyi giriniz: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim10} kişisine vahiy gönderdiniz. Vahiy: {secim_10}")
                devam10 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam10 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break

            elif secim == 11:
                secim11 = str(input("Bölgeyi Seçiniz: ")).lower()
                secim_11 = str(input("Depremin büyüklüğünü giriniz: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim_11} bölgesinde {secim_11} büyüklüğünde bir deprem yarattınız.")
                print("")
                devam11 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam11 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break
                print(f"Başarı ile {secim11} doğal afetini {secim_11} bölgesine gönderdiniz.")
                devam__11 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam__11 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break

            if secim == 12:
                secim12 = str(input("Göndereceğiniz Kişiyi seçiniz: "))
                secim_12 = str(input("Ne yollayacaksın?: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim12} kişisine {secim_12} eşyasını yolladınız.")
                devam12 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam12 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break

            elif secim == 13:
                secim13 = str(input("Göndereceğiniz virüsün ismi?: "))
                secim_13 = str(input("Bu virüs nerede başlasın?: "))
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim13} virüsünü şu bölgede başlattınız: {secim_13}")
                devam13 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam13 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break

            elif secim == 14:
                secim14 = str(input("Gündem ne hakkında olsun?: "))
                secim_14 = input("Gündem kaç gün sürsün?: ")
                print("Gerçekleştiriliyor.. 3")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 2")
                time.sleep(1)
                print("Gerçekleştiriliyor.. 1")
                time.sleep(1)
                print(f"Başarı ile {secim14} hakkında, {secim_14} kadar sürecek bir gündem yarattınız.")
                devam14 = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam14 == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break

            elif secim == 15:
                print(" ")
                break


            elif secim == 0:
                print("Çıkılıyor.. 3")
                time.sleep(1)
                print("Çıkılıyor.. 2")
                time.sleep(1)
                print("Çıkılıyor.. 1")
                time.sleep(1)
                exit()

            else:
                print("Yanlış komut!")
                yanlis = str(input("Çıkmak için T devam etmek D: ")).lower()
                if yanlis == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break


    if ultimate_secim == 2:
        while True:
            print(" ")
            print("ÇARPMA = 1")
            print("TOPLAMA = 2")
            print("ÇIKARTMA = 3")
            print("BÖLME = 4")
            print("ÜS ALMA = 5")
            print("ANA MENÜ = 6")


            def devam_etme():
                devam = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    exit()


            secim = int(input("Seçim: "))
            if secim == 1:
                sayi1 = int(input("1. Sayıyı giriniz: "))
                sayi2 = int(input("2. Sayıyı giriniz: "))
                print(f"Sonuç: {sayi1 * sayi2}")
                devam_etme()

            elif secim == 2:
                sayi1 = int(input("1. Sayıyı giriniz: "))
                sayi2 = int(input("2. Sayıyı giriniz: "))
                print(f"Sonuç: {sayi1 + sayi2}")
                devam_etme()

            elif secim == 3:
                sayi1 = int(input("1. Sayıyı giriniz: "))
                sayi2 = int(input("2. Sayıyı giriniz: "))
                print(f"Sonuç: {sayi1 - sayi2}")
                devam_etme()

            elif secim == 4:
                sayi1 = float(input("1. Sayıyı giriniz: "))
                sayi2 = float(input("2. Sayıyı giriniz: "))
                print(f"Sonuç: {sayi1 / sayi2}")
                devam_etme()

            elif secim == 5:
                sayi1 = int(input("1. Sayıyı giriniz: "))
                sayi2 = int(input("2. Sayıyı giriniz: "))
                print(f"Sonuç: {sayi1 ** sayi2}")
                devam_etme()

            elif secim == 6:
                print("Çıkılıyor.. 3")
                time.sleep(1)
                print("Çıkılıyor.. 2")
                time.sleep(1)
                print("Çıkılıyor.. 1")
                time.sleep(1)
                break

    if ultimate_secim == 3:
        while True:
            def devam_etme():
                devam = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    exit()


            print(" ")
            print("Ana Menüye Dönmek İçin Sayı Kısmına 198 yazın.")
            sayi = float(input("Sayıyı giriniz: "))
            if sayi == 198:
                print("Çıkılıyor.. 3")
                time.sleep(1)
                print("Çıkılıyor.. 2")
                time.sleep(1)
                print("Çıkılıyor.. 1")
                time.sleep(1)
                break
            yuzde = float(input("Yüzdeyi Giriniz: "))

            sonuc = (sayi * yuzde) / 100

            print(f"Sonuç: {sonuc}")
            devam_etme()

    if ultimate_secim == 4:
        while True:
            def devam_etme():
                devam = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    exit()


            print(" ")
            print("<18.5 Zayıf")
            print("18.5 - 24.9 Normal")
            print("25 - 29.9 Fazla kilolu")
            print("30 - 34.9 Obez (1. derece)")
            print("35 - 39.9 Obez (2. derece)")
            print("40+ Morbid obez")
            print(" ")
            print("Çıkmak İçin Boy Kısmına 211 Yazın.")
            print(" ")
            boy = int(input("Boyunuzu Giriniz: "))
            if boy == 211:
                print("Çıkılıyor.. 3")
                time.sleep(1)
                print("Çıkılıyor.. 2")
                time.sleep(1)
                print("Çıkılıyor.. 1")
                time.sleep(1)
                break
            boy = boy / 100
            kilo = int(input("Kilonuzu Giriniz: "))
            print(" ")
            vki = int(kilo / (boy ** 2))
            if vki < 18.5:
                print(f"Zayıfsınız. VKİ: {vki}")
            elif 18.5 <= vki <= 24.9:
                print(f"Normalsiniz. VKİ: {vki}")
            elif 25 <= vki <= 29.9:
                print(f"Fazla Kilolusunuz. VKİ: {vki}")
            elif 30 <= vki <= 34.9:
                print(f"1. Derece Obezsiniz. VKİ: {vki}")
            elif 35 <= vki <= 39.9:
                print(f"2. Derece Obezsiniz. VKİ: {vki}")
            else:
                print(f"Morbid Obezsiniz. VKİ: {vki}")
            devam_etme()



    if ultimate_secim == 5:
        while True:
            def devam_etme():
                devam = str(input("Çıkmak için T devam etmek D: ")).lower()
                if devam == "t":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    exit()


            liste = ["taş", "kağıt", "makas"]
            pc = random.choice(liste)
            print(" ")
            print("TAŞ KAĞIT MAKAS OYUNU")
            print("")
            print("Ana Menüye Dönmek İçin Seçime Q Yazın")
            secim = str(input("Seçim? (TAŞ/KAĞIT/MAKAS): ")).lower()
            if secim == "q":
                    print("Çıkılıyor.. 3")
                    time.sleep(1)
                    print("Çıkılıyor.. 2")
                    time.sleep(1)
                    print("Çıkılıyor.. 1")
                    time.sleep(1)
                    break
            print("")
            if secim == pc:
                print("Berabere!")
            elif (secim == "taş" and pc == "makas") or \
                    (secim == "kağıt" and pc == "taş") or \
                    (secim == "makas" and pc == "kağıt"):
                print("Kazandınız!")
            else:
                print(f"Kaybettiniz! Karşı seçim: {pc}")
            devam_etme()

    if ultimate_secim == 6:
        bakiye = 500
        print(f"Bakiye miktarınız: {bakiye}. Oynamak için enter tuşlayınız.")
        print("Her çevirme 100 tldir.")
        while True:
            key = keyboard.wait("enter")
            bakiye -= 100
            print("Çeviriliyor...")
            sembol = ["🍒"]
            sembol2 = ["🍋"]
            sembol3 = ["🔔"]
            semboller = [random.choice(sembol + sembol2 + sembol3) for _ in range(3)]
            print(semboller)

            if semboller[0] == semboller[1] == semboller[2]:
                bakiye = bakiye * 3
                print(f"Kazandınız. Paranız 3'e katlandı. Güncel bakiye: {bakiye}")
            else:
                print(f"Kaybettiniz. Güncel bakiye: {bakiye}")
            if bakiye < 100:
                print("Paranız bitti ve oyun bitti.")
                exit()
    if ultimate_secim == 7:
        uyuma_saat = [2, 3, 4, 5, 6, 7]
        random_uyuma = random.choice(uyuma_saat)

        guvenme_sekli = ["Yavuz sizi ekti(onun için kek yapmıştınız).", "Yaman sırasını değiştirdi.",
                         "Hamza planlara dahil edilmedi.", "Yaman ona yalan söyledi."]
        random_guvenme = random.choice(guvenme_sekli)


        def devam_etme():
            devam = str(input("Çıkmak için T devam etmek D: ")).lower()
            if devam == "t":
                print("Çıkılıyor.. 3")
                time.sleep(1)
                print("Çıkılıyor.. 2")
                time.sleep(1)
                print("Çıkılıyor.. 1")
                time.sleep(1)
                exit()


        while True:
            print(" ")
            print("HAMZA PANEL V1 💀")
            print(" ")
            print("KIZINIZIN ADINI KOYMAK İÇİN - 1")
            print("MARTI SESİ ÇIKARMAK İÇİN - 2")
            print("MAL MAL SİNİRLENMEK İÇİN - 3")
            print("TAVUKLU BÖREK İKRAM ETMEK İÇİN - 4")
            print("UYUMAK İÇİN - 5")
            print("BİRİNE GÜVENMEK İÇİN - 6")
            print("BİRİNE ÇIKMA TEKLİFİ ETMEK İÇİN - 7")
            print(" ")
            secim = int(input("Seçiminiz?: "))
            if secim == 1:
                kiziniz = str(input("Kızınızın adını giriniz: "))
                if kiziniz == "kumsal":
                    print("Doğru seçim! kızınızın ismi kumsal!")
                else:
                    print("Yanlış seçim! Kumsal olmalıydı!")
                devam_etme()
            elif secim == 2:
                print("Başarıyla martı sesi çıkardınız! Sınıfın çoğu seni oruspu evladı olarak nitelendiriyor.")
                devam_etme()
            elif secim == 3:
                print("Başarıyla mal mal sinirlendiniz! Tüm sınıf seni ucube bir oruspu evladı olarak görüyor!")
                devam_etme()
            elif secim == 4:
                print(
                    "Yavuza tavuklu börek ikram ettin! Yavuz emin ile böreğini paylaştı! herkes mutlu ve aranızdaki bağ güçlendi!")
                devam_etme()
            elif secim == 5:
                print(
                    f"Başarıyla uykuya daldınız. Bütün sınıf sen uyurken anana sövdü. Uyuma süreniz: {random_uyuma} ders.")
                devam_etme()
            elif secim == 6:
                print(f"Başarıyla güvendiniz. Olay: {random_guvenme}")
                devam_etme()
            elif secim == 7:
                isim = str(input("Kime çıkma teklifi edeceksiniz?: ")).lower()
                if isim == "kumsal":
                    print("Kumsal sizi işletti ve reddetti.")
                elif isim == "duru":
                    print("Çıkma teklifiniz kabul edildi.")
                elif isim == "yaman":
                    print("Are you gay?")
                    secim_1 = str(input("Seçiminiz?: "))
                    if secim_1 == "evet":
                        print("Vayoc reddedildin.")
                    else:
                        print("ozaman sg oc")
                else:
                    print(f"Çıkma teklifiniz {isim} tarafından reddedildi.")
                devam_etme()




