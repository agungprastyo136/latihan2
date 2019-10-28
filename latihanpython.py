Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input("masukan nilai 80:")
masukan nilai 80:
>>> b=input("masukan nilai 20:")
masukan nilai 20:
>>> print("variable 80=",a)
variable 80= 
>>> print("variable 20=",b)
variable 20= 
>>> print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))
TypeError: %d format: a number is required, not str
>>> print("hasil penggabungan {1}&{0}=%d".format(80,20) %(80+20))
hasil penggabungan 20&80=100
>>> 
>>> #konversi nilai variable
>>> a=int(80)
>>> b=int(20)
>>> print("hasil penjumlahan {1}+{0}=%d".format(80,20) %(80+20))
hasil penjumlahan 20+80=100
>>> print("hasil pembagian {1}/{0}=%d".format(80,20) %(80/20))
hasil pembagian 20/80=4
>>> 
