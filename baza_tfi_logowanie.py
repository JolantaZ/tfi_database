# -*- coding: utf-8 -*-
import pymysql

class Uczestnik:
        
    def selectu_dane(self):
        self.c.execute('SELECT ucz.nr_uczestnika, ucz.Imie, ucz.Nazwisko, ucz.Pesel, ucz.Data_ur, ad.ulica, ad.nr_domu, ad.nr_lokalu, ad.miejscowosc, ad.kod_poczt, ad.telefon, ad.e_mail FROM dane_uczestnika AS ucz NATURAL JOIN dane_teleadresowe AS ad WHERE ucz.Nr_uczestnika =' + '\'' +  str(login) + '\'')
        for row in self.c.fetchall():
            print('%6s %12s %15s %11s %12s %20s %3s %3s %15s %8s %12s %15s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
    def selectu_danefun(self):
        self.c.execute('SELECT fund.nr_uczestnika, fund.Nr_fund, ucz.Imie, ucz.Nazwisko, ucz.Pesel, ucz.Data_ur, fund.Fundusz, fund.Data_otwarcia, fund.Data_zamkniecia, fund.Status_fund FROM dane_uczestnika AS ucz NATURAL JOIN fundusze AS fund WHERE fund.nr_uczestnika = ' + '\'' +  str(login) + '\'')
        for row in self.c.fetchall():
            print('%6s %3s %12s %15s %11s %12s %20s %12s %12s %10s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    def selectu_aktywne(self):
        self.c.execute('SELECT ucz.nr_uczestnika, ucz.imie, ucz.nazwisko, fund.fundusz, sal.Nr_fund, sal.Data_wyceny, sal.Status_fund, sal.Saldo_pln, sal.Saldo_ju FROM dane_uczestnika AS ucz NATURAL JOIN fundusze AS fund NATURAL JOIN salda_funduszy AS sal WHERE sal.status_fund = "Aktywny" AND ucz.Nr_uczestnika = ' + '\'' +  str(login) + '\'')
        for row in self.c.fetchall():
            print('%6s %12s %15s %20s %3s %12s %10s %10s %5s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    def selectu_saldafun(self):
        self.c.execute('SELECT ucz.nr_uczestnika, ucz.imie, ucz.nazwisko, fund.fundusz, sal.Nr_fund, sal.Data_wyceny, sal.Status_fund, sal.Saldo_pln, sal.Saldo_ju FROM dane_uczestnika AS ucz NATURAL JOIN fundusze AS fund NATURAL JOIN salda_funduszy AS sal WHERE ucz.Nr_uczestnika = ' + '\'' +  str(login) + '\'')
        for row in self.c.fetchall():
            print('%6s %12s %15s %20s %3s %12s %10s %10s %5s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    def selectu_zlecenia(self):
        self.c.execute('SELECT * FROM zlecenia WHERE nr_uczestnika = ' + '\'' +  str(login) + '\'')
        for row in self.c.fetchall():
            print('%15s %15s %12s %15s %5s %6s' % (row[0],row[1],row[2],row[3],row[4], row[5]))
            
uczestnik = Uczestnik();
            
class Admin:
        
    def selecta_dane(self):
        self.c.execute('select * from pelne_dane_ucz;')
        for row in self.c.fetchall():
            print('%15s %15s %11s %12s %6s %20s %3s %3s %15s %8s %12s %15s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
    def selecta_fund(self):
        self.c.execute('select * from fundusze_uczestnikow;')
        for row in self.c.fetchall():
            print('%6s %3s %15s %15s %11s %12s %20s %12s %12s %15s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    def selecta_aktywne(self):
        self.c.execute('select * from fundusze_salda;')
        for row in self.c.fetchall():
            print('%6s %15s %15s %20s %3s %12s %12s %10s %5s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    def selecta_zlecenia(self):
        self.c.execute('SELECT * FROM zlecenia order by Data_zlec desc;')
        for row in self.c.fetchall():
            print('%15s %15s %12s %15s %5s %6s' % (row[0],row[1],row[2],row[3],row[4], row[5]))
            
    def selectu_dane2(self, nr_uczestnika):
        self.c.execute('SELECT ucz.nr_uczestnika, ucz.Imie, ucz.Nazwisko, ucz.Pesel, ucz.Data_ur, ad.ulica, ad.nr_domu, ad.nr_lokalu, ad.miejscowosc, ad.kod_poczt, ad.telefon, ad.e_mail FROM dane_uczestnika AS ucz NATURAL JOIN dane_teleadresowe AS ad WHERE ucz.Nr_uczestnika = %s;', nr_uczestnika)
        for row in self.c.fetchall():
            print('%6s %12s %15s %11s %12s %20s %3s %3s %15s %8s %12s %15s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
    def selectu_danefun2(self, nr_uczestnika):
        self.c.execute('SELECT fund.nr_uczestnika, fund.Nr_fund, ucz.Imie, ucz.Nazwisko, ucz.Pesel, ucz.Data_ur, fund.Fundusz, fund.Data_otwarcia, fund.Data_zamkniecia, fund.Status_fund FROM dane_uczestnika AS ucz NATURAL JOIN fundusze AS fund WHERE fund.nr_uczestnika =  %s;', nr_uczestnika)
        for row in self.c.fetchall():
            print('%6s %3s %12s %15s %11s %12s %20s %12s %12s %10s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    def selectu_aktywne2(self, nr_uczestnika):
        self.c.execute('SELECT ucz.nr_uczestnika, ucz.imie, ucz.nazwisko, fund.fundusz, sal.Nr_fund, sal.Data_wyceny, sal.Status_fund, sal.Saldo_pln, sal.Saldo_ju FROM dane_uczestnika AS ucz NATURAL JOIN fundusze AS fund NATURAL JOIN salda_funduszy AS sal WHERE sal.status_fund = "Aktywny" AND ucz.Nr_uczestnika =  %s;', nr_uczestnika)
        for row in self.c.fetchall():
            print('%6s %12s %15s %20s %3s %12s %10s %10s %5s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    def selectu_zlecenia2(self, nr_uczestnika):
        self.c.execute('SELECT * FROM zlecenia WHERE nr_uczestnika =  %s;', nr_uczestnika)
        for row in self.c.fetchall():
            print('%15s %15s %12s %15s %5s %6s' % (row[0],row[1],row[2],row[3],row[4], row[5]))            
            
    def insert(self):
        try:
            imie = input('imię: ')
            nazwisko = input('nazwisko: ')
            pesel = int(input('pesel: '))
            data_ur = input('data urodzenia (YYYY-MM-DD): ')
            self.c.execute("INSERT INTO dane_uczestnika (imie, nazwisko, pesel, data_ur) VALUES (%s, %s, %s, %s);", (imie,nazwisko,pesel, data_ur))
            self.conn.commit()
            self.c.execute("Select * from dane_uczestnika;")
            for row in self.c.fetchall():
                print('%6s %15s %15s %11s %12s' % (row[0],row[1],row[2],row[3],row[4]))
        except:
            print('Podaj poprawne dane! ')
            
    def insert2(self):
        try:
            nruczst = input('Podaj nr uczestnika:  ')
            ulica = input('ulica: ')
            nrdom = input('nr domu: ')
            nrlok = input('nr lokalu: ')
            miejsce = input('miejscowość: ')
            kod = input('kod pocztowy: ')
            tel = input('telefon kontaktowy: ')
            mail = input('adres e-mail: ')
            self.c.execute("INSERT INTO dane_teleadresowe (nr_uczestnika,ulica, nr_domu, nr_lokalu, miejscowosc, kod_poczt, telefon, e_mail) values (%s, %s, %s, %s, %s, %s, %s, %s); ", (nruczst,ulica,nrdom,nrlok,miejsce,kod,tel,mail))
            self.conn.commit()
            self.c.execute("Select * from pelne_dane_ucz;")
            for row in self.c.fetchall():
                print('%15s %15s %11s %12s %6s %20s %3s %3s %15s %8s %12s %15s' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        except:
            print('Podaj poprawne dane! ')
                

admin = Admin();


class Baza_tfi(Admin, Uczestnik):
    def __init__(self):
        while(True):
            menu = input('1.Zaloguj 2.Wyjdź  ')
            if(menu =='2'):
                print('Zakończyłeś sesję przeglądania ')
                break
            self.connOpen()
            typ_dostepu = self.login()
            if(typ_dostepu.upper() == 'ADMIN'):
                while(True):
                    dec1 = input('1.Przeglądaj  2.Wprowadź dane  3.Wyloguj  ')
                    if(dec1 == '1'):
                        menu = input('1. Dane uczestników 2.Fundusze uczestników 3.Aktywne z saldem 4.Historia zleceń 5.Wróć  ')
                        if(menu == '1'):
                            quest1 = input('1. Wszystkie 2.Wyszukaj 3.Wróć ')
                            if(quest1 == '1'):
                                self.selecta_dane()
                                quest1 = input('1. Wszystkie 2.Wyszukaj 3.Wróć ')
                            elif(quest1 == '2'):
                                self.selectu_dane2(self.user())
                                quest1 = input('1. Wszystkie 2.Wyszukaj 3.Wróć ')
                            elif(quest1 == '3'):
                                menu = input('1. Dane uczestników 2.Fundusze uczestników 3.Aktywne z saldem 4.Historia zleceń 5.Wróć  ')
                            else:
                                print('Wybierz jedną z opcji! ')    
                        elif(menu == '2'):
                            quest2 = input('1. Wszystkie 2.Wyszukaj 3.Wróć')
                            if(quest2 == '1'):
                                self.selecta_fund()
                                quest2 = input('1. Wszystkie 2.Wyszukaj 3.Wróć')
                            elif(quest2 == '2'):
                                self.selectu_danefun2(self.user())
                                quest2 = input('1. Wszystkie 2.Wyszukaj 3.Wróć')
                            elif(quest2 == '3'):
                                menu = input('1. Dane uczestników 2.Fundusze uczestników 3.Aktywne z saldem 4.Historia zleceń 5.Wróć  ')
                            else:
                                print('Wybierz jedną z opcji! ')
                        elif(menu == '3'):
                            quest3 = input('1. Wszystkie 2.Wyszukaj 3.Wróć ')
                            if(quest3 == '1'):
                                self.selecta_aktywne()
                                quest3 = input('1. Wszystkie 2.Wyszukaj 3.Wróć ')
                            elif(quest3 == '2'):
                                self.selectu_aktywne2(self.user()) 
                                quest3 = input('1. Wszystkie 2.Wyszukaj 3.Wróć ')
                            elif(quest2 == '3'):
                                menu = input('1. Dane uczestników 2.Fundusze uczestników 3.Aktywne z saldem 4.Historia zleceń 5.Wróć ')
                            else:
                                print('Wybierz jedną z opcji! ')
                        elif(menu == '4'):
                            quest4 = input('1. Wszystkie 2.Wyszukaj 3.Wróć ')
                            if(quest4 == '1'):
                                self.selecta_zlecenia()
                            elif(quest4 == '2'):
                                self.selectu_zlecenia2(self.user())
                            elif(quest2 == '3'):
                                menu = input('1. Dane uczestników 2.Fundusze uczestników 3.Aktywne z saldem 4.Historia zleceń 5.Wróć ')
                            else:
                                print('Wybierz jedną z opcji! ')
                        elif(menu == '5'):
                            dec1 = input('1.Przeglądaj  2.Wprowadź dane  3.Wyloguj  ')
                        else:
                            print('Wybierz jedną z opcji! ')
                    elif(dec1 == '2'):
                        menu2 = input('1.Dane osobowe 2.Dane teleadresowe 3.Wróć ')
                        if(menu2 == '1'):
                            self.insert()
                        elif(menu2 == '2'):
                            self.insert2()
                        elif(menu2 == '3'):
                            dec1 = input('1.Przeglądaj  2.Wprowadź dane  3.Wyloguj  ')
                        else:
                            print('Wybierz jedną z opcji! ')
                        
                    elif(dec1 == '3'):
                        self.connClose()
                        print('Zostałeś wylogowany! ')
                        break
                    else:
                        print('Zły wybór! Spróbuj ponownie ')
            elif(typ_dostepu.upper() == 'UCZESTNIK'):
                while(True):
                    dec2 = input('1.Dane osobowe 2.Fundusze 3.Historia Zleceń 4.Wyloguj ')
                    if(dec2 == '1'):
                        self.selectu_dane()
                    elif(dec2 == '2'):
                        menu3 = input('1.Historia funduszy 2. Aktywne z saldem 3.Wszystkie z saldem 4.Wróć  ')
                        if(menu3 == '1'):
                            self.selectu_danefun()
                        elif(menu3 == '2'):
                            self.selectu_aktywne()
                        elif(menu3 == '3'):
                            self.selectu_saldafun()
                        elif(menu3 == '4'):
                            dec2 = input('1.Dane osobowe 2.Fundusze 3.Historia Zleceń 4.Wyloguj ')
                        else:
                            print('Wybierz jedną z opcji! ')
                    elif(dec2 == '3'):
                        self.selectu_zlecenia()
                    elif(dec2 == '4'):
                        self.connClose()
                        print('Zostałeś wylogowany! ')
                        break
                    else:
                        print('Zły wybór! Spróbuj ponownie ')
            else:
                print('Błędne dane logowania! ')
                        
               
                        
                      
            
        
    def connOpen(self):
        self.conn = pymysql.connect('localhost','root','backdev','baza_tfi')
        self.c = self.conn.cursor()
    def login(self):
        global login
        login = input('Podaj login: ')
        haslo = input('Wprowadź hasło: ')
        self.c.execute("select typ_dostepu from admin_login where login=%s and haslo=%s union select typ_dostepu from uczestnik_login  where login=%s and haslo=%s;",(login,haslo,login,haslo))
        try:
            typ_dostepu = self.c.fetchall()[0][0]
        except:
            typ_dostepu = '0'
        return typ_dostepu
    
    def user(self):
        nr_ucz = input('Podaj numer uczestnika: ')
        self.c.execute("select nr_uczestnika from uczestnik_login  where nr_uczestnika = %s;", nr_ucz)
        try:
            nr_uczestnika = self.c.fetchall() [0][0]
        except:
            nr_uczestnika = '0'
        return nr_uczestnika
    

    def connClose(self):
        self.conn.close()
        

baza = Baza_tfi()