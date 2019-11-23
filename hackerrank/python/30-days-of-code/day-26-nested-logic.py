from datetime import date


returned_day, returned_month, returned_year = map(int, input().split())
due_day, due_month, due_year = map(int, input().split())


return_date = date(day=returned_day, month=returned_month, year=returned_year)
due_date = date(day=due_day, month=due_month, year=due_year)


fine = 0

if return_date > due_date:
    if return_date.year == due_date.year:
        if return_date.month == due_date.month:
            fine = 15 * (return_date.day - due_date.day)
        else:
            fine = 500 * (return_date.month - due_date.month)
    else:
        fine = 10000

print(fine)
