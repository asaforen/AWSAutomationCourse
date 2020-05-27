import mytimer
#import mymodules.mytimer2 as mytimer

mytimer.start_timer()
lines = 0
for row in open ("words"):
    lines += 1
mytimer.end_timer()


a=5



try:
    if a>5:
        mytimer.start_timer()
    mytimer.end_timer()
    print ("Number of lines:",lines)
except SystemError:
    print("with error")

#mytimer.start_timer()
# Added for Exercise 11, should crash
#mytimer.end_timer()

# Now handle the exception


print ("We are all done")
