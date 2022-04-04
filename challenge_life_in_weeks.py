age=input("What is your age ? ");

new_age=int(age);

r_days=(90-new_age)*365;
r_month=(90-new_age)*12;
r_weeks=(90-new_age)*52;

print(f"You have remaining {r_days} days, {r_weeks} weeks, {r_month} months");