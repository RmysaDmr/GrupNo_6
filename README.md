Markdown# 📊 Dijital Aboneliklerin Maliyeti: Seriler ve Kısmi Toplam Analizi

Bursa Uludağ Üniversitesi Matematik Bölümü Bitirme Projesi (Grup 6)

## 🎯 Projenin Amacı ve Tanımı
Bu proje; dijital abonelik platformlarının (Netflix, Spotify, Adobe vb.) mikro ödeme politikalarını ve kümülatif bütçe yüklerini **Seriler Teorisi**, **Kısmi Toplamlar ($S_n$)** ve **Parçalı Fonksiyonlar** ekseninde analitik olarak modelleyen Python tabanlı bir simülasyon aracıdır. Tüketicilerin "doğrusal (aritmetik)" zannettiği pasif harcamaların, periyodik şirket zamları ve finansal çarpanlarla nasıl "üstel (geometrik)" bir seriye dönüştüğünü matematiksel ve teknik olarak ispatlar.

---

## 🛠️ 1. Programın Detaylı Kurulumu ve Çalıştırılması

Projenin yerel bilgisayarınızda (PyCharm, VS Code veya Terminal üzerinde) sorunsuz çalışabilmesi için aşağıdaki adımların sırasıyla uygulanması gerekmektedir:

* **Adım 1: Python Ortamının Kontrolü:** Sisteminizde Python 3.8 veya üzeri bir sürümün kurulu olduğundan emin olun. Komut satırından `python --version` yazarak kontrol edebilirsiniz.
* **Adım 2: Deponun (Repository) Yerel Bilgisayara İndirilmesi:** GitHub üzerindeki bu projeyi kendi bilgisayarınıza çekmek için terminale aşağıdaki komutu yazın veya ZIP olarak indirin:
```bash
git clone [https://github.com/RmysaDmr/GrupNo_6.git](https://github.com/RmysaDmr/GrupNo_6.git)
cd GanttNo_6
Adım 3: Sanal Ortam Oluşturma (Opsiyonel): Proje bağımlılıklarının bilgisayarınızdaki diğer projelerle çakışmaması için PyCharm içinde veya terminalde bir sanal ortam (venv) oluşturabilirsiniz:Bashpython -m venv venv
Adım 4: Gerekli Paketlerin Yüklenmesi: Programın matematiksel hesaplama ve grafik motorunun çalışması için gereken paketleri pip paket yöneticisiyle sisteme kurun:Bashpip install numpy matplotlib
Adım 5: Programın Tetiklenmesi: Kurulum tamamlandıktan sonra ana scripti çalıştırarak dinamik veri giriş panelini başlatın:Bashpython nihai_proje_savunma_motoru.py
📚 2. Programda Kullanılan Kütüphaneler ve Teknik İşlevleriProjede dış bağımlılık olarak kullanılan bilimsel kütüphaneler ve bunların matematiksel modelimizdeki birebir görevleri aşağıda detaylandırılmıştır:A) NumPy (Numerical Python)Vektörel Hesaplama Çekirdeği: Dönem süreçlerini ve ayları tek tek döngüye sokmak yerine, zaman parametresini ($n$) doğrusal bir vektör dizisi olarak işlemek için np.arange() fonksiyonu kullanılmıştır.Ayrık Veri Analizi: Analiz derslerinde teorik olarak işlenen "ayrık veri (discrete data)" kümelerinin bilgisayar belleğinde yüksek performanslı matrisler (Arrays) halinde tutulmasını sağlar.Hassasiyet Analizi: Float (kayan nokta) veri tipindeki kuruş bazlı sapmaları doğrulamak amacıyla matrisel fark işlemlerinde (np.array() dönüşümleriyle) aktif rol oynamıştır.B) Matplotlib (pyplot)Kısmi Toplam ($S_n$) Görselleştirmesi: Hesaplanan kümülatif bütçe yükünü zamana bağlı olarak üstel bir eğri şeklinde çizmek için plt.plot() fonksiyonundan yararlanılmıştır.Aritmetik ve Geometrik Makas Analizi: Sabit fiyat varsayımı (Aritmetik Dizi) ile zamlı gerçek senaryo (Geometrik Seri) arasındaki maliyet makasını jürinin net görebileceği şekilde iki farklı katmanda kıyaslar.Parçalı Fonksiyon ve Basamak Modellemesi: Abonelik ödemelerinin sürekli bir fonksiyon olmadığını, aylık periyotlarda kesikli adımlarla ilerlediğini göstermek adına plt.step() (basamak grafiği) yapısı kullanılmıştır. Ayrıca ilk 3 aylık indirim bölgesini vurgulamak için plt.axvspan() ile alan boyaması yapılmıştır.Gelişmiş Panel Tasarımı: Tüm bu analiz çıktılarının tek bir pencerede akademik bir rapor düzeninde sunulabilmesi için plt.GridSpec() mimarisiyle 4 farklı grafik paneli tek ekrana entegre edilmiştir.💾 3. Veritabanı ve Veri Seti YapısıVeritabanı Yapısı: Bu proje, statik ve sınırlı bir veritabanı (SQL/NoSQL) mimarisi yerine Dinamik Tullanıcı Etkileşimli Giriş Motoru (input()) kullanmaktadır. Bu sayede sabit bir veri tabanına bağımlı olunmaksızın, pazar dinamiklerine göre değişen her türlü abonelik senaryosu anlık olarak simüle edilebilmektedir.Kullanılan Veri Seti: Projede kullanılan başlangıç fiyatı ve zam parametreleri, güncel dijital platformların (Örn: Netflix TR, Spotify TR) resmi web sitelerindeki reel fiyat listeleri referans alınarak anlık simülasyon girdisi olarak tanımlanmaktadır. Güncel fiyat takipleri için platformların resmi kullanıcı sözleşmeleri ve fiyat politikası sayfaları baz alınmıştır.
