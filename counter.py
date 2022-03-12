class Counter:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuü'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

    def kelime_sor(self):
        return input("Bir kelime giriniz")

    def çalıştır(self):
        self.kelime = self.kelime_sor()

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac += 1
            if self.sessizdir(harf)
                self.sayac_sesiz +=1
        return self.sayac

    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} sesli harf var."
        print(mesaj.format(self.kelime, self.artır()))


if __name__ == '__main__':
    sayaç = Counter()
    sayaç.çalıştır()
