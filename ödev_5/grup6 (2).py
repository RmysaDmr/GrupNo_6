import matplotlib.pyplot as plt
import numpy as np


def kapsamli_abonelik_analizi_final():
    print("--- Düzenlenmiş Dijital Abonelik Maliyet Analizi ---")

    # 1. Parametre Girişleri (Senaryon: Netflix, 150 TL, %25 Zam, 24 Ay)
    platform_adi = input("Platform Adı (Örn: Netflix): ")
    a = float(input("Başlangıç Aylık Ücreti (TL): "))
    r_yillik = float(input("Tahmini Yıllık Zam Oranı (Örn: %25 için 0.25): "))
    sure = int(input("Analiz Süresi (Ay): "))

    # Matematiksel Dönüşümler
    r_aylik = 1 + (r_yillik / 12)
    aylar = np.arange(1, sure + 1)

    # Hesaplama Dizileri
    aylik_maliyetler_zamli = []
    kismi_toplamlar_zamli = []
    kismi_toplamlar_sabit = []
    hatali_kismi_toplamlar = []

    total_zamli = 0
    total_sabit = 0
    total_zamli_hatali = 0

    # 2. Hesaplama Motoru
    for ay in aylar:
        # Parçalı Fonksiyon Modellemesi (İlk 3 ay indirimli senaryosu)
        if ay <= 3:
            guncel_maliyet = a * 0.6  # %40 indirimli dönem
        else:
            # Geometrik Seri Genel Terimi: a * r^(n-1)
            guncel_maliyet = a * (r_aylik ** (ay - 1))

        # Teknik Çözüm: Float hassasiyeti için yuvarlama
        guncel_maliyet_round = round(guncel_maliyet, 2)
        total_zamli += guncel_maliyet_round

        # Verileri Listelere Ekleme
        aylik_maliyetler_zamli.append(guncel_maliyet_round)
        kismi_toplamlar_zamli.append(round(total_zamli, 2))

        # Karşılaştırma Senaryosu (Sabit Fiyat - Aritmetik Seri)
        total_sabit += a
        kismi_toplamlar_sabit.append(total_sabit)

        # Hata Analizi Senaryosu (Yuvarlama olmadan birikim)
        total_zamli_hatali += guncel_maliyet
        hatali_kismi_toplamlar.append(total_zamli_hatali)

    # 3. Görselleştirme (Düzenlenmiş Layout)
    fig = plt.figure(figsize=(12, 10))
    grid = plt.GridSpec(3, 2, wspace=0.3, hspace=0.5)

    fig.suptitle(f'{platform_adi} Finansal Analiz ve Matematiksel Modelleme Raporu', fontsize=16, fontweight='bold')

    # Grafik 1: Kısmi Toplam (Sn) Eğrisi
    ax1 = fig.add_subplot(grid[0, :])
    ax1.plot(aylar, kismi_toplamlar_zamli, color='red', marker='o', markersize=3, label='Birikimli Maliyet (Sn)')
    ax1.fill_between(aylar, kismi_toplamlar_zamli, color='red', alpha=0.1)
    ax1.set_title('1. Birikimli Maliyet Eğrisi (Kısmi Toplam Analizi)')
    ax1.set_ylabel('Toplam Harcama (TL)')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend()

    # Grafik 2: Senaryo Karşılaştırması
    ax2 = fig.add_subplot(grid[1, 0])
    ax2.plot(aylar, kismi_toplamlar_sabit, color='blue', linestyle='--', label='Sabit Fiyat (Aritmetik)')
    ax2.plot(aylar, kismi_toplamlar_zamli, color='red', label='Zamlı (Geometrik)')
    ax2.set_title('2. Aritmetik vs. Geometrik Karşılaştırma')
    ax2.set_ylabel('Toplam Maliyet (TL)')
    ax2.legend()

    # Grafik 3: Parçalı Fonksiyon ve Basamaklı Yapı
    ax3 = fig.add_subplot(grid[1, 1])
    ax3.step(aylar, aylik_maliyetler_zamli, where='post', color='purple', label='Aylık Ödeme (Ayrık Veri)')
    ax3.axvspan(1, 3, color='yellow', alpha=0.2, label='İndirimli Periyot')
    ax3.set_title('3. Parçalı Fonksiyon ve Ayrık Veri Analizi')
    ax3.set_ylabel('Aylık Ücret (TL)')
    ax3.legend()

    # Grafik 4: Teknik Hata Analizi (Sapma)
    ax4 = fig.add_subplot(grid[2, :])
    sapma = np.array(hatali_kismi_toplamlar) - np.array(kismi_toplamlar_zamli)
    ax4.bar(aylar, sapma, color='gray', label='Birikimli Yuvarlama Farkı (Kuruş)')
    ax4.set_title('4. Teknik Analiz: Float Hassasiyeti ve Birikimli Sapma')
    ax4.set_xlabel('Zaman (Ay)')
    ax4.set_ylabel('Sapma (TL)')
    ax4.set_ylim(-0.05, 0.05)
    ax4.legend()

    # Manuel Yerleşim Düzenleme (Hata Veren tight_layout yerine)
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.6, wspace=0.3)

    print(f"\n--- Analiz Tamamlandı ---")
    print(f"Toplam Süre: {sure} Ay")
    print(f"Nihai Birikimli Maliyet: {kismi_toplamlar_zamli[-1]} TL")

    plt.show()


if __name__ == "__main__":
    kapsamli_abonelik_analizi_final()
