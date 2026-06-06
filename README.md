# 📊 Dijital Aboneliklerin Maliyeti: Seriler ve Kısmi Toplam Analizi

Bursa Uludağ Üniversitesi Matematik Bölümü Bitirme Projesi (Grup 6)

## 🎯 Projenin Amacı ve Tanımı
Bu proje; dijital abonelik platformlarının (Netflix, Spotify, Adobe vb.) mikro ödeme politikalarını ve kümülatif bütçe yüklerini **Seriler Teorisi**, **Kısmi Toplamlar ($S_n$)** ve **Parçalı Fonksiyonlar** ekseninde analitik olarak modelleyen Python tabanlı bir simülasyon aracıdır. Tüketicilerin "doğrusal (aritmetik)" zannettiği pasif harcamaların, periyodik şirket zamları ve finansal çarpanlarla nasıl "üstel (geometrik)" bir seriye dönüştüğünü matematiksel ve teknik olarak ispatlar.

---

## 🛠️ Programın Kurulumu ve Çalıştırılması

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla takip ediniz:

### 1. Depoyu Klonlayın (Repository Clone)
İlk olarak GitHub üzerindeki bu projeyi bilgisayarınıza indirin:
```bash
git clone [https://github.com/KULLANICI_ADINIZ/REPINIZIN_ADI.git](https://github.com/KULLANICI_ADINIZ/REPINIZIN_ADI.git)
cd REPINIZIN_ADI
2. Gerekli Kütüphaneleri YükleyinProgramın çalışması için gerekli olan bağımlılıkları terminal veya komut satırı üzerinden yükleyin:Bashpip install matplotlib numpy
3. Programı ÇalıştırınKurulum tamamlandıktan sonra ana scripti tetikleyin:Bashpython nihai_proje_savunma_motoru.py
Program sizden terminal üzerinden platform adı, başlangıç ücreti ve tahmini yıllık zam oranı gibi dinamik parametreleri isteyecektir.📚 Kullanılan Kütüphaneler ve FonksiyonlarıProjenin matematiksel hesaplama ve görselleştirme katmanlarında iki temel bilimsel kütüphane kullanılmıştır:NumPy (Numerical Python):Kullanım Amacı: Süreç içindeki ayları ayrık veri (discrete data) kümeleri olarak yönetmek, vektörel dizi işlemlerini hızlı bir şekilde gerçekleştirmek ve float hassasiyeti analizlerinde matrisel farkları hesaplamak için kullanılmıştır.Kritik Fonksiyon: np.arange() yardımıyla zaman ekseni ($n$) matematiksel bir indis dizisine dönüştürülmüştür.Matplotlib (pyplot):Kullanım Amacı: Hesaplanan kısmi toplam dizilerinin ($S_n$), aritmetik-geometrik makas analizlerinin ve parçalı fonksiyon kırılımlarının jüriye sunulacak akademik grafik çıktılarına dönüştürülmesini sağlar.Kritik Fonksiyonlar: Üstel büyüme için plt.plot(), ayrık veri yapısını göstermek için plt.step() ve float sapmalarını doğrulamak için plt.bar() fonksiyonları dinamik bir GridSpec mimarisiyle birleştirilmiştir.💾 Veritabanı ve Veri Seti YapısıVeritabanı Yapısı: Bu proje, statik ve sınırlı bir veritabanı (SQL/NoSQL) mimarisi yerine Dinamik Kullanıcı Etkileşimli Giriş Motoru (input()) kullanmaktadır. Bu sayede sabit bir veri tabanına bağımlı kalınmaksızın, pazar dinamiklerine göre değişen her türlü abonelik senaryosu anlık olarak simüle edilebilmektedir.Kullanılan Veri Seti: Projede kullanılan başlangıç fiyatı ve zam parametreleri, güncel dijital platformların (Örn: Netflix TR, Spotify TR) resmi web sitelerindeki reel fiyat listeleri referans alınarak anlık simülasyon girdisi olarak tanımlanmaktadır. Güncel fiyat takipleri için platformların resmi kullanıcı sözleşmeleri ve fiyat politikası sayfaları baz alınmıştır.
