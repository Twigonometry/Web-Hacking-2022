drop table if exists users;
create table users (id int not null, username string, password string, primary key (id));
insert into users values (1, "admin", "b5c8737eaf2e2e52bec770d83f1e9b06");

drop table if exists comments;
create table comments (id int not null, comment string, userid string, primary key (id));