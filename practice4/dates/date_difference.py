# Calculate difference between two dates in seconds

from datetime import datetime

date1 = datetime(2025, 5, 10, 12, 0, 0)
date2 = datetime(2025, 5, 11, 15, 30, 0)

difference = abs((date2 - date1).total_seconds())

print(difference)