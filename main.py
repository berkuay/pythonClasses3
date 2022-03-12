"""sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

for harf in kelime:
    if harf in sesli_harfler:
        sayaç += 1

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, sayaç))"""



"""sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır():
    global sayaç
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır()))"""


"""sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır(sayaç)))"""


"""sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(n):
    for harf in kelime:
        if seslidir(harf):
            n += 1
    return n

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır(sayaç)))"""

sesli_harfler = 'aeıioöuü'
sayaç = 0

def kelime_sor():
    return input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç, kelime):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

def ekrana_bas(kelime):
    mesaj = "{} kelimesinde {} sesli harf var."
    print(mesaj.format(kelime, artır(sayaç, kelime)))

def çalıştır():
    kelime = kelime_sor()
    ekrana_bas(kelime)

çalıştır()