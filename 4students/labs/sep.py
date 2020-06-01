#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(len(Belgium) * "-")
print(Belgium.replace(",",":"))
print(int(Belgium.split(",")[1]) + int(Belgium.split(",")[3]))
print(len(Belgium) * "-")
