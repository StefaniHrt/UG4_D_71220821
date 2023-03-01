print('='*20, 'BARIS ARITMATIKA', '='*20)
awal=int(input('Masukkan bilangan awal:'))
selisih=int(input('Masukkan selisih bilangan:'))
suku=int(input('Masukkan banyaknya suku:'))
def baris_aritmatika(awal,suku,selisih):
    deret=suku/2*(2*awal+(suku-1)*selisih)
    return deret
print('Total dari deret aritmatika tersebut adalah :', baris_aritmatika(awal,suku,selisih))