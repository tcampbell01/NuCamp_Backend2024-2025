Nullability: 

Nullable: Can be null (no value)
Non-Nullable: data which must have a valid --> bold line in ER diagram #how?

Uniqueness: Ensures attribute is unique for given entity or relationship (username for example) --> underlined in ER diagram

Relationship Participation --> Bold line between entity and attribute

Is there a drawio plugin for intellij? 

pgAdmin: localhost:5433 

CREATE TABLE drivers (
	id SERIAL,
	car_id INT NOT NULL,
	name TEXT NOT NULL,
	PRIMARY KEY(id)
);

ALTER TABLE drivers ADD CONSTRAINT fk_drivers_cars FOREIGN KEY(car_id) REFERENCES cars(id);


#Answers from Quiz: 

1. The attributes in an ER diagram generally translate to COLUMNS in a database table. 

2. Match each concept to the way it is represented in an ER diagram: 
    Relationship --> diamond
    Uniqueness --> underlined text
    Attribute --> Oval
    Non-nullable --> Bold line
    Primary Key --> Underlined Text
    Entity --> Rectangle

3. Select how each kind of relationship participation is represented in an ER diagram: 

    Participates at most once (either zero times or once) --> arrow from entity to relationship
    Required participation (participates at least once or more) --> Bold line from entity to relationship
    Participates zero or more times --> Line between entity and relationship
    Participates exactly once, no more or less --> Bold arrow from entity to relationship 

4. According to this ER diagram, a User must have a password that is unique --> False

5. Each database table can only have a single foreign key column --> False

6. In a relational model, the types of relationships that exist between entities include...
    - Many-to-many
    - one-to-one
    - one-to-many

7. In SQL, what keyword(s) do you use to create a column constraint of non-nullability? --> NOT NULL

8. What SQL column constraint denotes a unique row identifier? 
    - PRIMARY KEY

9. A primary key may be composite, meaning that it can be made up of more than one column. --> TRUE

10. True or False? Given the above table of college courses, the number and capacity columns together could serve as a composite primary key.  

department 	 number 	 capacity
 MATH	 101	 150
 CHEM	 210	 170
 PHYS	 140	 150
 ENG	 125	 35
 STATS	 101	 150

answer: FALSE 