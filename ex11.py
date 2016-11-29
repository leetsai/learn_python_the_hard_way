print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "Who is your favorite NBA player?",
nba_player = raw_input() # raw_input() gets an input from the user and return it as a string

print "So, you're %r old, %r tall, %r heavy and you like %r" % (age, height, weight, nba_player)
