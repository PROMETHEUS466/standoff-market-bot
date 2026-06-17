import os
import requests
from supabase import create_client

# GitHub Secrets'tan URL ve Key'i alıyoruz
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def pazar_verisini_cek():
    # Burası Standoff 2 pazar API'si (Örnek endpoint)
    # Kendi pazar analiz API'ni veya veri kaynağını buraya yazabilirsin
    url_api = "https://api.mocki.io/v2/cc96b990/standoff2"
    cevap = requests.get(url_api)
    return cevap.json()

def veritabanini_guncelle():
    veriler = pazar_verisini_cek()
    
    # Gelen veriyi döngüye alıp Supabase'e tek tek kaydediyoruz
    for skin in veriler['skins']:
        supabase.table("skins").update({
            "price": skin['price'], 
            "change": skin['change']
        }).eq("name", skin['name']).execute()
    
    print("Market verileri başarıyla güncellendi!")

if __name__ == "__main__":
    veritabanini_guncelle()
    
