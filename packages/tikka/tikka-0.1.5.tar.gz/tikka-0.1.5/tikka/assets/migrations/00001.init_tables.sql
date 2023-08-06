create table if not exists accounts(
        pubkey varchar unique primary key,
        uid varchar,
        selected boolean default 1,
        access_type varchar(8) default null
);
