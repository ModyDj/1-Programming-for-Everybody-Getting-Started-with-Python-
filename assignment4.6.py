'''
Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters.
'''
def computepay(h,r):
    if h > 40.0 :
        return 40.0 * r + (h - 40.0) * r * 1.5
    else:
        return h * r

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
p = computepay(float(hrs),float(rate))

print "Pay:", p