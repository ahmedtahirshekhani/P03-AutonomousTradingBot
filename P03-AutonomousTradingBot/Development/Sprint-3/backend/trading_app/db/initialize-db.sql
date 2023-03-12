drop table if exists analysts cascade;
drop table if exists investors cascade;
drop table if exists bots cascade;
drop table if exists trades cascade;

drop type if exists bot_state_enum cascade;
drop type if exists risk_appetite_enum cascade;
drop type if exists trade_type_enum cascade;

create type bot_state_enum as enum ('IDLE', 'RUNNING', 'FINISHED', 'TERMINATED');
create type risk_appetite_enum as enum ('LOW', 'MID', 'HIGH');
create type trade_type_enum as enum ('CALL', 'PUT');


create table analysts (
    id uuid,
    name varchar(100),
    address varchar(500),
    email varchar(100),
    phone_number varchar(100),
    hashed_password varchar(512),
  
    primary key (id)
);

create table investors (
    id uuid,
    name varchar(100),
    address varchar(500),
    email varchar(100),
    phone_number varchar(100),
    hashed_password varchar(512),
    ntn_number varchar(100),

    primary key (id)
);


create table bots (
    id uuid,
    analyst_id uuid,
    investor_id uuid,
    stocks_ticker varchar(20),
    initial_balance numeric,
    current_balance numeric,
    target_return numeric,
    risk_appetite risk_appetite_enum,
    in_trade boolean,
    state bot_state_enum,
    prices json,
    start_time timestamp with time zone,
    end_time timestamp with time zone,
    assigned_model smallint,

    primary key (id),
    foreign key (analyst_id)
        references analysts(id),
    foreign key (investor_id)
        references investors(id)
);

create table trades (
    id uuid,
    bot_id uuid,
    amount numeric,
    start_price numeric,
    started_at timestamp with time zone,
    trade_type trade_type_enum,
    ended_at timestamp with time zone,
    end_price numeric,
    is_profit boolean,

    primary key (id),
    foreign key (bot_id)
        references bots(id)
);
