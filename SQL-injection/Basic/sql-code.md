# Understand SQL Code

### Introduction to Database
1. **Rows:** Represents a single entry in a database table.
    - **Example:** In a `users` table, each row would contain information about one specific user. 
2. **Columns:** Represents a specific type of data within a table.
    - **Example:** In the `users` table, columns might include `id`, `firstname`, `lastname` and `email`.
```
+----+-----------+------------+----------------------+
| id | firstname |  lastname  |        email         |
+----+-----------+------------+----------------------+
| 1  |   Adam    |   Langley  |   adam@fakemail.ctf  |
+----+-----------+------------+----------------------+
| 2  |   Bob     | Gillingham |    bob@fakemail.ctf  |
+----+-----------+------------+----------------------+
| 3  |   Brian   |    Smith   | b.smith@fakemail.ctf |
+----+-----------+------------+----------------------+
```

---

### Introduction to SQL Code

**Challenge 1:** Select all the columns from the table named customers.
```sql
-- Simple Query
SELECT * FROM customers;--
```

**Challenge 2:** Select the id and firstname columns from the table named customers.
```sql
-- Column Selection
SELECT id, firstname FROM customers;--
```

**Challenge 3:** Select the id and firstname columns from the table named customers where the id is equal to 1.
```sql
-- Where: filters rows, selecting only those that meet a specified condition.
SELECT id, firstname FROM  customers WHERE id=3;--
```

**Challenge 4:** Select the id and firstname columns from the table named customers where the firstname column start with b.
```sql
-- Like: operator finds data matching a pattern, using % as a wildcard to represent any sequence of characters.
SELECT id, firstname FROM customers WHERE firstname LIKE 'b%';--
```

**Challenge 5:** Select the id and firstname columns from the table named customers where the firstname column starts with b and the id is greater than 2.
```sql
-- Multiple where clauses
SELECT id, firstname FROM customers WHERE firstname LIKE 'b%' AND id > 2;--
```

**Challenge 6:** Select all columns from the table named customers in ascending order by the column id.
```sql
-- order by ASC: sorts the query results in ascending order, from lowest to highest.
SELECT * FROM customers WHERE id ORDER BY ASC;--
```

**Challenge 7:** Select all the columns from the table names customers in descening order by the column id.
```sql
-- order by desc: sorts the query's results in descending order, from highest to lowest.
SELECT * FROM customers ORDER BY id DESC;--
```

**Challenge 8:** Select all the columns from the table named customers but limit the results to just the first row.
```sql
-- Limit: restricts the number of rows returned by a query.
SELECT * FROM customers LIMIT 1;--
```

**Challenge 9:** Select all the columns from the table named customers but limit the results to just the second row.
```sql
-- LIMIT SKIP
SELECT * FROM customers limit 1,1;--
```

**Challenge 10:** Select the email columns from the customers and suppliers table.
```sql
-- Union: combines the result sets of two or more SELECT statements into a single result set, removing duplicate rows.
SELECT email FROM customers UNION SELECT email FROM suppliers;--
```

---

**SQL Lab:** https://app.hackinghub.io/hubs/interactive-sqli-understanding-sql











