import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Abonelik:
    """Dijital aboneliklerin finansal verilerini ve zam senaryolarını

    modellemek için oluşturulmuş OOP (Nesne Yönelimli) sınıf mimarisi.
    """

    def __init__(self, ad, baslangic_fiyati):
        self.ad = ad
        self.baslangic_fiyati = baslangic_fiyati

    def maliyet_hesapla(self, ay_sayisi, yillik_zam_orani):
        """Aboneliğin zaman döngüsü içindeki yıllık zamlarını işleten

        ve aylık bazda harcama dizisini (a_n) üreten algoritma.
        """
        aylik_maliyetler = np.zeros(ay_sayisi)

        for ay in range(ay_sayisi):
            # Yıl hesabı: 0-11. aylar 0. yıl (zam yok), 12-23. aylar 1. yıl (%15 zamlı) vb.
            # Bu durum geometrik dizideki r^(yıl) çarpanına tam karşılık gelir.
            yil = ay // 12
            aylik_maliyetler[ay] = self.baslangic_fiyati * (
                (1 + yillik_zam_orani) ** yil
            )

        return aylik_maliyetler


class AbonelikSimulatoru:
    """Belirlenen senaryoları simüle eden, kısmi toplamları (S_n) hesaplayan

    ve veri analitiği kütüphaneleri ile görselleştirme yapan ana sistem.
    """

    def __init__(self, simulyasyon_suresi_ay=60):
        self.sure = simulyasyon_suresi_ay
        self.abonelikler = []

    def abonelik_ekle(self, abonelik):
        self.abonelikler.append(abonelik)

    def senaryo_calistir(self, yillik_zam_orani):
        """Tüm aboneliklerin maliyet dizilerini birleştirir ve

        numpy.cumsum kullanarak kısmi toplamlar serisini (S_n) hesaplar.
        """
        toplam_aylik_dizi = np.zeros(self.sure)

        for abonelik in self.abonelikler:
            toplam_aylik_dizi += abonelik.maliyet_hesapla(
                self.sure, yillik_zam_orani
            )

        # Matematiksel Temel: Kısmi Toplamlar Serisi (S_n)
        kismi_toplamlar = np.cumsum(toplam_aylik_dizi)

        aylar = np.arange(1, self.sure + 1)
        df = pd.DataFrame(
            {
                "Ay": aylar,
                "Aylik_Harcama_an": toplam_aylik_dizi,
                "Kismi_Toplam_Sn": kismi_toplamlar,
            }
        )

        return df


# ==========================================
# RAPORDAKİ DENEYLERİN TEST EDİLMESİ (60 AY)
# ==========================================

if __name__ == "__main__":
    print("--- Dijital Aboneliklerin Maliyeti Simülasyonu Başladı ---\n")

    plt.figure(figsize=(12, 7))

    # ------------------------------------------
    # DENEY 1: Baz Senaryo (Enflasyonsuz / Sabit Fiyat Modeli)
    # ------------------------------------------
    sim_deney1 = AbonelikSimulatoru(simulyasyon_suresi_ay=60)
    sim_deney1.abonelik_ekle(Abonelik("Toplam Sepet", 320))  # Aylık toplam 320 TL

    df_deney1 = sim_deney1.senaryo_calistir(yillik_zam_orani=0.00)
    deney1_sonuc = df_deney1["Kismi_Toplam_Sn"].iloc[-1]
    print(f"Deney 1 (Enflasyonsuz) 60. Ay Sonu Toplam Maliyet: {deney1_sonuc:,.2f} TL")

    # ------------------------------------------
    # DENEY 2: Reel Senaryo (Yıllık %15 Zamlı / Geometrik Yaklaşım)
    # ------------------------------------------
    sim_deney2 = AbonelikSimulatoru(simulyasyon_suresi_ay=60)
    sim_deney2.abonelik_ekle(Abonelik("Toplam Sepet", 320))  # Aylık toplam 320 TL

    df_deney2 = sim_deney2.senaryo_calistir(yillik_zam_orani=0.15)
    deney2_sonuc = df_deney2["Kismi_Toplam_Sn"].iloc[-1]
    print(f"Deney 2 (%15 Zamlı)     60. Ay Sonu Toplam Maliyet: {deney2_sonuc:,.2f} TL")

    # ------------------------------------------
    # DENEY 3: Agresif Senaryo (Aylık 1000 TL Sepet, %25 Zamlı)
    # ------------------------------------------
    sim_deney3 = AbonelikSimulatoru(simulyasyon_suresi_ay=60)
    sim_deney3.abonelik_ekle(Abonelik("Agresif Sepet", 1000))  # Aylık 1000 TL

    df_deney3 = sim_deney3.senaryo_calistir(yillik_zam_orani=0.25)
    deney3_sonuc = df_deney3["Kismi_Toplam_Sn"].iloc[-1]
    print(f"Deney 3 (%25 Zamlı)     60. Ay Sonu Toplam Maliyet: {deney3_sonuc:,.2f} TL")

    # ------------------------------------------
    # MATPLOTLIB İLE GÖRSELLEŞTİRME
    # ------------------------------------------
    plt.plot(
        df_deney1["Ay"],
        df_deney1["Kismi_Toplam_Sn"],
        label=f"Deney 1: Sabit Fiyat Modeli (%0 Zam) -> Sonuç: {deney1_sonuc:,.0f} TL",
        color="green",
        linewidth=2,
    )
    plt.plot(
        df_deney2["Ay"],
        df_deney2["Kismi_Toplam_Sn"],
        label=f"Deney 2: Reel Senaryo (%15 Zam) -> Sonuç: {deney2_sonuc:,.0f} TL",
        color="orange",
        linewidth=2.5,
    )
    plt.plot(
        df_deney3["Ay"],
        df_deney3["Kismi_Toplam_Sn"],
        label=f"Deney 3: Agresif Senaryo (%25 Zam) -> Sonuç: {deney3_sonuc:,.0f} TL",
        color="red",
        linewidth=2.5,
        linestyle="--",
    )

    # Grafik Tasarım Detayları
    plt.title(
        "Dijital Aboneliklerin Kümülatif Maliyeti: Serilerin Kısmi Toplam Analizi",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Zaman Parametresi (Ay - n)", fontsize=12)
    plt.ylabel("Kümülatif Toplam Maliyet (S_n - TL)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=11)
    plt.xticks(np.arange(0, 61, 12))

    print("\n[Bilgi] Grafik oluşturuldu. Doğrusal ve üstel kırılımları görebilirsiniz.")
    plt.show()