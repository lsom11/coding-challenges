select department, count(*) from employee
group by 1
having count(*) > 5