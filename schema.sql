drop table if exists updates;
create table updates (
  id integer primary key autoincrement,
  user string not null,
  condition string,
  location string,
  msg string not null
);
