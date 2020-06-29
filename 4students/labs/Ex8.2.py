import os

########################################################
# Insert your TIMER FUNCTIONS here
def start_timer():
   (user,star) = os.times()[0:2]
   '''
   another option:
   t = os.times()
   cpu = t[0] + t[1]
   '''
   global cpu
   cpu = user + star
   return cpu

def end_timer(txt="End Time"):
    (user,star) = os.times()[0:2]
    end_time = user + star
    print(txt, end_time-cpu)

#

start_timer()

lines = 0
'''
for row in open ("words"):
    lines += 1
    '''
end_timer()
print ("Number of lines:",lines)