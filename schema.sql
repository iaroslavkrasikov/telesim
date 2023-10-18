drop table if exists users, plans, simcards;

create table users
(
	telegram_id double precision not null,
	is_active boolean default false not null,
    balance money default 0.00 not null,
	currency varchar(3) default 'USD' not null
);

create unique index users_telegram_id_uindex
	on users (id);

alter table users
	add constraint users_pk
		primary key (id);

create table plans
(
	id serial not null,
	name varchar(255) not null,
	regions text not null,
	duration interval not null,
	limit_bytes int not null,
	price money not null,
	currency varchar(3) default 'USD' not null,
	secret varchar,
	is_active bool default false not null
);

create unique index plans_id_uindex
	on plans (id);

create unique index plans_name_uindex
	on plans (name);

alter table plans
	add constraint plans_pk
		primary key (id);

create table simcards
(
    id serial not null,
    user_id double precision not null
        constraint simcards_users_telegram_id_fk
            references users,
    plan_id int not null
        constraint simcards_plans_id_fk
            references plans,
    qr varchar(255) not null,
    activated_at timestamptz(6) default now() not null,
    deactivated_at timestamptz(6),
    remain_bytes int default 0 not null,
    remain_bytes_updated_at timestamp(6)
);

create unique index simcards_id_uindex
    on simcards (id);

create unique index simcards_pk
    on simcards (id);

-- alter table simcards
--     add constraint simcards_pk
--         primary key (id);


