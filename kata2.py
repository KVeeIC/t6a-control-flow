# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → cycle count
# Every 5th day → scanner audit
# Days that are both → full audit
# Any other day → normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT
# Day is the day of the month, starting with 1 with the range covering 1-30. Not 31.
for day in range(1, 31):
    if day % 15 == 0: 
        print(f"day {day}: full audit")
    elif day % 5 == 0:
        print(f"day {day}: scanner audit")
    elif day % 3 == 0:
        print(f"day {day}: cycle count")
    else:
        print(f"day {day}: normal operations")