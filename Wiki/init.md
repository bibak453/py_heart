On new game:
1. We initialize all the flags to zero (non-persistent ones)
2. We set the flag_date to 3
3. We set the flag_weekday to ((flag_date + 5) % 7)
4. We start the scenario at SCN 0000 BLK 01
