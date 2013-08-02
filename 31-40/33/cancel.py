def shared_digits(n,d):
	for nc in str(n):
		for nd in str(d):
			if nc == nd:
				return True
	return False

def get_cancel(n,d):
	ns = str(n)
	ds = str(d)

	for nc in str(n):
		for nd in str(d):
			if nc == nd:
				ns = ns.replace(nc, '')
				ds = ds.replace(nd, '')

	if len(ns) > 0 and len(ds) > 0:
		if int(ds) > 0:
			return int(ns) / (int(ds) * 1.0)
	else:
		return 0

for n in range(10,100):
	for d in range(10,100):
		num = n / (d * 1.0)
		if num < 1 and shared_digits(n, d) and get_cancel(n,d) == num:
			print str(n) + "/" + str(d) + " = " + str(n / (d * 1.0))
