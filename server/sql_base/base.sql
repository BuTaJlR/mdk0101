
create table User(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null
);

create table Personal(
	id integer primary key autoincrement,
	login varchar(16) not null unique,
	password varchar(16) not null,
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
insert into User (login, password)
	values ("UserName1", "1234"), ("UserName2", "1234");
insert into Personal (login, password, power_level) 
	values ('PresonalName1' , '1234', 1), ('PresonalName2' , '1234', 2);
insert into Excursion (museumId, presonalId) 
	values (1, 1), (2, 2);
insert into Ticket (excursionId, userId, price) 
	values(1, 1, 2500),(2, 2, 2500);
