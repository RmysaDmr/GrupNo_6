import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Gorsellerdeki "Matematiksel Model" ve "Cozum Plani" baz alinmistir
class AbonelikAnalizi:
    def __init__(self, isim, baslangic_fiyati, sure_ay):
        self.isim = isim
        self.a = baslangic_fiyati  # Ilk terim
        self.n = sure_ay  # Seri uzunlugu
        self.aylar = np.arange(1, sure_ay + 1)

    def hesapla_modeller(self, yillik_zam):
        # 1. Sabit Model (Aritmetik Seri: Sn = n * a)
        sabit_aylik = np.full(self.n, self.a)
        sabit_toplam = np.cumsum(sabit_aylik)

        # 2. Enflasyonlu Model (Geometrik Seri: Sn = a * (1-r^n)/(1-r))
        aylik_r = 1 + (yillik_zam / 12)
        enf_aylik = []
        toplam = 0
        for i in range(self.n):
            # Float hassasiyeti cozumu: round(value, 2)
            fiyat = round(self.a * (aylik_r ** i), 2)
            enf_aylik.append(fiyat)
            toplam = round(toplam + fiyat, 2)

        return sabit_aylik, sabit_toplam, np.array(enf_aylik), np.cumsum(enf_aylik)


def gorsellestir():
    # Parametreler (Gorsel 3 ve 10'daki ornek girdilere uygun)
    SURE = 24
    FIYAT = 200.0
    ZAM = 0.25  # %25 yillik artis

    analiz = AbonelikAnalizi("Dijital Servis", FIYAT, SURE)
    m1, s1, m2, s2 = analiz.hesapla_modeller(ZAM)

    # Grafik Tasarimi (Gorsel 13 - Gorsellestirme Sorunlari Cozumu)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    plt.subplots_adjust(hspace=0.4)

    # Grafik 1: Aylik Degisim (Basamakli yapi - plt.step)
    ax1.step(analiz.aylar, m1, where='post', label='Sabit Fiyat', color='blue')
    ax1.step(analiz.aylar, m2, where='post', label='Zamli (Geometrik)', color='red')
    ax1.set_title("Aylik Abonelik Ucreti Degisimi")
    ax1.set_ylabel("TL")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Grafik 2: Kismi Toplam (Birikimli Maliyet)
    ax2.plot(analiz.aylar, s1, label='Sabit Toplam', linestyle='--')
    ax2.plot(analiz.aylar, s2, label='Zamli Toplam (Sn)', linewidth=2)
    ax2.fill_between(analiz.aylar, s1, s2, color='orange', alpha=0.2)
    ax2.set_title("Kismi Toplam Analizi (Birikimli Maliyet)")
    ax2.set_xlabel("Zaman (Ay)")
    ax2.set_ylabel("Toplam TL")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Rapor ozeti (Gorsel 5 ve 14'e uygun terminal ciktisi)
    print(f"\n--- {SURE} Ay Sonu Analiz Ozeti ---")
    print(f"Sabit Model Toplam: {s1[-1]} TL")
    print(f"Zamli Model Toplam: {round(s2[-1], 2)} TL")
    print(f"Enflasyon Farkı: {round(s2[-1] - s1[-1], 2)} TL")

    plt.show()


if __name__ == "__main__":
    gorsellestir()