'''
Write a program to prompt the user for hours and 
rate per hour to compute gross pay.
'''
hours = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
pay = float(hours) * float(rate)
print "Pay:", pay