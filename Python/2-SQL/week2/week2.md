SLECT title, author, year
FROM books
WHERE genre = 'Novel' AND year < 1989

<> NOT EQUAL operator 

SELECT genre FROM books;

SELECT DISTINCT genre FROM books; 

#between 

SELECT b.title as twentieth_century_books
FROM books b
WHERE b.year BETWEEN 1900 AND 2000;

"fuzzy matching": 

SELECT b.title FROM books b
WHERE b.title LIKE 'T%';

SELECT b.title FROM books b
WHERE b.title LIKE '%T%';

#performs case insensitive 

SELECT b.title FROM books b
WHERE b.title ILIKE '%T%';

SELECT b.title, b.year FROM books b
WHERE b.year IN (1990, 1986, 1998);

#order by

SELECT 
    select_list
FROM
    table_name
ORDER BY
    sort_expression1[ASC | DESC],
    sort_expressionN [ASC | DESC];

SELECT * FROM books
ORDER BY genre, author DESC;

INSERT INTO divisions (name)
VALUES ('atlantic');

INSERT INTO teams (city, name, home_color, away_color, division_id) VALUES 
('New York', 'Islanders', 'Royal blue', 'White', 2),
('Seattle', 'Kraken', 'Deep sea blue', 'White', 3);

UPDATE divisions
SET name = 'Cosmopolitan'
WHERE name = 'Metropolitan';

DELETE FROM divisions
WHERE name = 'Cosmopolitan';

SELECT * FROM divisions;

SELECT * FROM books;

SELECT title, year FROM books;

SELECT title AS book_title, year AS book_year FROM books
WHERE title LIKE 'B%'
ORDER BY book_year DESC;

SELECT first_name, last_name 
FROM employees 
WHERE title = "Sales Representative" 
ORDER BY last_name, first_name;

SELECT first_name, home_phone 
FROM employees
WHERE first_name LIKE 'A%' 
AND home_phone LIKE '%4%'


#SQL Aggregate functions: 

COUNT
MAX
MIN
AVG
SUM 

#Group by : 

SELECT genre, COUNT (*) AS book_count
FROM books GROUP BY genre;

#HAVING function 

SELECT genre, COUNT(*) AS book_count
FROM books
GROUP BY genre
HAVING (COUNT(*)) > 1;

SELECT title AS book_title, year AS book_year FROM books
ORDER BY book_year DESC;

SELECT customer_id, order_date 

SELECT title AS book_title, year AS book_year FROM books
ORDER BY book_year DESC;

SELECT customer_id, order_date 

#Multi-Table Queries: 

SELECT title, president AS author, year FROM president_books
UNION ALL 
SELECT title, author, year FROM amazon_best_sellers;

SELECT title, author, year FROM amazon_best_sellers
INTERSECT
SELECT title, president AS author, year FROM president_books;

SELECT title, author, year FROM amazon_best_sellers
EXCEPT 
SELECT title, president AS author, year FROM president_books;

#SQL inner join: 

#INNER is default 

SELECT select_list
FROM left_table
LEFT JOIN right_table
ON left_column = right_column;


SQL COMMANDS: 

SELECT * FROM departments;

SELECT * FROM professors;

SELECT * FROM students;

SELECT s.last_name FROM students s
UNION
SELECT p.last_name FROM professors p;

SELECT s.last_name FROM students s
UNION ALL
SELECT p.last_name FROM professors p;

SELECT s.last_name FROM students s
UNION ALL
SELECT p.last_name FROM professors p
ORDER BY last_name;

SELECT s.first_name, s.last_name, d.name
FROM departments d
INNER JOIN students s
ON d.id = s.major_department_id;

SELECT s.first_name, s.last_name, d.name
FROM departments d
RIGHT JOIN students s
ON d.id = s.major_department_id;

SELECT s.first_name, s.last_name, d.name
FROM departments d
FULL JOIN students s
On d.id = s.major_department_id

#For each product, list the product_name and the corresponding category_name 

SELECT product_name, category_name FROM products p
JOIN categories c ON p.category_id = c.category_id;

#For each order, list the order_id and the corresponding shipper company_name if available, else NULL
SELECT o.order_id, s.company_name FROM orders o
LEFT JOIN shippers s ON o.ship_via = s.shipper_id

#For each customer order, list the customers company_name, order_id, and total quantity of products ordered

SELECT c.company_name, o.order_id, SUM(od.quantity) FROM orders o 
JOIN order_details od ON o.order_id = od.order_id 
JOIN customers c ON o.customer_id = c.customer_id 
GROUP BY o.order_id, c.company_name;

#Select each company_name that begins with the letter 'D', including those of customers, shippers, and suppliers. 

WITH customer_companies AS (
    SELECT company_name
    FROM customers
    WHERE company_name LIKE 'D%'
),
shipper_companies AS (
    SELECT company_name
    FROM shippers
    WHERE company_name LIKE 'D%'
),
supplier_companies AS (
    SELECT company_name
    FROM suppliers
    WHERE company_name LIKE 'D%'
)
SELECT company_name
FROM customer_companies
UNION
SELECT company_name
FROM shipper_companies
UNION
SELECT company_name
FROM supplier_companies;

WITH names AS (
    SELECT company_name FROM customers 
    UNION ALL 
    SELECT company_name FROM suppliers 
    UNION ALL 
    SELECT company_name FROM shippers
) SELECT company_name FROM names
WHERE company_name LIKE 'D%';

#Get the product_name of products that belong to categories having a category_name beginning with the letter 'C'. Use a subquery instead of a JOIN.
SELECT p.product_name FROM products p 
WHERE EXISTS(
    SELECT * FROM categories c 
    WHERE c.category_id = p.category_id 
    AND c.category_name LIKE 'C%'
);




