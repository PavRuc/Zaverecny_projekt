from vypis import Vypis  # importování třídy Vypis

vypis = Vypis()  # vložení třídy do proměnné

pokracovat = True  # přiřazení boolenovské hodnoty


spatne = "Nesprávné zadání. Zkuste to znovu.\n"  # vložení špatné odpovědi
neni = "\nHledaný pojištěnec se nenachází v seznamu. Pro návrat do hlavní nabídky stiskněte Enter\n"  # vložení špatné odpovědi do proměnné pro pozdější výpis, když nelze nalézt uživatele
velikost_sloupce = 12  # počet znaků v každém sloupci při výpisu pojištěných

# cyklus pro užívání aplikace dokud uživatel nezadá č. 4 - konec aplikace (False hodnota u Pokračovat)
while pokracovat:
    vypis.obrazovka_hlavicka_cela()  # vypsání hlavičky programu včetně výběru zadání
    spravne_zadani = False  # nastavení proměné
    while spravne_zadani != True:  # cyklus pro zadání správné odpovědi, dokud nebude zadána, bude se opakovat
        try:  # opatření proti špatné volbě požadavku
            vyber = int(input())  # musí být v menu zadáno pouze číslo - integer
            if vyber == 1:  # podmínka - pokud zvolíme v menu č. 1
                spravne_zadani = True  # již nebude splněna podmínka - provedli jsme správné zadání
                from pridat_pojisteneho import PridatPojisteneho  # importování třídy pro přidání nového pojištěného
                pridat_pojisteneho = PridatPojisteneho()  # náhraní třídy pro přidání pojištěného do proměnné
                pridat_pojisteneho.kompletni_zapis()  # zavolání funkce pro zápis nového pojištěného


            elif vyber == 2:  # podmínka - pokud zvolíme v menu č. 2
                pozice = -1  # nastavení proměnné, která pomůže s výpisem požadovaných indexů z listu
                vypis.obrazovka_hlavicka()  # vyčištění obrazovky a vypsání hlavičky - loga
                spravne_zadani = True  # již nebude splněna podmínka - provedli jsme správné zadání
                pojistenci = pridat_pojisteneho.__str__()  # načtení všech uložených/přidaných dat z třídy pridat_pojisteneho do proměnné pojistenci
                while pozice != (len(pojistenci) - 1):  # cyklus, který vypíše postupně všechny pojistence pod sebe
                    print("{0}{1}{2}{3}{4}{5}{6}".format(pojistenci[pozice + 1],
                                                         " " * (velikost_sloupce - len(pojistenci[pozice + 1])),
                                                         pojistenci[pozice + 2],
                                                         " " * (velikost_sloupce - len(pojistenci[pozice + 2])),
                                                         pojistenci[pozice + 3],
                                                         " " * (velikost_sloupce - len(str(pojistenci[pozice + 3]))),
                                                         pojistenci[pozice + 4]))
                    # výpis dat v uspořádaném formátu, každý sloupec nastaven na 15 znaků
                    pozice += 4  # po vypsání se posuneme o 4 indexy na dalšího pojistence
                print("\nPro návrat do hlavní nabídky stiskněte Enter\n")
                input()


            elif vyber == 3:  # podmínka - pokud zvolíme v menu č. 3
                spravne_zadani = True  # již nebude splněna podmínka - provedli jsme správné zadání
                vypis.obrazovka_hlavicka()  # vyčištění obrazovky a vypsání hlavičky - loga
                jmeno = input("Zadejte jméno pojištěného:\n")  # vstup pro hledání podle jména
                prijmeni = input("\nZadejte příjmení pojištěného:\n")  # vstup pro hledání podle příjmení
                vypis.obrazovka_hlavicka()  # vyčištění obrazovky a vypsání hlavičky - loga
                pojistenci = pridat_pojisteneho.__str__()  # načtení všech uložených/přidaných dat z třídy pridat_pojisteneho do proměnné pojistenci
                if (jmeno and prijmeni) in pojistenci:  # podmínka - pokud se zadané jméno a příjmení nachází v listu
                    index_jmeno = pojistenci.index(jmeno)  # zjištění indexu pro zadané jméno
                    index_prijmeni = pojistenci.index(prijmeni)  # zjištění indexu pro zadané příjmení
                    if (
                            index_prijmeni - index_jmeno) == 1:  # podmínka, že zadané jméno a příjmení musejí v listu být vedle sebe a tím pádem přísluší jednomu pojištěnci
                        print("{0}{1}{2}{3}{4}{5}{6}".format(pojistenci[index_jmeno],
                                                             " " * (velikost_sloupce - len(pojistenci[index_jmeno])),
                                                             pojistenci[index_prijmeni],
                                                             " " * (velikost_sloupce - len(pojistenci[index_prijmeni])),
                                                             pojistenci[index_prijmeni + 1], " " * (
                                                                         velikost_sloupce - len(
                                                                     str(pojistenci[index_prijmeni + 1]))),
                                                             pojistenci[index_prijmeni + 2]))
                        # výpis dat v uspořádaném formátu, každý sloupec nastaven na 15 znaků
                        print("\nPro návrat do hlavní nabídky stiskněte Enter\n")
                        input()
                    else:  # pokud jméno a příjmení nejsou v listu vedle sebe, vypíše informaci, že pojistenec není v listu
                        print(neni)
                        input()
                else:  # pokud nenajdeme jmeno a prijmeni v listu, vypíše informaci, že pojistenec není v listu
                    print(neni)
                    input()


            elif vyber == 4:  # podmínka - pokud zvolíme v menu č. 4
                spravne_zadani = True  # již nebude splněna podmínka - provedli jsme správné zadání
                pokracovat = False
                pass


            else:
                print(spatne)  # výpis hlášky o špatně zadaném vstupu v úvodním menu
        except:
            print(spatne)  # výpis hlášky o špatně zadaném vstupu v úvodním menu

vypis.obrazovka_hlavicka()
print("        Aplikace se ukončila. Hezký den. \n------------------------------------------------\n")




