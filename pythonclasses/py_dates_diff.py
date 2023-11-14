from datetime import datetime

date_one = "1999-01-31"
date_two = "2005-11-13"

# Changing strings dates to date objects
date1 = datetime.strptime(date_one, "%Y-%m-%d")
date2 = datetime.strptime(date_two, "%Y-%m-%d")

# Calculating date difference
date_diff = date2 - date1

# Getting number of days
number_of_days = date_diff.days

# Converting Days to weeks and months
number_of_weeks = number_of_days / 7
number_of_months = number_of_days / 30

print(f"The number of days between the two given dates is:", number_of_days)
print(f"The number of weeks between the two given dates are:", number_of_weeks)
print(f"The number of months between the two given dates are:", number_of_months.__trunc__())   # Converting months to only complete months
