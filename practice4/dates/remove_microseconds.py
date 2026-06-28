# Remove microseconds from current datetime

from datetime import datetime

current_time = datetime.now()

print(current_time.replace(microsecond=0))