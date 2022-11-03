'''
Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
tersebut tampilkan bilangan terbesarnya. Gunakan statement if
x
'''
a = int(input('Masukkan bilangan A: '))
b = int(input('Masukkan bilangan B: '))
c = int(input('Masukkan bilangan C: '))

if a>b:
    print(a, 'lebih besar dari',b)
if a<b:
    print(a, 'lebih kecil dari',b)
if a>c:
    print(a, 'lebih besar dari',c)
if a<c:
    print(a, 'lebih kecil dari',c)
if b>a:
    print(b, 'lebih besar dari',b)
if b<a:
    print(b, 'lebih kecil dari',a)
if b>c:
    print(b, 'lebih besar dari',c)
if b<c:
    print(b, 'lebih kecil dari',c)
if c>a:
    print(c, 'lebih besar dari',a)
if c<a:
    print(c, 'lebih kecil dari',a)
if c>b:
    print(c, 'lebih besar dari',b)
if c<b:
    print(c, 'lebih kecil dari',b)
