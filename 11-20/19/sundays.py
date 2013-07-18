import datetime
from dateutil.relativedelta import relativedelta

begindate = datetime.date(1901, 01, 01)

counted = 0

for x in range(1,1200):
	begindate = begindate + relativedelta(months=1)
	print begindate
	if begindate.weekday() == 6:
		counted = counted + 1

print counted
