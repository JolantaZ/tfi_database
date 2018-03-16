create database Baza_TFI;
use Baza_tfi;
show tables;

create table Dane_uczestnika (
Nr_uczestnika int primary key auto_increment unique not null,
Imie varchar(30) not null,
Nazwisko varchar(30) not null,
Pesel varchar(11) unique,
Data_ur date not null
);
INSERT INTO `baza_tfi`.`dane_uczestnika` (`Nr_uczestnika`, `Imie`, `Nazwisko`, `Pesel`, `Data_ur`) 
VALUES ('222111', 'Maria', 'Kowalska', '73070305885', '1973-07-03');

create table Dane_teleadresowe (
Nr_uczestnika int primary key not null,
ulica varchar(30),
nr_domu varchar(10),
nr_lokalu varchar(10),
miejscowosc varchar(45),
kod_poczt varchar(10),
telefon varchar(15),
e_mail varchar(45),
FOREIGN key (Nr_uczestnika) references Dane_uczestnika (Nr_uczestnika)
);
INSERT INTO `baza_tfi`.`dane_teleadresowe` (`Nr_uczestnika`, `ulica`, `nr_domu`, `nr_lokalu`,
 `miejscowosc`, `kod_poczt`, `telefon`, `e_mail`) 
VALUES ('222111', 'Gen. Sikorskiego', '20', '23', 'Bydgoszcz', '23-870', '523738952', null);

create table Fundusze (
Nr_fund int PRIMARY KEY not null unique auto_increment,
Nr_uczestnika int not null,
Fundusz varchar(45),
Data_otwarcia date,
Data_zamkniecia date,
Status_fund varchar(20),
FOREIGN KEY (Nr_uczestnika) references Dane_uczestnika (Nr_uczestnika)
);
INSERT INTO `baza_tfi`.`fundusze` (`Nr_fund`, `Nr_uczestnika`, `Fundusz`, `Data_otwarcia`, `Data_zamkniecia`, `Status_fund`)
VALUES ('1', '222111', 'Skarbowy', '2015-02-09', NULL, 'Aktywny');

create table Salda_funduszy (
Nr_fund int primary key not null,
Data_wyceny date,
Status_fund varchar(20),
Saldo_pln float not null,
Saldo_ju int not null,
foreign key (Nr_fund) references Fundusze (Nr_fund)
);
INSERT INTO `baza_tfi`.`salda_funduszy` (`Nr_fund`, `Data_wyceny`, `Status_fund`, `Saldo_pln`, `Saldo_ju`)
VALUES ('1', '2018-02-08', 'Aktywny', '2434.43', '31');

create table Zlecenia (
Nr_zlecenia bigint primary key not null auto_increment,
Typ_zlecenia varchar(20) not null,
Data_zlec date not null,
Status_zlec varchar(20) not null,
Nr_fund int,
Nr_uczestnika int not null,
foreign key (Nr_fund) references Fundusze (Nr_fund),
FOREIGN KEY (Nr_uczestnika) references Dane_uczestnika (Nr_uczestnika)
);
INSERT INTO `baza_tfi`.`zlecenia` (`Nr_zlecenia`, `Typ_zlecenia`, `Data_zlec`, 
`Status_zlec`, `Nr_fund`, `Nr_uczestnika`) 
VALUES ('1230000001', 'Otwarcie', '2007-04-06', 'Przetworzone', '21', '222123');

create table uczestnik_login (
nr_uczestnika int primary key,
haslo varchar(15) not null,
data_utw date not null,
typ_dostepu varchar(15) default 'uczestnik',
foreign key (nr_uczestnika) references dane_uczestnika (nr_uczestnika)
);
select * from uczestnik_login;

insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222111','12mako',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222112','13maro',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222113','14wosi',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222114','15krzi',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222115','16anby',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222116','17szja',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222117','18jali',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222118','19maza',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222119','20dour',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222120','21tepa',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222121','22majo',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222122','23kaso',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222123','24elwi',curdate());
insert into uczestnik_login (nr_uczestnika,haslo,data_utw) values ('222124','25pibu',curdate());


create table admin_login (
id_admin int primary key auto_increment,
a_login varchar(10) not null,
a_haslo varchar(15) not null,
data_utw date not null,
typ_dostepu varchar(15) default 'admin'
);
insert into admin_login (a_login,a_haslo,data_utw) values ('jzych','baza2018',curdate());
insert into admin_login (a_login,a_haslo,data_utw) values ('admin2','test2018',curdate());

use baza_tfi;


# I widok - pełne dane wszystkich uczestników
CREATE VIEW pelne_dane_ucz as
SELECT 
    ucz.Imie, ucz.Nazwisko, ucz.Pesel, ucz.Data_ur, ad.*
FROM
    dane_uczestnika AS ucz
        NATURAL JOIN
    dane_teleadresowe AS ad;
    
    
#II widok - dane o funduszach uczestników
CREATE VIEW fundusze_uczestnikow as
SELECT 
    fund.nr_uczestnika,
    fund.Nr_fund,
    ucz.Imie,
    ucz.Nazwisko,
    ucz.Pesel,
    ucz.Data_ur,
    fund.Fundusz,
    fund.Data_otwarcia,
    fund.Data_zamkniecia,
    fund.Status_fund
FROM
    dane_uczestnika AS ucz
        NATURAL JOIN
    fundusze AS fund;
    
    
#III widok -  wszystkie aktywne fundusze uczestników z saldem
CREATE VIEW fundusze_salda as
SELECT 
    ucz.nr_uczestnika,
    ucz.imie,
    ucz.nazwisko,
    fund.fundusz,
    sal.*
FROM
    dane_uczestnika AS ucz
        NATURAL JOIN
    fundusze AS fund
        NATURAL JOIN
    salda_funduszy AS sal
WHERE
    sal.status_fund = 'Aktywny';



# ZAPYTANIA
# z konta uczestnika:
# podejrzenie danych konktretnego uczestnika
SELECT 
    ucz.nr_uczestnika AS 'Nr uczestnika',
    ucz.Imie,
    ucz.Nazwisko,
    ucz.Pesel,
    ucz.Data_ur AS 'Data urodzenia',
    ad.ulica AS 'Ulica',
    ad.nr_domu AS 'Nr domu',
    ad.nr_lokalu AS 'Nr lokalu',
    ad.miejscowosc AS 'Miejscowość',
    ad.kod_poczt AS 'Kod pocztowy',
    ad.telefon AS Telefon,
    ad.e_mail AS 'E-mail'
FROM
    dane_uczestnika AS ucz
        NATURAL JOIN
    dane_teleadresowe AS ad
WHERE
    ucz.Nr_uczestnika = 222111;

    
#dane o funduszach konkretnego uczestnika
SELECT 
    fund.nr_uczestnika AS 'Nr uczestnika',
    fund.Nr_fund AS 'Nr funduszu',
    ucz.Imie,
    ucz.Nazwisko,
    ucz.Pesel,
    ucz.Data_ur AS 'Data urodzenia',
    fund.Fundusz,
    fund.Data_otwarcia AS 'Data otwarcia',
    fund.Data_zamkniecia AS 'Data zamknięcia',
    fund.Status_fund AS 'Status'
FROM
    dane_uczestnika AS ucz
        NATURAL JOIN
    fundusze AS fund
WHERE
    fund.nr_uczestnika = 222116;

    
# wszystkie aktywne fundusze z saldem dla danego uczestnika
SELECT 
    ucz.nr_uczestnika as 'Nr uczestnika',
    ucz.imie as 'Imię',
    ucz.nazwisko as 'Nazwisko',
    fund.fundusz as 'Fundusz',
    sal.Nr_fund as 'Nr funduszu',
    sal.Data_wyceny as 'Data wyceny',
    sal.Status_fund as 'Status',
    sal.Saldo_pln as 'Sadlo w PLN',
    sal.Saldo_ju as 'Saldo w j.u.'
FROM
    dane_uczestnika AS ucz
        NATURAL JOIN
    fundusze AS fund
        NATURAL JOIN
    salda_funduszy AS sal
WHERE
    sal.status_fund = 'Aktywny'
        AND ucz.Nr_uczestnika = 222117;

# wszystkie fundusze z saldem dla danego uczestnika
SELECT 
    ucz.nr_uczestnika,
    ucz.imie,
    ucz.nazwisko,
    fund.fundusz,
    sal.Nr_fund as 'Nr funduszu',
    sal.Data_wyceny as 'Data wyceny',
    sal.Status_fund as 'Status',
    sal.Saldo_pln as 'Sadlo w PLN',
    sal.Saldo_ju as 'Saldo w j.u.'
FROM
    dane_uczestnika AS ucz
        NATURAL JOIN
    fundusze AS fund
        NATURAL JOIN
    salda_funduszy AS sal
WHERE
    ucz.Nr_uczestnika = 222112;
    
    
#historia zleceń - zlecenia dla konkretnego nr funduszu
SELECT 
    Nr_zlecenia AS 'Nr zlecenia',
    Nr_fund AS 'Nr funduszu',
    Typ_zlecenia AS 'Typ zlecenia',
    Data_zlec AS 'Data zlecenia',
    Status_zlec AS 'Status'
FROM
    zlecenia
WHERE
    Nr_fund = 10
GROUP BY Data_zlec asc;
    
# wszystkie zlecenia dla danego uczestnika
SELECT 
    Nr_zlecenia AS 'Nr zlecenia',
    Nr_fund AS 'Nr funduszu',
    Typ_zlecenia AS 'Typ zlecenia',
    Data_zlec AS 'Data zlecenia',
    Status_zlec AS 'Status'
FROM
    zlecenia
WHERE
    Nr_uczestnika = 222114;


# Zapytania z konta admina:
#widoki
select * from pelne_dane_ucz;
select * from fundusze_uczestnikow;
select * from fundusze_salda;

# dane o funduszach uczestników z możliwością filtrowania po statusie funduszu
SELECT 
    fund.nr_uczestnika,
    fund.Nr_fund,
    ucz.Imie,
    ucz.Nazwisko,
    ucz.Pesel,
    ucz.Data_ur,
    fund.Fundusz,
    fund.Data_otwarcia,
    fund.Data_zamkniecia,
    fund.Status_fund
FROM
    dane_uczestnika AS ucz
        NATURAL JOIN
    fundusze AS fund
    where status_fund='Aktywny';
# z filtrowaniem po statusie funduszu: where status_fund='Aktywny','Zamkniety';


# wszystkie zlecenia malejąco
select * from zlecenia
order by Data_zlec desc;

# lub wszystkie zlecenia po statusie zlecenia (malejąco)
select * from zlecenia
where Status_zlec='Odrzucone'
order by Data_zlec desc; # 'Przetworzone','Odrzucone'


# wszystkie zlecenia dla danego uczestnika
SELECT 
    Nr_zlecenia AS 'Nr zlecenia',
    Nr_fund AS 'Nr funduszu',
    Typ_zlecenia AS 'Typ zlecenia',
    Data_zlec AS 'Data zlecenia',
    Status_zlec AS 'Status'
FROM
    zlecenia
WHERE
    Nr_uczestnika = 222114;


use baza_tfi;
# TRIGGERY
# po uaktualnieniu danych osobowych tworzy się zlecenie 'Zmiana danych' do tabeli zlecenia
delimiter $$
create trigger zm_danych
after update on dane_uczestnika 
for each row
insert into zlecenia
set typ_zlecenia='Zmiana danych', data_zlec=curdate(), status_zlec = 'Przetworzone', nr_uczestnika=old.nr_uczestnika;
$$
delimiter ;;
#test
#update dane_uczestnika set imie = 'Dorota Julia' where nr_uczestnika=222119;
#select * from zlecenia;


#po uaktualnieniu danych teleadresowych tworzy się zlecenie 'Zmiana danych' do tabeli zlecenia
delimiter $$
create trigger zm_danych_tele
after update on dane_teleadresowe
for each row
insert into zlecenia
set typ_zlecenia='Zmiana danych', data_zlec=curdate(), status_zlec = 'Przetworzone', nr_uczestnika=old.nr_uczestnika;
$$
delimiter ;;
#test
# update `baza_tfi`.`dane_teleadresowe` set e_mail=null where nr_uczestnika=222111;
#select * from zlecenia;

# tworzenie danych do logowania dla uczestnika
create trigger nowy_ucz
after insert on dane_uczestnika
for each row
insert into uczestnik_login set Nr_uczestnika = new.nr_uczestnika, haslo='password', data_utw=curdate(); 
#test
# INSERT INTO `baza_tfi`.`dane_uczestnika` (`Imie`, `Nazwisko`, `Pesel`, `Data_ur`) 
#VALUES ('Marika', 'Kowaalaal', '73070305855', '1973-07-03');


