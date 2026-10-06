# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start
interval =  15 #Once the time hit 15 minutes, the scanner is checked.
for check in range(interval, 151, interval):
    print(f"Check {check // interval}: {check} minutes after shift start")
    #Short condition to check scanner every 15 minutes, up to 150 minutes after shift start.