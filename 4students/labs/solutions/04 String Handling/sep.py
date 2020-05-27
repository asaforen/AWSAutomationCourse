#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

items = Belgium.split(',')
print('-' * len(Belgium))
print(':'.join(items))
#print items[1] + items[3]
print(int(items[1]) + int(items[3]))
print('-' * len(Belgium))