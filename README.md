Operational Risk Anomaly Detection Project
​Proje Amacı ve Önemi
​Bu mini Python projesi, sorumlu yapay zekâ (Responsible AI) ve finansal sistemlerdeki operasyonel risklerin belirlenmesi amacıyla geliştirilmiştir. Amacımız, sadece finansal verilerdeki sıra dışı olayları (anomalileri) tespit etmek değil, aynı zamanda bu kararların yorumlanabilir olmasını sağlamaktır. Proje, şeffaflık ve güvenilirliği artırmayı hedeflemektedir.

​Kullanılan Algoritma
​Anomali tespiti için gözetimsiz öğrenme (Unsupervised Learning) algoritması olan Isolation Forest tercih edilmiştir. Bu algoritma, verimli ve hızlı bir şekilde aykırı değerleri izole etme yeteneği sayesinde, operasyonel risk senaryolarına mükemmel uyum sağlamaktadır.

​Kod Yapısı ve Uygulama
​Tüm kod yapısı risk-detector.py adlı tek dosyada yer almaktadır. Dosya, sentetik veri seti oluşturma (simulating operational risks), Isolation Forest modelinin eğitimi ve anomali skorlarının hesaplanması adımlarını içermektedir.

​Sonuçlar (Results)
​Kodun çalıştırılmasıyla elde edilen özet çıktılar results.txt dosyasında mevcuttur. Bu çıktı, modelin 220 veri noktasını işlediğini ve belirlenen kontaminasyon oranı (%10) dahilinde 22 operasyonel riski (anomaliyi) başarıyla tespit ettiğini göstermektedir.

​Yüksek Lisans Hedefi ile Bağlantı
​Bu çalışma, yüksek lisans tezimin temelini oluşturacak olan Yorumlanabilir Anomali Tespiti (Interpretable Anomaly Detection) çerçevesinin ilk adımıdır. Amacım, bu modeli SHAP gibi yöntemlerle genişleterek, her bir anomali için kesin ve gerekçeli açıklamalar sunmaktır.
