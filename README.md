# Optical Mark Recognition (OMR)
 

## Uygulanan Yöntem
1. Yerelde kayıtlı optik görüntüsü programa dahil edildi.
2. Bir txt uzantılı dosyadan cevap anahtarı okundu.
3. Optik görüntüsü görüntü işlemye sokulmadan önce boyutları düzenlendi.
4. Görüntünün renk uzayı gri(gray) olarak ayarlandı.
5. Görüntü Gauss Süzgeci(Gaussian Blur) ile gürültülerden temizlendi.
6. Görüntü Canny kenar bulma algoritması ile çizgileri belirgin kılındı.
7. Görüntüden kontour bulma ile şekiller tespit edildi.
8. Tespit edilen şekillerin dörtgen ve belirli değerden fazla alana sahip olanlar filtrelendi.
9. Gerekli koşulu sağlayan dörtgenler bir listede alanlarına göre büyükten küçüğe sıralandı.
10. En büyük alana sahip olanın cevap şıkları alanı ikinci büyük olanın öğrenci numarası alanı olduğu biliniyor.
11. Bu alanların köşeleri tekrar organize edilerek bir perspektif dönüşümü gerçekleştirildi.
12. Bu dönüşümn ardından eşik değeri ile ikili(binary) hale dönüştürüldü.
13. Öğrenci numarası alanı için 10x10 luk bir alana sahip olduğunda 10x10 şeklinde parçalara ayrıldı ve her bir parçanın bir işaret alanını temsil ettiği bir listeye eklendi.
14. Cevap işaretleme kısmı 3 bloktan oluştuğu için önce 3 ayrı blok şeklinde ayrıldı. Her bir blok 5 şık + 1 soru sayısı ile 20 soru şeklinde olduğu için 6 dikey 20 yatay parçaya ayrılarak işaretleme alanlarının ayrılması sağlandı.
15. Ayrılan her parçanın beyaz piksel değeri kontrol edilerek rakip parça ile karşılaştırması sonucu en büyük değere sahip olanın işaretli olduğu varsayıldı.
16. İşaretli parçaların indexlerine göre hangi şık ve soruya ait olduğu tespit edilip cevap anahtarı ile karşılaştırıldı.

## Görüntü İşleme Aşamaları
Original Image           |  Gray Image | Blur Image
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/bozkurtmert0/optical-mark-recognition/blob/main/images/0019060365___0.jpg)  |  ![](https://github.com/bozkurtmert0/optical-mark-recognition/blob/main/images/0019060365___1.jpg)  |  ![](https://github.com/bozkurtmert0/optical-mark-recognition/blob/main/images/0019060365___2.jpg)

Canny Image           |  Contour Image | Find Rectangle
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/bozkurtmert0/optical-mark-recognition/blob/main/images/0019060365___3.jpg)  |  ![](https://github.com/bozkurtmert0/optical-mark-recognition/blob/main/images/0019060365___4.jpg)  |  ![](https://github.com/bozkurtmert0/optical-mark-recognition/blob/main/images/0019060365___5.jpg)



Biggest Rectangle            |  Second Biggest Rectangle
:-------------------------:|:-------------------------:
![](https://github.com/bozkurtmert0/optical-mark-recognition/blob/main/images/0019060365___6.jpg)  |  ![](https://github.com/bozkurtmert0/optical-mark-recognition/blob/main/images/0019060365___7.jpg)



## Kaynakça

* BELAG, I. A., GÜLTEPE, Y., AND ELMALTI, T. M. An image processing based
optical mark recognition with the help of scanner. International Journal of Engineering
Innovation & Research 7, 2 (2018).
* ÇELIK, N. C. Yapay görme tabanlı optik form de ̆gerlendirme yöntemi. Master’s thesis,
Eski ̧sehir Teknik Üniversitesi, 2019.
* DE ASSIS ZAMPIROLLI, F., GONZALEZ, J. A. Q., AND DE OLIVEIRA NEVES, R. P.
Automatic correction of multiple-choice tests using digital cameras and image proces-
sing. Universidade Federal do ABC (2010)
* KONUK, M. S. Android tabanlı Mobil Optik Okuma Test Okuma Sisteminin geli ̧stiril-
mesi Ve uygulaması. PhD thesis, Marmara Universitesi (Turkey), 2019
* KRISHNA, G., RANA, H. R., MADAN, I., AND SAHU, R. Implementation of omr
technology with the help of ordinary scanner. international journal of advanced research
in computer science and software engineering 3, 4 (2013)
* KÜÇÜKKARA, Z., AND TÜMER, A. E. An image processing oriented optical mark
recognition and evaluation system. International Journal of Applied Mathematics
Electronics and Computers 6, 4 (2018)
* KUMAR, A., SINGAL, H., AND BHAVSAR, A. Cost effective real-time image proces-
sing based optical mark reader. International Journal of Computer and Information
Engineering 12, 9 (2018),
* RONG, W., LI, Z., ZHANG, W., AND SUN, L. An improved canny edge detection
algorithm. In 2014 IEEE International Conference on Mechatronics and Automation
(2014)
* SENOL, M., AND F ̇IDAN, U. C# ile web kameradan optik form okuma (025101)(1-
10). Afyon Kocatepe Üniversitesi Fen Ve Mühendislik Bilimleri Dergisi
*  YÜKSEL, A. S., ÇANKAYA,  ̇I. A., YALÇINKAYA, M. A., AND ATE  ̧S, N. Mobil
tabanlı optik form de ̆gerlendirme sistemi. Pamukkale University Journal of Engineering
Sciences 22
