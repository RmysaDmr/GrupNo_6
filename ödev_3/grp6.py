import numpy as np
import sympy as sp


def netflix_analizi_ornek1():
    """
    Örnek Girdi 1 (Basit): Netflix Premium Analizi
    Amacı: Tekil bir platformun yıllık seri toplamını hesaplamak.
    """
    print("--- SENARYO 1: NETFLIX PREMIUM ANALİZİ ---")

    # Parametreler
    aylik_ucret = 229.99
    sure_ay = 12

    # 1. Sembolik Gösterim (Sympy)
    n = sp.symbols('n')
    m = sp.symbols('m')
    seri_denklemi = m * n

    print(f"Kullanılan Matematiksel Model: {seri_denklemi}")

    # 2. Sayısal Hesaplama (Numpy)
    # 12 ay boyunca sabit ödemeden oluşan bir dizi (array) oluşturuyoruz
    odemeler = np.full(sure_ay, aylik_ucret)

    # Kısmi toplamlar (Cumulative Sum) ile her ay sonundaki birikmiş maliyeti buluyoruz
    birikimli_maliyetler = np.cumsum(odemeler)

    print(f"Aylık Sabit Ücret: {aylik_ucret} TL")
    print(f"12. Ay Sonunda Toplam Harcama (S12): {birikimli_maliyetler[-1]:.2f} TL")
    print("-" * 45)


def coklu_platform_analizi_ornek2():
    """
    Örnek Girdi 2 (Karmaşık): Çoklu Platform Sepeti
    Amacı: Birden fazla aboneliğin 2 yıllık toplam yükünü analiz etmek.
    """
    print("\n--- SENARYO 2: ÇOKLU PLATFORM SEPETİ ANALİZİ ---")

    # Platformlar ve Aylık Ücretleri
    spotify = 59.99
    icloud = 39.99
    youtube = 79.99

    toplam_aylik = spotify + icloud + youtube  # 179.97 TL
    analiz_suresi = 24  # 24 Ay

    # Numpy ile 24 aylık veri seti
    sepet_dizisi = np.full(analiz_suresi, toplam_aylik)

    # Serinin kısmi toplamlarını hesaplıyoruz
    toplam_seri = np.cumsum(sepet_dizisi)

    print(f"Sepet İçeriği: Spotify, iCloud, YouTube")
    print(f"Toplam Aylık Kesinti: {toplam_aylik:.2f} TL")

    # Raporu doldurmak için örnek çıktı tablosu
    print("\nZaman Çizelgesi (Kısmi Toplamlar):")
    print(f"{'Dönem':<10} | {'Toplam Ödenen':<15}")
    print("-" * 30)

    # Belirli ayları (6, 12, 18, 24) ekrana basalım
    for ay in [5, 11, 17, 23]:
        print(f"{ay + 1}. Ay sonunda: {toplam_seri[ay]:.2f} TL")

    print(f"\n24 Ay Sonundaki Nihai Toplam: {toplam_seri[-1]:.2f} TL")
    print("-" * 45)


if __name__ == "__main__":
    # Programı çalıştıran ana blok
    netflix_analizi_ornek1()
    coklu_platform_analizi_ornek2()