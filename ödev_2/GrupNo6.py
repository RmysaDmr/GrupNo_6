import numpy as np
import matplotlib.pyplot as plt

# Aylık abonelik ücretleri (örnek)
abonelikler = {
    "Netflix": 150,
    "Spotify": 60,
    "YouTube Premium": 80
}

# Toplam aylık maliyet
aylik_toplam = sum(abonelikler.values())

# Kaç ay analiz edilecek
ay_sayisi = 12

# Aylar listesi
aylar = np.arange(1, ay_sayisi + 1)

# Kısmi toplam hesaplama (birikimli maliyet)
kismi_toplam = []

toplam = 0
for i in range(ay_sayisi):
    toplam += aylik_toplam
    kismi_toplam.append(toplam)

# Sonuçları yazdır
print("Aylık toplam maliyet:", aylik_toplam, "TL")
print("12 ay sonunda toplam maliyet:", toplam, "TL")

# Grafik çizimi
plt.plot(aylar, kismi_toplam, marker='o')
plt.title("Dijital Aboneliklerin Birikimli Maliyeti")
plt.xlabel("Ay")
plt.ylabel("Toplam Maliyet (TL)")
plt.grid()

plt.show()
