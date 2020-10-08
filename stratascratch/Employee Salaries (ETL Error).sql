select id, first_name, last_name, department_id, max(salary) as max from ms_employee_salary
group by 1,2,3,4
order by id
