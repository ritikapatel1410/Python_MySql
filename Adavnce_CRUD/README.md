# MySQL Advance CRUD Operation

This branch contain all the advance CRUD operation of MySQL 

* MySQL Aggregate Function 
* MySQL Import Export Operation
* MySQL Clauses
* MySQL Index 
* MySQL Join
* MySQL Store Procedure
* MySQL View
* MySQL BLOB Data type
* MySQL Window Function
  * Window Ranking Function
  * Window Analytical Function
  * Window Aggregate Function
  
* Export MySQL Database
  * Use mysqldump to export database
      * mysqldump -u username -p database_name > data-dump.sql
         * username is the username you can log in to the database with
         * database_name is the name of the database to export
         * data-dump.sql is the file in the current directory that stores the output
  * you can inspect the contents of data-dump.sql to check if it’s a legitimate SQL dump file
      * head -n 5 data-dump.sql

* Import MySQL Database
   * Log in to MySQL as root or another user with sufficient privileges to create new databases
     * mysql -u root -p
   * Then new create new database
     * CREATE DATABASE new_database
   * Then exit the MySQL shell and from the normal command line, you can import the dump file with the following command
     * mysql -u username -p new_database < data-dump.sql

Refrences

* https://www.javatpoint.com/
* https://www.tutorialspoint.com/difference-between-ddl-and-dml-in-dbms
* https://www.tutorialspoint.com/sql/sql-indexes.htm
* https://www.javatpoint.com/mysql-view
* https://www.w3schools.com/sql/sql_ref_mysql.asp
* https://www.mysqltutorial.org/mysql-window-functions/
* https://www.digitalocean.com/community/tutorials/how-to-import-and-export-databases-in-mysql-or-mariadb
