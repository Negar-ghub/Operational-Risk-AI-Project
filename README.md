Operasyonel Risk Anomali Tespiti (Operational Risk Anomaly Detection)
Proje Amacı ve Önemi
Bu mini Python projesi, sorumlu yapay zekâ (Responsible AI) ve finansal sistemlerdeki operasyonel risklerin belirlenmesi amacıyla geliştirilmiştir. Amacımız, sadece finansal verilerdeki sıra dışı olayları (anomalileri) tespit etmek değil, aynı zamanda bu kararların yorumlanabilir olmasını sağlamaktır. Proje, şeffaflık ve güvenilirliği artırmayı hedeflemektedir.
Kullanılan Algoritma: Isolation Forest
Anomali tespiti için gözetimsiz öğrenme (Unsupervised Learning) algoritması olan Isolation Forest tercih edilmiştir. Bu algoritma, verimli ve hızlı bir şekilde aykırı değerleri izole etme yeteneği sayesinde, operasyonel risk senaryolarına mükemmel uyum sağlamaktadır.
Kod Yapısı ve Uygulama
•	main.py: Veri seti yükleme, Isolation Forest modelinin eğitimi ve anomali skorlarının hesaplanması.
•	data_simulation.py: Proje için gerçek dünya operasyonel risklerini taklit eden sentetik veri setinin oluşturulması.
Yüksek Lisans Hedefi ile Bağlantı
Bu çalışma, yüksek lisans tezimin temelini oluşturacak olan Yorumlanabilir Anomali Tespiti (Interpretable Anomaly Detection) çerçevesinin ilk adımıdır. Amacım, bu modeli SHAP gibi yöntemlerle genişleterek, her bir anomali için kesin ve gerekçeli açıklamalar sunmaktır.

