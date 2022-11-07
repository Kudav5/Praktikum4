# modul 3
d = 0
while True:
    a = int(input('Masukkan bilangan / 0: '))
    if d < a:
        d = a
    if a==0:
        break
print('bilangan terbesar: ',d)