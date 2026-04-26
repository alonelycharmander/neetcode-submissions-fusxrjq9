CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT,
    weakness TEXT
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_id INTEGER REFERENCES pokemon_types(id)
);

INSERT INTO pokemon_types (id, name, weakness) VALUES
(1, 'Fire', 'Water'),
(2, 'Water', 'Grass'),
(3, 'Grass', 'Fire'),
(4, 'Electric', 'Ground');

INSERT INTO pokemon (id, name, type_id) VALUES
(4, 'Charmander', 1),
(7, 'Squirtle', 2),
(3, 'Bulbasaur', 3);
-- Do not modify above this line. --

select 
    b.name as type, 
    a.name as pokemon, 
    b.weakness
from 
    pokemon a  
right join 
    pokemon_types b 
on a.type_id = b.id 
order by b.name




