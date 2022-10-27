insert into Museum (name) values ("Эрмитаж");
insert into Museum (name) values ("Государственная Третьяковская галерея");
insert into Museum (name) values ("Оружейная палата");

insert into User (name, surname, number) values ("Иван", "Иванов", "1234567890");
insert into User (name, surname, number) values ("Дементьев", "Святовлав", "1324567891");
insert into User (name, surname, number) values ("Бирюков", "Антон", "1253567892");

insert into Personal (name, surname, number, power_level) values ('Попов', 'Юрий', '89964854865', 1);
insert into Personal (name, surname, number, power_level) values ('Кондаков', 'Никита', '88055598233', 2);
insert into Personal (name, surname, number, power_level) values ('Каскинов', 'Марат', '89047493536', 2);

insert into Excursion (museumId, presonalId, date_start) values (1, 1,'2020-20-02');
insert into Excursion (museumId, presonalId, date_start) values (2, 2,'2020-20-02');
insert into Excursion (museumId, presonalId, date_start) values (3, 3,'2020-20-02');

insert into Ticket (excursionId, userId, price) values (1, 1, 2500);
insert into Ticket (excursionId, userId, price) values (2, 2, 2500);
insert into Ticket (excursionId, userId, price) values (3, 3, 2500);
