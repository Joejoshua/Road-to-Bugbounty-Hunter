# **PortSwigger:** SQL Injection Vulnerability

**SQL Injection Vulnerability** is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. 

This can allow an attacker to view data that they are not normally able to retrieve. This might include data that belongs to other users, or any other data that the application can access. 

## **Lab that solved:**

1. SQL injection vulnerability in WHERE clause allowing retrieval of hidden data.
    - **Vulnerability:** 
	    - Product category filter.
    - **Goal:**
	    - Causes the application to display one or more unreleased products.

2. SQL injection vulnerability allowing login bypass.
    - **Vulnerability:** 
	    - Login function.
    - **Goal:** 
	    - Attack that logs in to the application as the `administrator` user.

3. SQL injection UNION attack, determining the number of columns returned by the query.
    - **Vulnerability:** 
	    - Product category filter.
    - **Goal:** 
	    - Determine the number of columns returned by the query.

4. SQL injection UNION attack, finding a column containing text.
    - **Vulnerability:** 
	    - Product category filter.
    - **Goal:** 
	    - Determine which columns are compatible with string data.

5. SQL injection UNION attack, retrieving data from other tables.
    - **Vulnerability:**  
	    - Product category filter.
	    - The database contains a different table called `users`, with columns called `username` and `password`.
    - **Goal:** 
	    - Perform a SQL injection UNION attack that retrieves all usernames and passwords
	    - Use the information to log in as the `administrator` user.

6. SQL injection UNION attack, retrieving multiple values in a single column.
    - **Vulnerability:** 
	    - Product category filter.
	    - The database contains a different table called `users`, with columns called `username` and `password`.
    - **Goal:** 
	    - Retrieves all usernames and passwords
	    - use the information to log in as the `administrator` user.

7. SQL injection attack, querying the database type and version on Oracle.
    - **Vulnerability:** 
	    - Product category filter.
    - **Goal:** 
	    - Display the database version string.

8. SQL injection attack, querying the database type and version on MySQL and Microsoft
    - **Vulnerability:** 
	    - Product category filter.
    - **Goal:** 
	    - Display the database version string.

9. SQL injection attack, listing the database contents on non-Oracle databases
    - **Vulnerability:** 
	    - Product category filter.
	    - The application has a login function, and the database contains a table that holds usernames and passwords.
    - **Goal:** 
	    - Determine the name of this table and the columns it contains
	    - Retrieve the contents of the table to obtain the username and password of all users.
	    - Log in as the `administrator` user.

10. SQL injection attack, listing the database contents on Oracle
    - **Vulnerability:** 
	    - Product category filter.
	    - The application has a login function.
	    - The database contains a table that holds usernames and passwords.

    - **Goal:** 
	    - Determine the name of this table and the columns it contains.
	    - Retrieve the contents of the table to obtain the username and password of all users.
	    - Log in as the `administrator` user.