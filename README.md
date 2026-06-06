# Yapay Sinir Ağları (YSA) - Ders Notları

Yapay Sinir Ağları (YSA), insan beyninin bilgi işleme yapısını taklit ederek öğrenme, genelleme yapma ve veri arasındaki ilişkileri keşfetme yeteneğine sahip bilgisayar sistemleridir.

---

## 1. Temel Kavramlar ve Tanımlar

### Yapay Sinir Hücresi (Perceptron / Adaline)
Bir yapay sinir hücresi temel olarak şu bileşenlerden oluşur:
* **Girdiler ($x_i$):** Dış dünyadan veya diğer hücrelerden gelen veriler.
* **Ağırlıklar ($w_i$):** Her bir girdinin hücre üzerindeki önem derecesini veya etkisini belirleyen katsayılar.
* **Net Girdi (NET):** Girdilerin ağırlıklarla çarpılıp toplanması ve üzerine sapma (bias) değerinin eklenmesiyle elde edilen değer.
* **Aktivasyon Fonksiyonu ($f$):** Net girdiyi işleyerek hücrenin nihai çıktısını üreten doğrusal olmayan fonksiyon.
* **Çıktı ($y$):** Hücrenin ürettiği sonuç.

### Bias (Sapma/Eşik) Nedir?
Bias ($b$ veya $w_0$), ağın girdiler sıfır olduğunda bile bir çıktı üretebilmesini sağlayan, orijinden kayma miktarını belirleyen sabit bir değerdir. Matematiksel olarak işlemleri kolaylaştırmak için genellikle $x_0 = 1$ girdisine sahip $w_0$ ağırlığı olarak modele eklenir.

---

## 2. Aktivasyon Fonksiyonları

Aktivasyon fonksiyonları, ağa **doğrusalsızlık (non-linearity)** kazandırır. Bu sayede ağ, karmaşık ve doğrusal olmayan problemleri öğrenebilir.

### Sık Kullanılan Aktivasyon Fonksiyonları:

1.  **Doğrusal (Linear) Fonksiyon:**
    $$f(\text{NET}) = c \cdot \text{NET}$$
    Çıktıyı değiştirmeden veya sabit bir katsayıyla çarparak iletir.

2.  **Adım (Step / Threshold) Fonksiyonu:**
    $$f(\text{NET}) = \begin{cases} 1, & \text{NET} \ge \theta \\ 0, & \text{NET} < \theta \end{cases}$$
    Belirlenen bir eşik değerine ($\theta$) göre çıktı 0 veya 1 olur.

3.  **İşaret (Signum) Fonksiyonu:**
    $$f(\text{NET}) = \begin{cases} 1, & \text{NET} \ge 0 \\ -1, & \text{NET} < 0 \end{cases}$$
    Net girdi pozitifse 1, negatifse -1 çıktısı üretir.

4.  **Sigmoid (Lojistik) Fonksiyonu:**
    $$f(\text{NET}) = \frac{1}{1 + e^{-\text{NET}}}$$
    Çıktıyı $(0, 1)$ aralığına sıkıştırır. Türevi kolay alınabildiği için geri yayılım algoritmasında sıkça tercih edilir.

5.  **Hiperbolik Tanjant (Tanh) Fonksiyonu:**
    $$f(\text{NET}) = \tanh(\text{NET}) = \frac{e^{\text{NET}} - e^{-\text{NET}}}{e^{\text{NET}} + e^{-\text{NET}}}$$
    Çıktıyı $(-1, 1)$ aralığına sıkıştırır. Merkezinin 0 olması nedeniyle genellikle Sigmoid'den daha iyi performans gösterir.

---

## 3. Öğrenme Kuralları ve Algoritmalar

YSA'da öğrenme, ağın verilen girdilere doğru çıktıları üretebilmesi için **ağırlıkların ($w$) optimize edilmesi (güncellenmesi)** sürecidir.

### Hebb Öğrenme Kuralı (Hebb Heuristic)
"Birlikte ateşlenen hücreler, birlikte bağlanır" prensibine dayanır. Eğer bir girdi hücresi ve çıktı hücresi aynı anda aktifse, aralarındaki ağırlık artırılır.
$$\Delta w_i = \alpha \cdot x_i \cdot y$$
$$w_i(t+1) = w_i(t) + \Delta w_i$$
*(Burada $\alpha$ öğrenme katsayısı, $x_i$ girdi, $y$ ise çıktıdır.)*

### Delta Öğrenme Kuralı (En Küçük Kareler / LMS)
Beklenen çıktı ($d$) ile mevcut çıktı ($y$) arasındaki hatayı (error) minimize etmeye çalışır. Gradyan inişi (Gradient Descent) yöntemini kullanır.
$$\text{Hata } (e) = d - y$$
$$\Delta w_i = \alpha \cdot (d - y) \cdot x_i$$
$$w_i(t+1) = w_i(t) + \Delta w_i$$

---

## 4. El Yazısı Notlar ve Matematiksel Çözümler

### Tek Katmanlı Ağda İleri Besleme Denklem Formatı
Sistem matris formunda şu şekilde modellenir:
$$\text{NET} = X \cdot W^T + b$$

Açık yazımı:
$$\text{NET} = x_1w_1 + x_2w_2 + \dots + x_nw_n + b$$
$$y = f(\text{NET})$$

---

### ÖRNEK ÇÖZÜM 1: Mantıksal VE (AND) Kapısı Problemi
Tek katmanlı bir perceptron ile AND kapısı fonksiyonunun modellenmesi:

**Girdi ve Beklenen Çıktı Tablosu:**
| $x_1$ | $x_2$ | Beklenen Çıktı ($d$) |
| :---: | :---: | :------------------: |
|   0   |   0   |          0           |
|   0   |   1   |          0           |
|   1   |   0   |          0           |
|   1   |   1   |          1           |

**Başlangıç Parametreleri:**
* Ağırlıklar: $w_1 = 0.3$, $w_2 = -0.1$
* Bias (Eşik): $b = w_0 = -0.2$ ($x_0 = 1$ kabul edilmiştir)
* Öğrenme Katsayısı: $\alpha = 0.5$
* Aktivasyon Fonksiyonu: Adım (Step) Fonksiyonu ($\text{NET} \ge 0 \rightarrow 1$, aksi halde $0$)

#### 1. İterasyon (Adım Adım Hesaplama):

* **1. Veri Seti için: $(x_1=0, x_2=0) \rightarrow d=0$**
    $$\text{NET} = (x_1 \cdot w_1) + (x_2 \cdot w_2) + b$$
    $$\text{NET} = (0 \cdot 0.3) + (0 \cdot (-0.1)) + (-0.2) = -0.2$$
    Çıktı: $y = f(-0.2) = 0$
    Hata: $e = d - y = 0 - 0 = 0$ (Hata yok, ağırlıklar değişmez)

* **2. Veri Seti için: $(x_1=0, x_2=1) \rightarrow d=0$**
    $$\text{NET} = (0 \cdot 0.3) + (1 \cdot (-0.1)) + (-0.2) = -0.3$$
    Çıktı: $y = f(-0.3) = 0$
    Hata: $e = d - y = 0 - 0 = 0$ (Hata yok, ağırlıklar değişmez)

* **3. Veri Seti için: $(x_1=1, x_2=0) \rightarrow d=0$**
    $$\text{NET} = (1 \cdot 0.3) + (0 \cdot (-0.1)) + (-0.2) = 0.1$$
    Çıktı: $y = f(0.1) = 1$
    Hata: $e = d - y = 0 - 1 = -1$ (**HATA VAR! Güncelleme yapılacak**)

    **Ağırlık Güncelleme:**
    $$\Delta w_1 = \alpha \cdot e \cdot x_1 = 0.5 \cdot (-1) \cdot 1 = -0.5$$
    $$\Delta w_2 = \alpha \cdot e \cdot x_2 = 0.5 \cdot (-1) \cdot 0 = 0$$
    $$\Delta b = \alpha \cdot e \cdot 1 = 0.5 \cdot (-1) \cdot 1 = -0.5$$

    **Yeni Değerler:**
    $$w_1^{\text{yeni}} = 0.3 + (-0.5) = -0.2$$
    $$w_2^{\text{yeni}} = -0.1 + 0 = -0.1$$
    $$b^{\text{yeni}} = -0.2 + (-0.5) = -0.7$$

---

### ÖRNEK ÇÖZÜM 2: Matris Formunda Delta Kuralı Uygulaması

Girdi vektörü $X = [0.5, -1.2, 0.8]$, Mevcut Ağırlık Vektörü $W = [0.1, 0.3, -0.2]$, Bias $b = 0.4$, Hedef Çıktı $d = 1$, Öğrenme katsayısı $\alpha = 0.2$ ve Aktivasyon fonksiyonu doğrusal ($f(x)=x$) olsun.

1.  **Net Girdi Hesabı:**
    $$\text{NET} = (0.5 \cdot 0.1) + (-1.2 \cdot 0.3) + (0.8 \cdot (-0.2)) + 0.4$$
    $$\text{NET} = 0.05 - 0.36 - 0.16 + 0.4 = -0.07$$
2.  **Çıktı ve Hata Hesabı:**
    $$y = f(-0.07) = -0.07$$
    $$\text{Hata } (e) = d - y = 1 - (-0.07) = 1.07$$
3.  **Delta Kuralına Göre Güncelleme:**
    $$\Delta w_1 = 0.2 \cdot 1.07 \cdot 0.5 = 0.107 \rightarrow w_1^{\text{yeni}} = 0.1 + 0.107 = 0.207$$
    $$\Delta w_2 = 0.2 \cdot 1.07 \cdot (-1.2) = -0.2568 \rightarrow w_2^{\text{yeni}} = 0.3 - 0.2568 = 0.0432$$
    $$\Delta w_3 = 0.2 \cdot 1.07 \cdot 0.8 = 0.1712 \rightarrow w_3^{\text{yeni}} = -0.2 + 0.1712 = -0.0288$$
    $$\Delta b = 0.2 \cdot 1.07 \cdot 1 = 0.214 \rightarrow b^{\text{yeni}} = 0.4 + 0.214 = 0.614$$

---

## 5. Çok Katmanlı Yapay Sinir Ağları (MLP)

Doğrusal olarak ayrılamayan (Örn: Özel VEYA / XOR Kapısı) problemleri çözmek için girdi ve çıktı katmanları arasına **Gizli Katmanlar (Hidden Layers)** eklenir.
