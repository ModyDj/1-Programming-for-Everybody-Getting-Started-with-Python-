'''
Rewrite your pay program using TRY and EXCEPT so that your program handles non-numeric input
gracefully by printing a message and exiting the program.
'''
try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Rate:")
    r = float(rate)
except:
    print 'Error, please enter numeric input'
    quit()

if h > 40.0 :
    print 'Pay:', 40.0 * r + (h - 40.0) * r * 1.5
else:
    print 'Pay:', h * r
