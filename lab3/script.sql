drop table if exists User;
drop table if exists Personal;
drop table if exists Ticket;
drop table if exists Excursion;
drop table if exists Museum;
drop table if exists Exhibit;
drop table if exists Exhibit_expansion;

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
