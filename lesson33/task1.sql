print(hr_database.show_tables())

hr_database.command_query("""
    ALTER TABLE Employee_details
    RENAME TO new_employee_details""")

hr_database.command_query("""
    ALTER TABLE new_employee_details
    ADD test INTEGER""")

hr_database.command_query("""
    INSERT INTO new_employee_details (employee_id, employee_age, employee_position, test)
    VALUES (22, 23, 'test1', 16)""")


hr_database.command_query("""
    UPDATE  new_employee_details
    SET employee_position =  'director'
    WHERE employee_id = 20 """)


hr_database.command_query("""
    DELETE FROM new_employee_details
    WHERE employee_id = 22 """)
