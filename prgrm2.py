hourly_wage=20.0
hours=6
day="Sunday"
daily_wages =hourly_wage * hours

print("condition : ",day == "sunday")
if day == "sunday":
    print("wages before: ",daily_wages)
    daily_wages*=2
    print("wages after dooubling: ",daily_wages)
print(f"daily wages :{daily_wages}euros")
