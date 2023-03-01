kalimat=input('Masukkan sebuah kalimat:').split()
def kata_terpanjang(kalimat):
    kata=max(kalimat, key=len)
    return kata
print('Kata terpanjang dalam kalimat tersebut adalah:',kata_terpanjang(kalimat))