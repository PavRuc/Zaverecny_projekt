from vypis import Vypis

class PridatPojisteneho:

    # metoda pro zadání křestního jména a zapsání na psolední místo seznamu, lze zadat libovolné znaky a libovolný počet
    def pridat_krestni(self):
        self.krestni = input("Zadejte křestní jméno pojištěného:\n")
        data_pojistencu.append(self.krestni)

    # metoda pro zadání příjmení a zapsání na psolední místo seznamu, lze zadat libovolné znaky a libovolný počet
    def pridat_prijemni(self):
        self.prijmeni = input("Zadejte příjmení pojištěného:\n")
        data_pojistencu.append(self.prijmeni)

    # metoda pro zadání tel. čísla a zapsání na psolední místo seznamu, ošetření, aby možný vsup byl pouze integer
    def pridat_telefon(self):
        self.spravne = False
        while self.spravne != True:
            try:
                self.telefon = int(input("Zadejte telefonní číslo pojištěného:\n"))
                self.spravne = True
            except:
                print("Špatný formát telefonního čísla. Zadejte pouze číslice:\n")
        data_pojistencu.append(self.telefon)

    # metoda pro zadání věku a zapsání na psolední místo seznamu, ošetření, aby možný vsup byl pouze integer v rozmězí 0 - 110 (let pojistence)
    def pridat_vek(self):
        self.spravne = False
        while self.spravne != True:
            try:
                self.vek = int(input("Zadejte věk pojištěného:\n"))
                if self.vek > 0 and self.vek < 110:
                    self.spravne = True
                else:
                    print("Špatný formát věku. Zadejte pouze číslice od 0 do 110 \n")
                    self.spravne = False
            except:
                print("Špatný formát věku. Použijte pouze číslice):\n")
        data_pojistencu.append(self.vek)


    # motoda, která se zavolá ze souboru main a díky které postupně zadáme všechny potřebné vstupy
    # obsahuje také vyčištění obrazovky a nahrání hlavičky na závěr a potvrzení o úspěšném přidání pojištěnce
    def kompletni_zapis(self):
        vypis.obrazovka_hlavicka()
        pridat_pojisteneho.pridat_krestni()
        pridat_pojisteneho.pridat_prijemni()
        pridat_pojisteneho.pridat_telefon()
        pridat_pojisteneho.pridat_vek()
        vypis.obrazovka_hlavicka()
        print("Nový pojištěnec uložen!\n\nPokračujte klávesou Enter")
        input()

    # magická metoda str, kterou budeme volat ze souboru main a které nám do proměnných bude ukládat celou databázi / list se všemi daty uživatelů
    def __str__(self):
        return data_pojistencu

pridat_pojisteneho = PridatPojisteneho()
vypis = Vypis()


data_pojistencu = []




