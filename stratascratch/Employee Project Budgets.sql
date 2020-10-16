select project_id, (budget / COUNT(emp_id)) avg_budget from ms_projects mp
left join ms_emp_projects mep on mp.id = mep.project_id
group by 1, budget
having count(emp_id) > 0
order by 2 desc