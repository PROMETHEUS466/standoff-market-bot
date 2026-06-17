import os
import requests
from supabase import create_client

# GitHub'daki gizli anahtarları okur
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def fiyatlari_guncelle():
    # Burada Standoff 2 pazarından veriyi çekecek kodun olacak
    yeni_fiyat = 4600 # Örnek veri
    
    # Supabase'e kayıt atma
    data = supabase.table("skins").update({"price": yeni_fiyat}).eq("name", "AKR Treasure Hunter").execute()
    print("Veri güncellendi!")

if __name__ == "__main__":
    fiyatlari_guncelle()
