'''
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
'''
hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
r
if h > 40.0 :
    print 'Pay:', 40.0 * r + (h - 40.0) * r * 1.5
else:
    print 'Pay:', h *r
