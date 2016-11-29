name = 'Lee Tsai'
age = 26 # this is the truth
height = 72 # inches
weight = 162 # lbs
eyes = 'Dark brown'
teeth = 'White' # duh
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "He's %i kilograms heavy." % (weight * 0.453592) # %i is like %d
print "He's %d kilograms heavy." % (weight * 0.453592) # %d is like %i
print "He's %r kilograms heavy." % (weight * 0.453592) # %r prints exactly as it is
print "He's %r kilograms heavy." % round(weight * 0.453592, 2) # rounding to the 2nd decimal place
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
