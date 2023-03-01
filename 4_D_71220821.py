b=list(input('Masukkan sekumpulan bilangan (pisahkan dengan koma):').split(','))
bil=[]
for i in b:
    B=int(i)
    bil.append(B)
terbesar=lambda bil: max(bil)
terkecil=lambda bil: min(bil)
print('Bilangan terbesar dari kumpulan bilangan yang di input adalah', terbesar(bil))
print('Bilangan terkecil dari kumpulan bilangan yang di input adalah', terkecil(bil))