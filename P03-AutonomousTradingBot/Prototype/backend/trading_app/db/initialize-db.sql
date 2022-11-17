drop table if exists analysts cascade;
drop table if exists investors cascade;

create type bot_state_enum as enum ('idle', 'running', 'finished', 'terminated');
create type risk_appetite_enum as enum ('low', 'mid', 'high');

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

create table trades (
    id uuid,
    bot_id uuid,
    stock_id varchar(100),
    amount numeric,
    buying_price numeric,
    selling_price numeric,
    spread numeric,
    started_at timestamp with time zone,
    ended_at timestamp with time zone,
    company_name varchar(100),

    primary key (id),
    foreign key (bot_id)
        references bots(id)
);

create table bots (
    id uuid,
    analyst_id uuid,
    investor_id uuid,
    state bot_state_enum,
    assigned_model smallint,
    risk_appetite risk_appetite_enum,
    target_return numeric,
    duration timestamp with time zone,

    primary key (id),
    foreign key (analyst_id)
        references analysts(id),
    foreign key (investor_id)
        references investors(id)
);