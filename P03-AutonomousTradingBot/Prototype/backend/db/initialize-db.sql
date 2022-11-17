drop table if exists analysts cascade;
drop table if exists investors cascade;

create table analysts (
    id uuid,
    name varchar(100),
    address varchar(500),
    email varchar(100),
    phone_number varchar(100),
    password varchar(512),
    expiry timestamp with time zone,
    token varchar(512),

    primary key (id)
);

create table investors (
    id uuid,
    name varchar(100),
    address varchar(500),
    email varchar(100),
    phone_number varchar(100),
    password varchar(512),
    expiry timestamp with time zone,
    token varchar(512),

    primary key (id)
);