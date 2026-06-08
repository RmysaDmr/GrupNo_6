import matplotlib.pyplot as plt


def abonelik_analizi(baslangic_fiyati, sure_ay, yillik_zam_orani):
    toplam_maliyet = 0
    aylik_liste = []
    mevcut_fiyat = baslangic_fiyati

    print("-" * 45)
    print(f"{'Ay':<5} | {'Aylık Ücret':<15} | {'Kümülatif Toplam':<15}")
    print("-" * 45)

    for ay in range(1, sure_ay + 1):
        # Ara Çıktı ve İşlem
        toplam_maliyet += mevcut_fiyat
        aylik_liste.append(toplam_maliyet)

        # Tablo çıktısını ekrana bas (Ara Çıktı)
        print(f"{ay:<5} | {mevcut_fiyat:<15.2f} | {toplam_maliyet:<15.2f}")

        # Her yıl başında (12, 24, 36. aylar) zam uygula
        if ay % 12 == 0:
            eski_fiyat = mevcut_fiyat
            mevcut_fiyat *= (1 + yillik_zam_orani)
            print(f"[Ara Bilgi] {ay}. ayda zam yapıldı: {eski_fiyat:.2f} -> {mevcut_fiyat:.2f}")

    return aylik_liste


# Senaryo Parametreleri
aylar = abonelik_analizi(baslangic_fiyati=200, sure_ay=24, yillik_zam_orani=0.25)

# Grafik Çıktısı
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(aylar) + 1), aylar, marker='s', linestyle='-', color='red', label='Toplam Maliyet')
plt.fill_between(range(1, len(aylar) + 1), aylar, color='red', alpha=0.1)
plt.title("Dijital Abonelik Maliyeti: Kısmi Toplam Analizi")
plt.xlabel("Zaman (Ay)")
plt.ylabel("Toplam Harcama (TL)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()