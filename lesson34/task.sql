print(tabulate(hr_database.sqlQuery("""SELECT e.first_name, e.last_name, d.department_name, d.department_id
                                        FROM employees AS e
                                        LEFT JOIN department AS d ON e.department_id = d.department_id
                                        """), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT e.first_name, e.last_name, d.department_name, l.city, l.state_province
                                        FROM employees AS e
                                        LEFT JOIN department AS d ON e.department_id = d.department_id
                                        LEFT JOIN locations AS l ON d.location_id = l.location_id
                                        """), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT e.first_name, e.last_name, d.department_id, d.department_name
                                        FROM employees AS e
                                        LEFT JOIN department AS d ON e.department_id = d.department_id
                                        WHERE d.department_id = 40 OR d.department_id = 80
                                        """), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT e.first_name, e.last_name, d.department_id, d.department_name
                                        FROM department AS d
                                        LEFT JOIN employees AS e ON d.department_id = e.department_id
                                        """), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""
                                        SELECT e.first_name, e.employee_id, e.manager_id, m.first_name
                                        FROM employees AS e
                                        LEFT JOIN employees m ON e.manager_id = m.employee_id
                                        """), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT e.first_name|| ' '||e.last_name AS FullName, j.job_title, j.max_salary - e.salary AS delta_salary
                                        FROM employees AS e
                                        LEFT JOIN jobs AS j ON e.job_id = j.job_id
                                        """), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT j.job_title, AVG(e.salary) AS avg_salary
                                        FROM employees AS e
                                        LEFT JOIN jobs AS j ON e.job_id = j.job_id
                                        GROUP BY j.job_title
                                        """), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT e.first_name|| ' '||e.last_name AS FullName, e.salary, l.city
                                        FROM employees AS e
                                        LEFT JOIN department AS d ON e.department_id = d.department_id
                                        LEFT JOIN locations AS l ON d.location_id = l.location_id
                                        WHERE l.city LIKE 'London'
                                        """), headers="keys", tablefmt="psql"))

print(tabulate(hr_database.sqlQuery("""SELECT  d.department_name, COUNT(e.employee_id) AS number_employees
                                        FROM employees AS e
                                        LEFT JOIN department AS d ON e.department_id = d.department_id
                                        GROUP BY d.department_name
                                        """), headers="keys", tablefmt="psql"))
