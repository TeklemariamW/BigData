create database datacamp;
use datacamp;

Create table airbnb_listins(
Id int, City varchar(20),
Country varchar(30),
number_of_rooms int,
year_listed int
);

insert into airbnb_listins
values
(1, 'Paris', 'France', 5, 2018),
(2,	'Tokyo',	'Japan',	2,	2017),
(3,	'New York',	'USA',	2,	2022),
(4, 'Asmara', 'Eritrea', 5, 2018),
(5,	'Khartoum',	'Sudan',	2,	2016),
(6,	'Oslo',	'Norway',	2,	2022);

select * from airbnb_listings limit 3;

#SET SQL_SAFE_UPDATES = 1;


update airbnb_listings set number_of_rooms = 4 where Id = 3;

select distinct number_of_rooms from airbnb_listings;
select * from airbnb_listings where number_of_rooms between 3 and 5;

select count(*) from airbnb_listings; #Total number of airbnb in the list
select sum(number_of_rooms) from airbnb_listings; #total number of rooms
select avg(number_of_rooms) from airbnb_listings;
select max(number_of_rooms) from airbnb_listings;#highest number of rooms

select * from airbnb_listings;

update airbnb_listings set City = "Paris" , Country = 'France' where Id = 6;

#Grouping, filtering, and sorting
select country, avg(number_of_rooms) as 'Number of rooms'  #group by
from airbnb_listings group by Country;

select country, max(number_of_rooms) as number
from airbnb_listings group by country;

select country, avg(number_of_rooms) as avg_rooms from airbnb_listings
group by country order by avg_rooms desc limit 1;

select country, avg(number_of_rooms) as avg_rooms from airbnb_listings 
where country in ('Japan' , 'usa') group by Country;
