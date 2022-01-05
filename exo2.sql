WITH temp_table
     AS (SELECT dp.id    AS dp_id,
                dp.NAME  AS dp_name,
                Count(*) AS number_of_employee
         FROM   departement AS dp
                INNER JOIN employee
                        ON dp.id = employee.dept_id
         GROUP  BY dp_id,
                   dp_name)
SELECT id,
       NAME,
       COALESCE(number_of_employee, 0) AS number_of_employee
FROM   departement
       LEFT JOIN temp_table
              ON id = dp_id
ORDER  BY number_of_employee DESC,
          NAME  
