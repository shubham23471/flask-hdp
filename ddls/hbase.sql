create table if not exists us_population(
    state char(2) not null,
    city varchar not null, 
    population bigint
    constraint my_pk primary key (state, city)
);

-- upsert means : insert this row but if the contains of this row already exist then update it 
upsert into us_population values ('NY', 'New York', 6789123);
upsert into us_population values ('CA', 'Los Angeles', 234678);
