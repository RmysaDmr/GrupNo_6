import matplotlib.pyplot as plt
import numpy as np

def abonelik_analizi_yap(ay_sayisi=24):
    aylar = np.arange(1, ay_sayisi + 1)
    baslangic_fiyati = 100

    # --- SENARYO 1: LİNEER ARTIŞ (Aritmetik Dizi) ---
    # Her ay sabit 10 TL zam yapıldığını varsayıyoruz.
    artis_miktari = 10
    lineer_maliyetler = baslangic_fiyati + (aylar - 1) * artis_miktari
    lineer_toplam = np.cumsum(lineer_maliyetler) # Kısmi toplamlar (Sn)

    # --- SENARYO 2: GEOMETRİK ARTIŞ (Enflasyonist Model) ---
    # Her ay %5 zam yapıldığını varsayıyoruz (r = 1.05).
    artis_orani = 1.05
    geometrik_maliyetler = baslangic_fiyati * (artis_orani ** (aylar - 1))
    geometrik_toplam = np.cumsum(geometrik_maliyetler) # Kısmi toplamlar (Sn)

    # --- SENARYO 3: BASAMAKLI MODEL (İndirimli Başlangıç) ---
    # İlk 6 ay 50 TL, sonraki aylar 180 TL sabit fiyat.
    basamakli_maliyetler = np.where(aylar <= 6, 50, 180)
    basamakli_toplam = np.cumsum(basamakli_maliyetler) # Kısmi toplamlar (Sn)

    # --- GRAFİK ÇİZİMLERİ ---
    plt.figure(figsize=(15, 10))
    plt.suptitle(f"{ay_sayisi} Aylık Dijital Abonelik Maliyet Analizi", fontsize=16)

    # Grafik 1: Aylık Ödeme Miktarları Karşılaştırması
    plt.subplot(2, 2, 1)
    plt.plot(aylar, lineer_maliyetler, 'g-o', label='Lineer (+10 TL/Ay)')
    plt.plot(aylar, geometrik_maliyetler, 'r-s', label='Geometrik (%5 Zam)')
    plt.step(aylar, basamakli_maliyetler, 'b-', where='post', label='Basamaklı Model')
    plt.title("Aylık Fiyat Değişimleri")
    plt.xlabel("Ay")
    plt.ylabel("Birim Fiyat (TL)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Grafik 2: Birikimli Toplam Maliyet (Kısmi Toplamlar - Sn)
    plt.subplot(2, 2, 2)
    plt.fill_between(aylar, lineer_toplam, color="green", alpha=0.2, label='Lineer Toplam')
    plt.fill_between(aylar, geometrik_toplam, color="red", alpha=0.2, label='Geometrik Toplam')
    plt.fill_between(aylar, basamakli_toplam, color="blue", alpha=0.2, label='Basamaklı Toplam')
    plt.plot(aylar, lineer_toplam, 'g--')
    plt.plot(aylar, geometrik_toplam, 'r--')
    plt.plot(aylar, basamakli_toplam, 'b--')
    plt.title("Toplam Ödenen Miktar (Kısmi Toplamlar)")
    plt.xlabel("Ay")
    plt.ylabel("Toplam Maliyet (TL)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Grafik 3: Model Farklarının Analizi (Geometrik vs Lineer Farkı)
    plt.subplot(2, 2, (3, 4))
    fark = geometrik_toplam - lineer_toplam
    plt.bar(aylar, fark, color='orange', label='Maliyet Farkı (Geo - Lin)')
    plt.axhline(0, color='black', linewidth=1)
    plt.title("Geometrik ve Lineer Model Arasındaki Birikimli Maliyet Farkı")
    plt.xlabel("Ay")
    plt.ylabel("Fark (TL)")
    plt.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # Terminal Çıktıları
    print("-" * 30)
    print(f"{ay_sayisi} Ay Sonundaki Sonuçlar:")
    print(f"Lineer Model Toplam: {lineer_toplam[-1]:.2f} TL")
    print(f"Geometrik Model Toplam: {geometrik_toplam[-1]:.2f} TL")
    print(f"Basamaklı Model Toplam: {basamakli_toplam[-1]:.2f} TL")
    print("-" * 30)

# Fonksiyonu çalıştır
if __name__ == "__main__":
    abonelik_analizi_yap(24)