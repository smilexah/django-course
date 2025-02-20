CREATE TABLE book
(
    title     TEXT,
    publisher TEXT,
    author    TEXT
);

insert into book
values ('The Sparrow Warrior', 'Super Hero Publications', 'Patric Javagal');
insert into book
values ('The European History', 'Super Hero Publications', 'Eric Robbins');
insert into book
values ('The European History 2', 'Super Hero Publications 2', 'Eric Robbins 2');

select title, publisher, author
from book;

select *
from book;

SELECT author
FROM book
WHERE title = 'The Sparrow Warrior';

UPDATE book
SET publisher = 'The Northside Publications 2',
    title     = 'The Sparrow Warrior 2'
WHERE title = 'The European History 2';


delete
from book
where title = 'The Sparrow Warrior';