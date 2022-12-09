print(tabulate(hr_database.sqlQuery("""SELECT first_name AS 'First Name', last_name AS 'Last Name'
                                     FROM employees"""), headers="keys", tablefmt="psql"))


print(tabulate(hr_database.sqlQuery("""SELECT DISTINCT department_id
                                     FROM employees"""), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT *
                                     FROM employees
                                     ORDER BY first_name DESC"""), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT first_name, last_name, salary, salary * 0.12 AS PF
                                     FROM employees"""), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT  MAX(salary), MIN(salary)
                                     FROM employees"""), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT ROUND(CAST(salary as DECIMAL(10,2)), 2) AS salary
                                        FROM employees"""), headers="keys", tablefmt="psql"))
