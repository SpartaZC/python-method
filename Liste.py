# Mike List ~

import string
import random 
print(' ~~ created By ~ose ~~')

typeu = int (input("enter the use type => :"))
lenght =int(input (" length user => "))
file= open("c","a")
if lenght ==4 :
    user = string.ascii_lowercase + string.digits()
    le = 1 
    while le < lenght:
     file.write(''.join(random.choice(user) for i in range (4))+'\r\n')
     le += 1
elif lenght ==3 :
    user = string.ascii_lowercase + string.digits()
    le = 1 
    while le < lenght:
     file.write(''.join(random.choice(user) for i in range (3))+'\r\n')
     le += 1
elif lenght ==2 :
    user = string.ascii_lowercase + string.digits()
    le = 1 
    while le < lenght:
     file.write(''.join(random.choice(user) for i in range (2))+'\r\n')
     le += 1
file.close()
