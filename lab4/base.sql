
create table User(
	id integer PRIMARY KEY autoincrement,
	number varchar(12) NOT NULL ,
	name varchar(20) NOT NULL,
	surname varchar(20) NOT NULL
);

create table Personal(
	id integer primary key autoincrement,
	number varchar(12) not null ,
	name varchar(20) not null,
	surname varchar(20) not null,
	power_level integer not null
);

create table Ticket(
	id integer primary key autoincrement,
	excursionId integer not null,
	userId integer not null,
	price integer not null,
	foreign key (excursionId) references Excursion(id),
	foreign key (userId) references User(id) 
);

create table Excursion(
	id integer primary key autoincrement,
	date_start date,
	museumId integer not null,
	presonalId integer not null,
	foreign key (museumId) references Museum(id)	
	foreign key (presonalId) references Personal(id)
);

create table Museum(
	id integer primary key autoincrement,
	name varchar(256) not null
);

insert into Museum (name) 
	values ("Historical Museum"), ("Weapons Museum");
insert into User (name, surname, number)
	values ("UserName1", "UserSurname1", "1234567890"), ("UserName2", "UserSurname2", "1253567892");
insert into Personal (name, surname, number, power_level) 
	values ('PresonalName1', 'presonalSurname1', '88055598233', 1);
insert into Excursion (museumId, presonalId, date_start) 
	values (1, 1,'2020-20-02'), (2, 2,'2020-20-02');
insert into Ticket (excursionId, userId, price) 
	values(1, 1, 2500),(2, 2, 2500)