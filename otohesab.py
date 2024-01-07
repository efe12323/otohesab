import requests
import time

def takip_et(hesap_linki):
    # Hesap linkini girin
    hesap_linki = input("Takip edilecek hesap linkini girin: ")

    # 1000 tane otomatik hesap oluşturun
    for i in range(1, 1001):
        # Rastgele bir kullanıcı adı ve e-posta adresi oluşturun
        kullanici_adi = "kullanici_adi_" + str(i)
        email = "kullanici_adi_" + str(i) + "@example.com"

        # Hesap oluşturma isteğini gönderin
        istek = requests.post("https://www.instagram.com/accounts/create/",
                             data={"username": kullanici_adi, "email": email})

        # İsteğin başarılı olup olmadığını kontrol edin
        if istek.status_code == 200:
            print("Hesap başarıyla oluşturuldu:", kullanici_adi)
        else:
            print("Hesap oluşturma başarısız:", kullanici_adi)

        # 1 saniye bekleyin
        time.sleep(1)

    # Hesapları takip etme isteğini gönderin
    for i in range(1, 1001):
        istek = requests.post("https://www.instagram.com/accounts/action/follow/?id=" + hesap_linki)

        # İsteğin başarılı olup olmadığını kontrol edin
        if istek.status_code == 200:
            print("Hesap başarıyla takip edildi:", kullanici_adi)
        else:
            print("Hesap takip etme başarısız:", kullanici_adi)

        # 1 saniye bekleyin
        time.sleep(1)

if __name__ == "__main__":
    takip_et("https://www.instagram.com/hesap_linki")
