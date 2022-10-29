
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
	exhibitId integer not null,
	foreign key (museumId) references Museum(id)	
	foreign key (presonalId) references Personal(id)
	foreign key (exhibitId) references Exhibit_expansion(exhibitId)
);

create table Museum(
	id integer primary key autoincrement,
	name varchar(256) not null,
	exhibitId integer not null
);

create table Exhibit(
	id integer primary key autoincrement,
	museumId integer not null,
	name varchar(20),
	discription varchar(256),
	foreign key (museumId) references Museum(id)
);

create table Exhibit_expansion(
	id integer primary key autoincrement,
	exhibitId integer not null,
	excursionId integer not null,
	foreign key (exhibitId) references Exhibit(id)
	foreign key (excursionId) references Excursion(id)
);

insert into Museum (name, exhibitId) 
	values ("Historical Museum",1), ("Weapons Museum",1);
insert into User (name, surname, number)
	values ("UserName1", "UserSurname1", "1234567890"), ("UserName2", "UserSurname2", "1253567892");
insert into Personal (name, surname, number, power_level) 
	values ('PresonalName1', 'presonalSurname1', '88055598233', 1);
insert into Excursion (museumId, presonalId, date_start, exhibitId) 
	values (1, 1,'2020-20-02',1), (2, 2,'2020-20-02',1);
insert into Ticket (excursionId, userId, price) 
	values(1, 1, 2500),(2, 2, 2500);
insert into Exhibit(museumId, name, discription)
	values(1,"exName1","exDiscriptrion");
insert into Exhibit_expansion(exhibitId, excursionId)
	values(1,1);
