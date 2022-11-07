'''
Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
tersebut tampilkan bilangan terbesarnya. Gunakan statement if
Uraikan langkah atau algoritmanya pada file README.md, sertakan juga flowchart
dan screenshot hasil eksekusi program. Tampilkan 3 kondisi inputan data.
'''
print ('Program mengurutkan data')
a = int(input('Masukkan bilangan A: '))
b = int(input('Masukkan bilangan B: '))
c = int(input('Masukkan bilangan C: '))

if a>b:
    print(a, 'lebih besar dari',b)
elif a<b:
    print(a, 'lebih kecil dari',b)
elif a>c:
    print(a, 'lebih besar dari',c)
elif a<c:
    print(a, 'lebih kecil dari',c)
elif b>a:
    print(b, 'lebih besar dari',a)
elif b<a:
    print(b, 'lebih kecil dari',a)
elif b>c:
    print(b, 'lebih besar dari',c)
elif b<c:
    print(b, 'lebih kecil dari',c)
elif c>a:
    print(c, 'lebih besar dari',a)
elif c<a:
    print(c, 'lebih kecil dari',a)
elif c>b:
    print(c, 'lebih besar dari',b)
elif c<b:
    print(c, 'lebih kecil dari',b)
print('Urutan bilangan dari terkecil hingga terbesar: ')