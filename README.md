# TDK Sozluk Python Tkinter Projesi

Program TDK Sozluk veritabanına request atarak girilen kelimenin anlamlarını fetchledikten sonra kullanıcıya gösterir. 

sozluk.gov.tr'ye request atarken sorun yaşadığım için: 
```
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
``` 
Payloadını ekleyerek sorunu çözdüm.
